def dedup(my_list, new_file):
    d = list()
    for single_line in my_list:
        if single_line.split(',')[1] not in [i.split(',')[1] for i in d]:
            d.append(single_line)
    print(len(my_list), len(d))
    new_file.writelines(d)


with open('plec.txt', 'r') as my_file:
    data = my_file.readlines()[1:]

males = open('m.txt', 'w')
females = open('f.txt', 'w')

males_list = list()
females_list = list()

for line in data:
    gender = line.split(',')[3]
    if gender == 'm':
        males_list.append(line)
    if gender == 'f':
        females_list.append(line)

dedup(males_list, males)
dedup(females_list, females)

# females 22746 17553
