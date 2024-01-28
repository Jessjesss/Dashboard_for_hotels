import csv
import random
from datetime import date, timedelta

# Генерация случайных дат в диапазоне от start до end
def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )

# Определение интервала дат для генерации бронирований
start_date = date(2022, 3, 1)
end_date = date(2023, 3, 1)

# Чтение файла с данными номеров и формирование словаря room_id -> price
rooms = {}
with open('hotel_rooms.csv', mode='r', encoding='utf-8', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        room_id = int(row['room_id'])
        hotel_id = int(row['hotel_id'])
        price = int(row['price'])
        rooms[room_id] = price

# Определение списка описаний бронирований
descriptions = ['', 'Hochet zaekhat poranshe', '', '', 'Perezvonit, esli osvoboditsya lyuks', '','Hochet vid iz okna na gory']

# Генерация данных для каждого бронирования
bookings = []
for i in range(1000):
    booking_id = i + 1
    room_id = random.randint(1, 183)
    if room_id in range(1,39):
        hotel_id = 1
    elif room_id in range(39,80):
        hotel_id = 2
    elif room_id in range(80,118):
        hotel_id = 3
    else:
        hotel_id = 4
    guest_id = random.randint(1, 150200)
    channel_id = random.randint(1, 8)
    arrival_date = random_date(start_date, end_date)
    random_days = random.randint(1, 14)
    departure_date = arrival_date + timedelta(days=random_days)
    total_price = rooms[room_id]
    prepayment = total_price//2
    description = random.choice(descriptions)
    bookings.append([
        booking_id, hotel_id, room_id, guest_id, channel_id, 
        arrival_date, departure_date, prepayment, total_price, description
    ])

# Запись данных в CSV файл
with open('bookings.csv', mode='w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([
        'booking_id', 'hotel_id', 'room_id', 'guest_id', 'channel_id', 
        'arrival_date', 'departure_date', 'prepayment', 'total_price', 'description'
    ])
    writer.writerows(bookings)