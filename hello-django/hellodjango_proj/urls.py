"""
URL configuration for hellodjango_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
import math

# def rectangle_area(request):
#     try:
#         height = float(request.GET.get('height', 8))
#         width = float(request.GET.get('width', 3))
#         area = height * width
#         return HttpResponse(f'<p>Rectangle Area: {area}</p>')
#     except ValueError:
#         return HttpResponse('<p>Invalid input</p>')
    
# def rectangle_perimeter(request):
#     try:
#         height = float(request.GET.get('height', 5))
#         width = float(request.GET.get('width', 4))
#         perimeter = 2 * (height + width)
#         return HttpResponse(f'<p>Rectangle Perimter: {perimeter}</p>')
#     except ValueError:
#         return HttpResponse('<p>Invalid input</p>')
    
# def circle_area(request):
#     try:
#         radius = float(request.GET.get('radius', 16))
#         radius_squared = radius ** 2
#         area = math.pi * radius_squared
#         return HttpResponse(f'<p>Circle area: {area}</p>')
#     except ValueError:
#         return HttpResponse('<p>Invalid input</p>')

# def circle_perimeter(request):
#     try:
#         radius = float(request.GET.get('radius', 16))
#         perimeter = 2 * math.pi * radius
#         return HttpResponse(f'<p>Circle perimeter: {perimeter}</p>')
#     except ValueError:
#         return HttpResponse('<p>Invalid input</p>')

def rectangle_area(request, height, width):
    try:
        area = height * width
        return HttpResponse(f'<p>Rectangle Area: {area}</p>')
    except ValueError:
        return HttpResponse('<p>Invalid input</p>')
    
def rectangle_perimeter(request, height, width):
    try:
        perimeter = 2 * (height + width)
        return HttpResponse(f'<p>Rectangle Perimter: {perimeter}</p>')
    except ValueError:
        return HttpResponse('<p>Invalid input</p>')
    
def circle_area(request, radius):
    try:
        radius_squared = radius ** 2
        area = math.pi * radius_squared
        return HttpResponse(f'<p>Circle area: {area}</p>')
    except ValueError:
        return HttpResponse('<p>Invalid input</p>')

def circle_perimeter(request, radius):
    try:
        perimeter = 2 * math.pi * radius
        return HttpResponse(f'<p>Circle perimeter: {perimeter}</p>')
    except ValueError:
        return HttpResponse('<p>Invalid input</p>')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rectangle/area/<int:height>/<int:width>/', rectangle_area),
    path('rectangle/perimeter/<int:height>/<int:width>/', rectangle_perimeter),
    path('circle/area/<int:radius>/', circle_area),
    path('circle/perimeter/<int:radius>/', circle_perimeter)
]
