from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Phone",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("price", models.PositiveIntegerField()),
                ("image", models.URLField(max_length=500)),
                ("release_date", models.DateField()),
                ("lte_exists", models.BooleanField()),
                ("slug", models.SlugField(max_length=200, unique=True)),
            ],
        ),
    ]
