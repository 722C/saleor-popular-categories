from django.views import generic

from .models import PopularCategory


class PopularCategoriesList(generic.ListView):
    model = PopularCategory
    template_name = 'popular_categories/list.html'
