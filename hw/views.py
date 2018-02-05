from django.shortcuts import render

# Create your views here.
def invitation_list(request):
    return render(request, 'hw/invitation_list.html', {})
