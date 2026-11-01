from datetime import date

from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from phones.models import Phone


class PhoneTests(TestCase):
    def setUp(self):
        Phone.objects.create(
            id=1,
            name="Iphone X",
            price=80000,
            image="https://example.com/iphone.jpg",
            release_date=date(2017, 6, 1),
            lte_exists=True,
        )
        Phone.objects.create(
            id=2,
            name="Nokia 8",
            price=20000,
            image="https://example.com/nokia.jpg",
            release_date=date(2013, 1, 20),
            lte_exists=False,
        )

    def test_slug(self):
        self.assertEqual(Phone.objects.get(id=1).slug, "iphone-x")

    def test_catalog(self):
        response = self.client.get(reverse("catalog"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["phones"]), 2)

    def test_product(self):
        response = self.client.get(
            reverse("phone", args=["iphone-x"])
        )
        self.assertEqual(response.status_code, 200)

    def test_missing_product(self):
        response = self.client.get(
            reverse("phone", args=["unknown-phone"])
        )
        self.assertEqual(response.status_code, 404)

    def test_sort_by_name(self):
        response = self.client.get("/catalog/?sort=name")
        self.assertEqual(
            list(response.context["phones"].values_list("name", flat=True)),
            ["Iphone X", "Nokia 8"],
        )

    def test_sort_by_min_price(self):
        response = self.client.get("/catalog/?sort=min_price")
        self.assertEqual(response.context["phones"].first().name, "Nokia 8")

    def test_sort_by_max_price(self):
        response = self.client.get("/catalog/?sort=max_price")
        self.assertEqual(response.context["phones"].first().name, "Iphone X")

    def test_import_phones(self):
        call_command("import_phones")
        self.assertEqual(Phone.objects.count(), 3)
        self.assertTrue(Phone.objects.get(id=1).lte_exists)
        self.assertFalse(Phone.objects.get(id=3).lte_exists)
        call_command("import_phones")
        self.assertEqual(Phone.objects.count(), 3)
