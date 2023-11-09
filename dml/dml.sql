-- Sample data for customer table
INSERT INTO customer (customer_type, first_name, last_name, email, phone)
VALUES
('C', 'John', 'Doe', 'john.doe@company.com', '555-111-1111'),
('C', 'Alice', 'Smith', 'alice.smith@company.com', '555-222-2222'),
('C', 'Bob', 'Johnson', 'bob.johnson@company.com', '555-333-3333'),
('C', 'Emily', 'Davis', 'emily.davis@company.com', '555-444-4444'),
('C', 'Daniel', 'Clark', 'daniel.clark@company.com', '555-555-5555');

-- Sample data for address table
INSERT INTO address (address_street, address_city, address_state, address_zipcode, customer_id)
VALUES
('123 Main St', 'Cityville', 'StateA', '12345', 1),
('456 Oak Ave', 'Townburg', 'StateB', '56789', 2),
('789 Pine Rd', 'Villagetown', 'StateC', '10111', 3),
('321 Maple Blvd', 'Cityopolis', 'StateD', '31415', 4),
('654 Birch Lane', 'Townsville', 'StateE', '92638', 5);

-- Sample data for corporation table
INSERT INTO corporation (corp_name, reg_no)
VALUES
('Tech Innovations Inc.', 'Tech123456'),
('Global Logistics Co.', 'Logistics7890'),
('Finance Solutions Ltd.', 'FinanceABCDE'),
('HealthCare Providers LLC', 'HealthCare123'),
('Energy Dynamics Corp.', 'EnergyXYZ789');


-- Sample data for cust_corporate table
INSERT INTO cust_corporate (emp_id, corp_id)
VALUES
('EMP001', 1),
('EMP002', 2),
('EMP003', 3),
('EMP004', 4),
('EMP005', 5);

-- Sample data for cust_individual table
INSERT INTO cust_individual (dl_no, insurance_company, insurance_policy_no)
VALUES
('DL123456', 'ABC Insurance', 'POLICY123'),
('DL789012', 'XYZ Insurance', 'POLICY456'),
('DL345678', '123 Insurance', 'POLICY789'),
('DL901234', '456 Insurance', 'POLICYABC'),
('DL567890', '789 Insurance', 'POLICYDEF');

-- Sample data for vehicle_class table
INSERT INTO vehicle_class (class, rent_charge, extra_charge)
VALUES
('Sedan', 50.00, 5.00),
('SUV', 70.00, 7.00),
('Truck', 80.00, 8.00),
('Compact Car', 45.00, 4.50),
('Luxury Car', 100.00, 10.00);

-- Sample data for office_location table
INSERT INTO office_location (address_street, address_city, address_state, address_zipcode, phone)
VALUES
('123 Main St', 'Cityville', 'StateA', '12345', '555-111-1111'),
('456 Oak Ave', 'Townburg', 'StateB', '56789', '555-222-2222'),
('789 Pine Rd', 'Villagetown', 'StateC', '10111', '555-333-3333'),
('321 Maple Blvd', 'Cityopolis', 'StateD', '31415', '555-444-4444'),
('654 Birch Lane', 'Townsville', 'StateE', '92638', '555-555-5555');

-- Sample data for vehicle table
INSERT INTO vehicle (location_id, class_id, make, model, make_year, vin_no, liscense_plate_no)
VALUES
(1, 1, 'Toyota', 'Camry', '2022-01-01', 'VIN123456', 'ABC123'),
(2, 2, 'Honda', 'CRV', '2022-01-01', 'VIN789012', 'XYZ456'),
(3, 3, 'Ford', 'F-150', '2022-01-01', 'VIN345678', '123DEF'),
(4, 4, 'Chevrolet', 'Malibu', '2022-01-01', 'VIN901234', '456GHI'),
(5, 5, 'Tesla', 'Model 3', '2022-01-01', 'VIN567890', '789JKL');


-- Sample data for coupon table
INSERT INTO coupon (coupon_type, discount)
VALUES
('C', 0.1),
('I', 0.05),
('C', 0.15),
('I', 0.1),
('C', 0.2);

-- Sample data for coupon_corp table
INSERT INTO coupon_corp (corp_id)
VALUES
(1),
(2),
(3),
(4),
(5);

-- Sample data for coupon_indiv table
INSERT INTO coupon_indiv (valid_from, valid_to)
VALUES
('2023-01-01', '2023-03-31'),
('2023-04-01', '2023-06-30'),
('2023-07-01', '2023-09-30'),
('2023-10-01', '2023-12-31'),
('2024-01-01', '2024-03-31');

-- Sample data for rental_service table
INSERT INTO rental_service (pickup_date, dropoff_date, start_odo, end_odo, daily_limit, service_status, pickup_location_id, dropoff_location_id, customer_id, vehicle_id, coupon_id)
VALUES
('2023-01-01', '2023-01-05', 100.00, 200.00, 50.00, 'Completed', 1, 2, 1, 1, 1),
('2023-02-01', '2023-02-07', 150.00, 300.00, 70.00, 'Completed', 2, 3, 2, 2, 2),
('2023-03-01', '2023-03-10', 120.00, 250.00, 60.00, 'InProgress', 3, 4, 3, 3, 3),
('2023-04-01', '2023-04-15', 200.00, 350.00, 80.00, 'Scheduled', 4, 5, 4, 4, 4),
('2023-05-01', '2023-05-08', 180.00, 280.00, 55.00, 'Completed', 5, 1, 5, 5, 5);


-- Sample data for invoice table
INSERT INTO invoice (invoice_date, amount, service_id)
VALUES
('2023-01-01', 100.00, 1),
('2023-02-01', 120.00, 2),
('2023-03-01', 90.00, 3),
('2023-04-01', 150.00, 4),
('2023-05-01', 80.00, 5);

-- Sample data for payment table
INSERT INTO payment (pay_method, card_no, pay_amount, pay_date, invoice_id)
VALUES
('Card', '1234-5678-9012-3456', 100.00, '2023-01-15', 1),
('Cash', NULL, 120.00, '2023-02-15', 2),
('Card', '9876-5432-1098-7654', 90.00, '2023-03-15', 3),
('Gift Card', NULL, 150.00, '2023-04-15', 4),
('Card', '1111-2222-3333-4444', 80.00, '2023-05-15', 5);