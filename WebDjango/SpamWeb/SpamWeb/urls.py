"""SpamWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from . import view
# from . import search
# from . import webspam
# from django.views.static import serve
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('hello/',view.hello),
#     path('search-form/',search.search_form),
#     path('search/',search.search),
#     path('webspam/',webspam.webspam_main),
# ]

from django.contrib import admin
from django.conf.urls import url
from . import view
from . import search
from . import webspam
from django.views.static import serve

urlpatterns = [
    url('admin/', admin.site.urls),
    url('hello/',view.hello),
    url('search-form/',search.search_form),
    url('search/',search.search),
    url('webspam/',webspam.webspam_main),
]