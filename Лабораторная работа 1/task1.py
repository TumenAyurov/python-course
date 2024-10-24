numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
Nonenumber = sum(number for number in numbers if number is not None)/len([number for number in numbers])
numbers[numbers.index(None)] = Nonenumber
print("Измененный список:", numbers)
