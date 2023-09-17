
from shop.order import Order
from shop.order_element import OrderElement
from shop.product import Product
from tax_calculator import TaxCalculator


def run_homework():

    cookie = Product(name="Ciastko", category_name="Jedzenie", unit_price=4)
    other_cookie = Product(name="Inne ciastko", category_name="Jedzenie", unit_price=4)
    juice = Product(name="Sok", category_name="Napoje", unit_price=3)
    first_order_elements = [
        OrderElement(product=cookie, quantity=3),
        # OrderElement(product=other_cookie, quantity=3),
        OrderElement(product=juice, quantity=4),
    ]
    # first_order_elements.append(OrderElement(product=juice, quantity=4))
    # first_order_elements[0].quantity = 10

    second_order_elements = [
        OrderElement(product=juice, quantity=4),
        OrderElement(product=cookie, quantity=3),
        OrderElement(product=juice, quantity=4),
        # OrderElement(product=cookie, quantity=3),
        # OrderElement(product=juice, quantity=4),
        # OrderElement(product=cookie, quantity=3)
    ]
    print(first_order_elements[0].calculate_price())
    print(TaxCalculator.tax_for_order_element(first_order_elements[0]))



if __name__ == '__main__':
    run_homework()
