


# yourproject/catalogue/models.py

from django.db import models


from oscar.apps.catalogue.abstract_models import AbstractProduct, AbstractCategory

class Product(AbstractProduct):
    video_url = models.CharField(max_length=2048, blank=True)
    tutorial = models.TextField(blank=True)
    aliexpress_url = models.URLField(blank=True)

    @property
    def num_5stars(self):
        return self.reviews.filter(
            status=self.reviews.model.APPROVED, score=5
        ).count()
    @property
    def percent_5stars(self):
        return (100 * self.num_5stars) / self.reviews.all().count()

    @property
    def num_4stars(self):
        return self.reviews.filter(
            status=self.reviews.model.APPROVED, score=4
        ).count()
    @property
    def percent_4stars(self):
        return (100 * self.num_4stars) / self.reviews.all().count()

    @property
    def num_3stars(self):
        return self.reviews.filter(
            status=self.reviews.model.APPROVED, score=3
        ).count()
    @property
    def percent_3stars(self):
        return (100 * self.num_3stars) / self.reviews.all().count()

    @property
    def num_2stars(self):
        return self.reviews.filter(
            status=self.reviews.model.APPROVED, score=2
        ).count()
    @property
    def percent_2stars(self):
        return (100 * self.num_2stars) / self.reviews.all().count()

    @property
    def num_1stars(self):
        return self.reviews.filter(
            status=self.reviews.model.APPROVED, score=1
        ).count()
    @property
    def percent_1stars(self):
        return (100 * self.num_1stars) / self.reviews.all().count()




class Category(AbstractCategory):

    @property
    def last_name(self):
        names = [category.name for category in self.get_ancestors_and_self()]
        return names[1]

from oscar.apps.catalogue.models import *