from rest_framework import serializers
import datetime


class DateRangeValidator:

    today = datetime.date.today()

    def __init__(self, base):
        self.base = base
        self.date_from = self.base['date_from']
        self.date_to = self.base['date_to']

        if self.date_from > self.date_to:
            message = 'date_to should not greater than date_from.'
            raise serializers.ValidationError(message)
        
        if self.date_from > self.today or self.date_to > self.today:
            message = 'Date should not greater than today.'
            raise serializers.ValidationError(message)
