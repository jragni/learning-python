#!/usr/bin/env Python
# Author: Jhensen Ray Agni

pizzaType = ['cheese','pepperoni','hawaiian','combo','chicken parmesan']

statement = "\nI really like {} pizza"
dislikeStatement = "\nActually, I don't like {} pizza nor {} pizza."
for pizza in pizzaType:
    print(statement.format(pizza.title())) 


dislikedPizzas =[ pizzaType.pop(3)]
dislikedPizzas.append(pizzaType.pop(2))
print(dislikeStatement.format(dislikedPizzas[0],dislikedPizzas[1]))

  

