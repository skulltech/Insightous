from django.shortcuts import render
from django.http import HttpResponse

from .forms import TwitterUsernameForm
from .core import twitterscraper, ibm



def index(request):
	if request.method == 'POST':
		form = TwitterUsernameForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			insight = ibm.personality_insights(ibm.fetch_tweets('SkullTech101'))
			return HttpResponse(insight)
