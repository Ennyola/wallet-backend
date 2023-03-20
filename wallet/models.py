from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from datetime import datetime

# Create your models here.

class Funds(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_balance = models.FloatField(default= 0.00)
    previous_balance = models.FloatField(default= 0.00 )
    money_added = models.FloatField(default = 0.00)
    money_removed = models.FloatField(default= 0.00)

    def __str__(self):
        return self.user.username

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    money_saving = models.FloatField(default=0.00)
    money_spending = models.FloatField(default= 0.00)
    time_of_transaction = models.DateTimeField(default = datetime.now().isoformat())

    def __str__(self):
        return self.user.username

class Accounts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_name = models.CharField(max_length = 500)
    card_number = models.IntegerField(default= 0000000000000000)
    