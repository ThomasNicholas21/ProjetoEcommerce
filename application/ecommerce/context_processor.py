def get_cart_amount(request):
    cart = request.session.get('cart', {})
    total_items = 0
    
    if cart:
        for item in cart.values():
            total_items += item.get('amount', 0)
    
    return {'cart_amount': total_items}
