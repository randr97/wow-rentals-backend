-- This dml updates the rental services which triggers a invoice creation process within the database
UPDATE dsr_rental_service
SET
    pickup_date = '2023-06-01',
    dropoff_date = '2025-01-01',
    start_odo = 13000.00,
    end_odo = 25000.00,
    daily_limit = 65.00,
    service_status = 'C',
    pickup_location_id = 2,
    dropoff_location_id = 3,
    customer_id = 6,
    vehicle_id = 6,
    coupon_id = 6
WHERE service_id = 1;

UPDATE dsr_rental_service
SET
    pickup_date = '2023-04-01',
    dropoff_date = '2025-01-01',
    start_odo = 17000.00,
    end_odo = 25000.00,
    daily_limit = 75.00,
    service_status = 'C',
    pickup_location_id = 3,
    dropoff_location_id = 4,
    customer_id = 7,
    vehicle_id = 7,
    coupon_id = 7
WHERE service_id = 2;

UPDATE dsr_rental_service
SET
    pickup_date = '2023-08-01',
    dropoff_date = '2025-01-01',
    start_odo = 14000.00,
    end_odo = 25000.00,
    daily_limit = 62.00,
    service_status = 'C',
    pickup_location_id = 4,
    dropoff_location_id = 5,
    customer_id = 8,
    vehicle_id = 8,
    coupon_id = 8
WHERE service_id = 3;

UPDATE dsr_rental_service
SET
    pickup_date = '2023-09-01',
    dropoff_date = '2025-01-01',
    start_odo = 22000.00,
    end_odo = 25000.00,
    daily_limit = 85.00,
    service_status = 'C',
    pickup_location_id = 5,
    dropoff_location_id = 1,
    customer_id = 9,
    vehicle_id = 9,
    coupon_id = 9
WHERE service_id = 4;

UPDATE dsr_rental_service
SET
    pickup_date = '2023-10-01',
    dropoff_date = '2025-01-01',
    start_odo = 20000.00,
    end_odo = 25000.00,
    daily_limit = 70.00,
    service_status = 'C',
    pickup_location_id = 1,
    dropoff_location_id = 2,
    customer_id = 10,
    vehicle_id = 10,
    coupon_id = 10
WHERE service_id = 5;

UPDATE dsr_rental_service
SET
    pickup_date = '2024-03-01',
    dropoff_date = '2025-01-01',
    start_odo = 19000.00,
    end_odo = 25000.00,
    daily_limit = 68.00,
    service_status = 'C',
    pickup_location_id = 1,
    dropoff_location_id = 2,
    customer_id = 27,
    vehicle_id = 15,
    coupon_id = 17
WHERE service_id = 9;

UPDATE dsr_rental_service
SET
    pickup_date = '2024-07-01',
    dropoff_date = '2025-01-01',
    start_odo = 20000.00,
    end_odo = 25000.00,
    daily_limit = 70.00,
    service_status = 'C',
    pickup_location_id = 5,
    dropoff_location_id = 1,
    customer_id = 30,
    vehicle_id = 19,
    coupon_id = 20
WHERE service_id = 13;

UPDATE dsr_rental_service
SET
    pickup_date = '2024-08-01',
    dropoff_date = '2025-01-01',
    start_odo = 17000.00,
    end_odo = 25000.00,
    daily_limit = 65.00,
    service_status = 'C',
    pickup_location_id = 1,
    dropoff_location_id = 2,
    customer_id = 31,
    vehicle_id = 20,
    coupon_id = 21
WHERE service_id = 14;

UPDATE dsr_rental_service
SET
    pickup_date = '2024-07-01',
    dropoff_date = '2025-01-01',
    start_odo = 20000.00,
    end_odo = 25000.00,
    daily_limit = 70.00,
    service_status = 'C',
    pickup_location_id = 5,
    dropoff_location_id = 1,
    customer_id = 34,
    vehicle_id = 19,
    coupon_id = 24
WHERE service_id = 17;

UPDATE dsr_rental_service
SET
    pickup_date = '2024-08-01',
    dropoff_date = '2025-01-01',
    start_odo = 17000.00,
    end_odo = 25000.00,
    daily_limit = 65.00,
    service_status = 'C',
    pickup_location_id = 1,
    dropoff_location_id = 2,
    customer_id = 35,
    vehicle_id = 20,
    coupon_id = 25
WHERE service_id = 18;


INSERT INTO dsr_invc_payment (payment_id, invoice_id, amount)
VALUES
(1, 1, 1598.00),
(2, 2, 24414.73),
(3, 3, 4794.00),
(4, 4, 7645.22),
(5, 5, 8189.75),
(6, 6, 1598.00),
(7, 7, 24414.73),
(8, 8, 4794.00),
(9, 9, 7645.22),
(10, 10, 8189.75);
