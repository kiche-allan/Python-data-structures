#it ensures that the keys that a value is assigned to are unique, just as a dictionary cannot have the name great twice

customer = {
    "Name" : "Allan Kiche",
    "Age" : 21,
    "Is_verified":True
}

#we can access anythin from the above list using the sqiuare brackets

#.get returns a boolean value, it  doesnt return an error when we use a different key
print(customer["Name"])

#WE CAN ASLO ADD NEW PAIR VALUES TO A DICTIONARY
customer["Birthdate"] = "January 30 1999"

print(customer["Birthdate"])

#TEST
#write a program that changes input values to words

#have a dictionary that maps it to word
phone = input("Phone ")

digits_map = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output =""
for ch in phone:
    output +=digits_map.get(ch, "!") +  " "
print(output)