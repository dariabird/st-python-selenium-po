import pytest


def test_add_and_delete_three_product(app):
    for i in range(3):
        app.add_product_to_cart()
    for i in range(3):
        app.delete_product_from_cart()
