# Generated by Django 3.2.23 on 2024-01-29 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fruitsVegetables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('description', models.TextField()),
                ('categary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categary.categary')),
            ],
        ),
    ]
