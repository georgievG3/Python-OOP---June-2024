from project.stores.base_store import BaseStore


class ToyStore(BaseStore):

    def __init__(self, name: str, location: str):
        super().__init__(name, location, 100)

    @property
    def store_type(self):
        return "ToyStore"

    def store_stats(self):

        stats = [f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}"]
        stats.append(self.get_estimated_profit())
        stats.append("**Toys for sale:")

        toys_dict = {}
        for product in self.products:
            if product.model not in toys_dict:
                toys_dict[product.model] = []
            toys_dict[product.model].append(product.price)

        for model, prices in sorted(toys_dict.items()):
            avg_price = sum(prices) / len(prices)
            stats.append(f"{model}: {len(prices)}pcs, average price: {avg_price:.2f}")

        return "\n".join(stats)
