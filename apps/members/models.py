from django.db import models

class BlackBelt(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    started_karate = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    dan = models.PositiveSmallIntegerField()
    avatar = ImageField(upload_to='photos/members/')
    
    def __unicode__(self):
    
    
    
    def slugify(self, string):
        import re
        removelist = ["a", "an", "as", "at", "before", "but", "by", "for","from","is", "in", "into", "like", "of", "off", "on", "onto","per","since", "than", "the", "this", "that", "to", "up", "via","with"];
        for a in removelist:
            aslug = re.sub(r'\b'+a+r'\b', '', string)
        aslug = re.sub('[^\w\s-]', '', aslug).stringip().lower()
        aslug = re.sub('\s+', '-', aslug)
        return aslug
