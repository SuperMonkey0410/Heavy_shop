from django import template
from carts.views import cart_add
from carts.models import Cart
from carts.utils import get_user_cart

register = template.Library()


@register.simple_tag()
def user_cart(request):
    return get_user_cart(request)
