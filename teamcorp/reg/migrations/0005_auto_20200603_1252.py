# Generated by Django 3.0.6 on 2020-06-03 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0004_auto_20200603_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=10),
        ),
        migrations.AddField(
            model_name='register',
            name='guardian_role',
            field=models.CharField(choices=[('Guardian', 'Guardian'), ('Mother', 'Mother'), ('Father', 'Father'), ('Grandparent', 'Grandparent'), ('Uncle', 'Uncle'), ('Aunt', 'Aunt')], default='Guardian', max_length=50),
        ),
        migrations.AddField(
            model_name='register',
            name='no_of_children',
            field=models.CharField(choices=[('1', '1-2'), ('2', '2-3'), ('3', '3-4'), ('4', '4-5'), ('5', '5+')], default='1', max_length=1),
        ),
    ]
