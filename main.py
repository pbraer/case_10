# Case-study №9 / Gas station operation model
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Zhuravlev A. (%)

# Information about machines
with open('azs.txt', 'r') as info:
    to_read = info.readlines()
    azs_info = {}
    for line in to_read:
        inf = []
        number = line[:line.find(' ')]
        line = line[line.find(' ') + 1:]
        q_max = line[:line.find(' ')]
        line = line[line.find(' ') + 1:]
        inf.append(int(q_max))
        petrol = line[:line.find('\n')]
        if petrol.find(' ') != -1:
            petrol = petrol.split(' ')
            petrol = set(petrol)
        inf.append(petrol)
        azs_info[number] = inf
print(azs_info)
