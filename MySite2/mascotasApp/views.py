from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""def index(request):
    return HttpResponse(
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Perro pastor aleman cachorrito</h1>
        <p>Perro bonito</p>
        <img src="https://images.unsplash.com/photo-1598398386929-4d5370672e9f?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y2FjaG9ycm8lMjBwYXN0b3IlMjBhbGVtYW58ZW58MHx8MHx8fDA%3D" alt="">
    </body>
    </html>
)"""

def mascota2(request):
    return render(request,"index.html")