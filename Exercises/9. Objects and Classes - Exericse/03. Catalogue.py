class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        result = []
        for i in self.products:
            if i[0] == first_letter:
                result.append(i)
        return result

    def __repr__(self):
        sorted_list = sorted(self.products, key=lambda x: x)
        result = f"Items in the {self.name} catalogue:"
        for i in sorted_list:
            result += "\n" + i
        return f"{result}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

