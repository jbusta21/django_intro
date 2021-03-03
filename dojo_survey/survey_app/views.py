from django.shortcuts import render, redirect

def index(request):
    return render(request, 'form.html')

def process(request):
    if request.method == 'POST':
        context = {
            'yourname': request.POST.get('name'),
            'dojolocation': request.POST.get('dojolocation'),
            'favoritelanguage': request.POST.get('favoritelanguage')
        }
        return render(request, 'result.html', context)
    return render(request, 'result.html')
