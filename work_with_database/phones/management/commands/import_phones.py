import csv
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from phones.models import Phone


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = Path(settings.BASE_DIR) / "phones.csv"

        with path.open(encoding="utf-8", newline="") as file:
            phones = csv.DictReader(file, delimiter=";")

            with transaction.atomic():
                for phone in phones:
                    Phone.objects.update_or_create(
                        id=int(phone["id"]),
                        defaults={
                            "name": phone["name"],
                            "price": int(phone["price"]),
                            "image": phone["image"],
                            "release_date": phone["release_date"],
                            "lte_exists": phone["lte_exists"] == "True",
                        },
                    )

        self.stdout.write("Телефоны загружены")
