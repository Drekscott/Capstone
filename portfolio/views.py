from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from portfolio.models import Project
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from forms import ProjectForm



# Create your views here.
def my_portfolio(request, portfolio_id=1):
    return render_to_response('portfolio.html',
                                {'my_portfolio': Project.objects.get(id=portfolio_id)})
    port_List=Project.objects.all()
    t = loader.get_template('portfolio.html')
    c = Context({'port_List':port_List, })
    return HttpResponse(t.render(c))

def create(request):
    if request.POST:
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/my_portfolios/all')
    else:
        form = ProjectForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_portfolio.html', args)

def my_portfolios(request):
    return render_to_response('portfolios.html',
                                {'my_portfolios':Project.objects.all()})
def like_portfolio(request, portfolio_id):
    if portfolio_id:
        a = Project.objects.get(id=portfolio_id)
        count = a.likes
        count+=1
        a.likes=count
        a.save()
    return HttpResponseRedirect('/my_portfolios/get/%s' % portfolio_id)
