from django.db import models

# Create your models here.

BUYING = (
    (3, 'v-high'),
    (2, 'high'),
    (1, 'med'),
    (0,'low'))

class BreastCancerChecker(models.Model):
	# """mean_radius 	mean_texture 	mean_perimeter 	mean_area 	mean_smoothness  date"""

    buying = models.IntegerField(choices=BUYING, null=True)
    maint = models.IntegerField(default=0, null=True)
    doors = models.IntegerField(default=0, null=True)
    persons = models.IntegerField(default=0, null=True)
    lug_boot = models.IntegerField(default=0, null=True)
    safety = models.IntegerField(default=0, null=True)
    # mean_smoothness = models.Flo(default=0.11840, null=True)
    # date = models.DateTimeField(auto_now_add=True)
    predictions = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        pass
        # ordering = ['-date']

   