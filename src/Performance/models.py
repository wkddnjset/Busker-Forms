from django.db import models

# Create your models here.

# 공연 테이블
class Performance(models.Model):

    date = models.DateField(auto_now_add=True, null=True)
    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)
    place = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)