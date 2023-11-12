INSERT INTO dsr_customer (customer_type, first_name, last_name, email, phone, address_street, address_city, address_state, address_zipcode)
VALUES
('I', 'John', 'Doe', 'john.doe@example.com', '555-1234', '123 Main St', 'Anytown', 'CA', '12345'),
('I', 'Alice', 'Smith', 'alice.smith@example.com', '555-9876', '789 Oak St', 'Nowhere', 'TX', '98765'),
('I', 'Eva', 'Miller', 'eva.miller@example.com', '555-1357', '987 Maple St', 'Nowhere', 'TX', '75309'),
('I', 'Charlie', 'Brown', 'charlie.brown@example.com', '555-5678', '741 Birch St', 'Anytown', 'CA', '95124'),
('I', 'Grace', 'Taylor', 'grace.taylor@example.com', '555-9876', '963 Oak St', 'Nowhere', 'TX', '15973'),
('I', 'David', 'Jones', 'david.jones@example.com', '555-8642', '147 Walnut St', 'Anytown', 'CA', '25836'),
('I', 'Sophie', 'White', 'sophie.white@example.com', '555-8790', '582 Cedar St', 'Nowhere', 'TX', '47102'),
('I', 'Michael', 'Clark', 'michael.clark@example.com', '555-4321', '916 Pine St', 'Anytown', 'CA', '79358'),
('I', 'Emma', 'Johnson', 'emma.johnson@example.com', '555-2468', '361 Elm St', 'Nowhere', 'TX', '11543'),
('I', 'Bob', 'Johnson', 'bob.johnson@example.com', '555-2468', '321 Elm St', 'Anytown', 'CA', '13579'),
('I', 'Andrew', 'Taylor', 'andrew.taylor@example.com', '555-1357', '605 Maple St', 'Anytown', 'CA', '33756'),
('C', 'XYZ Corp', 'Ltd.', 'contact@xyzcorp.com', '555-4321', '101 Pine St', 'Everytown', 'FL', '43210'),
('C', 'ABC Company', 'Inc.', 'info@abccompany.com', '555-5678', '456 Market St', 'Somewhereville', 'NY', '56789'),
('C', 'EFG Enterprises', 'LLC', 'info@efgenterprises.com', '555-8642', '654 Walnut St', 'Somewhereville', 'NY', '24680'),
('C', 'LMN Co.', 'Corp.', 'contact@lmnco.com', '555-8790', '369 Cedar St', 'Everytown', 'FL', '80246'),
('C', 'PQR Ltd.', 'Company', 'info@pqrcompany.com', '555-4321', '852 Pine St', 'Somewhereville', 'NY', '35791'),
('C', 'UVW Corporation', 'Inc.', 'contact@uvwcorp.com', '555-2468', '753 Elm St', 'Everytown', 'FL', '46802'),
('C', 'RST Enterprises', 'LLC', 'info@rstenterprises.com', '555-1357', '369 Maple St', 'Somewhereville', 'NY', '36985'),
('C', 'JKL Co.', 'Corp.', 'contact@jklco.com', '555-5678', '794 Birch St', 'Everytown', 'FL', '68294'),
('C', 'GHI Ltd.', 'Company', 'info@ghiltd.com', '555-9876', '239 Oak St', 'Somewhereville', 'NY', '90417'),
('C', 'NOP Corporation', 'Inc.', 'contact@nopcorp.com', '555-8642', '484 Walnut St', 'Everytown', 'FL', '22689'),
('C', 'QRS Enterprises', 'LLC', 'info@qrsenterprises.com', '555-8790', '726 Cedar St', 'Somewhereville', 'NY', '44892');

-- Sample data for corporation table
INSERT INTO dsr_corporation (corp_name, reg_no)
VALUES
('Tech Innovations Inc.', 'Tech123456'),
('Global Logistics Co.', 'Logistics7890'),
('Finance Solutions Ltd.', 'FinanceABCDE'),
('HealthCare Providers LLC', 'HealthCare123'),
('Energy Dynamics Corp.', 'EnergyXYZ789'),
('Tech Innovations Inc. 2', 'Tech123457'),
('Global Logistics Co. 2', 'Logistics7891'),
('Finance Solutions Ltd. 2', 'FinanceABCDF'),
('HealthCare Providers LLC 2', 'HealthCare124'),
('Energy Dynamics Corp. 2', 'EnergyXYZ790'),
('Tech Innovations Inc. 3', 'Tech123458'),
('Global Logistics Co. 3', 'Logistics7892'),
('Finance Solutions Ltd. 3', 'FinanceABCDG'),
('HealthCare Providers LLC 3', 'HealthCare125'),
('Energy Dynamics Corp. 3', 'EnergyXYZ791'),
('Energy Dynamics Corp. 5', 'EnergyXYZ793');

