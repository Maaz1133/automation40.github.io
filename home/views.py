from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from datetime import datetime
from home.models import home1 ,BlogPost
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User

from .forms import BlogPostForm



# Create your views here.

def home_new(request):
    if request.method == "POST":
        # process the form data and save it to the database
        name = request.POST.get('name')
        email = request.POST.get('email')
        message1 = request.POST.get('message1')
        home = home1(name=name, email=email, message1=message1, date=datetime.today())
        home.save()
        messages.success(request, 'Your message has been sent!')
        # redirect to the same page to clear the form
        return redirect('home')
    else:
         allPosts= BlogPost.objects.all()
         print(allPosts)
         context={'allPosts': allPosts}
         return render(request, 'index.html',context)
    


def Arti(request):
    return render(request, 'newarti.html') 



def chatgpt(request):
    return render(request, 'chatgpt.html') 


def loginmyy(request):
     context = {}
     if request.method == 'POST':
        emailin = request.POST.get('emailin')
        passwordin = request.POST.get('password')
        print(emailin, passwordin)
        user = authenticate(request, username=emailin, password=passwordin)
        if user is not None:
            
            login(request, user)
            context['username'] = request.user.username
            
            return redirect('home')
        else:
            messages.error(request, 'your password or email is invalid')
     else:
       error = None
     return render(request, 'index.html')
    

def signup(request):
  if request.method == 'POST':
        emailup = request.POST.get('email')
        passwordin = request.POST.get('pass')
        password_con= request.POST.get('passcon')
        if passwordin==password_con:
         print(emailup,passwordin,password_con)
         my_user=User.objects.create_user(username=emailup, email=emailup,password=passwordin)
         messages.success(request, 'User created successfully')
         return redirect('loginmyy')
        else:
         messages.error(request, 'Password and confirm password are incorrect')   
         return redirect('home')
  else:
    error = None
    return render(request, 'index.html')


def logoutPage(request):
    logout(request)
    return redirect('home')

def automation(request):
   
    return render(request, 'automation.html')

 
def search(request):
    query = request.GET.get('q')
    print(query)
    if query:
        # do the search using the query string
        results = MyModel.objects.filter(title__icontains=query)  # use the 'title' field
    else:
        results = []
    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search_results.html', context)

def create_blog_post(request):
     allPosts= BlogPost.objects.all()
     print(allPosts)
     context={'allPosts': allPosts}
     return render(request, "/", context)


def edit_blog_post(request, URL):
          post = BlogPost.objects.get(URL=URL)
          context = {'post': post}
          
          return render(request, 'add_post.html', context)




