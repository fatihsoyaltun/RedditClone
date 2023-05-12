from django.shortcuts import render

# Create your views here.

def profilayarlar(request):
    return render(request, 'settingsProfil.html')

def genelayarlar(request):
    return render(request, 'UserSettings.html')