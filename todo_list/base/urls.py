from django.urls import path

from .views import main,login,register,task_form,task_confirm,logout,change_status

urlpatterns = [
    path("main/", main, name="main"),
    path("login/",login,name="login"),
    path("",register,name="register"),
    path("form/",task_form,name = "form"),
    path("delete/<int:task_id>", task_confirm,name="delete"),
    path("logout",logout,name = "logout"),
    path('change-status/<int:task_id>/', change_status, name='change_status'),
]