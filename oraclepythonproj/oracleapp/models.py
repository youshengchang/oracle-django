from django.db import models

class locations(models.Model):
      location_id = models.IntegerField(primary_key = True)
      street_address = models.CharField(max_length = 40)
      postal_code = models.CharField(max_length = 12)
      city = models.CharField(max_length = 30)
      state_province = models.CharField(max_length = 25)
      country_id = models.CharField(max_length = 2)
      class Meta:
          db_table = "locations"

