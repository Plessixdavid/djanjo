from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from mysite.models import Ideogramm
import random

# Create your views here.

def index(request):
    css = "mysite/style.css"
    return render(request, "mysite/index.html", {"css":css})


def hanasuregister(request):
    
    css = "mysite/inscrip_style.css"
    return render(request, "mysite/inscription.html", {"css":css})

@login_required
def hanasuhome(request):
    css = "mysite/home_style.css"
    return render(request, "mysite/home_page.html", {"css":css})

def hanasugame(request):

    ideogramms = Ideogramm.objects.all()
    random_ideogramm = random.choice(ideogramms)
    random_ideogramm2 = random.choice(ideogramms)
    image_ideogramm = random.choice([random_ideogramm, random_ideogramm2])
    css = "mysite/maneki_style.css"
    print(random_ideogramm)
    print(random_ideogramm2)
    print(image_ideogramm)



    context = {
        "image" : image_ideogramm.Img_link,
        "random_ideogramm2": random_ideogramm2,
        "random_ideogramm": random_ideogramm,
        "css":css
    }
    return render(request, "mysite/maneki.html",context )

def contact(request):
    css = "mysite/home_style.css"
    return render(request, "mysite/contact.html", {"css":css})