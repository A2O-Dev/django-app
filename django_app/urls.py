"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.shortcuts import redirect
from django.urls import path, include
from product_api import urls as product_urls
from rest_framework.authtoken.views import obtain_auth_token
from product_api.views import ApiRoot

urlpatterns = [
    path('', ApiRoot.as_view()),
    path('api/auth/', include('rest_framework.urls')),
    path('oauth/token/', obtain_auth_token),
    path('api/products/', include(product_urls))
]
