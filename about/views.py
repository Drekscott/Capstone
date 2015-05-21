from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from about.models import About
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
def index (request):
    about_List=About.objects.all()
    t = loader.get_template('about.html')
    c = Context({'about_List':about_List, })
    return HttpResponse(t.render(c))
