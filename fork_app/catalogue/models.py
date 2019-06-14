


# yourproject/catalogue/models.py

from django.db import models


from oscar.apps.catalogue.abstract_models import AbstractProduct, AbstractCategory

class Product(AbstractProduct):
    video_url = models.CharField(max_length=2048, blank=True)
    tutorial = models.TextField(blank=True)
    aliexpress_url = models.URLField(blank=True)

    def calculate_rating(self):
        results

from oscar.apps.catalogue.models import *


