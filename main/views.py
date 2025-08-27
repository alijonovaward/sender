import requests
from django.shortcuts import render

def send_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        image = request.FILES.get('image')

        files = {'image': image.file} if image else None
        data = {'name': name, 'surname': surname}

        # Qabul qiluvchi serverga POST yuborish
        url = "http://127.0.0.1:8001/"
        requests.post(url, data=data, files=files)

    return render(request, 'main/form.html')
