from django.shortcuts import render


from core.erp.models import Category, Product
# Create your views here.
# def my_first_view(request):
#     return render(request, "base.html", dict(name='Krull', where='Mountain'))
def my_first_view(request):
    datab = Category.objects.all()
    content = {
        'url': '/prueba/uno',
        'data': datab
    }
    return render(request, 'base.html', content)


def my_second_view(request):
    datab = Product.objects.all()
    content = {
        'url': '/prueba/uno',
        'data': datab
    }
    return render(request, 'second.html', content)

