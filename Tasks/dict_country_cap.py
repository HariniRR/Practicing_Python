#program that creates a dictionary with five countries as keys and their capitals as values. Print the capital of a specific country.
my_dict = {"Afghanistan": "Kabul",
    "Bangladesh": "Dhaka",
    "Bhutan": "Thimphu",
    "India": "New Delhi",
    "Maldives": "Malé",
    "Nepal": "Kathmandu",
    "Pakistan": "Islamabad",
    "Sri Lanka": "Sri Jayawardenepura Kotte"
}
country = input("Enter the name of a South Asian country: ")
if country in my_dict:
    print(f"The capital of {country} is: {my_dict[country]}")
else:
    print("Country not found in the dictionary.")

'''op
Enter the name of a South Asian country: India
The capital of India is: New Delhi'''
