from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic
from . import service


# Create your views here.


class CategoryView(generic.TemplateView):
	def get(self, request):
		category_list = service.get_categories()
		return render(request, 'events/categories.html', category_list)


class CategoryResultView(generic.TemplateView):
	def post(self, request):
		choice_set = request.POST.getlist('checks')
		if len(choice_set)!=3:
			return HttpResponseRedirect(reverse('events:redirect'))
		request.session['choice_set'] = choice_set
		page = request.POST.get('page')
		request.session['page'] = page
		event_list = service.get_results(choice_set, page)
		eventbucket = event_list['events']
		return render(request, 'events/final_results.html', {'eventbucket':eventbucket, 'page':page,
			'nextPage':'2', 'priorPage':'1'})
	

def page(request, page):
		choice_set = request.session['choice_set']
		event_list = service.get_results(choice_set, page)
		eventbucket = event_list['events']
		request.session['page'] = page
		nextPage = int(page)+1
		priorPage = int(page)-1
		return render(request, 'events/final_results.html', {'eventbucket':eventbucket, 'page':page,
			'nextPage':nextPage, 'priorPage':priorPage})


