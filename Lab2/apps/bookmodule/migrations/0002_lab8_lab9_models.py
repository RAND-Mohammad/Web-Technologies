# Generated for Lab 8 and Lab 9.

import django.utils.timezone
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bookmodule", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("city", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Author",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("DOB", models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Publisher",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("location", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("age", models.IntegerField()),
                ("address", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="bookmodule.address")),
            ],
        ),
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name="book",
            name="pubdate",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="book",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="book",
            name="rating",
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="book",
            name="publisher",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="bookmodule.publisher"),
        ),
        migrations.AddField(
            model_name="book",
            name="authors",
            field=models.ManyToManyField(to="bookmodule.author"),
        ),
    ]
