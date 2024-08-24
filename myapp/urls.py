from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.upload_image, name='upload_image'),
    path('edit/<int:image_id>/', views.edit_image, name='edit_image'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('signup/', views.signup, name='signup'),
]
