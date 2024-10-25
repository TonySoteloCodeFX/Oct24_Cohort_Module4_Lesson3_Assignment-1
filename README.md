<h1>Assignments: OOP Principles</h1>
<hr>

<b>Some helpful hints:</b> 
1. <b>Modular Design:</b> Break down your application into logical modules.

2. <b>Reusability:</b> By using modules, you can easily reuse code. 

3. <b>Maintainability</b>: With modular code, making changes or updates becomes simpler and less risky.

4. <b>Testing:</b> Testing modules independently becomes more straightforward. You can write and run tests for each module to ensure its functionality before integrating it into the main system.

5. <b>Importing Modules:</b> Use the import statement to include modules in your main application script. 

6. <b>Directory Structure:</b> Organize your modules in a clear directory structure.

7. <b>Naming Conventions:</b> Follow Python naming conventions for your modules. Typically, module names should be lowercase with underscores to improve readability (e.g., smart_device.py).

8. <b>Documenting Modules:</b> Provide documentation for each module. A brief comment at the beginning of each module explaining its purpose and functionality can be very helpful.

By adhering to a modular approach, your solutions for the assignments will not only be more effective and efficient but also align with industry standards. This practice will prepare you for larger-scale projects in your programming career.
<hr>

<h3>1. Encapsulation in Personal Budget Management</h3>

<b>Objective:</b> The aim of this assignment is to reinforce the understanding of encapsulation in Python, focusing on the use of private attributes and getters and setters.

<b>Problem Statement:</b> You are required to build a Personal Budget Management application. The application will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details remain private and are accessed or modified through public methods.

<h5>Task 1:</h5> Define Budget Category Class Create a class `BudgetCategory` with private attributes for category name and allocated budget. - Initialize these attributes in the constructor.
<br><br>

<b>Expected Outcome:</b> A "BudgetCategory" class capable of storing category details securely.

<h5>Task 2:</h5> Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget. - Ensure that the setter methods include validation (e.g., budget should be a positive number).
<br><br>

<b>Expected Outcome:</b> Methods that allow controlled access and modification of the private attributes, with validation checks in place.

<h5>Task 3:</h5> Add Budget Functionality Implement a method to add expenses to a category and adjust the budget accordingly. - Validate the expense amount before making deductions from the budget.
<br><br>

<b>Expected Outcome:</b> Ability to track expenses per category and update the remaining budget safely.

<h5>Task 4:</h5> Display Budget Details Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.

<b>Expected Outcome:</b> Users can view a summary of each budget category, showcasing encapsulation in action.

Code Examples:

```
class BudgetCategory:
    # Constructor and private attributes
    # ...

    # Getters and setters for category name and budget
    # ...

    def add_expense(self, amount):
        # Method to add an expense to the category
        # ...

    def display_category_summary(self):
        # Method to display the budget category details
        # ...

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
```

<b>NOTE:</b> Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs. If there are classes/objects, make sure they are instantiated and the methods are called.

The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.