-- Sample data for cust_corporate table
INSERT INTO dsr_cust_corporate (customer_id, emp_id, corp_id)
VALUES
(12, 'EMP002', 1),
(13, 'EMP004', 1),
(14, 'EMP006', 1),
(15, 'EMP008', 2),
(16, 'EMP010', 2),
(17, 'EMP012', 2),
(18, 'EMP014', 3),
(19, 'EMP016', 3),
(20, 'EMP018', 3),
(21, 'EMP020', 4),
(22, 'EMP022', 5);


-- Sample data for cust_individual table
INSERT INTO dsr_cust_individual (customer_id, dl_no, insurance_company, insurance_policy_no)
VALUES
(1, 'DL123456', 'ABC Insurance', 'POLICY123'),
(2, 'DL789012', 'XYZ Insurance', 'POLICY456'),
(3, 'DL345678', '123 Insurance', 'POLICY789'),
(4, 'DL901234', '456 Insurance', 'POLICYABC'),
(5, 'DL567890', '789 Insurance', 'POLICYDEF'),
(6, 'DL111111', 'AAA Insurance', 'POLICY111'),
(7, 'DL333333', 'CCC Insurance', 'POLICY333'),
(8, 'DL555555', 'EEE Insurance', 'POLICY555'),
(9, 'DL777777', 'GGG Insurance', 'POLICY777'),
(10, 'DL999999', 'III Insurance', 'POLICY999'),
(11, 'DL112233', 'KKK Insurance', 'POLICY112');


-- Sample data for vehicle_class table
INSERT INTO dsr_vehicle_class (class, rent_charge, extra_charge)
VALUES
('Sedan', 50.00, 5.00),
('SUV', 70.00, 7.00),
('Truck', 80.00, 8.00),
('Compact Car', 45.00, 4.50),
('Luxury Car', 100.00, 10.00),
('Convertible', 85.00, 8.50),
('Sports Car', 120.00, 12.00),
('Minivan', 65.00, 6.50),
('Electric Car', 75.00, 7.50),
('Hybrid', 70.00, 7.00);


-- Sample data for office_location table
INSERT INTO dsr_office_location (address_street, address_city, address_state, address_zipcode, phone)
VALUES
('123 Main St', 'Cityville', 'StateA', '12345', '555-111-1111'),
('456 Oak Ave', 'Townburg', 'StateB', '56789', '555-222-2222'),
('789 Pine Rd', 'Villagetown', 'StateC', '10111', '555-333-3333'),
('321 Maple Blvd', 'Cityopolis', 'StateD', '31415', '555-444-4444'),
('654 Birch Lane', 'Townsville', 'StateE', '92638', '555-555-5555'),
('987 Cedar St', 'Hamletville', 'StateF', '13579', '555-666-6666'),
('159 Redwood Ave', 'Ruraltown', 'StateG', '24680', '555-777-7777'),
('753 Elm Rd', 'Suburbia', 'StateH', '97531', '555-888-8888'),
('246 Walnut Blvd', 'Metropolis', 'StateI', '86420', '555-999-9999'),
('802 Pine Lane', 'Cityscape', 'StateJ', '75309', '555-000-0000'),
('364 Cedar St', 'Villageville', 'StateK', '46802', '555-112-2334'),
('951 Birch Ave', 'Hamletburg', 'StateL', '98765', '555-443-3221'),
('573 Maple Rd', 'Townsville', 'StateM', '11223', '555-554-4332'),
('210 Oak Blvd', 'Suburbopolis', 'StateN', '33445', '555-665-5443'),
('846 Pine Lane', 'Cityburg', 'StateO', '55667', '555-776-6554'),
('479 Elm Rd', 'Villagescape', 'StateP', '77889', '555-887-5665'),
('632 Redwood Ave', 'Metrotown', 'StateQ', '99000', '555-998-4776'),
('268 Walnut St', 'Ruralburg', 'StateR', '11222', '555-009-3887'),
('713 Cedar Ave', 'Cityville', 'StateS', '33444', '555-210-2998'),
('345 Oak Rd', 'Townburg', 'StateT', '55666', '555-321-1009'),
('908 Pine Blvd', 'Villagetown', 'StateU', '77888', '555-432-2110'),
('531 Maple Lane', 'Cityopolis', 'StateV', '99000', '555-543-3221'),
('174 Birch St', 'Townsville', 'StateW', '11222', '555-654-4332'),
('789 Redwood Ave', 'Villagescape', 'StateX', '33445', '555-765-5443');


