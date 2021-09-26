# Case-study №9 / Gas station operation model
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Zhuravlev A. (%)

import random
import math

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
        inf.append('')
        azs_info[number] = inf

# Information about day

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
    done = 'В ' + hour + ':' + minute +' новый клиент: ' + hour + ':' + minute + ' ' + petrol + ' ' + litres + ' ' + need_minutes + ' встал в очередь к автомату №' + number
    return done

def new_client_fail(hour, minute, petrol, litres, need_minutes):
    hour = str(hour)
    if len(hour) == 1:
        hour = '0' + hour
    minute = str(minute)
    if len(minute) == 1:
        minute = '0' + minute
    fail = 'В ' + hour + ':' + minute + ' новый клиент:  ' + hour + ':' + minute + ' ' + petrol + ' ' + litres + ' ' + need_minutes + ' не смог заправить автомобиль и покинул АЗС.'
    return fail


def new_client_go(new_hour, new_minute, hour, minute, petrol, litres, need_minutes):
    go = 'В ' + new_hour + ':' + new_minute + ' клиент:  ' + hour + ':' + minute + ' ' + petrol + ' ' + litres + ' ' + need_minutes + ' заправил свой автомобиль и покинул АЗС.'
    return go

# Writing about information of machine at the moment

def machine_info(number, max_queue, petrol, amount):
    m_inf = 'Автомат №' + number + ' максимальная очередь: ' + max_queue + ' Марки бензина: ' + petrol + ' ->' + amount
    return m_inf


def result(sum_litres, sum, lose):
        print('Количество литров, проданное за сутки по каждой марке бензина: ', sum_litres, sep='')
        print('Общая сумма продаж за сутки: ', sum, sep='')
        print('Количество клиентов, которые покинули АЗС не заправив автомобиль из-за «скопившейся» очереди: ', lose, sep='')


result_today = {}
now = []
for avt in azs_info:
    info = azs_info[avt]
    if len(info[1]) == 3:
        petrol = ''
        for el in info[1]:
            petrol = petrol + el + ' '
        petrol = petrol[:len(petrol) - 1]
    else:
        petrol = info[1]
    m_inf = machine_info(str(avt), str(info[0]), str(petrol), str(info[2]))
    now.append(m_inf)

for client in day_info:
    h_time = str(client[0])
    if len(h_time) == 1:
        h_time = '0' + h_time
    m_time = str(client[1])
    if len(m_time) == 1:
        m_time = '0' + m_time
    before = len(result_today)
    for machine in azs_info:
        inf = azs_info[machine]
        if 0 <= len(inf[2]) <= inf[0] and client[3] in inf[1] or client[3] == inf[1]:
            need_min = math.ceil(client[2]/10 + random.randint(-1, 1))
            done = new_client_done(h_time, m_time, str(client[3]), str(client[2]), str(need_min), str(machine))
            old_h = h_time
            old_m = m_time
            m_time = client[1] + need_min
            h_time = client[0]
            if m_time >= 60:
                m_time -= 60
                h_time += 1
            m_time = str(m_time)
            h_time = str(h_time)
            if len(h_time) == 1:
                h_time = '0' + h_time
            if len(m_time) == 1:
                m_time = '0' + m_time
            go = new_client_go(h_time, m_time, old_h, old_m, str(client[3]), str(client[2]), str(need_min))
            result_today[done] = now
            result_today[go] = now
            break
    if len(result_today) != before:
        fail = new_client_fail(h_time, m_time, str(client[3]), str(client[2]), str(math.ceil(client[2] / 10 + random.randint(-1, 1))))
        result_today[done] = now

result_list = list(result_today.keys())
result_list.sort()

for step in result_list:
    data = result_today[step]
    print(step)
    for avt in data:
        print(avt)
