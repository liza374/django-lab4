from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def news_page(request):
    return render(request, 'news.html')
