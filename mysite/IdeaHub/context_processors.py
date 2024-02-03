from .models import Category

# This function is a context processor that makes 'category_menu' globally available to all templates. 
# It replaces the need for repeatedly defining 'get_context_data' in each view to pass 'category_menu' context. 
# Use it to provide context for a dropdown menu in the base template.
def category_menu(request):
    return {'category_menu': Category.objects.all()}
