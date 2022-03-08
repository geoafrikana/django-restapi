from django.http import JsonResponse, HttpResponse
from products.models import Product

def api_home(request, *args, **kwargs):
    body = request.body.decode('utf-8')
    data = {}
    try:
        data = json.loads(body)
        data = data['content']
    except:
        print('not working')

    print(data)
    print(request.GET)
    print(request.POST)
    print(request.headers)
    
    return JsonResponse(data)

