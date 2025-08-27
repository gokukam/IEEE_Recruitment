# Lists whose intersection must be taken
list1 = [3, 4, 5, 1, 4, 6, 1, 7, 7]
list2 = [5, 8, 2, 9, 9, 4, 6, 3]

# Final intersection list
final = []

# Traversing one of them (can be list2 also)
for i in list1:
    # Add element to final only if it is common to both lists and does not
    # already exist in final
    if i in list2 and i not in final:
        final.append(i)

print(final)
