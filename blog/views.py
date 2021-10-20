from django.shortcuts import render
#from django.http import HttpResponse

posts = [

    {
        'author': 'mariele',
        'title': 'book rec of month',
        'content': 'book rec',
        'date_posted' : '28 sept 2021'
    },

       {
        'author': 'anonymous',
        'title': 'book rec of month',
        'content': 'book rec',
        'date_posted' : '20 sept 2021'
    }
]

def home(request):

    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
