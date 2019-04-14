def calc(meters=3.5, interval=3.5):
    ''' this script calculates the best intervals for
        electric fence stems based on given measurements
    '''
    result = {
        'stem':int((meters/interval) + 1),
        'interval': interval,
        'distance': meters
        }

    if meters % interval == 0:
        return result

    MAX = interval + 0.5
    MIN = interval - 0.5
    int_division = meters // interval
    meter_closest = []
    interval_list = []

    min_range = int(MIN * 100)
    max_range = int((MAX * 100) + 1)

    range_list = range(min_range, max_range, 1)

    for i in range_list:
        i_decimal = i/100
        interval_list.append(i_decimal)
        meter_closest.append(i_decimal * int_division)

    closest = min(meter_closest, key=lambda x:abs(x-meters))

    result['stem'] = int_division + 1
    result['interval'] = interval_list[meter_closest.index(closest)]
    result['distance'] = closest

    return result

while True:
    meters = input('Digite a distancia: ')
    interval = input('Digite o intervalo: ')

    result = calc(float(meters), float(interval))
    print()
    print(int(result['stem']), 'hastes')
    print('Intervalo:', result['interval'], 'metros')
    print('Distancia considerada:', result['distance'], 'metros')
    #print(calc(float(meters), float(interval)))
    print('\nMais um calculo?\n')

