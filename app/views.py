from django.shortcuts import render

# Create your views here.
def homepage(request):
    name="tolhs"
    age=23




    context={
        "onoma": name,
        "etwn": age,
    }
    return render(request, "app/index.html", context)