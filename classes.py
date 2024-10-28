from helpers import hr

class BudgetCategory:
    categories = []

    def __init__(self, category_name, category_budget):
        self.__category_name = category_name
        self.__category_budget = category_budget
        self.expenses = []
        BudgetCategory.categories.append(self)

    def add_expense(self, expense_name, expense_amount):
        '''Prints confirmation and subtracts expense from category budget.'''
        try:
            if expense_amount > self.__category_budget:
                hr(50)
                print("This expense exceeds your budget.")
            else:
                self.__category_budget -= expense_amount
                self.expenses.append({'Expense': expense_name, 'Amount': expense_amount})
                hr(50)
                print(f"{expense_name} has been added to your {self.__category_name} budget")
        except ValueError:
            print("You must enter a numeric value.")

    def get_category_name(self):
        '''Returns category name.'''
        return self.__category_name
    
    def set_category_name(self, new_name):
        '''Prints confirmation of name change.'''
        old_name = self.__category_name
        self.__category_name = new_name
        hr(50)
        print(f"Category: {old_name}, has been changed to {new_name}")
    
    def get_category_budget(self):
        '''Returns category budget.'''
        return self.__category_budget
    
    def set_category_budget(self, new_budget):
        '''Prints confirmation of new budget.'''
        old_budget = self.__category_budget
        self.__category_budget = new_budget + old_budget
        hr(50)
        print(f"Budget has changed from ${old_budget:.2f}, to ${new_budget}")
            
    def display_expenses(self):
        '''Displays remaining budget and all expenses with detail.'''
        hr(50)
        print(f"Remaining {self.__category_name} Budget: ${self.__category_budget:.2f}\n")
        for item in self.expenses:
            print(f"Expense: {item['Expense']}, Amount: ${item['Amount']}")

    @classmethod
    def display_categories(cls):
        '''Displays all categories and budgets.'''
        hr(50)
        print("Categories:\n")
        for category in cls.categories:
            print(f"Category: {category.get_category_name()}\nBudget: {category.get_category_budget()}\n")