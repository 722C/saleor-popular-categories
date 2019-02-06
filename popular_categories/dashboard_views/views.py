from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.utils.translation import pgettext_lazy

from saleor.core.utils import get_paginator_items
from saleor.dashboard.views import staff_member_required
from .filters import PopularCategoryFilter
from .forms import PopularCategoryForm

from ..models import PopularCategory


@staff_member_required
@permission_required('popular_categories.view')
def popular_category_list(request):
    popular_categories = (
        PopularCategory.objects.all().select_related('category')
        .order_by('category'))
    popular_category_filter = PopularCategoryFilter(
        request.GET, queryset=popular_categories)
    popular_categories = get_paginator_items(
        popular_category_filter.qs, settings.DASHBOARD_PAGINATE_BY, request.GET.get('page'))
    # Call this so that cleaned_data exists on the filter_set
    popular_category_filter.form.is_valid()
    ctx = {
        'popular_categories': popular_categories, 'filter_set': popular_category_filter,
        'is_empty': not popular_category_filter.queryset.exists()}
    return TemplateResponse(request, 'popular_categories/dashboard/list.html', ctx)


@staff_member_required
@permission_required('popular_categories.edit')
def popular_category_create(request):
    popular_category = PopularCategory()
    form = PopularCategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy('Dashboard message', 'Created popular category')
        messages.success(request, msg)
        return redirect('popular-category-dashboard-list')
    ctx = {'popular_category': popular_category, 'form': form}
    return TemplateResponse(request, 'popular_categories/dashboard/detail.html', ctx)


@staff_member_required
@permission_required('popular_categories.edit')
def popular_category_details(request, pk):
    popular_category = PopularCategory.objects.get(pk=pk)
    form = PopularCategoryForm(
        request.POST or None, instance=popular_category)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy(
            'Dashboard message', 'Updated popular category %s') % popular_category.name
        messages.success(request, msg)
        return redirect('popular-category-dashboard-list')
    ctx = {'popular_category': popular_category, 'form': form}
    return TemplateResponse(request, 'popular_categories/dashboard/detail.html', ctx)


@staff_member_required
@permission_required('popular_categories.edit')
def popular_category_delete(request, pk):
    popular_category = get_object_or_404(PopularCategory, pk=pk)
    if request.method == 'POST':
        popular_category.delete()
        msg = pgettext_lazy('Dashboard message',
                            'Removed popular category %s') % popular_category
        messages.success(request, msg)
        return redirect('popular-category-dashboard-list')
    return TemplateResponse(
        request, 'popular_categories/dashboard/modal/confirm_delete.html', {'popular_category': popular_category})
