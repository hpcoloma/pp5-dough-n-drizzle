from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def show_footer(context):
    # Check if the current user has access to admin-related pages
    user = context['request'].user
    is_admin = user.is_authenticated and user.is_superuser

    # Check if the page is one of the specified pages
    exclude_pages = ['home', 'add_products', 'discount_list']

    # Get the current path and return True if the footer should be shown
    current_path = context['request'].path.strip('/')
    return not (current_path in exclude_pages or is_admin)