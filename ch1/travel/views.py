from django.shortcuts import render
from .models import Category, Post


def main(request):
    return render(request, 'travel/_main.html')

def local_list(request):
    queryset = Category.objects.all()

    return render(request, 'travel/local_list.html', {
        'local' : queryset
    })