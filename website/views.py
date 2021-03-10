from django.shortcuts import render

posts = [
    
    {
         'author': 'Noah',
         'title': 'Website post 1',
         'content': 'First post content',
         'date_posted': 'March 9th 2021',
     
     },
    {
         'author': 'Jane Doe',
         'title': 'Website post 2',
         'content': 'Second post content',
         'date_posted': 'June 9th 2021',
     
     }

    ]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'website/home.html',context)


def about(request):
    return render(request, 'website/about.html', {'title': 'About'})