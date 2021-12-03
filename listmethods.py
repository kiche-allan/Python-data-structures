numbers = [5, 7, 2, 1, 7, 4, 7]

numbers.append(20)

print(numbers)

numbers.insert(0,17)

print(numbers)

numbers.remove(7)


print(numbers)

# numbers.clear()

print(numbers.index(5))

print(50 in numbers)

# counting the occurences of an item

print(numbers.count(7))


# sorting the list in ascending order

print(numbers.sort())
print(
    numbers
)

# sorting the list in descending order
numbers.reverse()
print(numbers)


#
#
# copying a list
numbers2 = numbers.copy()
numbers.append(10)

print(numbers2)

il = [2, 2, 4, 4, 9, 9, 1, 5]

unique = []

for ils in il:
    if ils not in unique:
        unique.append(ils)
print(unique)
