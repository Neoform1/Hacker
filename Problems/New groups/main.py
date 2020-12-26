# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
groups_dict = dict.fromkeys(groups, None)
n_groups = int(input())
# print(n_groups)
for i in range(n_groups):
    # print(i)
    groups_dict[groups[i]] = int(input())
print(groups_dict)
