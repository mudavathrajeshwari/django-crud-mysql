from django.db import models


class Customer(models.Model):
    cid = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=100)
    cemail = models.EmailField()
    ccity = models.CharField(max_length=100)