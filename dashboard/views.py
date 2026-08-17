from django.shortcuts import render

# Create your views here.
def index(request):

    data = {
        'title': "Landing Page' Dashboard",
    }

    return render(request, 'dashboard/index.html', data)