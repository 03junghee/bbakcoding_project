# bbakcoding_project/urls.py
from django.contrib import admin
from django.urls import path
from study import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), # 메인 페이지 연결
]