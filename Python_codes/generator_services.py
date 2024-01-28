import csv

# Создаем список услуг для каждого отеля
hotel_1_services = [
    {'category': 'Banya', 'name': 'Finskaya sauna', 'price': 1500, 'discount': '', 'description': 'Dlya 6-8 chelovek'},
    {'category': 'Banya', 'name': 'Russkaya banya', 'price': 2000, 'discount': '', 'description': 'Dlya 4-6 chelovek'},
    {'category': 'Banya', 'name': 'Banya na drovakh', 'price': 2500, 'discount': '', 'description': 'Dlya 2-4 chelovek'},
    {'category': 'SPA', 'name': 'Muzhskoy massazh', 'price': 3500, 'discount': '', 'description': 'Klassicheskiy massazh dlya muzhchin'},
    {'category': 'SPA', 'name': 'Zhenskiy massazh', 'price': 3500, 'discount': '', 'description': 'Klassicheskiy massazh dlya zhenshchin'},
    {'category': 'SPA', 'name': 'Spa procedury', 'price': 5000, 'discount': '', 'description': 'Kompleks spa-protsedur'},
    {'category': 'RESTAURANT', 'name': 'Zavtrak', 'price': 500, 'discount': '', 'description': 'Blyuda evropeyskoy kukhni'},
    {'category': 'RESTAURANT', 'name': 'Obed', 'price': 800, 'discount': '', 'description': 'Blyuda evropeyskoy i aziskoy kukhni'},
    {'category': 'RESTAURANT', 'name': 'Uzhin', 'price': 1000, 'discount': '', 'description': 'Blyuda evropeyskoy i natsionalnoy kukhni'},
    {'category': 'FITNESS', 'name': 'Gimnastika', 'price': 500, 'discount': '', 'description': 'Zanyatiya gimnastikoy'},
    {'category': 'FITNESS', 'name': 'Kardiotrenirovki', 'price': 800, 'discount': '', 'description': 'Zanyatiya na kardiotrenazherakh'},
    {'category': 'FITNESS', 'name': 'Personalnyy trener', 'price': 2500, 'discount': '', 'description': 'Individualnye trenirovki'},
    {'category': 'Prokat', 'name': 'Prokat gornolyzhnogo snaryazheniya', 'price': 2500, 'discount': '', 'description': 'Snowboard ili lyzhi complect'},
    {'category': 'Prikat', 'name': 'Prokat botinok', 'price': 1000, 'discount': '', 'description': ''},
    {'category': 'Prikat', 'name': 'Prokat odezhdy', 'price': 2000, 'discount': '', 'description': ''},
    {'category': 'POOL', 'name': 'Basseyn', 'price': 1000, 'discount': 0, 'description': 'Basseyn dlya vsekh gostey'},
    {'category': 'POOL', 'name': 'Jacuzzi', 'price': 1500, 'discount': 0, 'description': 'Relaksatsiya v dzhakuzi'},
    {'category': 'ROOM_SERVICE', 'name': 'Pitstsa', 'price': 800, 'discount': '', 'description': 'Pitstsa dostavlyaetsya v nomer'},
    {'category': 'ROOM_SERVICE', 'name': 'Sushi', 'price': 1000, 'discount': '', 'description': 'Sushi dostavlyaetsya v nomer'}

]

hotel_2_services = [    
    {'category': 'Banya', 'name': 'Finskaya sauna', 'price': 2500, 'discount': '', 'description': 'Dlya 6-8 chelovek'},
    {'category': 'Banya', 'name': 'Russkaya banya', 'price': 3000, 'discount': '', 'description': 'Dlya 4-6 chelovek'},    
    {'category': 'Banya', 'name': 'Banya na drovah', 'price': 3500, 'discount': '', 'description': 'Dlya 2-4 chelovek'},    
    {'category': 'Bassein', 'name': 'Krytyy bassein', 'price': 3500, 'discount': '', 'description': 'Dlya 10-12 chelovek'},    
    {'category': 'Bassein', 'name': 'Otkrytyy bassein', 'price': 4500, 'discount': '', 'description': 'Dlya 10-12 chelovek'},  
    {'category': 'RESTAURANT', 'name': 'Zavtrak', 'price': 1500, 'discount': '', 'description': 'Blyuda evropeyskoy kukhni'},
    {'category': 'RESTAURANT', 'name': 'Obed', 'price': 2000, 'discount': '', 'description': 'Blyuda evropeyskoy i aziskoy kukhni'},
    {'category': 'RESTAURANT', 'name': 'Uzhin', 'price': 2000, 'discount': '', 'description': 'Blyuda evropeyskoy i natsionalnoy kukhni'},  
    {'category': 'Sport', 'name': 'Tennisnyy kort', 'price': 4000, 'discount': '', 'description': 'Vechernee osveshchenie'},    
    {'category': 'Sport', 'name': 'Basketbolnaya ploshchadka', 'price': 2000, 'discount': '', 'description': 'Dlya komandnoy igry'},    
    {'category': 'Sport', 'name': 'Futbolnoe pole', 'price': 5000, 'discount': '', 'description': 'Dlya 11 igrokov'},    
    {'category': 'Spa', 'name': 'SPA-kompleks', 'price': 7000, 'discount': '', 'description': 'Massazh, kosmetologiya, fitnes'},    
    {'category': 'Razvlecheniya', 'name': 'Kinoteatr', 'price': 3000, 'discount': '', 'description': 'Sovremennoe oborudovanie'},    
    {'category': 'Razvlecheniya', 'name': 'Karaoke-zal', 'price': 2500, 'discount': '', 'description': 'Dlya 4-6 chelovek'},    
    {'category': 'Razvlecheniya', 'name': 'Billiard', 'price': 1500, 'discount': '', 'description': 'Amerikanskiy i russkiy'},    
    {'category': 'Razvlecheniya', 'name': 'Nastolnye igry', 'price': 500, 'discount': '', 'description': 'Shakhmaty, nardy i dr.'}

]

