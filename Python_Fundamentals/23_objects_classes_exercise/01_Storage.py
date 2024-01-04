class Storage:


    def __init__(self,capacity) -> None:
        self.capacity=capacity
        self.storage=[]
    
    def add_product(self, product: str):
        if self.capacity>len(self.storage):
            self.storage.append(product)
    def get_products(self):
        return self.storage