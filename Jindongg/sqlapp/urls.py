from django.conf.urls import url
from sqlapp import views

urlpatterns = [
    url(r'^BOSS/$', views.BOSS),
    url(r'^login/',views.login),
    url(r'^regist/',views.regist),
    url(r'^flow1/',views.flow1),
    url(r'^flow2/',views.flow2),
    url(r'^flow3/',views.flow3)
]
