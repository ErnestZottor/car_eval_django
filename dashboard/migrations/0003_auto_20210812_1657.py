# Generated by Django 3.2.6 on 2021-08-12 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_breastcancerchecker_predictions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breastcancerchecker',
            name='mean_area',
        ),
        migrations.RemoveField(
            model_name='breastcancerchecker',
            name='mean_perimeter',
        ),
        migrations.RemoveField(
            model_name='breastcancerchecker',
            name='mean_radius',
        ),
        migrations.RemoveField(
            model_name='breastcancerchecker',
            name='mean_smoothness',
        ),
        migrations.RemoveField(
            model_name='breastcancerchecker',
            name='mean_texture',
        ),
        migrations.RemoveField(
            model_name='breastcancerchecker',
            name='name',
        ),
        migrations.RemoveField(
            model_name='breastcancerchecker',
            name='surname',
        ),
        migrations.AddField(
            model_name='breastcancerchecker',
            name='buying',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='breastcancerchecker',
            name='doors',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='breastcancerchecker',
            name='lug_boot',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='breastcancerchecker',
            name='maint',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='breastcancerchecker',
            name='persons',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='breastcancerchecker',
            name='safety',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
