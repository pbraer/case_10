print('hi')
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


class GasStation:
    def __init__(self, number, queue_len, gas_types, queue=0, time=0, litres=0, client_gas=0):
        self.number = number
        self.queue_len = queue_len
        self.gas_types = gas_types
        self.queue = queue
        self.time = time
        self.litres = litres
        self.client_gas = client_gas

    def __repr__(self):
        return 'Автомат №'+self.number + ' Максимальная очередь: ' + self.queue_len + ' Марки бензина:' + self.gas_types + '->' + self.queue


a = GasStation('1', '3', '98, 92, 95', '1')
print(a)


