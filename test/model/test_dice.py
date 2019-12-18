import game_objects as go


dice = go.Dice()
dice.roll()
dice.show()
initial_values = dice.values
print("available_values: {}".format(dice.get_available_values()))

# Remove value 1
print("Remove 1st value")
value_1 = initial_values[0]
dice.remove_from_available_values(value_1)
print("available_values: {}".format(dice.get_available_values()))
print("values left: {}".format(dice.number_of_values_left()))

# Remove value 2
print("Remove 2nd value")
value_2 = initial_values[1]
dice.remove_from_available_values(value_2)
print("available_values: {}".format(dice.get_available_values()))
print("values left: {}".format(dice.number_of_values_left()))
