-- This dml updates the rental services which triggers a invoice creation process within the database
UPDATE dsr_rental_service
SET 
    pickup_date = '2023-06-01',
    dropoff_date = '2023-06-08',
    start_odo = 13000.00,
    end_odo = 13040.00,
    daily_limit = 75.00,
    service_status = 'C',
    pickup_location_id = 2,
    dropoff_location_id = 3,
    customer_id = 6,
    vehicle_id = 6,
    coupon_id = 6
WHERE
    service_id = 1;
    
    
UPDATE dsr_rental_service
SET 
    pickup_date = '2023-04-01',
    dropoff_date = '2023-06-08',
    start_odo = 17000.00,
    end_odo = 17800.00,
    daily_limit = 75.00,
    service_status = 'C',
    pickup_location_id = 3,
    dropoff_location_id = 4,
    customer_id = 7,
    vehicle_id = 7,
    coupon_id = 7
WHERE
    service_id = 2;
    
UPDATE dsr_rental_service
SET 
    pickup_date = '2023-08-01',
    dropoff_date = '2023-08-22',
    start_odo = 14000.00,
    end_odo = 14075.00,
    daily_limit = 75.00,
    service_status = 'C',
    pickup_location_id = 4,
    dropoff_location_id = 5,
    customer_id = 8,
    vehicle_id = 8,
    coupon_id = 8
WHERE
    service_id = 3;
    
UPDATE dsr_rental_service
SET 
    pickup_date = '2023-09-01',
    dropoff_date = '2023-09-12',
    start_odo = 22000.00,
    end_odo = 22200.00,
    daily_limit = 75.00,
    service_status = 'C',
    pickup_location_id = 5,
    dropoff_location_id = 1,
    customer_id = 9,
    vehicle_id = 9,
    coupon_id = 9
WHERE
    service_id = 4;
    
UPDATE dsr_rental_service
SET 
    pickup_date = '2023-10-01',
    dropoff_date = '2023-10-11',
    start_odo = 20000.00,
    end_odo = 20100.00,
    daily_limit = 75.00,
    service_status = 'C',
    pickup_location_id = 1,
    dropoff_location_id = 2,
    customer_id = 10,
    vehicle_id = 10,
    coupon_id = 10
WHERE
    service_id = 5;


INSERT INTO dsr_invc_payment (payment_id, invoice_id, amount)
VALUES
(8, 1, 1598.00),
(9, 2, 24414.73),
(10, 2, 24414.73),
(11, 3, 4794.00),
(12, 4, 7645.22),
(13, 5, 8189.75);
