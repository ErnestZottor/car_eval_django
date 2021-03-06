# Generated by Django 3.2.6 on 2021-08-13 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_breastcancerchecker_buying'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breastcancerchecker',
            name='doors',
            field=models.IntegerField(choices=[(3, '5-more'), (2, '4'), (1, '3'), (0, '2')], null=True),
        ),
        migrations.AlterField(
            model_name='breastcancerchecker',
            name='lug_boot',
            field=models.IntegerField(choices=[(2, 'big'), (1, 'med'), (0, 'small')], null=True),
        ),
        migrations.AlterField(
            model_name='breastcancerchecker',
            name='maint',
            field=models.IntegerField(choices=[(3, 'v-high'), (2, 'high'), (1, 'med'), (0, 'low')], null=True),
        ),
        migrations.AlterField(
            model_name='breastcancerchecker',
            name='persons',
            field=models.IntegerField(choices=[(2, 'more'), (1, '4'), (0, '2')], null=True),
        ),
        migrations.AlterField(
            model_name='breastcancerchecker',
            name='safety',
            field=models.IntegerField(choices=[(2, 'high'), (1, 'med'), (0, 'low')], null=True),
        ),
    ]
