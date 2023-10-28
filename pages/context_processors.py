from .models import About
   
def about(request):
    about_obj = About.objects.first()
    return {'about': about_obj}