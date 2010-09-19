import os
import Image

from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def selected(request, pattern):
    import re
    pattern = r'^%s$' % pattern
    if re.search(pattern, request.path):
        return 'selected'
    return ''

@register.filter
def thumbnail(file, size):
    width, height = size.split('x')
    width = int(width)
    height = int(height)
    basename, format = file.rsplit('.', 1)
    thumb = 'thumb-' + basename + '-' + size + '.' + format
    thumb_filename = os.path.join(settings.MEDIA_ROOT, thumb)
    thumb_url = os.path.join(settings.MEDIA_URL, thumb)

    filename = os.path.join(settings.MEDIA_ROOT, file)
    if os.path.exists(thumb_filename):
        if os.path.getmtime(thumb_filename) < os.path.getmtime(filename):
            create_new = True
            os.unlink(thumb_filename)
        else:
            create_new = False
    else:
        create_new = True
    
    if create_new:
        image = Image.open(filename)
        image.thumbnail([width, height], Image.ANTIALIAS)
        image.save(thumb_filename, image.format)

    return thumb_url
    
@register.simple_tag
def thumbnail(image_url, width, height):
    """
    Given the url to an image, resizes the image using the given width and 
    height on the first time it is requested, and returns the url to the new 
    resized image. If width or height are zero then the original ratio is 
    maintained.
    """
    
    image_url = unicode(image_url)
    basename, format = image_url.rsplit('.', 1)
    image_path = os.path.join(settings.MEDIA_ROOT, image_url)
    image_dir, image_name = os.path.split(image_path)
    thumb_name = "thumb-%s-%sx%s.%s" % (os.path.splitext(image_name)[0], width, height, format)
    thumb_path = os.path.join(image_dir, thumb_name)
    thumb_url = "%s/%s" % (os.path.dirname(image_url), thumb_name)

    # abort if thumbnail exists, original image doesn't exist, invalid width or 
    # height are given, or PIL not installed
    print image_url
    if not image_url:
        return ""
    if os.path.exists(thumb_path):
        return settings.MEDIA_URL + thumb_url
    try:
        width = int(width)
        height = int(height)
    except ValueError:
        return settings.MEDIA_URL + image_url
    print settings.MEDIA_ROOT
    print image_path
    if not os.path.exists(image_path) or (width == 0 and height == 0):
        return settings.MEDIA_URL + image_url
    try:
        from PIL import Image, ImageOps
    except ImportError:
        return settings.MEDIA_URL + image_url

    print 'ok'
    # open image, determine ratio if required and resize/crop/save
    image = Image.open(image_path)
    if width == 0:
        width = image.size[0] * height / image.size[1]
    elif height == 0:
        height = image.size[1] * width / image.size[0]
    #if image.mode not in ("L", "RGB"):
    #    image = image.convert("RGB")
    try:
        image = ImageOps.fit(image, (width, height), Image.ANTIALIAS)
        #transparency = image.info['transparency'] 
        image.save(thumb_path, quality=100)
    except:
        return settings.MEDIA_URL + image_url
    return settings.MEDIA_URL + thumb_url
