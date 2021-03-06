# Generated by Django 2.1.4 on 2018-12-11 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0078_auto_20180723_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='os_family',
            field=models.CharField(choices=[('Darwin', 'macOS'), ('Windows', 'Windows'), ('Linux', 'Linux'), ('ChromeOS', 'Chrome OS')], db_index=True, default='Darwin', max_length=256, verbose_name='OS Family'),
        ),
        migrations.AlterField(
            model_name='pendingappleupdate',
            name='update',
            field=models.CharField(blank=True, db_index=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='updatehistory',
            name='update_type',
            field=models.CharField(choices=[('third_party', '3rd Party'), ('apple', 'Apple')], max_length=254, verbose_name='Update Type'),
        ),
        migrations.AlterField(
            model_name='updatehistoryitem',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('error', 'Error'), ('install', 'Install'), ('removal', 'Removal')], max_length=254, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='level',
            field=models.CharField(choices=[('SO', 'Stats Only'), ('RO', 'Read Only'), ('RW', 'Read Write'), ('GA', 'Global Admin')], default='RO', max_length=2),
        ),
    ]
