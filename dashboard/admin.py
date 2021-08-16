from django.contrib import admin
from .models import BreastCancerChecker

@admin.register(BreastCancerChecker)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('buying', 'doors', 'persons', 'lug_boot', 'safety', 'predictions')



