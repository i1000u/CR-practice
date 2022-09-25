from django.contrib import admin
from django.urls import path
import cashbookapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',cashbookapp.views.main, name='main'),
    path('write/', cashbookapp.views.write, name='write'),
    path('read/',cashbookapp.views.read, name='read'),
    path('detail/<str:id>/',cashbookapp.views.detail, name='detail'),
]
