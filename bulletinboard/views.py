from django.http import HttpResponse

# Create your views here.
def post_view(request):
    return HttpResponse('Welcome the the Bullletin Board')

