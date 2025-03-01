from .models import Cart
from main.models import Product

def get_user_cart(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
    if not request.session.session_key:
        request.session.create()
    return Cart.objects.filter(session_key=request.session.session_key)
