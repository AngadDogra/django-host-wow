from django.db import models
from django.utils import timezone

class Company(models.Model):
    company_name = models.CharField(max_length=20)
    date = models.DateField()
    close_last = models.FloatField()
    volume = models.FloatField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()

    class Meta:
        ordering = ['-date', 'company_name']
        indexes = [
            models.Index(fields=['company_name', 'date']),
            models.Index(fields=['date'],)
        ]

    def __str__(self):
        return f"{self.company_name} - {self.date}"

    def price_change(self):
        """Calculate price change percentage"""
        if self.open != 0:
            return ((self.close_last - self.open) / self.open) * 100
        return 0

    def is_positive_day(self):
        """Check if it was a positive trading day"""
        return self.close_last > self.open
    

class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    class Meta:
        managed = False  # Tell Django this is an existing table
        db_table = 'actor'  # Specify the actual table name
        app_label = 'bands'

    def db_for_read(self):
        return 'sakila'

    def db_for_write(self):
        return 'sakila'