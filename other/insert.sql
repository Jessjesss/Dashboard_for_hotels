insert into hotels.sales_fact 
select
	 *
from hotels.sales_fact






-- booking_id,hotel_id,room_id,guest_id,channel_id берутся с букингс и должны быть одинаковые
-- insert into hotels.sales_fact 
-- select
-- 	 100+row_number() over() as fact_id,
-- 	 guest_id,
-- 	 service_id,
-- 	 room_id,
-- 	 hotel_id,
-- 	 booking_id,
-- 	 channel_id,
-- 	 sales_date,
-- 	 sales
-- from hotels.bookings_dim as b
-- inner join booking_id on b.booking_id = booking_id