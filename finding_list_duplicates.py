my_list = [1, 2, 3, 3, 2, 1]

# Set to track unique elements and list to track duplicates
unique_elements = set()
dups = []

for elem in my_list:
    if elem in unique_elements:  # If element is already in set, it's a duplicate
        if elem not in dups:  # Make sure to add it only once to dups
            dups.append(elem)
    else:
        unique_elements.add(elem)  # Otherwise, add the element to unique_elements

print(dups)


# *** ----- Another Way ----- ***

# list_of_dup = []
# list_of_non_dup = []
# for elem in vals_list:
#     if elem in list_of_non_dup:
#         if elem not in list_of_dup:
#             list_of_dup.append(elem)
#     else:
#         list_of_non_dup.append(elem)
# print(f"list_of_dup {list_of_dup}")
# print(f"list_of_non_dup {list_of_non_dup}")

