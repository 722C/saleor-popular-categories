from django import template

register = template.Library()


@register.inclusion_tag('popular_categories/dashboard/side_nav_inclusion.html',
                        takes_context=True)
def popular_categories_side_nav(context):
    return context
