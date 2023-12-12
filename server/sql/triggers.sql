-- INVOICE Trigger
DROP TRIGGER IF EXISTS after_booking_update;
DROP TRIGGER IF EXISTS arc_fkarc_17_dsr_coupon_indiv_insert;
DROP TRIGGER IF EXISTS arc_fkarc_17_dsr_coupon_indiv_update;
DROP TRIGGER IF EXISTS arc_fkarc_17_dsr_coupon_corp_insert;
DROP TRIGGER IF EXISTS arc_fkarc_17_dsr_coupon_corp_update;
DROP TRIGGER IF EXISTS arc_fkarc_1_dsr_cust_corporate_insert;
DROP TRIGGER IF EXISTS arc_fkarc_1_dsr_cust_corporate_update;
DROP TRIGGER IF EXISTS arc_fkarc__dsr_cust_individual_insert;
DROP TRIGGER IF EXISTS arc_fkarc__dsr_cust_individual_update;
DROP TRIGGER IF EXISTS before_insert_dsr_rental_service;
DROP TRIGGER IF EXISTS chk_coupon_valid;

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
            ((DATEDIFF(NEW.dropoff_date, NEW.pickup_date) + 1) * new_rent_charge) +
            (
                GREATEST(
                    (NEW.end_odo - NEW.start_odo) - ((DATEDIFF(NEW.dropoff_date, NEW.pickup_date) + 1) * NEW.daily_limit),
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

-- Triggers for dsr_coupon_indiv
CREATE TRIGGER arc_fkarc_17_dsr_coupon_indiv_insert BEFORE INSERT ON swimlane_couponindividual
FOR EACH ROW
BEGIN
    DECLARE d VARCHAR(1);
    SELECT a.coupon_type INTO d FROM swimlane_coupon a WHERE a.coupon_id = new.coupon_id_id;
    IF ( d IS NULL OR d <> 'I' ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK DSR_INDIVCOUP_COUPON_FK in Table DSR_COUPON_INDIV violates Arc constraint on Table DSR_COUPON - discriminator column coupon_type doesn''t have value ''I''';
    END IF;
END;
//

CREATE TRIGGER arc_fkarc_17_dsr_coupon_indiv_update BEFORE UPDATE ON swimlane_couponindividual
FOR EACH ROW
BEGIN
    DECLARE d VARCHAR(1);
    SELECT a.coupon_type INTO d FROM swimlane_coupon a WHERE a.coupon_id = new.coupon_id_id;
    IF ( d IS NULL OR d <> 'I' ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK DSR_INDIVCOUP_COUPON_FK in Table DSR_COUPON_INDIV violates Arc constraint on Table DSR_COUPON - discriminator column coupon_type doesn''t have value ''I''';
    END IF;
END;
//

-- Triggers for dsr_coupon_corp
CREATE TRIGGER arc_fkarc_17_dsr_coupon_corp_insert BEFORE INSERT ON swimlane_couponcorporate
FOR EACH ROW
BEGIN
    DECLARE d VARCHAR(1);
    SELECT a.coupon_type INTO d FROM swimlane_coupon a WHERE a.coupon_id = new.coupon_id_id;
    IF ( d IS NULL OR d <> 'C' ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK DSR_CORPCOUP_COUPON_FK in Table DSR_COUPON_CORP violates Arc constraint on Table DSR_COUPON - discriminator column coupon_type doesn''t have value ''C''';
    END IF;
END;
//

CREATE TRIGGER arc_fkarc_17_dsr_coupon_corp_update BEFORE UPDATE ON swimlane_couponcorporate
FOR EACH ROW
BEGIN
    DECLARE d VARCHAR(1);
    SELECT a.coupon_type INTO d FROM swimlane_coupon a WHERE a.coupon_id = new.coupon_id_id;
    IF ( d IS NULL OR d <> 'C' ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK DSR_CORPCOUP_COUPON_FK in Table DSR_COUPON_CORP violates Arc constraint on Table DSR_COUPON - discriminator column coupon_type doesn''t have value ''C''';
    END IF;
END;
//

-- Triggers for dsr_cust_corporate
CREATE TRIGGER arc_fkarc_1_dsr_cust_corporate_insert BEFORE INSERT ON swimlane_customercorporate
FOR EACH ROW
BEGIN
    DECLARE d VARCHAR(1);
    SELECT a.user_type INTO d FROM users_management_user a WHERE a.customer_id = new.customer_id_id;
    IF ( d IS NULL OR d <> 'C' ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK DSR_CORPCUST_CUST_FK in Table DSR_CUST_CORPORATE violates Arc constraint on Table DSR_CUSTOMER - discriminator column customer_type doesn''t have value ''C''';
    END IF;
END;
//

CREATE TRIGGER arc_fkarc_1_dsr_cust_corporate_update BEFORE UPDATE ON swimlane_customercorporate
FOR EACH ROW
BEGIN
    DECLARE d VARCHAR(1);
    SELECT a.user_type INTO d FROM users_management_user a WHERE a.customer_id = new.customer_id_id;
    IF ( d IS NULL OR d <> 'C' ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK DSR_CORPCUST_CUST_FK in Table DSR_CUST_CORPORATE violates Arc constraint on Table DSR_CUSTOMER - discriminator column customer_type doesn''t have value ''C''';
    END IF;
END;
//

-- Triggers for dsr_cust_individual
CREATE TRIGGER arc_fkarc__dsr_cust_individual_insert BEFORE INSERT ON swimlane_customerindividual
FOR EACH ROW
BEGIN
    DECLARE d VARCHAR(1);
    SELECT a.user_type INTO d FROM users_management_user a WHERE a.customer_id = new.customer_id_id;
    IF ( d IS NULL OR d <> 'I' ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK DSR_INDIVCUST_CUST_FK in Table DSR_CUST_INDIVIDUAL violates Arc constraint on Table DSR_CUSTOMER - discriminator column customer_type doesn''t have value ''I''';
    END IF;
END;
//

CREATE TRIGGER arc_fkarc__dsr_cust_individual_update BEFORE UPDATE ON swimlane_customerindividual
FOR EACH ROW
BEGIN
    DECLARE d VARCHAR(1);
    SELECT a.user_type INTO d FROM users_management_user a WHERE a.customer_id = new.customer_id_id;
    IF ( d IS NULL OR d <> 'I' ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK DSR_INDIVCUST_CUST_FK in Table DSR_CUST_INDIVIDUAL violates Arc constraint on Table DSR_CUSTOMER - discriminator column customer_type doesn''t have value ''I''';
    END IF;
END;
//

CREATE TRIGGER before_insert_dsr_rental_service BEFORE INSERT ON vehicle_booking
FOR EACH ROW
BEGIN
    DECLARE user_type_var VARCHAR(1);
    DECLARE coupon_type_var VARCHAR(1);
    -- Get customer type
    SELECT user_type INTO user_type_var FROM users_management_user WHERE customer_id = NEW.customer_id_id;
    -- Get coupon type
    SELECT coupon_type INTO coupon_type_var FROM swimlane_coupon WHERE coupon_id = NEW.coupon_id_id;
    -- Check if customer type matches coupon type
    IF ( NEW.coupon_id_id IS NOT NULL AND user_type_var <> coupon_type_var) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Customer type does not match Coupon type';
    END IF;
END;
//

-- Constraint for Individual Coupon to be valid
CREATE TRIGGER chk_coupon_valid BEFORE UPDATE ON vehicle_booking
FOR EACH ROW
BEGIN
	DECLARE coupon_type_val VARCHAR(1);
	DECLARE user_type_val VARCHAR(1);
	DECLARE valid_to_val DATE;
    DECLARE pickup_date DATE;
    DECLARE user_corp_id BIGINT;
    DECLARE coupon_corp_id BIGINT;
    IF (NEW.coupon_id_id IS NOT NULL) THEN
        -- Get customer type
        SELECT
            user_type
        INTO 
            user_type_val
        FROM 
            users_management_user
        WHERE  customer_id = NEW.customer_id_id;
        -- Get coupon type and validity dates
        SELECT coup.coupon_type INTO coupon_type_val
        FROM swimlane_coupon coup
        WHERE coup.coupon_id = NEW.coupon_id_id;

        IF(user_type_val <> coupon_type_val) THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Invalid coupon for user';
        END IF;
        IF(user_type_val = 'I') THEN
            SELECT valid_to INTO valid_to_val
            FROM swimlane_couponindividual sci WHERE sci.coupon_id_id = NEW.coupon_id_id;
            IF(valid_to_val < NEW.created_at) THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Expired coupon!';
            END IF;
        END IF;
        IF(user_type_val = 'C') THEN
            -- select coupon corp id
            SELECT corp_id_id INTO coupon_corp_id
            FROM swimlane_couponcorporate scc WHERE scc.coupon_id_id = NEW.coupon_id_id;
            -- select user corp id
            SELECT corp_id_id INTO user_corp_id
            FROM swimlane_customercorporate scc WHERE scc.customer_id_id = NEW.customer_id_id;
            IF(coupon_corp_id <> user_corp_id) THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'This coupon is NA';
            END IF;
        END IF;
    END IF;
END;
//
