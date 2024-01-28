CREATE DATABASE IF NOT EXISTS HOTELS ENGINE = Atomic;

/*-----------------------------------------------*/
--- Create HOTELS.guests_dim table
/*-----------------------------------------------*/

CREATE TABLE IF NOT EXISTS HOTELS.guests_dim
(
    guest_id UInt64 NOT NULL,
    first_name String NOT NULL,
    last_name String NOT NULL,
    surname String NOT NULL,
    gender String NOT NULL,
    dob Date NOT NULL,
    age UInt8 NOT NULL,
    phone UInt64 NOT NULL,
    email String NULL,
    country String NOT NULL,
    region String NOT NULL,
    city String NOT NULL,
    street String NOT NULL,
    category String NOT NULL,
    total_nights UInt32 NOT NULL
) 
ENGINE = MergeTree()
PRIMARY KEY (guest_id)
ORDER BY guest_id;


/*-----------------------------------------------*/
--- Create HOTELS.rooms_dim table
/*-----------------------------------------------*/


CREATE TABLE HOTELS.rooms_dim
(
    room_id UInt64 NOT NULL,
    hotel_id UInt64 NOT NULL,
    room_type String NOT NULL,
    number UInt16 NOT NULL,
    floor UInt8 NOT NULL,
    price Decimal(9, 4) NOT NULL,
    view String NOT NULL,
    description String NULL
) 
ENGINE = MergeTree()
PRIMARY KEY (room_id)
ORDER BY room_id;

/*-----------------------------------------------*/
--- Create HOTELS.hotels_dim table
/*-----------------------------------------------*/

CREATE TABLE HOTELS.hotels_dim
(
    hotel_id UInt64 NOT NULL,
    name String NOT NULL,
    address String NOT NULL,
    phone_number UInt64 NOT NULL,
    count_rooms UInt32 NOT NULL,
    description String NULL
) ENGINE = MergeTree()
PRIMARY KEY (hotel_id)
ORDER BY hotel_id;

/*-----------------------------------------------*/
--- Create HOTELS.booking_channel_dim table
/*-----------------------------------------------*/

CREATE TABLE HOTELS.booking_channel_dim
(
    channel_id UInt64 NOT NULL,
    phone String NULL,
    email String NULL,
    vk String NULL,
    instagram String NULL,
    telegram String NULL,
    website_module String NULL,
    OTA String NULL,
    reception String NULL
) 
ENGINE = MergeTree()
PRIMARY KEY (channel_id)
ORDER BY channel_id;

/*-----------------------------------------------*/
--- Create HOTELS.services_dim table
/*-----------------------------------------------*/

CREATE TABLE HOTELS.services_dim
(
    service_id UInt64 NOT NULL,
    hotel_id UInt64 NOT NULL,
    category String NOT NULL,
    name String NOT NULL,
    price Decimal(9, 4) NOT NULL,
    discount Decimal(9, 4) NULL,
    description String NULL
) 
ENGINE = MergeTree()
PRIMARY KEY (service_id)
ORDER BY service_id;

/*-----------------------------------------------*/
--- Create HOTELS.booking_dim table
/*-----------------------------------------------*/

CREATE TABLE HOTELS.booking_dim
(
    booking_id UInt64 NOT NULL,
    hotel_id UInt64 NOT NULL,
    room_id UInt64 NOT NULL,
    guest_id UInt64 NOT NULL,
    channel_id UInt64 NOT NULL,
    arrival_date Date NOT NULL,
    departure_date Date NOT NULL,
    prepayment Decimal(9, 4) NOT NULL,
    total_price Decimal(9, 4) NOT NULL,
    description String NULL
) 
ENGINE = MergeTree()
PRIMARY KEY (booking_id)
ORDER BY booking_id;

/*-----------------------------------------------*/
--- Create HOTELS.employees_dim table
/*-----------------------------------------------*/

CREATE TABLE HOTELS.employees_dim
(
    employee_id UInt64 NOT NULL,
    hotel_id UInt64 NOT NULL,
    first_name String NOT NULL,
    last_name String NOT NULL,
    department String NULL,
    position String NOT NULL,
    phone UInt64 NOT NULL,
    email String NULL,
    salary Decimal(9, 4) NOT NULL
) 
ENGINE = MergeTree()
PRIMARY KEY (employee_id)
ORDER BY employee_id;

/*-----------------------------------------------*/
--- Create HOTELS.sales_fact table
/*-----------------------------------------------*/

CREATE TABLE HOTELS.sales_fact
(
    fact_id UInt64 NOT NULL,
    guest_id UInt64 NOT NULL,
    service_id UInt64 NOT NULL,
    room_id UInt64 NOT NULL,
    hotel_id UInt64 NOT NULL,
    booking_id UInt64 NOT NULL,
    channel_id UInt64 NOT NULL,
    date DateTime NOT NULL,
    sales Decimal(12, 4) NOT NULL
) ENGINE = MergeTree()
ORDER BY (fact_id);