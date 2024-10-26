class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.categories = {}

    def get_category(self, category):
        if category in self.categories:
            print(category)

    def set_category(self):
        pass

    def get_budget(self):
        pass

    def set_budget(self):
        pass