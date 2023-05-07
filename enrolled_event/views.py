from django.shortcuts import render

# Create your views here.
def enrolled_event_view(request):
    return render(request, 'enrolled_event.html')