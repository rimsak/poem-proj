from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, ('index.html'))

def article(request):
    return render(request, ('article.html'))
def poem(request):
    return render(request, ('poem.html'))
def blog(request):
    return render(request, ('blog.html'))
def lifestyle(request):
    return render(request, ('lifestyle.html'))
def story(request):
    return render(request, ('story.html'))
def join(request):
    return render(request, ('join.html'))
