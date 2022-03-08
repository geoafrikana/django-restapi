from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict
from products.models import Product

def api_home(request, *args, **kwargs): 
    model_data = Product.objects.all().order_by('?').first()
    if model_data:
        data = model_to_dict(model_data, fields = ['id'])
    return JsonResponse(data)

