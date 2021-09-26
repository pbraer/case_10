# Case-study №9 / Gas station operation model
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Zhuravlev A. (%)

from random import randint

#petrol price
price = {'АИ-92': 45.02, 'АИ-80': 31.50, 'АИ-98': 57.72}

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

# Information about day
#print(azs_info)

with open('input.txt', 'r') as info:
    to_read = info.readlines()
    day_info = []
    for line in to_read:
        inf = []
        hours = line[:line.find(':')]
        hours = int(hours)
        inf.append(hours)
        minutes = line[line.find(':') + 1: line.find(' ')]
        minutes = int(minutes)
        inf.append(minutes)
        line = line[line.find(' ') + 1:]
        litres = line[:line.find(' ')]
        litres = int(litres)
        inf.append(litres)
        petrol = line[line.find(' ') + 1: line.find('\n')]
        inf.append(petrol)
        day_info.append(inf)


# Writing about new client

def new_client_done(hour, minute, petrol, litres, need_minutes, number):
    hour = str(hour)
    if len(hour) == 1:
        hour = '0' + hour
    minute = str(minute)
    if len(minute) == 1:
        minute = '0' + minute
    print('В ', hour, ':', minute, ' новый клиент:  ', hour, ':', minute, ' ', petrol, ' ', litres, ' ', need_minutes,
          ' встал в очередь к автомату №', number, sep='')

def new_client_fail(hour, minute, petrol, litres, need_minutes):
    hour = str(hour)
    if len(hour) == 1:
        hour = '0' + hour
    minute = str(minute)
    if len(minute) == 1:
        minute = '0' + minute
    print('В ', hour, ':', minute, ' новый клиент:  ', hour, ':', minute, ' ', petrol, ' ', litres, ' ', need_minutes,
          ' не смог заправить автомобиль и покинул АЗС.', sep='')


new_client_done(1, 1, 'АИ-68', 50, 4, 3)


# Writing about information of machine at the moment

def machine_info(number, max_queue, petrol, amount):
    print('Автомат №', number, ' максимальная очередь: ', max_queue, ' Марки бензина: ', petrol, ' ->', amount, sep='')


machine_info(3, 4, 'АИ-68', '**')

def result(sum_litres, sum, lose):
        print('Количество литров, проданное за сутки по каждой марке бензина: ', sum_litres, sep='')
        print('Общая сумма продаж за сутки: ', sum, sep='')
        print('Количество клиентов, которые покинули АЗС не заправив автомобиль из-за «скопившейся» очереди: ', lose, sep='')

