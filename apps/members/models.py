from django.db import models
from django.template.defaultfilters import slugify

def upload_black_belts(instance, filename):
    import os
    name, extension =  filename.rsplit('.')
    path = os.path.join('photos', 'members', '%s.%s' % (slugify('%s %s' % (instance.first_name, instance.last_name)), extension))
    return path

class BlackBelt(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    started_karate = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    dan = models.PositiveSmallIntegerField()
    avatar = models.ImageField(upload_to=upload_black_belts, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
        
    def save(self, *args, **kwargs):
        try:
            current = BlackBelt.objects.get(id=self.id)
            # We might want to do something about this code because it generates
            # RuntimeError: 'maximum recursion depth exceeded while calling a Python object'
            # in <type 'exceptions.RuntimeError'> ignored
            if current.avatar != self.avatar:
                current.avatar.delete()
        except: pass
        return super(BlackBelt, self).save(*args, **kwargs)
        
    def _get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)
