# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assembly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assembly_name', models.CharField(max_length=50)),
                ('assembly_part_number', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('supplier_pn', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField()),
                ('extended_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('notes', models.TextField()),
                ('cad_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=25)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='FinishTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finish', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(max_length=50)),
                ('part_number', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('manufacturer_pn', models.CharField(blank=True, max_length=50, null=True)),
                ('dimensions', models.CharField(max_length=30)),
                ('uom', models.CharField(max_length=15)),
                ('cost_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('part_url', models.URLField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('cad_file', models.FileField(blank=True, null=True, upload_to='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
                ('finish', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.FinishTable')),
            ],
        ),
        migrations.CreateModel(
            name='PlatingTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plating', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_number', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('shipping_address', models.TextField()),
                ('expected_delivery', models.DateField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
                ('product', models.ManyToManyField(to='app.Assembly')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingTerms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_type', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('preferred_shipper', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubAssembly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_assembly_name', models.CharField(max_length=50)),
                ('sub_assembly_number', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('manufacturer_pn', models.CharField(blank=True, max_length=50, null=True)),
                ('dimensions', models.CharField(max_length=30)),
                ('uom', models.CharField(max_length=15)),
                ('cost_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('part_url', models.URLField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('cad_file', models.FileField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
                ('finish', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.FinishTable')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=25)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('items_supplied', models.ManyToManyField(blank=True, null=True, to='app.Part')),
            ],
        ),
        migrations.AddField(
            model_name='subassembly',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Supplier'),
        ),
        migrations.AddField(
            model_name='subassembly',
            name='plating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.PlatingTable'),
        ),
        migrations.AddField(
            model_name='subassembly',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SubCategory'),
        ),
        migrations.AddField(
            model_name='project',
            name='shipping_terms',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ShippingTerms'),
        ),
        migrations.AddField(
            model_name='platingtable',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Supplier'),
        ),
        migrations.AddField(
            model_name='part',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Supplier'),
        ),
        migrations.AddField(
            model_name='part',
            name='plating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.PlatingTable'),
        ),
        migrations.AddField(
            model_name='part',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SubCategory'),
        ),
        migrations.AddField(
            model_name='finishtable',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Supplier'),
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(blank=True, null=True, to='app.Project'),
        ),
        migrations.AddField(
            model_name='assembly',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category'),
        ),
        migrations.AddField(
            model_name='assembly',
            name='list_of_assemblies',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.SubAssembly'),
        ),
        migrations.AddField(
            model_name='assembly',
            name='list_of_parts',
            field=models.ManyToManyField(blank=True, null=True, to='app.Part'),
        ),
        migrations.AddField(
            model_name='assembly',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SubCategory'),
        ),
        migrations.AddField(
            model_name='assembly',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Supplier'),
        ),
    ]
