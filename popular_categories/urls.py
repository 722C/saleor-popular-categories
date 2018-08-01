from django.conf.urls import url

from . import storefront_views
from .dashboard_views import views as dashboard_views

urlpatterns = [
    url(r'^popular-categories/$',
        storefront_views.PopularCategoriesList.as_view(),
        name='popular-category-list'),
    url(r'^dashboard/popular-categories/$',
        dashboard_views.popular_category_list,
        name='popular-category-dashboard-list'),
    url(r'^dashboard/popular-categories/create/$',
        dashboard_views.popular_category_create,
        name='popular-category-dashboard-create'),
    url(r'^dashboard/popular-categories/(?P<pk>[0-9]+)/$',
        dashboard_views.popular_category_details,
        name='popular-category-dashboard-detail'),
    url(r'^dashboard/popular-categories/(?P<pk>[0-9]+)/delete/$',
        dashboard_views.popular_category_delete,
        name='popular-category-dashboard-delete'),
]
