from django.shortcuts import render
from .models import Register
from django.http.response import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.
def index(request):
    ob1=Register.objects.all()
    return render(request,"index.html",{"val":ob1})
def Regi(request):
    Name=request.POST['name']
    Place=request.POST['place']
    Age=request.POST['age']
    Email=request.POST['email']
    # return render(request,"index.html")

    ob=Register()
    ob.Name=Name
    ob.Place=Place
    ob.Age=Age
    ob.Email=Email
    ob.save()
    return HttpResponse("<script>alert('Inserted successfully');window.location='/view'</script>")
def view(request):
    ob2=Register.objects.all()
    return render(request,"view.html",{"val":ob2})
def deleteUser(request,id):
    ob = Register.objects.get(id=id)
    ob.delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/view'</script>")
def editUser(request,id):
    ob3 = Register.objects.get(id=id)
    request.session['did']=id
    return render(request,"edit.html",{"var":ob3})
def inserteditUser(request):
    Name=request.POST['name']
    Place=request.POST['place']
    Age=request.POST['age']
    Email=request.POST['email']
    ob4=Register.objects.get(id=request.session['did'])
    ob4.Name=Name
    ob4.Place=Place
    ob4.Age=Age
    ob4.Email=Email
    ob4.save()
    return HttpResponse("<script>alert('edited successfully');window.location='/view'</script>")
# def viewpagination(request):
#     ob5=Register.objects.all()
#     items=2
#     paginator = Paginator(ob5, items)
#     page = request.GET.get('page')
#     try:
#         current_page = paginator.page(page)
#     except PageNotAnInteger:
#         current_page = paginator.page(1)
#     except EmptyPage:
#         current_page = paginator.page(paginator.num_pages)
#     return render(request, 'view.html', {'current_page': current_page})
def search(request):
    if request.method == 'POST':
        search_term = request.POST.get('searchitems', '')
        results = Register.objects.filter(Q(Name__icontains=search_term) |
            Q(Place__icontains=search_term) |
            Q(Age__icontains=search_term) |
            Q(Email__icontains=search_term))
        return render(request, 'view.html', {'val': results})
    return render(request, 'view.html', {'val': Register.objects.all()})

