
#
# while True:
#     # Initialize an empty list to store the filtered data
#     filtered_data = []
#
#     # Iterate through the data
#     for i, sublist in enumerate(data):
#         if i == 0:
#             filtered_data.append(sublist)
#         else:
#             prev_sublist = filtered_data[-1]  # Use the last element of filtered_data
#             diff = abs(sublist[1] - prev_sublist[2][2])
#             if diff > 300:
#                 continue
#             else:
#                 filtered_data.append(sublist)
#
#     # If no sublists were removed in the current iteration, break the loop
#     if len(filtered_data) == len(data):
#         break
#
#     # Update the data for the next iteration
#     data = filtered_data
#
# # Print the final filtered data
# for sublist in filtered_data:
#     print(sublist)

#
# from itertools import tee, zip_longest
#

#
#
# # Define a function to check if a sublist should be removed
# def should_remove(prev_sublist, current_sublist):
#     return abs(current_sublist[1] - prev_sublist[2][2]) > 300
#
#
# # Use tee to create two iterators over the data
# data1, data2 = tee(data, 2)
# next(data2, None)  # Advance data2 by one item
#
# # Zip the two iterators together, comparing each sublist with the previous one
# filtered_data = [current_sublist for prev_sublist, current_sublist in zip_longest(data1, data2) if
#                  not should_remove(prev_sublist, current_sublist)]
#
# # Print the final filtered data
# for sublist in filtered_data:
#     print(sublist)
#
# #

#
# from functools import reduce
#

#
#
# # Define a function to check if a sublist should be removed
# def should_remove(prev_sublist, current_sublist):
#     return abs(current_sublist[1] - prev_sublist[2][2]) > 300
#
#
# # Use reduce to filter the data
# filtered_data = reduce(lambda acc, x: acc + [x] if not should_remove(acc[-1], x) else acc, data[1:], [data[0]])
#
# # Print the final filtered data
# for sublist in filtered_data:
#     print(sublist)


from functools import reduce



# Use reduce to filter the data

# filtered_data = reduce(lambda acc, x: acc + [x] if abs(x[1] - acc[-1][2][2]) <= 100 else acc, data[1:], [data[0]])
filtered_data = reduce(
    lambda acc, x: acc + [x] if (not acc and not x[0].isdigit()) or (acc and abs(x[1] - acc[-1][2][2]) <= 300) else acc,
    data, [])
# Print the final filtered data
for sublist in filtered_data:
    print(sublist)