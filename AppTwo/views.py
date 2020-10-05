from django.shortcuts import render
from . forms import NewUsersLogin, NewCompany

# Create your views here.
def index(request):
    return render(request, "AppTwo/index.html")


def template(request):
    return render(request "AppTwo/template.html"


def other(request):

    comp = NewCompany()

    if request.method == "POST":
        
        comp = NewCompany(request.POST)
        
        if comp.is_valid():
            comp.save(commit=True)
            return index(request)

        else:
            print("there was an error")
    return render(request, "AppTwo/other.html",{'comp': comp})


def relative(request):
    return render(request, "AppTwo/relative_temp.html")

def users(request):

    form = NewUsersLogin()

    if request.method == "POST":

        form = NewUsersLogin(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("there was an error")

    return render(request, "AppTwo/users.html", {'form': form})
