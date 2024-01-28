# import csv
# import random

# with open('sales_fact.csv', 'w', newline='') as file:
#     # Создаем объект writer для записи данных в CSV файл
#     writer = csv.writer(file)
#     writer.writerow(['fact_id', 'service_id', 'hotel_id', 'room_id', 'booking_id', 'guest_id', 'channel_id', 'employee_id', 'sales_date', 'sales'])
   
#     # Идентификатор
#     fact_id = 1
#     with open('C:/Users/Jess/pet_project/bookings.csv', 'r', newline='') as fl:
#         data = csv.reader(fl)
    
#     # Записываем данные по каждому отелю
#         for row in data:
#             for i in range(25):
#                 service_id = random.randint(1, 79)
#                 hotel_id = data[1]
#                 room_id = data[2]
#                 booking_id = data[0]
#                 guest_id = data[3]
#                 channel_id = data[4]
#                 employee_id = 22
#                 sales_date = 22
#                 sales = 100
#         # [random.choice(range(start, end, 2)) for start, end in [(101, 110), (201, 210), (301, 310)]]
#         # room_number = random.choice(number)

#         # Записываем данные в CSV файл
#                 writer.writerow([fact_id, service_id, hotel_id, room_id, booking_id, guest_id, channel_id, employee_id, sales_date, sales])
#         # Увеличиваем идентификатор услуги на 1
#                 fact_id += 1




# booking_id,hotel_id,room_id,guest_id,channel_id берутся с букингс и должны быть одинаковые



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


# Создаем список, куда будем записывать данные из bookings.csv
booking_data = []
fact_id = 0

with open('bookings.csv', 'r', newline='') as file:
    data = csv.reader(file)
    next(data) # Пропускаем заголовки на первой строке
    
    for row in data:
        booking_id = row[0]
        hotel_id = row[1]
        room_id = row[2]
        guest_id = row[3]
        channel_id = row[4]
        
        # Добавляем данные в наш список
        booking_data.append([booking_id, hotel_id, room_id, guest_id, channel_id])

# Запишем данные в sales_fact.csv
with open('sales_fact.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['fact_id', 'service_id', 'hotel_id', 'room_id', 'booking_id', 'guest_id', 'channel_id', 'employee_id', 'sales_date', 'sales'])
    
    # Заполняем данные из списка и добавляем случайные значения
    for i in range(len(booking_data)):
        booking_id = booking_data[i][0]
        hotel_id = booking_data[i][1]
        room_id = booking_data[i][2]
        guest_id = booking_data[i][3]
        channel_id = booking_data[i][4]
        
        service_id = random.randint(1,79)
        employee_id = random.randint(1,5)
        sales_date = random_date(start_date, end_date)
        sales = 100
        fact_id += 1
        # Пишем одну строку в sales_fact.csv
        writer.writerow([fact_id, service_id, hotel_id, room_id, booking_id, guest_id, channel_id, employee_id, sales_date, sales])
