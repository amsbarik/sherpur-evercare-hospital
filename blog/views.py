from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required

from core.views import is_superuser
from .models import Blog, BlogCategory
from .forms import BlogForm, BlogCategoryForm


# Create your views here.
def blogs(request):
    blogs = Blog.objects.filter(is_active=True).order_by('published_at').all()

    return render(request, 'blog/blogs.html', {'blogs': blogs})


# blog details 
def blog_details(request, pk):
    blog = Blog.objects.get(id=pk)

    return render(request, 'blog/blog_details.html', {'blog': blog})




# admin panel views ///////////////////////////////////////

# BlogCategory views 
@login_required
@user_passes_test(is_superuser)
def blog_category_list(request):
    blog_categories = BlogCategory.objects.order_by('created_at').all()
    
    return render(request, 'blog/admin/blog_category_list.html', {'blog_categories': blog_categories})


# blog_category create & update form view 
@login_required
@user_passes_test(is_superuser)
def blog_category_form(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            form = BlogCategoryForm()
        else:
            blog_category = BlogCategory.objects.get(id=pk)
            form = BlogCategoryForm(instance=blog_category)
            
        return render(request, 'blog/admin//blog_category_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = BlogCategoryForm(request.POST, request.FILES)
        else:
            blog_category = BlogCategory.objects.get(id=pk)
            form = BlogCategoryForm(request.POST, request.FILES, instance=blog_category)

        if form.is_valid():
            form.save()
            
        return redirect('blog_category_list')


# blog_category delete view 
# @login_required
# @user_passes_test(is_superuser)
# def blog_category_delete(request, pk):
#     blog_category = BlogCategory.objects.get(id=pk)
#     blog_category.delete()
#     return redirect('blog_category_list')


# blogs 
@login_required
@user_passes_test(is_superuser)
def blog_list(request):
    blogs = Blog.objects.order_by('created_at').all()
    
    return render(request, 'blog/admin//blog_list.html', {'blogs': blogs})


# blog create & update form view 
@login_required
@user_passes_test(is_superuser)
def blog_form(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            form = BlogForm()
        else:
            blog = Blog.objects.get(id=pk)
            form = BlogForm(instance=blog)
            
        return render(request, 'blog/admin//blog_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = BlogForm(request.POST, request.FILES)
        else:
            blog = Blog.objects.get(id=pk)
            form = BlogForm(request.POST, request.FILES, instance=blog)

        if form.is_valid():
            form.save()
            
        return redirect('blog_list')


# blog delete view 
# @login_required
# @user_passes_test(is_superuser)
# def blog_delete(request, pk):
#     blog = Blog.objects.get(id=pk)
#     blog.delete()
#     return redirect('blog_list')





