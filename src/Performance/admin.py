from django.contrib import admin
from .models import *
from .forms import Performs
# Register your models here.

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'start_time', 'end_time', 'place']
    form = Performs

