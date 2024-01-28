import csv
import random

with open('hotel_rooms.csv', mode='w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["room_id", "hotel_id", "type", "number", "floor", "price", "view", "description"])

    hotels = {
        1: {'name': 'Отель 1', 'num_rooms': 38, 'price_range': (2500, 3500)},
        2: {'name': 'Отель 2', 'num_rooms': 41, 'price_range': (4500, 5500)},
        3: {'name': 'Отель 3', 'num_rooms': 38, 'price_range': (3000, 4000)},
        4: {'name': 'Отель 4', 'num_rooms': 66, 'price_range': (7000, 8000)},
    }

    price_ranges = {
        'SNL': (2000, 3500),
        'DBL': (2500, 4000),
        'TWN': (3000, 4500),
        'SUITE': (11000, 20000),
        'JSUITE': (7000, 11000),
    }
    room_types = ['SNL', 'DBL', 'TWN', 'SUITE', 'JSUITE']
    view_types = ['Mountain', 'Forest']

    room_id = 1
    for hotel_id, hotel in hotels.items():
        hotel_name = hotel['name']
        num_rooms = hotel['num_rooms']
        for i in range(num_rooms):
            type = random.choice(room_types)
            number = [random.choice(range(start, end, 2)) for start, end in [(101, 110), (201, 210), (301, 310)]]
            room_number = random.choice(number)
            floor = random.randint(1, 4)
            price_range = price_ranges[type]
            price = round(random.uniform(*price_range) / 1000) * 1000
            view = random.choice(view_types)
            if type == 'SNL':
                description = f"Odnomestnyj nomer s odnoj krovat'yu"
            elif type == 'DBL':
                description = f"Dvuhmestnyj nomer s odnoj krovat'yu"
            elif type == 'TWN':
                description = f"Dvuhmestnyj nomer s dvumya otdel'nymi krovatyami"
            elif type == 'JSUITE':
                description = f"Polulyuks bol'shoj so svoej kuhnej"
            else:
                description = f"Roskoshnyj nomer lyuks s gostinoj i spal'nej'"
            writer.writerow([room_id, hotel_id, type, room_number, floor, price, view, description])
            room_id += 1