-- Sample data for vehicle table
INSERT INTO dsr_vehicle (location_id, class_id, make, model, make_year, vin_no, liscense_plate_no)
VALUES
(1, 1, 'Toyota', 'Camry', '2022-01-01', 'VIN123456', 'ABC123'),
(2, 2, 'Honda', 'CRV', '2022-01-01', 'VIN789012', 'XYZ456'),
(3, 3, 'Ford', 'F-150', '2022-01-01', 'VIN345678', '123DEF'),
(4, 4, 'Chevrolet', 'Malibu', '2022-01-01', 'VIN901234', '456GHI'),
(5, 5, 'Tesla', 'Model 3', '2022-01-01', 'VIN567890', '789JKL'),
(6, 1, 'Nissan', 'Altima', '2022-01-01', 'VIN012345', 'MNO987'),
(7, 2, 'Subaru', 'Outback', '2022-01-01', 'VIN678901', 'PQR654'),
(8, 3, 'Jeep', 'Wrangler', '2022-01-01', 'VIN234567', 'STU321'),
(9, 4, 'Hyundai', 'Sonata', '2022-01-01', 'VIN890123', 'VWX987'),
(10, 5, 'BMW', 'X5', '2022-01-01', 'VIN456789', 'YZA123'),
(11, 1, 'Mercedes-Benz', 'C-Class', '2022-01-01', 'VIN012345', 'BCD456'),
(12, 2, 'Audi', 'Q5', '2022-01-01', 'VIN678901', 'EFG789'),
(13, 3, 'Kia', 'Sorento', '2022-01-01', 'VIN234567', 'HIJ012'),
(14, 4, 'Mazda', 'CX-5', '2022-01-01', 'VIN890123', 'KLM345'),
(15, 5, 'Volvo', 'XC90', '2022-01-01', 'VIN456789', 'NOP678'),
(16, 1, 'Jaguar', 'F-Pace', '2022-01-01', 'VIN012345', 'QRS901'),
(17, 2, 'Lexus', 'RX', '2022-01-01', 'VIN678901', 'TUV234'),
(18, 3, 'Porsche', 'Cayenne', '2022-01-01', 'VIN234567', 'WXY567'),
(19, 4, 'Land Rover', 'Discovery', '2022-01-01', 'VIN890123', 'ZAB890'),
(20, 5, 'Buick', 'Enclave', '2022-01-01', 'VIN456789', 'CDE123'),
(21, 1, 'GMC', 'Terrain', '2022-01-01', 'VIN012345', 'FGH456'),
(22, 2, 'Cadillac', 'XT5', '2022-01-01', 'VIN678901', 'IJK789'),
(23, 3, 'Lincoln', 'Navigator', '2022-01-01', 'VIN234567', 'LMN012');


-- Sample data for coupon table
INSERT INTO dsr_coupon (coupon_type, discount)
VALUES
('I', 10.05),
('I', 10.1),
('I', 10.05),
('I', 10.1),
('I', 20.05),
('I', 20.1),
('I', 20.05),
('I', 20.1),
('I', 20.05),
('I', 20.1),
('C', 20.1),
('C', 99.99),
('C', 30.2),
('C', 30.1),
('C', 30.15),
('C', 30.2),
('C', 40.1),
('C', 40.15),
('C', 40.2),
('C', 40.1),
('C', 40.15),
('C', 40.2),
('C', 40.1),
('C', 50.15),
('C', 70.2);
-- Sample data for coupon_corp table
INSERT INTO dsr_coupon_corp (coupon_id, corp_id)
VALUES
(11, 1),
(12, 2),
(13, 3),
(14, 4),
(15, 5),
(16, 6),
(17, 7),
(18, 8),
(19, 9),
(20, 10);

-- Sample data for coupon_indiv table
INSERT INTO dsr_coupon_indiv (coupon_id, valid_from, valid_to)
VALUES
(1, '2023-01-01', '2023-12-31'),
(2, '2023-01-01', '2023-12-31'),
(3, '2023-01-02', '2023-12-01'),
(4, '2023-01-02', '2023-12-01'),
(5, '2023-01-03', '2023-12-02'),
(6, '2023-01-03', '2023-12-02'),
(7, '2023-01-04', '2023-12-03'),
(8, '2023-01-04', '2023-12-03'),
(9, '2023-01-05', '2023-12-04'),
(10, '2023-01-05', '2023-12-04');


