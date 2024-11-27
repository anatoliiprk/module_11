import inspect as ins

print('------\nЗадание по теме "Интроспекция"\n------')

# Создание требуемой функции
def introspection_info(obj):
    dict_info = {}
    dict_info['type'] = type(obj)
    attribute_list = []
    method_list = []
    for attr_name in dir(obj):
        if callable(attr_name):
            method_list.append(attr_name)
        else:
            attribute_list.append(attr_name)
    dict_info['attribute'] = attribute_list
    dict_info['methos'] = method_list
    module_path = ins.getmodule(obj)
    module_path = str(module_path)
    start = module_path.find('__')
    end = module_path.rfind('__')+2
    module_name = module_path[start:end]
    dict_info['module'] = module_name
    return dict_info

# Классы для проверки работы заданной функции

class Horse:
    def __init__(self, x_distance = 0, y_distance = 0, sound = 'Frrr'):
        self.x_distance = x_distance
        self.sound = sound
        super().__init__(y_distance)

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    def __init__(self, y_distance = 0, sound = 'I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__(self, x_distance = 0, y_distance = 0, sound = '', dx = 0, dy = 0):
        super().__init__(x_distance, y_distance, sound)
        Horse.run(self, dx)
        Eagle.fly(self, dy)

    def move(self, dx: int, dy: int):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        coordinates = (self.x_distance, self.y_distance)
        return coordinates

    def voice(self):
        print(self.sound)

# Проверка работы заданной фунции
h1 = Horse
e1 = Eagle
p1 = Pegasus
p1(3,5)

horse_info = introspection_info(h1)
print(horse_info)
eagle_info = introspection_info(e1)
print(eagle_info)
pegasus_info = introspection_info(p1)
print(pegasus_info)
