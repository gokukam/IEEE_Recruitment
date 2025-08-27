# Cutoff list
cutoff = [
    ("Pilani", "CS", 327),
    ("Pilani", "Chemical", 247),
    ("Pilani", "Msc. Eco", 271),
    ("Pilani", "Msc. Bio", 236),
    ("Goa", "CS", 301),
    ("Goa", "Chemical", 239),
    ("Goa", "Msc. Eco", 263),
    ("Goa", "Msc. Bio", 234),
    ("Hyderabad", "CS", 298),
    ("Hyderabad", "Chemical", 238),
    ("Hyderabad", "Msc. Eco", 261),
    ("Hyderabad", "Msc. Bio", 234),
]

# The empty dict to which list must be converted
cutoff_dict = {}

# Traversing list of tuples
for row in cutoff:
    campus, branch, marks = row  # Unpacking tuple to get values
    if campus not in cutoff_dict:
        cutoff_dict[campus] = {}  # Creating new campus key if does not exist

    # Finally, adding branch for the campus with marks
    cutoff_dict[campus][branch] = marks

print(cutoff_dict)
