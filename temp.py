# *** ----- Naive solution ----- ***

# uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# substrings_list = []

# for out_count in range(0,23):
#     substrings = uppercase[out_count]
#     inn_start = out_count+1

#     if inn_start>len(uppercase):
#         inn_start = inn_start % out_count
#     else: 
#         inn_start = inn_start

#     inn_end = out_count+4

#     if inn_end>len(uppercase):
#         inn_end = inn_end % out_count
#     else: 
#         inn_end = inn_end

#     for inn_count in range(inn_start, inn_end):
#         substrings += uppercase[inn_count]
#     substrings_list.append(substrings)

# *** ----- Better solution ----- ***
    
#uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#ascii_hash_values = dict()

# #Checkpoint 1
# def ascii_hash(s):
#   ascii_hash = 1
#   for c in s:
#     ascii_hash *= ord(c)
#   return ascii_hash

# #Checkpoint 2
# substrings_list =[]
# for out_count in range(23):  
#     substrings = uppercase[out_count:out_count+4]
#     substrings_list.append(substrings)

# for substrings in substrings_list:
#   ascii_hash_values.update({substrings: ascii_hash(substrings)})
# #print(ascii_hash_values)


# import itertools

# uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ascii_product = dict()
# seen = dict()
# dup_dict = dict()

# combination_of_twos = list(itertools.combinations(uppercase, 2))
# combination_of_twos_string = [''.join(combo) for combo in combination_of_twos]
# #print(combination_of_twos_string)

# for string in combination_of_twos_string:
#     product = 1
#     for c in string:
#         product *= ord(c)
#     ascii_product.update({string: product})

# for e_key, e_val in ascii_product.items():
#     if e_val in seen:
#         #if e_val not in dup_dict:
#             dup_dict.update({e_key:e_val})
#     else:
#         seen.update({e_key:e_val})
# print(dup_dict)

