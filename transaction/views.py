from .serializers import TransactionSerializer, DateRangeSerializer
from .models import Transaction
from rest_framework.viewsets import ModelViewSet
from common.views import LoggerAPIView
import datetime
from rest_framework.response import Response


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class TransactionData(LoggerAPIView):
    """Get transaction data for current month or a date range"""

    def get_data_date_range(self, start, end):
        transactions = Transaction.objects.filter(created_utc__gte=start, created_utc__lte=end).all()

        total_earn = sum(item.amount for item in transactions if item.transaction_type == 0)
        total_spend = sum(item.amount for item in transactions if item.transaction_type == 1)
        total_transaction = transactions.count()

        serialized_data = TransactionSerializer(transactions, many=True)
        data = {
            "data": serialized_data.data,
            "total": {
                "transaction": total_transaction,
                "earn": total_earn,
                "spend": total_spend
            }
        }
        return data

    def get(self, request):
        """By default we'll get this month data"""

        today = datetime.date.today()
        month_first_day = today - datetime.timedelta(days=today.day)
        data = self.get_data_date_range(month_first_day, today)
        return Response(data, 200)
    
    def post(self, request):
        serializer = DateRangeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            data = self.get_data_date_range(data['date_from'], data['date_to'])
            return Response(data, 200)
