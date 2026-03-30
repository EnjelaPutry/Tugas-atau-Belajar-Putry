from django.shortcuts import render

# Ini fungsi untuk menampilkan halaman utama
def index(request):
    return render (request,'index.html')
