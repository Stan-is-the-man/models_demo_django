from django.urls import path

from models_demo.web.views import index, delete_employee, department_details

urlpatterns = (
    path('', index, name='index'),
    path('delete/<int:pk>/', delete_employee, name='delete employee'),
    path('departments/<int:pk>/', department_details, name='details department'),

)
