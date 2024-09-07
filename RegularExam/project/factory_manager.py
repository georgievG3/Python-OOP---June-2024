from typing import List
from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:

    VALID_PRODUCT_TYPES = {"Chair": Chair, "HobbyHorse": HobbyHorse}
    VALID_STORE_TYPES = {"FurnitureStore": FurnitureStore, "ToyStore": ToyStore}

    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products: List[BaseProduct] = []
        self.stores: List[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):

        if product_type not in self.VALID_PRODUCT_TYPES.keys():
            raise Exception("Invalid product type!")

        product = self.VALID_PRODUCT_TYPES[product_type](model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):

        if store_type not in self.VALID_STORE_TYPES.keys():
            raise Exception(f"{store_type} is an invalid type of store!")

        store = self.VALID_STORE_TYPES[store_type](name, location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):

        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        if store.store_type == "FurnitureStore":

            filtered_products = [p for p in products if p.sub_type == "Furniture"]

            for product in filtered_products:

                store.products.append(product)
                self.products.remove(product)

            store.capacity -= len(filtered_products)
            prices = sum(p.price for p in filtered_products)
            self.income += prices

            if filtered_products:

                return f"Store {store.name} successfully purchased {len(filtered_products)} items."

            return "Products do not match in type. Nothing sold."

        elif store.store_type == "ToyStore":

            filtered_products = [p for p in products if p.sub_type == "Toys"]

            for product in filtered_products:

                store.products.append(product)
                self.products.remove(product)

            store.capacity -= len(filtered_products)
            prices = sum(p.price for p in filtered_products)
            self.income += prices

            if filtered_products:

                return f"Store {store.name} successfully purchased {len(filtered_products)} items."

            return "Products do not match in type. Nothing sold."

    def unregister_store(self, store_name: str):

        store = next((s for s in self.stores if store_name == s.name), None)

        if not store:
            raise Exception("No such store!")

        if len(store.products) > 0:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str):

        filtered_products = [p for p in self.products if p.model == product_model]

        for product in filtered_products:
            product.discount()

        return f"Discount applied to {len(filtered_products)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):

        store = next((s for s in self.stores if store_name == s.name), None)

        if store:

            return store.store_stats()

        return "There is no store registered under this name!"

    def statistics(self):

        stats = [f"Factory: {self.name}", f"Income: {self.income:.2f}"]
        stats.append("***Products Statistics***")
        stats.append(
            f"Unsold Products: {len(self.products)}. Total net price: {sum(p.price for p in self.products):.2f}")

        product_dict = {}
        for product in self.products:
            if product.model not in product_dict:
                product_dict[product.model] = 0
            product_dict[product.model] += 1

        for model in sorted(product_dict.keys()):
            stats.append(f"{model}: {product_dict[model]}")

        stats.append(f"***Partner Stores: {len(self.stores)}***")
        for store in sorted(self.stores, key=lambda s: s.name):
            stats.append(store.name)

        return "\n".join(stats)
