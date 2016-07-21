# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 17:33
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
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('supplier_pn', models.CharField(blank=True, max_length=50, null=True)),
                ('assembly_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('cad_file', models.FileField(blank=True, null=True, upload_to='cad_files')),
            ],
        ),
        migrations.CreateModel(
            name='AssemblyQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('assembly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Assembly')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(blank=True, max_length=25, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinishTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finish', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
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
                ('dimensions', models.CharField(max_length=50)),
                ('uom', models.CharField(max_length=15)),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('part_url', models.URLField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('cad_file', models.FileField(blank=True, null=True, upload_to='cad_file')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image_files', verbose_name='Part Image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
                ('finish', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.FinishTable')),
            ],
        ),
        migrations.CreateModel(
            name='PlatingTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plating', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_number', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=50)),
                ('quantity_per_product', models.IntegerField(blank=True, null=True)),
                ('price_per_product', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('extended_price_per_product', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('price_per_project', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('shipping_address', models.TextField(blank=True, null=True)),
                ('expected_delivery', models.DateField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
                ('products', models.ManyToManyField(blank=True, null=True, to='app.Assembly')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingTerms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_type', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('preferred_shipper', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubAssembly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_assembly_name', models.CharField(max_length=50)),
                ('sub_assembly_number', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('mfg_supplier_pn', models.CharField(blank=True, max_length=50, null=True)),
                ('subassembly_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('cad_file', models.FileField(blank=True, null=True, upload_to='cad_files')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
                ('finish', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.FinishTable')),
            ],
        ),
        migrations.CreateModel(
            name='SubAssemblyQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('assembly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SubAssembly')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Part')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(blank=True, max_length=25, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='subassembly',
            name='mfg_supplier',
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
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.SubCategory'),
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
            model_name='assemblyquantity',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Part'),
        ),
        migrations.AddField(
            model_name='assembly',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Category'),
        ),
        migrations.AddField(
            model_name='assembly',
            name='finish',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.FinishTable'),
        ),
        migrations.AddField(
            model_name='assembly',
            name='plating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.PlatingTable'),
        ),
        migrations.AddField(
            model_name='assembly',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.SubCategory'),
        ),
        migrations.AddField(
            model_name='assembly',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Supplier'),
        ),
    ]
