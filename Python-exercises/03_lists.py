skills = ["Python", "Java", "AWS"]

print("Original:", skills)

skills.append("Docker")
print("After adding:", skills)

skills.remove("Java")
print("After removing:", skills)

print("First skill:", skills[0])
print("Number of skills:", len(skills))