from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    return render_to_response('portal/home.html', context_instance=RequestContext(request))
    
def club(request):
    return render_to_response('portal/club.html', context_instance=RequestContext(request))
