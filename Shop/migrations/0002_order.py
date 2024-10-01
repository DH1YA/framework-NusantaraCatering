# Generated by Django 5.1.1 on 2024-10-01 14:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('delivery_address', models.TextField()),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('delivery_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('delivered', 'Delivered')], default='pending', max_length=10)),
                ('payment_status', models.CharField(choices=[('unpaid', 'Unpaid'), ('paid', 'Paid')], default='unpaid', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.user')),
            ],
        ),
    ]
