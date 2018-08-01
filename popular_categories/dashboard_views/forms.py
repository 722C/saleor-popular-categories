from django import forms
from django.db.models import Q
from django.utils.translation import pgettext_lazy

from saleor.product.models import Category
from ..models import PopularCategory


class PopularCategoryForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all())

    class Meta:
        model = PopularCategory
        verbose_name_plural = 'popular categories'
        fields = ['category']

    def __init__(self, *args, **kwargs):
        super(PopularCategoryForm, self).__init__(*args, **kwargs)

        # Modify the queryset so that we don't show categories that are
        # already popular.
        # We need to do this differently for when the
        # user is adding vs editing so we can explicitly include the current
        # category when they are editing.
        if self.instance.pk:
            self.fields['category'].queryset = self.fields[
                'category'].queryset.filter(
                    Q(id=self.instance.category.pk) |
                    Q(popular__isnull=True))
        else:
            self.fields['category'].queryset = self.fields[
                'category'].queryset.filter(popular__isnull=True)
