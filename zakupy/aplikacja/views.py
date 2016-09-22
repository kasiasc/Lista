from django.shortcuts import render
from django.http import HttpResponse
from aplikacja.models import Product
from aplikacja.models import List

def index(request):
    product_list = Product.objects.order_by()
    list_list = List.objects.order_by()
    context_dict = {'lists': list_list,
    'products': product_list,}

    return render(request, 'aplikacja/index.html', context_dict)
	
#def details(request,details_id):
#    product_list = Product.objects.order_by()
#    context_dict = {'products': product_list,
#    }	
#	
#   return render(request, 'aplikacja/details.html', context_dict)
#
#   return HttpResponse("Tu beda listy zakupow!")
# Create your views here.
