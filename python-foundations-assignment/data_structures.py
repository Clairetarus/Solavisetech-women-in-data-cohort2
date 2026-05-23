# Favorite Tools List
tools = ["Python", "Excel", "Power BI"]

tools.append("GitHub")
tools.remove("Excel")

print("Favorite Tools:", tools)

# Student Scores
scores = [78, 85, 90, 67, 88]

print("Highest Score:", max(scores))
print("Lowest Score:", min(scores))
print("Average Score:", sum(scores) / len(scores))

# Shopping List Manager
shopping_list = []

shopping_list.append("Milk")
shopping_list.append("Bread")
shopping_list.append("Eggs")

print("Shopping List:", shopping_list)

shopping_list.remove("Bread")

print("Updated Shopping List:", shopping_list)

# Country Capitals using Tuples
countries = (
    ("Kenya", "Nairobi"),
    ("Uganda", "Kampala"),
    ("Tanzania", "Dodoma")
)

print("Country Capitals:", countries)

# Unique Visitors using Sets
visitors = ["Claire", "John", "Claire", "Mary"]

unique_visitors = set(visitors)

print("Unique Visitors:", unique_visitors)

# Common Skills
skills1 = {"Python", "SQL", "Excel"}
skills2 = {"Python", "Power BI", "Excel"}

common_skills = skills1.intersection(skills2)

print("Common Skills:", common_skills)

# Student Record using Dictionary
student = {
    "name": "Claire",
    "age": 20,
    "course": "Computer Science"
}

print("Student Record:", student)

# Mini Contact Book
contacts = {
    "Alice": "0712345678",
    "Brian": "0798765432"
}

search = input("Enter contact name: ")

if search in contacts:
    print("Phone Number:", contacts[search])
else:
    print("Contact not found")
