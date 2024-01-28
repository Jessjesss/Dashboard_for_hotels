create schema hotels;

-- Создание таблицы sales_fact
CREATE TABLE IF NOT EXISTS hotels.sales_fact (
    fact_id INTEGER PRIMARY KEY,
    guest_id INTEGER,
    service_id INTEGER,
    room_id INTEGER,
    hotel_id INTEGER,
    booking_id INTEGER,
    channel_id INTEGER,
    sales_date DATE,
    sales NUMERIC(12, 4)
);

-- Создание таблицы guests_dim
CREATE TABLE IF NOT EXISTS hotels.guests_dim (
    guest_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    surname VARCHAR(50),
    gender VARCHAR(10),
    dob INTEGER,
    age INTEGER,
    phone INTEGER,
    email VARCHAR(30),
    country VARCHAR(40),
    region VARCHAR(40),
    city VARCHAR(40),
    street VARCHAR(40),
    category VARCHAR(30),
    total_nights INTEGER
);

-- Создание таблицы rooms_dim
CREATE TABLE IF NOT EXISTS hotels.rooms_dim (
    room_id INTEGER PRIMARY KEY,
    hotel_id INTEGER,
    room_type VARCHAR(20),
    number INTEGER,
    floor INTEGER,
    price NUMERIC(10, 4),
    view VARCHAR(20),
    description VARCHAR(50)
);

-- Создание таблицы hotels_dim
CREATE TABLE IF NOT EXISTS hotels.hotels_dim (
    hotel_id INTEGER PRIMARY KEY,
    name VARCHAR(30),
    address VARCHAR(50),
    phone_number INTEGER,
    count_rooms INTEGER,
    description VARCHAR(50)
);

-- Создание таблицы booking_channel_dim
CREATE TABLE IF NOT EXISTS hotels.booking_channel_dim (
    channel_id INTEGER PRIMARY KEY,
    channel_name VARCHAR(30),
    description VARCHAR(50)
);

-- Создание таблицы services_dim
CREATE TABLE IF NOT EXISTS hotels.services_dim (
    service_id INTEGER PRIMARY KEY,
    hotel_id INTEGER,
    category VARCHAR(20),
    name VARCHAR(20),
    price NUMERIC(12, 4),
    discount NUMERIC(4, 2),
    description VARCHAR(50)
);

-- Создание таблицы booking_dim
CREATE TABLE IF NOT EXISTS hotels.booking_dim (
    booking_id INTEGER PRIMARY KEY,
    hotel_id INTEGER,
    room_id INTEGER,
    guest_id INTEGER,
    channel_id INTEGER,
    arrival_date DATE,
    departure_date DATE,
    prepayment NUMERIC(10, 2),
    total_price NUMERIC(10, 4),
    description VARCHAR(50)
);

-- Создание таблицы employees_dim
CREATE TABLE IF NOT EXISTS hotels.employees_dim (
    employee_id INTEGER PRIMARY KEY,
    hotel_id INTEGER,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(30),
    position VARCHAR(30),
    phone INTEGER,
    email VARCHAR(30),
    salary NUMERIC(10, 0)
);