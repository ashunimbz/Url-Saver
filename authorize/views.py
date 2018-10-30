from django.shortcuts import render,redirect
from registration.forms import RegistrationForm
from authorize.forms import CategoryForm,UrlForm
from django.http import HttpResponse
from authorize.models import Category
# Create your views here.

def home(request):
    if request.user.is_authenticated:
         category = request.user.categories.all()
         c = category.count()
         return render(request , 'home.html' , {'category':category,'c':c})
    else:
        return redirect('/accounts/register/')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            inst =  form.save(commit=False)
            flag = True
            for categories in request.user.categories.all():
                if categories.name == inst.name:
                    flag = False
            if flag:
                inst.users = request.user
                inst.save()
                return redirect('authorize:home')
            else:
                return render(request, 'cat.html', {'form': form , 'flag' :True})
    else:
        form =  CategoryForm()
        return render(request , 'cat.html',{'form':form , 'flag' :False})


def add_url(request,cat_id):
    if request.method == 'POST':
        form  =  UrlForm(request.POST)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.category  = Category.objects.get(id = cat_id)
            inst.save()
        return redirect('authorize:show_urls',cat_id = cat_id)
    else:
        form = UrlForm()
        category =  Category.objects.get(id = cat_id)
        return render(request,'url.html',{'form':form , 'category':category})



def show_urls(request, cat_id):
    cat= Category.objects.get(id = cat_id)
    return render(request  ,  'detail_url.html' , {'cat':cat})


