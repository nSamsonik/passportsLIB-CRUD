from django.db import models


class Record(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=100)

    inv_num = models.CharField(max_length=50)

    ser_num = models.CharField(max_length=50)

    place_pass = models.CharField(max_length=50)

    status_pass = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + "   |   " + self.place_pass
