# Generated by Django 3.2.4 on 2021-09-22 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uesrname', models.CharField(max_length=20, verbose_name='用户名')),
                ('goodsname', models.TextField(verbose_name='物品名称')),
                ('goodsnum', models.SmallIntegerField(default=0, verbose_name='物品数量')),
                ('goodsmy', models.SmallIntegerField(default=0, verbose_name='物品总价（单位为元）')),
                ('createtime', models.DateTimeField(default=datetime.datetime(2021, 9, 22, 11, 36, 29, 960515))),
            ],
        ),
    ]
