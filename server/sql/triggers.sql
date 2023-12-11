-- INVOICE Trigger
DROP TRIGGER IF EXISTS after_booking_update;

DELIMITER //
CREATE TRIGGER after_booking_update AFTER UPDATE ON vehicle_booking
FOR EACH ROW
BEGIN
    DECLARE invoice_amount DECIMAL(10, 2);
    DECLARE coupon_discount DECIMAL(10, 2);
    DECLARE goods_and_services_tax DECIMAL(10, 2);
    DECLARE bill_to_address VARCHAR(255);
    DECLARE ship_to_address VARCHAR(255);
    DECLARE new_rent_charge DECIMAL(10, 2);
    DECLARE new_extra_charge DECIMAL(10, 2);


    -- Check if the trip status is updated to 'COMPLETE'
    IF NEW.trip_status = 'C' AND OLD.trip_status != 'C' THEN
        -- rent charge
        SELECT vv2.rent_charge INTO new_rent_charge
        FROM vehicle_booking vb
        INNER JOIN vehicle_vehicle vv on vv.vehicle_id = vb.vehicle_id_id 
        INNER JOIN vehicle_vehicleclass vv2 on vv2.class_id = vv.class_id_id
        WHERE vb.booking_id = NEW.booking_id;

        -- extra charge
        SELECT
            vv2.extra_charge INTO new_extra_charge
        FROM vehicle_booking vb
        INNER JOIN vehicle_vehicle vv on vv.vehicle_id = vb.vehicle_id_id 
        INNER JOIN vehicle_vehicleclass vv2 on vv2.class_id = vv.class_id_id
        WHERE vb.booking_id = NEW.booking_id;

        -- Calculate the total amount based on your logic
        SET invoice_amount = (
            (DATEDIFF(NEW.dropoff_date, NEW.pickup_date) * new_rent_charge) +
            (
                GREATEST(
                    (NEW.end_odo - NEW.start_odo) - (DATEDIFF(NEW.dropoff_date, NEW.pickup_date) * NEW.daily_limit),
                    0
                ) * new_extra_charge
            )
        );

        -- Apply coupon discount
        SELECT discount INTO coupon_discount
        FROM swimlane_coupon
        WHERE coupon_id = NEW.coupon_id_id;

        SET invoice_amount = invoice_amount - (invoice_amount * IFNULL(coupon_discount, 0) / 100);

        -- Calculate goods and services tax
        SET goods_and_services_tax = invoice_amount * 0.18;

        -- Set bill to address
        SELECT umu.address_street INTO bill_to_address
        FROM users_management_user umu
        WHERE umu.customer_id = NEW.customer_id_id;

        -- Set ship to address
        SELECT vo.address_street INTO ship_to_address
        FROM vehicle_officelocation vo
        WHERE location_id = NEW.dropoff_location_id;

        -- Insert the invoice record
        INSERT INTO vehicle_invoice (
            bill_to_address
            , ship_to_address
            , dropoff_location
            , taxes
            , total
            , booking_id_id
        )
        VALUES (
            bill_to_address
            , ship_to_address
            , ship_to_address
            , goods_and_services_tax
            , invoice_amount + goods_and_services_tax
            , NEW.booking_id
        );
    END IF;
END
//
