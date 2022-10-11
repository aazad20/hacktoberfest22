
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def learndj(request):
    # return HttpResponse("Heelo Buddy")
    key = {'c1' :'Hello', 'c2' : 'bussdy'}
    return render(request, 'c1/info.html', key)
