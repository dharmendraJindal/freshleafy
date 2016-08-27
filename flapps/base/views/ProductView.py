from django.shortcuts import render


def product_view(request):
    template = 'app.html'
    return render(request, template)