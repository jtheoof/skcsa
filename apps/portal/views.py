from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.members.models import BlackBelt

def home(request):
    return render_to_response('portal/home.html', context_instance=RequestContext(request))
    
def club(request):
    black_belts = BlackBelt.objects.all()
    return render_to_response('portal/club.html', {
        'black_belts': black_belts,
        }, context_instance=RequestContext(request))
