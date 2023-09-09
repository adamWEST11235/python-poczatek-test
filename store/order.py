from product_store import products, take_product_from_store

def add_new_product_to_order(product, quantity):

    if product not in products.keys():
        print("We don't have product like this")
        return None
    if quantity > products[product]['quantity']:
        print("We don't have enough product")
        return None


    price = products[product]["price"] * quantity

    new_order ={
        "product": product,
        "quantity": quantity,
        "price": price
    }
    take_product_from_store(product,quantity)
    return new_order