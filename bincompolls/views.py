from django.shortcuts import render, get_object_or_404
from .models import AnnouncedPuResults

# Create your views here.


def home(request):
    
    return render(request, 'bincompolls/index.html')


def pollin_unit_result(request):

    pu_result = AnnouncedPuResults.objects.all()

    context = {'pu_result':pu_result}
    return render(request, 'bincompolls/pollin_unit_result.html', context)