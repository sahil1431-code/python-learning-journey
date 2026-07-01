# Week 1 Python Learning Journey
# Student Information Manager

student = {
    "name": "Rudra",
    "age": 20,
    "course": "B.Tech CSE",
    "skills": ["Python", "Git", "Problem Solving"]
}

print("===== Student Details =====")
print(f"Name   : {student['name']}")
print(f"Age    : {student['age']}")
print(f"Course : {student['course']}")

print("\nSkills:")
for skill in student["skills"]:
    print("-", skill)

# Tuple Unpacking
location = ("Bhubaneswar", "Odisha")
city, state = location

print("\nLocation:")
print(f"City  : {city}")
print(f"State : {state}")

# Object Identity
a = 100
b = 100

print("\nObject Identity")
print("id(a):", id(a))
print("id(b):", id(b))
print("Same Object:", a is b)
