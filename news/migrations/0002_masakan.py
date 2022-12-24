# Generated by Django 4.1.3 on 2022-12-16 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Masakan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("strArea", models.CharField(max_length=200)),
                ("strCategory", models.CharField(max_length=200)),
                ("strMeal", models.CharField(max_length=200)),
                ("strMealThumb", models.CharField(max_length=200)),
                ("strInstructions", models.TextField()),
                ("strYoutube", models.CharField(max_length=225)),
                ("strIngredient1", models.CharField(max_length=225)),
                ("strIngredient2", models.CharField(max_length=225)),
                ("strIngredient3", models.CharField(max_length=225)),
                ("strIngredient4", models.CharField(max_length=225)),
                ("strIngredient5", models.CharField(max_length=225)),
                ("strIngredient6", models.CharField(max_length=225)),
                ("strIngredient7", models.CharField(max_length=225)),
                ("strIngredient8", models.CharField(max_length=225)),
                ("strIngredient9", models.CharField(max_length=225)),
                ("strIngredient10", models.CharField(max_length=225)),
                ("strIngredient11", models.CharField(max_length=225)),
                ("strIngredient12", models.CharField(max_length=225)),
                ("strIngredient13", models.CharField(max_length=225)),
                ("strIngredient14", models.CharField(max_length=225)),
                ("strIngredient15", models.CharField(max_length=225)),
                ("strIngredient16", models.CharField(max_length=225)),
                ("strIngredient17", models.CharField(max_length=225)),
                ("strIngredient18", models.CharField(max_length=225)),
                ("strIngredient19", models.CharField(max_length=225)),
                ("strIngredient20", models.CharField(max_length=225)),
                ("strMeasure1", models.CharField(max_length=225)),
                ("strMeasure2", models.CharField(max_length=225)),
                ("strMeasure3", models.CharField(max_length=225)),
                ("strMeasure4", models.CharField(max_length=225)),
                ("strMeasure5", models.CharField(max_length=225)),
                ("strMeasure6", models.CharField(max_length=225)),
                ("strMeasure7", models.CharField(max_length=225)),
                ("strMeasure8", models.CharField(max_length=225)),
                ("strMeasure9", models.CharField(max_length=225)),
                ("strMeasure10", models.CharField(max_length=225)),
                ("strMeasure11", models.CharField(max_length=225)),
                ("strMeasure12", models.CharField(max_length=225)),
                ("strMeasure13", models.CharField(max_length=225)),
                ("strMeasure14", models.CharField(max_length=225)),
                ("strMeasure15", models.CharField(max_length=225)),
                ("strMeasure16", models.CharField(max_length=225)),
                ("strMeasure17", models.CharField(max_length=225)),
                ("strMeasure18", models.CharField(max_length=225)),
                ("strMeasure19", models.CharField(max_length=225)),
                ("strMeasure20", models.CharField(max_length=225)),
            ],
        ),
    ]
