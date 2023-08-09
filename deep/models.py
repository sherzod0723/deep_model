from django.db import models
from datetime import datetime
from django.http.response import HttpResponse


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    age = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default='False')

    def save(
            self, *args, **kwargs
    ):
        self.age = datetime.now().year - self.birth_date.year
        if self.age > 26:
            super().save(*args, **kwargs)
        else:
            return HttpResponse("hato xolat")

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        super().save(*args, **kwargs)

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime

        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        "Returns the person's full name."
        return f"{self.first_name} {self.last_name}".upper()



class Poll(models.Model):
    name = models.CharField(max_length=255)
    sure_name = models.CharField(max_length=345)
    poll_id = models.IntegerField(default=1)
