class Catalogue:
    def __init__(self,  name:str) -> None:
        self.name=name
        self.products=[]

    def add_product(self, product_name: str):
        self.products.append(product_name)
    
    def get_by_letter(self, first_letter: str):
        result_list=list(filter(lambda x:str(x).startswith(first_letter)==True,self.products))
        return result_list
    def __repr__ (self):
        list_to_print=self.products.copy()
        list_to_print.sort()
        all_prods='\n'.join(list_to_print)
        return f"Items in the {self.name} catalogue:\n{all_prods}"

cat=Catalogue('Test')

cat.add_product('prod')
cat.add_product('shrod')
print(cat.get_by_letter('p'))
print(cat)