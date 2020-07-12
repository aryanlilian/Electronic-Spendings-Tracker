from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm, BugetForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import is_authenticated


def buget_assembly(buget):
    total_buget = 0
    for i in buget:
        total_buget += i.amount
    return total_buget


def spendings_assembly(spendings):
    total_spendings = 0
    for i in spendings:
        total_spendings += i.amount
    return total_spendings


def spendings_percentages_of_buget(buget, spendings):
    spendings_percent = 0
    if buget > 0:
        spendings_percent = round((spendings / buget) * 100, 2)
    return spendings_percent


def savings_percentages_of_buget(buget, savings):
    savings_percent = 0
    if buget > 0:
        savings_percent = round((savings / buget) * 100, 2)
    return savings_percent


@login_required
def dashboard(request):
    buget = Buget.objects.filter(user=request.user)
    spendings = Spending.objects.filter(user=request.user)
    total_buget = buget_assembly(buget)
    total_spendings = spendings_assembly(spendings)
    total_savings = total_buget - total_spendings
    spendings_percent = spendings_percentages_of_buget(
        total_buget, total_spendings)
    savings_percent = savings_percentages_of_buget(total_buget, total_savings)
    context = {
        'title': 'Dashboard',
        'total_spendings': total_spendings,
        'total_buget': total_buget,
        'total_savings': total_savings,
        'spendings_percent': spendings_percent,
        'savings_percent': savings_percent,
        'spendings': spendings,
        'buget': buget,
    }
    return render(request, 'users/dashboard.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        buget_form = BugetForm(request.POST, instance=request.user.buget)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid() and buget_form.is_valid():
            buget_form.save()
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        buget_form = BugetForm(instance=request.user.buget)
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'buget_form': buget_form,
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Profile'
    }
    return render(request, 'users/profile.html', context)


@is_authenticated
def login_page(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'username or password is incorrect')
    return render(request, 'users/login.html')


@is_authenticated
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'users/register.html', context)


def logout_page(request):
    logout(request)
    return render(request, 'users/logout.html', {'title': 'Logout'})


def create_spending(request):
    Spending.objects.create(user=request.user, name=request.POST['spending_name'],
                            category=request.POST['category'], amount=request.POST['amount'])
    return redirect('dashboard')


def delete_spending(request, pk):
    spending = Spending.objects.get(id=pk)
    if request.method == 'POST':
        spending.delete()
        return redirect('dashboard')
    context = {
        'item': spending
    }
    return render(request, 'users/delete.html', context)