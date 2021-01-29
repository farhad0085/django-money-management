from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'transaction_type', 'title', 'short_note', 'created_utc', 'updated_utc']

    def short_note(self, obj):
        return obj.body[:30]


admin.site.register(Transaction, TransactionAdmin)