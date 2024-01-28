import random
import csv

gender = ['Female', 'Male']
random.choice(gender)

def hotel_id_(dep):
    hotel_id = [1, 2, 3, 4]
    if dep == 'Sales and Marketing Department':
        hotel_id = ''
        return hotel_id
    else:
        hotel_id = random.choice(hotel_id)
        return hotel_id


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

def generate_gender():
    gender = ["Female", "Male"]
    return random.choice(gender)


def generate_department():
    department_names = {
        'Room division': ['Housekeeping', 'Laundry', 'Maintenance', 'Room service'],
        'Front Office': ['Receptionist', 'Concierge', 'Reservationist', 'Bellhop'],
        'Sales and Marketing Department': ['Sales and booking manager', 'Marketing manager', 'Event coordinator'],
        'Technical Department': ['IT specialist', 'Security', 'Electrician', 'Plumber']
    }
    department = random.choice(list(department_names.keys()))
    position = random.choice(department_names[department])
    return department, position

def generate_phone():
    return random.randint(8911111111, 8962999999)

def generate_email(first_name, last_name):
    letters = first_name + last_name
    email = letters + '@mail.com'
    return email

def generate_salary():
    return random.randint(22000, 85000)

# Генерация данных и запись в CSV-файл
with open('employees.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['employee_id', 'hotel_id', 'first_name', 'last_name', 'department', 'position', 'phone', 'email', 'salary'])
    for i in range(1, 500):
        gender = generate_gender()
        first_name = generate_first_name(gender)
        last_name = generate_last_name(gender)
        email = generate_email(first_name, last_name)
        dep, pos = generate_department()
        h_id = hotel_id_(dep)
        writer.writerow([101+i, h_id, first_name, last_name, generate_phone(), email, dep, pos, generate_salary()])
