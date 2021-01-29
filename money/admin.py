from django.contrib import admin
from .models import Transaction, Tag, Budget


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'transaction_type', 'title', 'short_note', 'created_utc', 'updated_utc']

    def short_note(self, obj):
        return obj.body[:30]

class BudgetAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'month', 'created_utc', 'updated_utc']

    def month(self, obj):
        return obj.updated_utc.strftime("%B, %Y")

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(Tag, TagAdmin)