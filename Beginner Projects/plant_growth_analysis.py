# First we store data in a list
growth = [3, 1, 2, 4, 2, 3, 2]

# Second we sort out the list depending on what value client is after. 
growth.sort()
smallest_growth = growth[0]
print(f'The smallest growth in the week is: {smallest_growth}cm')
biggest_growth = growth[len(growth) - 1]
print(f'The biggest growth in the week is: {biggest_growth}cm')
average_growth = sum(growth) / len(growth)
print(f'The average growth in the week is: {average_growth}cm')

# Here we combine data for further analysis for client
new_growth = [2, 0, 3, 2, 4, 5, 4]
joined_growth = growth + new_growth

# Here is an alternative syntax to get results from 2nd code block above
joined_smallest_growth = min(joined_growth)
print(f'The smallest growth in these 2 weeks is: {joined_smallest_growth}cm')
joined_biggest_growth = max(joined_growth)
print(f'The biggest growth in these 2 weeks is: {joined_biggest_growth}cm')
joined_average_growth = sum(joined_growth) / len(joined_growth)
print(f'The average growth in these 2 weeks is: {joined_average_growth}cm')

# And here the client wants to know how many times smallest and biggest growth values occured
joined_smallest_growth_count = joined_growth.count(joined_smallest_growth)
print(f'The smallest growth happened {joined_smallest_growth_count} times in these 2 weeks')
joined_biggest_growth_count = joined_growth.count(joined_biggest_growth)
print(f'The biggest growth happened {joined_biggest_growth_count} times in these 2 weeks')