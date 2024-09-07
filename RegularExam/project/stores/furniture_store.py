from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):

    def __init__(self, name: str, location: str):
        super().__init__(name, location, 50)

    @property
    def store_type(self):
        return "FurnitureStore"

    def store_stats(self):

        stats = [f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}"]
        stats.append(self.get_estimated_profit())
        stats.append("**Furniture for sale:")

        furniture_dict = {}
        for product in self.products:
            if product.model not in furniture_dict:
                furniture_dict[product.model] = []
            furniture_dict[product.model].append(product.price)

        for model, prices in sorted(furniture_dict.items()):
            avg_price = sum(prices) / len(prices)
            stats.append(f"{model}: {len(prices)}pcs, average price: {avg_price:.2f}")

        return "\n".join(stats)
