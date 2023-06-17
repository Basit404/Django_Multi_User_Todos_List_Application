from django.shortcuts import render, HttpResponse, redirect

# importing authenticate, login and logout
from django.contrib.auth import authenticate, login as loginUser, logout

# importing usercreationform and authenticationform
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# importing custom classes from forms and models
from home.forms import TODOForm
from home.models import TODO

# importing login_required
from django.contrib.auth.decorators import login_required

# Create your views here.


# function for table of homepage
@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user=user).order_by("priority")
        return render(request, "home.html", context={'form': form, 'todos': todos})


# function for login into Application
def login(request):
    if request.method == "GET":
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, "login.html", context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect("/home")
        else:
            context = {"form": form}
            return render(request, "login.html", context=context)


# function for sign up into Application
def signup(request):
    if request.method == "GET":
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "signup.html", context=context)
    else:
        form = UserCreationForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect("/login")
        else:
            return render(request, "signup.html", context=context)


# function for adding data
@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect("home")
        else:
            return render(request, "home.html", context={'form': form})


# function for deleting data
def delete_todo(request, id):
    TODO.objects.get(pk = id).delete()
    return redirect("home")


# function for changing status to "Pending" or "Completed"
def change_todo(request, id, status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect("home")


# function for logout from Application
def signout(request):
    logout(request)
    return redirect('login')