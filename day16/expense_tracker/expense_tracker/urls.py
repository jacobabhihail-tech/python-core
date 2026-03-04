from django.urls import path
from .views import expense_list

urlpatterns = [
    path('admin/', admin.site.urls)
    path('', include('expenses.urls')),
]