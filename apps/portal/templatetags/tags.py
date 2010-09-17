import os
import Image

from django import template
from django.conf import settings

register = template.Library()

@register.filter
def thumbnail(file, size):
    width, height = size.split('x')
    width = int(width)
    height = int(height)
    basename, format = file.rsplit('.', 1)
    thumb = basename + '_' + size + '.' + format
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
