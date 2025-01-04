from django.shortcuts import render

# Create your views here.
# testing the frontpage 
def test_frontpage(request):
    return render(request, 'core/frontpage.html')