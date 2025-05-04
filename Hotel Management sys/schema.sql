create database hotel_db;

use hotel_db;

-- creating  Guests Table 

create table if not exists Guests(
    guest_id int auto_increment primary key,
    guest_name varchar(255),    
    guest_email varchar(255),
    phone_no varchar(20),
    address varchar(255)

);

-- creating Rooms Table

create table if not exists Rooms(
    room_id int auto_increment primary key,
    room_type varchar(100),
    per_night_price decimal(10,2),
    availability boolean
);

-- creatnig booking table

create table if not exists Booking(
    booking_id int auto_increment primary key,
    guest_id int,
    room_id int,
    check_in date,
    check_out date,
    booking_date date,
    foreign key (guest_id) references Guests(guest_id),
    foreign key (room_id) references Rooms(room_id)   
);

-- creating  payment table 

create table if not exists Payments(
    payment_id int auto_increment primary key,
    booking_id int,
    payment_date date,
    amount decimal (10,2),
    payment_method varchar(50),
    foreign key (booking_id) references Booking(booking_id)
);

-- creating employee table

create table if not exists Employees(
    emp_id int auto_increment primary key,
    emp_name varchar(225),
    position varchar(100),
    salary decimal (10,2),
    contact_no varchar(20)
    );

-- creating services table

create table if not exists Services(
    service_id int auto_increment primary key,
    service_name varchar(100),
    service_cost decimal (10,2)
);

-- creating guest services 

create table if not exists Guest_Services(
    guest_id int,
    service_id int,
    service_date date,
    foreign key (guest_id) references Guests(guest_id),
    foreign key (service_id) references Services(service_id)
);

-- DML 

-- inserting data in guest table

insert into Guests(guest_name , guest_email, phone_no, address )
values 
    ("Sara Ali", "sara.ali@example.com", "03123456789", "Lahore"),
    ("Ahmed Raza", "ahmed.raza@example.com", "03219876543", "Islamabad"),
    ("Fatima Noor", "fatima.noor@example.com", "03337654321", "Peshawar"),
    ("Ali Ahmed", "ali.ahmed@example.com", "03456789012", "Karachi"),
    ("Maya Khan", "maya.khan@example.com", "03569874321", "Quetta");
    
-- inserting into rooms

insert into Rooms(room_type,per_night_price,availability)
values 
    ('Single', 5000, True),
    ('Double', 8000, True),
    ('Suite', 15000, False),
    ('Deluxe', 20000, True),
    ('Presidential Suite', 50000, False);
    
-- inserting into Booking 
insert into Booking(guest_id,room_id,check_in, check_out,booking_date)
values
    (1, 1,' 2025-05-01', '2025-05-05', '2025-04-20'),
    (2, 2, '2025-05-10', '2025-05-15', '2025-04-22'),
    (3, 3, '2025-05-03', '2025-05-07', '2025-04-21'),
    (4, 4, '2025-05-12', '2025-05-18', '2025-04-23'),
    (5, 5, '2025-05-20', '2025-05-25', '2025-04-24');
   
-- inserting into payment
insert into Payments(booking_id,payment_date, amount, payment_method)
values
    (6,'2025-05-01',5000,'Cash'),
    (7,'2025-05-10',7000,'Online'),
    (8,'2025-05-03',7500,'Cash'),
    (9,'2025-05-12',8000,'Cash'),
    (10,'2025-05-20',8500,'Cash');

-- inserting into Employees
    
insert into Employees(emp_name, position, salary,contact_no)
values
    ('Waqar', 'Receptionist', 30000, '030000000'),
    ('Noor', 'Manager',50000,'123456789'),
    ('John','Cleaner',10000,'012345678'),
    ('Elsa','Receptionist',30000,'030012345'),
    ('Ali','Security Guard',20000,'920000000');
  
-- insserting intoo services
insert into Services(service_name,service_cost)
values
    ('Spa',5000),
    ('Laundry',1000),
    ('Room Cleaning',1000),
    ('Spa',5000),
    ('Airport Pickup',3500);


-- inserting into guests services 
insert into Guest_Services(guest_id, service_id,service_date)
values
    (1,1,'2025-05-05'),
    (2,2,'2025-05-12'),
    (3,3,'2025-05-18'),
    (4,4,'2025-05-07'),
    (5,5,'2025-05-20');


-- create view  for checking guest details 

create view  GuestBookingDetails as 
select 
	g.guest_name,
    g.guest_email,
    b.booking_id,
    b.check_in,
    b.check_out,
    b.booking_date,
	r.room_id
from Guests g
join Booking b on g.guest_id = b.guest_id
join Rooms r on b.room_id = r.room_id;

-- view for checking paymenthistory 

create view PaymentHistory as
select
    p.payment_id,
    g.guest_name,
    b.booking_id,
    p.amount,
    p.payment_method,
    p.payment_date
from Payments p
join Booking b on p.booking_id = b.booking_id
join Guests g on b.guest_id = g.guest_id;

-- view for checking used services
create view UsedService as 
select 
	g.guest_name,
    s.service_name,
    s.service_cost,
    gs.service_date
from Guest_Services gs
join Guests g on gs.guest_id = g.guest_id
join Services s on gs.service_id = s.service_id;

 
select * from GuestBookingDetails;
select * from PaymentHistory;
select * from UsedService;

-- creating stroed procedures

 -- procedures for adding guests 
delimiter $$
create procedure AddGuests(
	in g_name varchar(255),
    in g_email varchar(255),
    in g_phone varchar(20),
    in g_address varchar(255))
begin 
	insert into Guests(guest_name , guest_email, phone_no, address)
    values (g_name, g_eamil, g_phone, g_address);
end $$
delimiter $$

-- procedures for adding payments

delimiter $$
create procedure AddPayment(
	in p_booing_id int,
    in p_date date,
    in p_amount decimal(10,2),
    in p_method varchar(50)
)
begin 
	insert into Payments(booking_id,payment_date, amount, payment_method)
    values (p_booking_id, p_date, p_amount, p_method);
end $$
delimiter ;


call AddGuests('Usman Tariq', 'usman@example.com', '03111222333', 'Multan');
call AddPayment(1, '2025-05-05', 5000, 'Online');

