# Описание модели базы даных

DWH включает в себя 1 таблицу фактов (sales_fact) и 7 таблиц измерений:

- guests_dim
- rooms_dim
- hotels_dim
- booking_channel_dim
- services_dim
- booking_dim
- employees_dim

Таблица - sales_fact (хранит записи о событиях (фактах))


|      fact_id      |      integer         |      id продажи         |
|-------------------|----------------------|-----------------------------------------------|
|     guest_id      |     integer          |     id гостя            |
|     service_id    |     integer          |     id услуги           |
|     room_id       |     integer          |     id номера           |
|     hotel_id      |     integer          |     id отеля            |
|     booking_id    |     integer          |     id бронирования     |
|     channel_id    |     integer          |     id канала продаж    |
|     sales_date    |     timestamp             |     Дата и время продажи                              |
|     sales         |     numeric(12,4)    |     Сумма продаж                                   |

---
Таблица - guests_dim (содержит информацию о гостях).
|      guest_id       |      integer       |      id гостя            |
|---------------------|--------------------|------------------------------------------------|
|     first_name      |    varchar(50)    |     Имя гостя                                  |
|     last_name       |    varchar(50)    |     Фамилия гостя                              |
|     surname         |    varchar(50)    |     Отчество гостя                             |
|     gender          |    varchar(10)    |     Пол гостя                                  |
|     dob             |     integer        |     Дата рождения гостя                        |
|     age             |     integer        |     Возраст гостя                              |
|     phone           |     integer        |     Телефон гостя                              |
|     email           |    varchar(30)    |     Почта гостя ( может быть NULL)             |
|     country         |    varchar(40)    |     Страна проживания гостя                    |
|     region          |    varchar(40)    |     Регион/штат проживания гостя               |
|     city            |    varchar(40)    |     Город проживания гостя                     |
|     street          |    varchar(40)    |     Улица и номер дома, где проживает гость    |
|     category        |    varchar(30)    |     Категория гостя                            |
|     total_nights    |     integer        |     Количество прожитых суток в отеле          |

---
Таблица - rooms_dim (содержит информацию о номерах)

|      room_id       |      integer         |      id номера                   |
|--------------------|----------------------|--------------------------------------------------------|
|     hotel_id       |     integer          |     Идентификатор отеля, к которому относится номер    |
|     room_type      |    varchar(20)      |     Тип номера (SNL, DBL, TWN, JSUITE, SUITE)          |
|     number         |     integer          |     Номер комнаты                                      |
|     floor          |     integer          |     Номер этажа                                        |
|     price          |     numeric(10,4)    |     Цена за ночь                                       |
|     view           |    varchar(20)      |     Вид из окна                                        |
|     description    |    varchar(50)      |     Описание номера                                    |
---

Таблица - hotels_dim (содержит информацию об отелях).

|      hotel_id       |      integer       |      id отеля     |
|---------------------|--------------------|-----------------------------------------|
|     name            |    varchar(30)    |     Название отеля                      |
|     address         |    varchar(50)    |     Адрес отеля                         |
|     phone_number    |     integer        |     Номер телефона отеля                |
|     count_rooms     |     integer        |     Количество номеров                  |
|     description     |    varchar(50)    |     Описание отеля                      |
---
Таблица - booking_channel_dim (содержит информацию о каналах продаж).

|      channel_id     |      integer       |      id канала продаж     |
|---------------------|--------------------|-------------------------------------------------|
|     channel_name    |    varchar(30)    |     Название канала продаж                      |
|     description     |    varchar(50)    |     Описание канала продаж                      |
---

Таблица - services_dim (содержит информацию об услугах).

|      service_id     |      integer         |      id услуги               |
|---------------------|----------------------|----------------------------------------------------|
|     hotel_id        |     integer          |     Идентификатор отеля, где оказывается услуга    |
|     category        |    varchar(20)      |     Категория услуги                               |
|     name            |    varchar(20)      |     Название услуги                                |
|     price           |     numeric(12,4)    |     Стоимость услуги                               |
|     discount        |     numeric(4,2)     |     Скидка                                         |
|     description     |    varchar(50)      |     Описание услуги                                
---
Таблица - booking_dim (содержит информацию о бронированиях).
|      booking_id       |      integer         |      id бронирования                   |
|-----------------------|----------------------|--------------------------------------------------------------|
|     hotel_id          |     integer          |     Идентификатор отеля, в котором был произведен   заказ    |
|     room_id           |     integer          |     Идентификатор номера, на который сделан заказ            |
|     guest_id          |     integer          |     Имя гостя                                                |
|     channel_id        |     integer          |     Канал продаж                                             |
|     arrival_date      |     date             |     Дата заезда                                              |
|     departure_date    |     date             |     Дата выезда                                              |
|     prepayment        |     numeric(10,2)    |     Предоплата                                               |
|     total_price       |     numeric(10,4)    |     Общая стоимость бронирования                             |
|     description       |    varchar(50)      |     Описание                                                 |
---
Таблица - employees_dim(хранит данные о сотрудниках)
|      employee_id     |      integer         |      id сотрудника                              |
|----------------------|----------------------|-----------------------------------------------------------------------|
|     hotel_id         |     integer          |     id отеля, в котором   работает сотрудник    |
|     first_name       |    varchar(50)      |     Имя сотрудника                                                    |
|     last_name        |    varchar(50)      |     Фамилия сотрудника                                                |
|     department       |    varchar(30)      |     Название отдела, в котором работает сотрудник                     |
|     position         |    varchar(30)      |     Должность сотрудника                                              |
|     phone            |     integer          |     Номер телефона сотрудника                                         |
|     email            |    varchar(30)      |     Email сотрудника                                                  |
|     salary           |     numeric(10,0)    |     Заработная плата сотрудника                                       |
|