from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def jannat(request):
    context = {
        'player_name' : 'jannat',
        'total_goal' : 10
    }
    return render(request, 'index.html', context)
