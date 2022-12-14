from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from django.contrib import messages
from .models import*
from .forms import StockCreateForm, StockSearchForm, StockUpdateForm

# Create your views here.

def home(request):
    title = 'Welcome: This is the Home Page'
    form = 'Welcome: This is the Home Page'
    context = {
        "title": title,
        "test": form,
    }
    return render(request, "home.html",context)


def list_items(request):
    header = 'LIST OF ITEMS'
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {
        "header": header,
        "queryset": queryset,
        "form": form,
    }
    if request.method =='POST':#if search button is clicked
        queryset = Stock.objects.filter(#category__icontains=form['category'].value(),
                                        item_name__icontains=form['item_name'].value()
                                        )

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'ITEM_NAME', 'QUANTITY'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.category, stock.item_name, stock.quantity])
            return response

        context = {
            "form": form,
            "header": header,
            "queryset": queryset
        }    
    return render(request, "list_items.html",context)


def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Added successfully')
        return redirect('/list_items')
    context = {
        "form" : form,
        "title" : "Add Item",
    }
    return render(request, "add_items.html", context)



def update_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully')
            return redirect('/list_items')
    
    context = {
        'form': form
    }


    return render(request, 'add_items.html', context)


def delete_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Deleted successfully')
        return redirect('/list_items')
    return render(request, 'delete_items.html')



def stock_detail(request, pk):
    queryset = Stock.objects.get(id=pk)
    context = {
        #"title" : queryset.item_name,
        "queryset" : queryset, #used to display the details of the item
    }
    return render(request, "stock_detail.html", context)