hotel_3_services = [    
    {'category': 'Banya', 'name': 'Finskaya sauna', 'price': 3000, 'discount': '', 'description': 'Dlya 6-8 chelovek'},
    {'category': 'Banya', 'name': 'Russkaya banya', 'price': 3500, 'discount': '', 'description': 'Dlya 4-6 chelovek'},    
    {'category': 'Banya', 'name': 'Banya na drovah', 'price': 4000, 'discount': '', 'description': 'Dlya 2-4 chelovek'},    
    {'category': 'Bassein', 'name': 'Krytyy bassein', 'price': 4000, 'discount': '', 'description': 'Dlya 10-12 chelovek'},    
    {'category': 'Bassein', 'name': 'Otkrytyy bassein', 'price': 5000, 'discount': '', 'description': 'Dlya 10-12 chelovek'},  
    {'category': 'RESTAURANT', 'name': 'Zavtrak', 'price': 2000, 'discount': '', 'description': 'Blyuda evropeyskoy kukhni'},
    {'category': 'RESTAURANT', 'name': 'Obed', 'price': 2500, 'discount': '', 'description': 'Blyuda evropeyskoy i aziskoy kukhni'},
    {'category': 'RESTAURANT', 'name': 'Uzhin', 'price': 2500, 'discount': '', 'description': 'Blyuda evropeyskoy i natsionalnoy kukhni'},  
    {'category': 'Sport', 'name': 'Tennisnyy kort', 'price': 4500, 'discount': '', 'description': 'Vechernee osveshchenie'},    
    {'category': 'Sport', 'name': 'Basketbolnaya ploshchadka', 'price': 2500, 'discount': '', 'description': 'Dlya komandnoy igry'},    
    {'category': 'Sport', 'name': 'Futbolnoe pole', 'price': 6000, 'discount': '', 'description': 'Dlya 11 igrokov'},    
    {'category': 'Spa', 'name': 'SPA-kompleks', 'price': 8000, 'discount': '', 'description': 'Massazh, kosmetologiya, fitnes'}, 
    {'category': 'Prokat', 'name': 'Prokat gornolyzhnogo snaryazheniya', 'price': 3000, 'discount': '', 'description': 'Snowboard ili lyzhi complect'},
    {'category': 'Prokat', 'name': 'Prokat botinok', 'price': 1500, 'discount': '', 'description': ''},
    {'category': 'Prokat', 'name': 'Prokat odezhdy', 'price': 3000, 'discount': '', 'description': ''},      
    {'category': 'Razvlecheniya', 'name': 'Nastolnye igry', 'price': 800, 'discount': '', 'description': 'Shakhmaty, nardy'},
    {'category': 'POOL', 'name': 'Basseyn', 'price': 2000, 'discount': 0, 'description': 'Basseyn dlya vsekh gostey'},
    {'category': 'POOL', 'name': 'Jacuzzi', 'price': 2500, 'discount': 0, 'description': 'Relaksatsiya v dzhakuzi'},
    {'category': 'ROOM_SERVICE', 'name': 'Pitstsa', 'price': 1500, 'discount': '', 'description': 'Pitstsa dostavlyaetsya v nomer'},
    {'category': 'ROOM_SERVICE', 'name': 'Sushi', 'price': 1500, 'discount': '', 'description': 'Sushi dostavlyaetsya v nomer'}
]


