


# yourproject/catalogue/models.py

from django.db import models


from oscar.apps.catalogue.abstract_models import AbstractProduct, AbstractCategory
from oscar.apps.catalogue.reviews.abstract_models import AbstractProductReview


class Product(AbstractProduct):
    video_url = models.CharField(max_length=2048, blank=True)
    tutorial = models.TextField(blank=True)
    aliexpress_url = models.URLField(blank=True)

    @property
    def num_5stars(self):
        return self.reviews.filter(status=self.reviews.model.APPROVED, score=5).count()
    @property
    def num_4stars(self):
        return self.reviews.filter(status=self.reviews.model.APPROVED, score=4).count()
    @property
    def num_3stars(self):
        return self.reviews.filter(status=self.reviews.model.APPROVED, score=3).count()
    @property
    def num_2stars(self):
        return self.reviews.filter(status=self.reviews.model.APPROVED, score=2).count()
    @property
    def num_1stars(self):
        return self.reviews.filter(status=self.reviews.model.APPROVED, score=1).count()


from oscar.apps.catalogue.models import *


