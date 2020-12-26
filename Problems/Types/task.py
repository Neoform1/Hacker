#  Posted from EduTools plugin
# import sys

# args = sys.argv
# args = input()
# the variable "args" is already defined

my_list = []  # your code here

if len(args) != 5:
    print("The script should be called with four arguments")
else:
    first_num = int(args[1])
    second_num = int(args[2])
    third_num = int(args[3])
    fourth_num = int(args[4])
    my_list = [first_num, second_num, third_num, fourth_num]

print(str(my_list))
# print(args)
# print(arg)
