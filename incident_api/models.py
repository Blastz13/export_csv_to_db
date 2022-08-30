from django.db import models


class Incident(models.Model):
    crime_id = models.IntegerField()
    original_crime_type_name = models.TextField()
    report_date = models.DateTimeField(db_index=True)
    call_date = models.DateTimeField()
    offense_date = models.DateTimeField()
    call_time = models.DateTimeField()
    call_date_time = models.DateTimeField()
    disposition = models.TextField()
    address = models.TextField()
    city = models.TextField(null=True)
    state = models.TextField()
    agency_id = models.IntegerField()
    address_type = models.TextField()
    common_location = models.TextField(null=True)

    def __str__(self):
        return f'{self.crime_id}'
