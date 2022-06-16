from email.headerregistry import Address
from multiprocessing import context
from unicodedata import category
#fr om multiprocessing import context
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
#from scrapy import Item
from .models import book
from .forms import bookform
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
def  home(request):
    k= book.objects.all()
    c=k.count()
    context={'c':c,'k':k}
    return render(request,'demo/base.html',context)
def table(request):
    k= book.objects.all()
    k=k.values()
    #print(k)
       
    context={'k':k,}
    return render(request,'demo/table.html',context) 



@staff_member_required(login_url='/login/')
def createe(request):
    
    if request.method =='POST' :
        book.objects.create(title = request.POST.get('title'), author = request.POST.get('author'),isbn = request.POST.get('isbn'),category = request.POST.get('category'),)
        
        return redirect('/')
    return render(request,'demo/create.html')  




@staff_member_required(login_url='/login/')  
def updateOrder(request, pk):

	order = book.objects.get(id=pk)
	form = bookform(instance=order)

	if request.method == 'POST':
		form = bookform(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/table')

	context = {'form':form}
	return render(request, 'demo/up.html', context)    




@staff_member_required(login_url='/login/')
def deleteOrder(request, pk):
	order =book.objects.get(id=pk)
    
	if request.method == "POST":
		order.delete()
		return redirect('/table')
    
	context = {'item':order}
	return render(request, 'demo/delete.html', context)

