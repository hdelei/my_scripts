
class Map:    
    
    def __init__(self, cols, rows, airports, clouds):
        #cols and rows only necessary to draw a map
        self.clouds = clouds        
        self.airports = airports
        
    def days(self):
        day_count = []

        for airport in self.airports:
            for cloud in self.clouds:
                x_diff = airport[0] - cloud[0]
                y_diff = airport[1] - cloud[1]
                day_count.append(abs(x_diff) + abs(y_diff))                
                print(day_count)
        
        
        minimum = min(day_count)
        maximum = minimum

        # if len(day_count) > 1 and len(self.airports) > 1:
        #     maximum = min(day_count[0::2])

        if len(day_count) > 1 and len(self.airports) > 1:
            day_count.sort()
            index = day_count.index(minimum)
            maximum = day_count[index+1]
            
        print('RETURN:', [minimum, maximum], '\n')
        return [minimum, maximum]    

BROKEN = ' is broken'

map = Map(11, 11, [(1,1)], [(7,10)])
TAG = '1 airport and 1 cloud function'
print(TAG)
assert map.days() == [15,15], TAG + ' is broken'

map = Map(11, 11, [(1, 1)], [(7, 10), (7, 9)])
TAG = '1 airport and 2 clouds function'
print(TAG)
assert map.days() == [14, 14], TAG + BROKEN

map = Map(10, 10, [(0,3),(1,4)], [(0,0), (1,8)])
TAG = '2 airports and 2 clouds function'
print(TAG)
assert map.days() == [3, 4], TAG + BROKEN

#Testar melhor com 3 aeroportos
map = Map(10, 10, [(0,3),(1,4), (0,0)], [(0,0), (1,7), (1,8)])
#assert map.days() == [1, 2], '2 map and 2 clouds function is broken'
print('3 airports and 3 clouds:', map.days())