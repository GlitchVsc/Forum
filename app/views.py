from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    name="tolhs"
    age=23

    user = CustomUser.objects.get(id=1)



    context={
        "onoma": name,
        "etwn": age,
        "user": user,
    }
    return render(request, "app/index.html", context)