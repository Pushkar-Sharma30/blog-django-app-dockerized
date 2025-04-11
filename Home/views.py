from django.shortcuts import render, HttpResponse,redirect

from Blog import settings
# from Home.razorpay_integration.razorpay_integration import initiate_payment
from .models import Blog, Category, Contact
from django.contrib.auth.models import User
import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q


# from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


# client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))


# Create your views here.



def home(request):
    blogs = Blog.objects.all().order_by('id')
    # users = User.objects.all()
    # u = User.objects.get(pk=request.user.pk)
    # red = Blog._meta.get_fields()
    # print(red)
    # all_post = Post.objects.all().
    paginator = Paginator(blogs, 2, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
   
    categories = Category.objects.all()
    print(request.GET)
    categoryID = request.GET.get('category')
    print(categoryID)
    if categoryID:
        # blogs = Blog.objects.filter(category=categoryID)
        blogs = Blog.objects.filter(category=categoryID).order_by('id')

        paginator = Paginator(blogs, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        # blogs = Blog.objects.all()
        page_obj = paginator.get_page(page_number)

        #filter and pagintion dont work 
        


    context = {
        # 'users':users,
        'blogs':blogs,
        'categories':categories,
        'page_obj':page_obj,
        'categoryID':categoryID
    }
    # print(context)
    return render(request,'blog.html',context)


@login_required(login_url="login")
def add_blog(request):
    
    error_message = None
    categories = Category.objects.all()
  
    if request.method == 'GET':
        categories = Category.objects.all()
        context={
        'categories':categories,
        }
        return render(request,'add_blog.html', context)
    
# else block
    else:

        
        title = request.POST.get('title')
        
        content = request.POST.get('content')
        
        # author = User.objects.get(username=request.POST.get('author'))
        # CartItem.objects.create(user_id=1, product_id=1, quantity=1)
        category = Category.objects.get(name=request.POST.get('category'))
        print(category)
        user = User.objects.get(username=request.user) # or obtain the user however you lik
        # category = request.POST.get('category')
        image = request.FILES.get('uploadimg')
        new_post = Blog(title=title,content=content, image=image, category=category, authors=user) # author=author
        if (not title):
            error_message = 'Title is required'
        elif not content:
            error_message = "Content is required"

        elif not category:
            error_message = "Category is required"

        elif not image:
            error_message = "Cover image is required"

        if not error_message:
            # messages.success(request, 'Registered successfully')
            new_post.save()
            # new_post.user = request.user
            return redirect('blog')
        else:
            data = {
                'error': error_message,
                'categories':categories,
                # 'value': value,
            }
        
        return render(request,'add_blog.html', data)

         
    # return render(request,'add_blog.html', context)


# @login_required(login_url="login")
# def update_blog(request, id):
#     categories = Category.objects.all()
#     context={
#         'categories':categories,
#     }
    

#     if request.method == 'POST' and request.FILES['uploadimg']:
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         # CartItem.objects.create(user_id=1, product_id=1, quantity=1)
#         category = Category.objects.get(name=request.POST.get('category'))
#         print(category)
#         # category = request.POST.get('category')
#         image = request.FILES.get('uploadimg')
#         new_post = Blog(id=id, title=title,content=content, image=image, category=category)
#         new_post.save()
#         return redirect('blog')
#     return render(request,'update_blog.html', context)









@login_required(login_url="login")
def read_blog(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'read_blog.html', {'blog':blog})



# def blogs_by_category(request, id):
#     if request.method == "GET":
#         categoryID = request.GET.get('category')
#         cat_blog = Blog.objects.filter(id=id)
#         context = {
#             'cat_blog': cat_blog,
#         }
#         return render(request, 'blog.html',context)


# def show_blog(request):
#     blogs = Blog.objects.all()
#     context = {
#         'blogs':blogs
#     }
#     print(context)
#     return render(request, 'home.html',context)

def about(request):
    return render(request, 'about.html')

@login_required(login_url="login")
def contact(request):
    return render(request, 'contact.html')

@login_required(login_url="login")
def premium(request):
  return render(request, 'premium.html')



@login_required(login_url="login")
def search(request):
    if request.method == "GET":
        search_result = request.GET['search']
        
        # blogs = Blog.objects.all()
        # if Q:
        #     blogs = blogs.filter(Q(title__icontains = search_result) | Q(content__icontains = search_result) | Q(authors__username__icontains = search_result) | Q(category__name__icontains = search_result))
        blogs = Blog.objects.all().order_by('id')

#     paginator = Paginator(blogs, 2, orphans=1)
        paginator = Paginator(blogs, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        #  print(categoryID)
        if search_result:
            # blogs = Blog.objects.filter(category=categoryID)
            blogs = Blog.objects.filter(title__icontains=search_result).order_by('id')

            paginator = Paginator(blogs, 1)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        context = {
        'blogs' : blogs,
        'page_obj':page_obj,
        'search_result':search_result
        }
        return render(request, 'blog.html',context)
    elif request.method=='POST':
        return render(request,'blog.html')  
    else:
        return HttpResponse("An error occured!")


        
        
#  blogs = Blog.objects.all().order_by('id')

#     paginator = Paginator(blogs, 2, orphans=1)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
   
#     categories = Category.objects.all()
#     print(request.GET)
#     categoryID = request.GET.get('category')
#     print(categoryID)
#     if categoryID:
#         # blogs = Blog.objects.filter(category=categoryID)
#         blogs = Blog.objects.filter(category=categoryID).order_by('id')

#         paginator = Paginator(blogs, 1)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#     else:
#         # blogs = Blog.objects.all()
#         page_obj = paginator.get_page(page_number)

#         #filter and pagintion dont work 
        


    # context = {
    #     # 'users':users,
    #     'blogs':blogs,
    #     'categories':categories,
    #     'page_obj':page_obj,
    #     'categoryID':categoryID
    # }
    # # print(context)
    # return render(request,'blog.html',context)







def base(request):
    return render(request, 'common/base.html')


@login_required(login_url="login")
def create_blog(request): 
    
    error_message = None
    categories = Category.objects.all()
  
    if request.method == 'GET':
        categories = Category.objects.all()
        context={
        'categories':categories,
        }
        return render(request,'create_blog.html', context)
    
# else block
    else:

        
        title = request.POST.get('title')
        
        content = request.POST.get('content')
        
        # author = User.objects.get(username=request.POST.get('author'))
        # CartItem.objects.create(user_id=1, product_id=1, quantity=1)
        category = Category.objects.get(name=request.POST.get('category'))
        print(category)
        user = User.objects.get(username=request.user) # or obtain the user however you lik
        # category = request.POST.get('category')
        image = request.FILES.get('uploadimg')
        new_post = Blog(title=title, content=content, image=image, category=category, authors=user) # author=author
        print(new_post)
        # if (not title):
        #     error_message = 'Title is required'
        # elif not content:
        #     error_message = "Content is required"

        # elif not category:
        #     error_message = "Category is required"

        # elif not image:
        #     error_message = "Cover image is required"

        # if not error_message:
            # messages.success(request, 'Registered successfully')
        new_post.save()
            # new_post.user = request.user
        return redirect('blog')
        # else:
        data = {
                # 'error': error_message,
             'categories':categories,
                # 'value': value,
        }
        
        return render(request,'create_blog.html', data)
    
@login_required(login_url="login")
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_text = Contact(name=name, email=email, message=message)
        contact_text.save()
        messages.success(request, "Thank you for contacting us. <br> We'll get back to you soon.")
        redirect('contact')
    return render(request, 'contact.html')



@login_required(login_url="login")
def delete_blog(request, id):
        blog = Blog.objects.get(id=id).delete()
        return redirect('blog')









def update_blog(request, id):
    blog = Blog.objects.get(id=id)
    categories = Category.objects.all()
    context = {
         'blog': blog,
         'categories':categories,
     }
    
    if request.method == 'POST' and request.FILES['uploadimg']:
        title = request.POST.get('title')
        content = request.POST.get('content')
        # CartItem.objects.create(user_id=1, product_id=1, quantity=1)
        user = User.objects.get(username=request.user)
        category = Category.objects.get(name=request.POST.get('category'))
        print(category)
        # category = request.POST.get('category')
        image = request.FILES.get('uploadimg')
        new_post = Blog(id=id, title=title,content=content, image=image, category=category, authors=user)
        new_post.save()
        return redirect('blog')
    return render(request,'update_blog.html', context)
    