from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="index"),
    path("<id>",views.take_test,name="take_test"),
    path("api/<id>",views.api_ques,name="api_ques"),
]