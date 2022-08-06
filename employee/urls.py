from django.urls import path
from .views import *


urlpatterns = [
    path("",home),
    path("home/",home),
    path("add-employee/",emp_add),
    path("delete-employee/<int:idnum>",emp_delete),
    path("update-employee/<int:idnum>",emp_update),
    path("do-update-employee/<int:idnum>",do_emp_update),
]