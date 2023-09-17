
from shop.order import Order
from shop.order_element import OrderElement
from shop.product import Product


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
    ]


    first_order = Order(client_first_name="Kuba", client_last_name="Kowalski", order_elements=first_order_elements)
    second_order = Order(client_first_name="Kuba", client_last_name="Kowalski", order_elements=second_order_elements)
    # second_order.client_last_name = "Lewandowski"

    second_order.add_new_product(other_cookie, 5)

    print(second_order)

if __name__ == '__main__':
    run_homework()
