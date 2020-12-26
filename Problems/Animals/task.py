# read animals.txt
new_list = []
animals = open('animals.txt', 'r')

for a in animals:
    new_list.append(a.replace('\n', ' '))
animals.close()

# and write animals_new.txt
animals_new = open('animals_new.txt', 'w')
animals_new.writelines(new_list)
animals_new.close()
