from django.db.models import Q
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.members.models import BlackBelt

def home(request):
    return render_to_response('portal/home.html', context_instance=RequestContext(request))
    
def club(request):
    black_belts = BlackBelt.objects.all()
    professors = BlackBelt.objects.filter(Q(last_name__icontains='pierini') |
                                          Q(last_name__icontains='augier'))
    president = BlackBelt.objects.get(last_name__icontains='Gilardone')
    accountant = BlackBelt.objects.get(last_name__icontains='Gay')
    secretary = BlackBelt.objects.get(last_name__icontains='Bousquet')
    
    return render_to_response('portal/club.html', {
        'black_belts': black_belts,
        'professors': professors,
        'president': president,
        'accountant': accountant,
        'secretary': secretary,
        }, context_instance=RequestContext(request))
