from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>/',views.delete_expense, name='delete_expense'),
    path('edit/<int:id>/', views.edit_expense, name='edit_expense'),
    path('login/', views.login_view, name='login'),
    path('logut/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]