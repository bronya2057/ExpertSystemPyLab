from collections import OrderedDict

rules_in_order = OrderedDict()

array_of_array = [['1000-2000', 'Veg', 'Yes'], ['1000-2000', 'Veg', 'Yes']]

str = ", ".join(array_of_array[0])

rules_in_order[str] = "Hello"

print(rules_in_order)