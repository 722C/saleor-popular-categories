from django.utils.translation import npgettext, pgettext_lazy
from django_filters import (CharFilter, OrderingFilter)

from saleor.core.filters import SortedFilterSet

from ..models import PopularCategory

SORT_BY_FIELDS = {
    'category__name': pgettext_lazy('Category list sorting option', 'name')}


class PopularCategoryFilter(SortedFilterSet):
    category__name = CharFilter(
        label=pgettext_lazy('Category list filter label', 'Name'),
        lookup_expr='icontains')
    sort_by = OrderingFilter(
        label=pgettext_lazy('Category list filter label', 'Sort by'),
        fields=SORT_BY_FIELDS.keys(),
        field_labels=SORT_BY_FIELDS)

    class Meta:
        model = PopularCategory
        fields = []

    def get_summary_message(self):
        counter = self.qs.count()
        return npgettext(
            'Number of matching records in the dashboard popular categories list',
            'Found %(counter)d matching popular category',
            'Found %(counter)d matching popular categories',
            number=counter) % {'counter': counter}
