from django.db import models
from django.conf import settings

class Address(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    street = models.CharField(max_length=128)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64, blank=True, default='France')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    def __unicode__(self):
        ret = u''
        if self.name:
            ret += u'%s ' % self.name
        ret += u'%s %s' % (self.street, self.city)
        return ret
        
    def save(self, *args, **kwargs):
        self.get_geocode_data()
        super(Address, self).save(*args, **kwargs)
    
    def get_geocode_data(self):
        import re
        from libs.api.googlemaps import GoogleMapsGeoCodeAPI
        api = GoogleMapsGeoCodeAPI(settings.LOGGER)
        json = api.get_geocode(self.street, self.city, self.country)
        settings.LOGGER.debug('returned json: %s' % json)
        match = re.search(r'"lat": (?P<lat>-?\d+\.\d+),\s*"lng": (?P<lng>-?\d+\.\d+)', json)
        if match:
            self.latitude = float(match.group('lat'))
            self.longitude = float(match.group('lng'))

class Event(models.Model):
    address = models.ForeignKey(Address)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    external_link = models.URLField(null=True, blank=True)
    poster = models.ImageField(upload_to='events/%Y/%m/%d', null=True, blank=True)
    
    def __unicode__(self):
        import datetime
        return u'%s: ' % (date_begin.strftime('%Y'), title)
   
    
