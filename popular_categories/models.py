from django.db import models

from django.utils.translation import pgettext_lazy

from saleor.core.permissions import MODELS_PERMISSIONS


# Add in the permissions specific to our models.
MODELS_PERMISSIONS += [
    'popular_categories.view',
    'popular_categories.edit'
]


class PopularCategory(models.Model):
    category = models.OneToOneField(
        'product.Category', on_delete=models.CASCADE, related_name='popular')
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'popular_categories'

        permissions = (
            ('view', pgettext_lazy('Permission description',
                                   'Can view popular categories')
             ),
            ('edit', pgettext_lazy('Permission description',
                                   'Can edit popular categories')))

    def __str__(self):
        return self.category.name
