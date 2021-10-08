# Generated by Django 3.2.8 on 2021-10-06 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_c', to='customer.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='establish',
            field=models.CharField(choices=[('0', '不成立'), ('1', '成立')], default='1', max_length=1),
        ),
    ]
