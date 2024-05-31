from django.shortcuts import get_object_or_404, render
from .models import PictureBook, Picture
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserEditForm, CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
from taggit.models import Tag
import json


def index(request):
    query = request.GET.get('q')
    if query:
        books = PictureBook.objects.filter(
            Q(title__icontains=query) |
            Q(tags__name__icontains=query) |
            Q(author__icontains=query)
        ).distinct()
    else:
        books = PictureBook.objects.all()

    return render(request, 'library/home_page.html', {
        'books': books,
        'tags': Tag.objects.all()[:5],
        'user': request.user
    })

def book_list(request):
    query = request.GET.get('q')
    if query:
        books = PictureBook.objects.filter(
            Q(title__icontains=query) |
            Q(tags__name__icontains=query) |
            Q(author__icontains=query)
        ).distinct()
    else:
        books = PictureBook.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(PictureBook, pk=pk)
    #page_number = request.GET.get('page', 0)
    #picture = get_object_or_404(Picture, book=book, page_number=page_number)
    return render(request, 'library/reader.html', {'book': book})

def books_by_tag(request, tag_slug):
    books = PictureBook.objects.filter(tags__name__in=[tag_slug])
    return render(request, 'library/book_list.html', {'books': books})

def register(request):
    error_msg = {}
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('register')
        else:
            error_msg = form.errors
    else:
        form = UserRegistrationForm()
    print("error_msg: ", dict(form.errors))
    context = {
        'form': form,
        'error_msg': json.dumps(error_msg) if error_msg else '{}'
    }
    return render(request, 'library/signin-signup.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'library/signin-signup.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def account_view(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            # Update the user's session to prevent logout
            update_session_auth_hash(request, password_form.user)
            messages.success(request, 'Your account has been updated!')
            return redirect('account')
    else:
        user_form = UserEditForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'library/account.html', {
        'user_form': user_form,
        'password_form': password_form
    })


def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('index')
    return render(request, 'library/delete_account.html')
