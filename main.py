from store.order import add_new_product_to_order

def create_order():
    full_order = []
    while True:
        product_name = input(
            "Czy chcesz coś jeszcze zamówić. Podaj nazwę produktu. Wpisz X jeśli to już wszystko ").lower()
        if product_name == 'x':
            return full_order
        quantity_to_order = int(input("Podaj ilość produktów"))
        ret = add_new_product_to_order(product_name, quantity_to_order)
        print(ret)
        full_order.append(ret)


if __name__ == '__main__':
    k = create_order()
    print(k)