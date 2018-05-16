# Generated by Django 2.0.5 on 2018-05-16 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20180509_0035'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='C:\\Users\\moame\\Desktop\\vmpub/media/slide-show/')),
            ],
        ),
        migrations.AlterField(
            model_name='catalog',
            name='photo',
            field=models.FileField(upload_to='C:\\Users\\moame\\Desktop\\vmpub/media/catalog/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.FileField(upload_to='C:\\Users\\moame\\Desktop\\vmpub/media/categories/'),
        ),
        migrations.AlterField(
            model_name='impression',
            name='photo',
            field=models.FileField(upload_to='C:\\Users\\moame\\Desktop\\vmpub/media/impression/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.FileField(upload_to='C:\\Users\\moame\\Desktop\\vmpub/media/products/'),
        ),
        migrations.AlterField(
            model_name='productphoto',
            name='photo',
            field=models.FileField(upload_to='C:\\Users\\moame\\Desktop\\vmpub/media/product-photos/'),
        ),
    ]