-- Sample data for rental_service table
INSERT INTO dsr_rental_service (
    pickup_date, dropoff_date, start_odo, end_odo, daily_limit, service_status, pickup_location_id, dropoff_location_id, customer_id, vehicle_id, coupon_id
)
VALUES
('2023-06-01', NULL, 13000.00, NULL, 65.00, 'P', 2, 3, 6, 6, 6),
('2023-04-01', NULL, 17000.00, NULL, 75.00, 'P', 3, 4, 7, 7, 7),
('2023-08-01', NULL, 14000.00, NULL, 62.00, 'P', 4, 5, 8, 8, 8),
('2023-09-01', NULL, 22000.00, NULL, 85.00, 'P', 5, 1, 9, 9, 9),
('2023-10-01', NULL, 20000.00, NULL, 70.00, 'P', 1, 2, 10, 10, 10),
('2023-12-01', '2023-12-05', 15000.00, 15540.00, 63.00, 'C', 3, 4, 12, 12, 12),
('2024-01-01', '2024-01-15', 23000.00, 23960.00, 88.00, 'C', 4, 5, 13, 13, 13),
('2024-02-01', '2024-02-08', 21000.00, 21620.00, 73.00, 'C', 5, 1, 14, 14, 14),
('2024-03-01', NULL, 19000.00, NULL, 68.00, 'P', 1, 2, 15, 15, 15),
('2024-04-01', '2024-04-09', 16000.00, 16640.00, 64.00, 'C', 2, 3, 16, 16, NULL),
('2024-05-01', '2024-05-15', 24000.00, 25020.00, 90.00, 'C', 3, 4, 17, 17, 17),
('2024-06-01', '2024-06-18', 22000.00, 22900.00, 75.00, 'C', 4, 5, 18, 18, NULL),
('2024-07-01', NULL, 20000.00, NULL, 70.00, 'P', 5, 1, 19, 19, 19),
('2024-08-01', NULL, 17000.00, NULL, 65.00, 'P', 1, 2, 20, 20, 20),
('2024-09-01', '2024-09-15', 25000.00, 26040.00, 95.00, 'C', 2, 3, 21, 21, 21),
('2024-10-01', '2024-10-08', 23000.00, 23640.00, 80.00, 'C', 3, 4, 22, 22, 22);


-- Sample data for payment table
INSERT INTO dsr_payment (pay_method, card_no, pay_date, customer_id)
VALUES
('DEBIT', '1234-5678-9012-3456', '2023-01-15', 1),
('DEBIT', '9876-5432-1098-7654','2023-03-15', 2),
('GIFT', '1222444','2023-04-15', 2),
('DEBIT', '1111-2222-3333-4444','2023-05-15', 2),
('DEBIT', '5555-6666-7777-8888','2023-06-15', 3),
('DEBIT', '9999-0000-1111-2222','2023-07-15', 4),
('GIFT', '33335555','2023-08-15', 5),
('DEBIT', '4444-5555-6666-7777','2023-09-15', 6),
('DEBIT', '7777-8888-9999-0000', '2023-10-15', 7),
('GIFT', '88882222', '2023-11-15', 7),
('CREDIT', '1234-5678-9012-3456','2023-12-15', 8),
('CREDIT', '9876-5432-1098-7654', '2024-01-15', 9),
('GIFT', '1222444','2024-02-15', 10),
('CREDIT', '1111-2222-3333-4444', '2024-03-15', 11),
('CREDIT', '5555-6666-7777-8888', '2024-04-15', 12),
('CREDIT', '9999-0000-1111-2222','2024-05-15', 13),
('GIFT', '33335555', '2024-06-15', 14),
('CREDIT', '4444-5555-6666-7777','2024-07-15', 15),
('CREDIT', '7777-8888-9999-0000', '2024-08-15', 16),
('GIFT', '88882222','2024-09-15', 17),
('DEBIT', '1234-5678-9012-3456','2024-10-15', 18),
('CREDIT', '9876-5432-1098-7654', '2024-11-15', 19),
('GIFT', '1222444', '2024-12-15', 20),
('DEBIT', '1111-2222-3333-4444', '2025-01-15', 20);
