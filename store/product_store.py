products = {
    "bred": {
        "price": 2.1,
        "quantity": 20
    },
    "milk": {
        "price": 1.1,
        "quantity": 40
    }
}

def take_product_from_store(product, quantity):
    products[product]["quantity"] -= quantity