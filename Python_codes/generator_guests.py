import random
import csv
from datetime import date, timedelta

gender = ['Female', 'Male']
random.choice(gender)

def generate_first_name(gender):
    male_first_names = ['Pavel', 'Sergey', 'Artem', 'Denis', 'Ivan', 'Dmitry', 'Maxim', 'Alexey', 'Andrey', 'Roman', 'Alexander', 'Mikhail', 'Vladimir', 'Nikita', 'Kirill', 'Egor', 'Timofey', 'Evgeny', 'Vasily', 'Ilya', 'Gleb', 'Daniil', 'David', 'Victor', 'Fyodor', 'Arseny']
    female_first_names = ['Alina', 'Olga', 'Anna', 'Ekaterina', 'Natalya', 'Victoria', 'Kseniya', 'Tatiana', 'Lyudmila', 'Anastasia', 'Elena', 'Darya', 'Maria', 'Alexandra', 'Elizaveta', 'Milana', 'Sofia', 'Valeria', 'Arina', 'Kristina', 'Yulia', 'Karina', 'Polina', 'Nadezhda']
    if gender == 'Male':
        return random.choice(male_first_names)
    else:
        return random.choice(female_first_names)

def generate_last_name(gender):
    if gender == 'Female':
        female_last_names = ['Ivanova', 'Petrova', 'Sidorova', 'Smirnova', 'Kuznetsova', 'Vasilieva', 'Popova', 'Sokolova', 'Mikhailova', 'Fedorova', 'Morozova', 'Volkova', 'Alekseeva', 'Lebedeva', 'Kozlova', 'Novikova', 'Yegorova', 'Pavlova', 'Nikitina']
        return random.choice(female_last_names)
    else:
        male_last_names = ['Ivanov', 'Petrov', 'Sidorov', 'Smirnov', 'Kuznetsov', 'Vasiliev', 'Popov', 'Sokolov', 'Mikhailov', 'Fedorov', 'Morozov', 'Volkov', 'Alekseev', 'Lebedev', 'Kozlov', 'Novikov', 'Yegorov', 'Pavlov', 'Nikitin']
        return random.choice(male_last_names)

def generate_surname(gender):
    if gender == 'Female':
        female_surnames = ['Aleksandrovna', 'Dmitrievna', 'Igorevna', 'Alekseevna', 'Dmitrievna', 'Igorevna', 'Petrovna', 'Sergeevna', 'Andreevna']
        return random.choice(female_surnames)
    else:
        male_surnames = ['Aleksandrovich', 'Dmitrievich', 'Igorevich', 'Alekseevich', 'Dmitrievich', 'Igorevich', 'Petrovich', 'Sergeevich', 'Andreevich']
        return random.choice(male_surnames)

def generate_gender():
    gender = ["Female", "Male"]
    return random.choice(gender)

def generate_dob():
    start_date = date(1935, 1, 1)
    end_date = date(2023, 2, 1)
    days = (end_date - start_date).days
    random_days = random.randint(0, days)
    birthday = start_date + timedelta(days=random_days)
    return birthday

def generate_age(birthday):
    today = date.today()
    age = today.year - birthday.year
    return age

def generate_phone():
    return random.randint(8911111111, 8962999999)

def generate_email(first_name, last_name):
    letters = first_name + last_name
    email = letters + '@mail.com'
    return email


def generate_country():
    countries = ['Rossiya', 'Kazakhstan', 'Kitay', 'Rossiya', 'Rossiya', 'Germaniya', 'Rossiya', 'Rossiya', 'Rossiya', 'Rossiya']
    return random.choice(countries)


def generate_region(countries):
    if countries == 'Rossiya':
        regions = ['Kemerovskaya oblast']*10 + ['Novosibirskaya oblast']*15 + ['Moskovskaya oblast']*30 + ['Krasnoyarskiy kray']*10 + ['Tyumenskaya oblast']*10 + ['Omskaya oblast']*5 + ['Krasnodarskiy kray']*10 + ['Sverdlovskaya oblast']*5 + ['Altayskiy kray']*5
        return random.choice(regions)
    else:
        return 'Unknow'
    
def generate_city(region):
    if region == 'Kemerovskaya oblast':
        cities = ['Kemerovo', 'Novokuznetsk', 'Prokopievsk', 'Kiselevsk', 'Leninsk-Kuznetskiy', 'Mezhdurechensk', 'Topki']
    elif region == 'Novosibirskaya oblast':
        cities = ['Novosibirsk', 'Berdsk', 'Iskitim', 'Kuybyshev', 'Ob']
    elif region == 'Moskovskaya oblast':
        cities = ['Moskva', 'Krasnogorsk', 'Khimki', 'Lyubertsy', 'Mytishchi', 'Odintsovo']
    elif region == 'Krasnoyarskiy kray':
        cities = ['Krasnoyarsk', 'Norilsk', 'Kansk', 'Achinsk', 'Kodinsk']
    elif region == 'Tyumenskaya oblast':
        cities = ['Tyumen', 'Tobolsk', 'Ishim', 'Yalutorovsk', 'Zavodoukovsk']
    elif region == 'Omskaya oblast':
        cities = ['Omsk', 'Tara', 'Nazivayevsk', 'Kalachinsk', 'Murmanskovo']
    elif region == 'Krasnodarskiy kray':
        cities = ['Krasnodar', 'Sochi', 'Novorossiysk', 'Anapa', 'Gelendzhik']
    elif region == 'Sverdlovskaya oblast':
        cities = ['Ekaterinburg', 'Kamensk-Uralskiy', 'Nizhniy Tagil', 'Pervouralsk', 'Revda']
    elif region == 'Altayskiy kray':
        cities = ['Barnaul', 'Biysk', 'Zarinsk', 'Rubtsovsk', 'Yarovoye']
    else:
        cities = ['Unknown']
    return random.choice(cities)

def generate_street():
    if countries == 'Rossiya':
        streets = ['ul. Lenina', 'ul. Pushkina', 'ul. Gagarina', 'ul. Mira', 'ul. Sadovaya', 'ul. Zelenaya', 'ul. Kirova', 'ul. Krasnaya', 'ul. Zheleznodorozhnaya', 'ul. Sovetskaya']
        return random.choice(streets) + ' ' + str(random.randint(1, 100))
    else:
        return 'Unknow'

def generate_category():
    categories = ''
    return categories

def generate_total_nights():
    return random.randint(1, 30)


# Генерация данных и запись в CSV-файл
with open('guests.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['guest_id', 'first_name', 'last_name', 'surname', 'gender', 'dob', 'age', 'phone', 'email', 'country', 'region', 'city', 'street', 'category', 'total_nights'])
    for i in range(1, 150100):
        gender = generate_gender()
        first_name = generate_first_name(gender)
        last_name = generate_last_name(gender)
        birthday = generate_dob()
        countries = generate_country()
        region = generate_region(countries)
        email = generate_email(first_name, last_name)
        writer.writerow([101+i, first_name, last_name, generate_surname(gender), gender, birthday, generate_age(birthday), generate_phone(), email, countries, region, generate_city(region), generate_street(), generate_category(), generate_total_nights()])
