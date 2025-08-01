from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_student, name='students'),
    path("create/", views.create_student, name='create'),
    path("update/<int:pk>", views.update_student, name='update'),
    path("delete/<int:pk>", views.delete_student, name='delete')

]



