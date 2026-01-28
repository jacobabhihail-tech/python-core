from django.contrib import admin
from .models import Expense

#admin.site.register(Expense)
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_dispaly = ('id','name', 'amount', 'created-at')
    list_filter = ('created_at',)
    search_fields =('id','name',)
    ordering = ('-created_at',)

#ordering = ('created_at',)     # Oldest → Newest
#ordering = ('-created_at',)    # Newest → Oldest ✅