# Generated by Django 5.0.7 on 2024-08-08 09:38

import django.db.models.deletion
import mptt.fields
import servicer.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=255, unique=True)),
                ('name_ru', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=servicer.models.PathAndRename('category/'))),
                ('order_number', models.IntegerField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_children', to='servicer.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=255)),
                ('name_ru', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255)),
                ('profile_type', models.CharField(choices=[('company', 'Company'), ('specialist', 'Specialist')], max_length=20)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to=servicer.models.PathAndRename('organization_images/'))),
                ('description_uz', models.TextField()),
                ('description_ru', models.TextField()),
                ('description_en', models.TextField()),
                ('city', models.CharField(choices=[('TASHKENT', 'Tashkent'), ('ANDIJON', 'Andijon'), ('SAMARQAND', 'Samarqand')], max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('house_number', models.CharField(max_length=255)),
                ('landmark', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicer.category')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=servicer.models.PathAndRename('profile/'))),
                ('rating', models.PositiveIntegerField(default=0)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='servicer.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to=servicer.models.PathAndRename('service/'))),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='servicer.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.DurationField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicer.profile')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicer.service')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.DurationField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicer.organization')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicer.service')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=servicer.models.PathAndRename('organization_portfolio/'))),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_images', to='servicer.organization')),
            ],
            options={
                'unique_together': {('organization', 'image')},
            },
        ),
    ]
