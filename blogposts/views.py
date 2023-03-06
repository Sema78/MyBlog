from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView, LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, UserRegistrationForm, LoginForm

# Create your views here.

from django.shortcuts import render
from .models import Post


def home(request):
    return render(request, 'blogposts/main.html', {'home': home})

def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(post_list, 10) # 10 post per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'blogposts/post_list.html', context)



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    print([post.title])
    return render(request, 'blogposts/post_detail.html', context)

def post_list_short(request):
    posts = Post.objects.all().order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blogposts/post_list_short.html', context)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blogposts/post_form.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'blogposts/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, f"Welcome back, {username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'blogposts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

def password_reset(PasswordResetView):
    template_name = 'registration/password_reset_form.html'