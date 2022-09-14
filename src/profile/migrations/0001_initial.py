class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cars", "0003_cars_provider"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("username", models.CharField(max_length=256, unique=True)),
                (
                    "email",
                    models.EmailField(db_index=True, max_length=256, unique=True),
                ),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("bio", models.TextField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_verified", models.BooleanField(default=False)),
                (
                    "cars",
                    models.ManyToManyField(
                        null=True, related_name="car_profile", to="cars.Cars"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