hotel_4_services = [
    {'category': 'Banya', 'name': 'Finskaya sauna', 'price': 3500, 'discount': '', 'description': 'Dlya 6-8 chelovek'},
    {'category': 'Banya', 'name': 'Russkaya banya', 'price': 4000, 'discount': '', 'description': 'Dlya 4-6 chelovek'},    
    {'category': 'Banya', 'name': 'Banya na drovah', 'price': 4500, 'discount': '', 'description': 'Dlya 2-4 chelovek'},    
    {'category': 'Bassein', 'name': 'Krytyy bassein', 'price': 4500, 'discount': '', 'description': 'Dlya 10-12 chelovek'},    
    {'category': 'Bassein', 'name': 'Otkrytyy bassein', 'price': 5500, 'discount': '', 'description': 'Dlya 10-12 chelovek'},  
    {'category': 'RESTAURANT', 'name': 'Zavtrak', 'price': 2500, 'discount': '', 'description': 'Blyuda evropeyskoy kukhni'},
    {'category': 'RESTAURANT', 'name': 'Obed', 'price': 3000, 'discount': '', 'description': 'Blyuda evropeyskoy i aziskoy kukhni'},
    {'category': 'RESTAURANT', 'name': 'Uzhin', 'price': 3000, 'discount': '', 'description': 'Blyuda evropeyskoy i natsionalnoy kukhni'},  
    {'category': 'Sport', 'name': 'Tennisnyy kort', 'price': 5000, 'discount': '', 'description': 'Vechernee osveshchenie'},    
    {'category': 'Sport', 'name': 'Basketbolnaya ploshchadka', 'price': 3000, 'discount': '', 'description': 'Dlya komandnoy igry'},    
    {'category': 'Sport', 'name': 'Futbolnoe pole', 'price': 7000, 'discount': '', 'description': 'Dlya 11 igrokov'},    
    {'category': 'Spa', 'name': 'SPA-kompleks', 'price': 9000, 'discount': '', 'description': 'Massazh, kosmetologiya, fitnes'}, 
    {'category': 'Massage', 'name': 'Klassicheskiy massazh', 'price': 3500, 'discount': '', 'description': ''},
    {'category': 'Massage', 'name': 'Sportivnyy massazh', 'price': 4000, 'discount': '', 'description': ''},
    {'category': 'Massage', 'name': 'Tayskiy massazh', 'price': 5000, 'discount': '', 'description': ''},
    {'category': 'Massage', 'name': 'Massazh spiny i shei', 'price': 3000, 'discount': '', 'description': ''},
    {'category': 'Prokat', 'name': 'Prokat gornolyzhnogo snaryazheniya', 'price': 3000, 'discount': '', 'description': 'Snowboard ili lyzhi complect'},
    {'category': 'Prokat', 'name': 'Prokat gornolyzhnogo snaryazheniya', 'price': 4000, 'discount': '', 'description': 'Snowboard ili lyzhi komplect'},
    {'category': 'Prokat', 'name': 'Prokat botinok', 'price': 2000, 'discount': '', 'description': ''},
    {'category': 'Prokat', 'name': 'Prokat odezhdy', 'price': 4000, 'discount': '', 'description': ''},   
    {'category': 'Razvlecheniya', 'name': 'Kinoteatr', 'price': 4000, 'discount': '', 'description': 'Sovremennoe oborudovanie'},
    {'category': 'Razvlecheniya', 'name': 'Karaoke-zal', 'price': 3000, 'discount': '', 'description': 'Dlya 4-6 chelovek'},    
    {'category': 'Razvlecheniya', 'name': 'Billiard', 'price': 2000, 'discount': '', 'description': 'Amerikanskiy i russkiy'} 
]
# Создаем список отелей
hotels = [
    {'hotel_id': 1, 'services': hotel_1_services},
    {'hotel_id': 2, 'services': hotel_2_services},
    {'hotel_id': 3, 'services': hotel_3_services},
    {'hotel_id': 4, 'services': hotel_4_services}
]

# Открываем файл для записи
with open('services.csv', 'w', newline='') as file:
    # Создаем объект writer для записи данных в CSV файл
    writer = csv.writer(file)
    
    # Записываем заголовки столбцов
    writer.writerow(['service_id', 'hotel_id', 'category', 'name', 'price', 'discount', 'description'])
    
    # Идентификатор услуги
    service_id = 1
    
    # Записываем данные по каждому отелю
    for hotel in hotels:
        for service in hotel['services']:
            # Записываем данные в CSV файл
            writer.writerow([service_id, hotel['hotel_id'], service['category'], service['name'], service['price'], service['discount'], service['description']])
            
            # Увеличиваем идентификатор услуги на 1
            service_id += 1
