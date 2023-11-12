CREATE TABLE dsr_corporation (
    corp_id   BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for every corporation.',
    corp_name VARCHAR(50) NOT NULL COMMENT 'Name of the corporation.',
    reg_no    VARCHAR(50) NOT NULL COMMENT 'Registration Number for the corporation.'
);


CREATE TABLE dsr_coupon (
    coupon_id   BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for every coupon',
    coupon_type VARCHAR(1) NOT NULL COMMENT 'Type of Coupon - Individual (I) or Corporate(C)',
    discount    DECIMAL(5, 2) NOT NULL COMMENT 'Discount available'
);


CREATE TABLE dsr_coupon_corp (
    coupon_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Coupon ID',
    corp_id   BIGINT NOT NULL COMMENT 'Corporation ID for the coupon'
);


CREATE TABLE dsr_coupon_indiv (
    coupon_id  BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    valid_from DATETIME NOT NULL COMMENT 'Coupon Valid From Date',
    valid_to   DATETIME NOT NULL COMMENT 'Coupon Valid To Date'
);


CREATE TABLE dsr_cust_corporate (
    customer_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for every customer.',
    corp_id     BIGINT NOT NULL COMMENT 'Corporation ID for the Employee',
    emp_id      VARCHAR(10) NOT NULL COMMENT 'Employee ID for the corporate'
);


CREATE TABLE dsr_cust_individual (
    customer_id         BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for every customer.',
    dl_no               VARCHAR(15) NOT NULL COMMENT 'Driver''s License Number for the Individual.',
    insurance_company   VARCHAR(50) NOT NULL COMMENT 'Insurance Company for the individual.',
    insurance_policy_no VARCHAR(50) NOT NULL COMMENT 'Individual''s insurance policy number.'
);


CREATE TABLE dsr_customer (
    customer_id     BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for every customer.',
    customer_type   VARCHAR(1) NOT NULL COMMENT 'Type of Customer - Individual(I) or Corporate(C).',
    first_name      VARCHAR(20) NOT NULL COMMENT 'First Name of the customer.',
    last_name       VARCHAR(20) NOT NULL COMMENT 'Last name of the customer.',
    email           VARCHAR(50) NOT NULL COMMENT 'Email for contact.',
    phone           VARCHAR(13) NOT NULL COMMENT 'Primary contact of the customer.',
    address_street  VARCHAR(100) NOT NULL COMMENT 'Street for the address.',
    address_city    VARCHAR(30) NOT NULL COMMENT 'City of the address.',
    address_state   VARCHAR(20) NOT NULL COMMENT 'State of the address.',
    address_zipcode VARCHAR(7) NOT NULL COMMENT 'Zipcode of the address.'
);


CREATE TABLE dsr_invc_payment (
    payment_id BIGINT NOT NULL COMMENT 'Payment ID used for transaction payment',
    invoice_id BIGINT NOT NULL COMMENT 'Invoice ID for the transaction payment',
    amount DECIMAL(9, 2) NOT NULL COMMENT 'Amount paid for that transaction',
    PRIMARY KEY (payment_id, invoice_id)
);


CREATE TABLE dsr_invoice (
    invoice_id     BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for an invoice.',
    service_id     BIGINT NOT NULL COMMENT 'Service ID for the generated invoice',
    invoice_date   DATETIME NOT NULL COMMENT 'Date on which the invoice was generated.',
    invoice_amount DECIMAL(10, 2) NOT NULL COMMENT 'Final Calculate Amount for rental service.'
);
CREATE UNIQUE INDEX dsr_invoice__idx ON dsr_invoice ( service_id ASC );


CREATE TABLE dsr_office_location (
    location_id     BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for officel locations.',
    address_street  VARCHAR(100) NOT NULL COMMENT 'Street address.	',
    address_city    VARCHAR(30) NOT NULL COMMENT 'City of the office.',
    address_state   VARCHAR(20) NOT NULL COMMENT 'State in which the office resides.',
    address_zipcode VARCHAR(7) NOT NULL COMMENT 'Zip code for the address.',
    phone           VARCHAR(13) NOT NULL COMMENT 'Primary contact number for the office.'
);


CREATE TABLE dsr_payment (
    payment_id  BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for every payment.',
    customer_id BIGINT NOT NULL COMMENT 'Customer ID for the payment option',
    pay_method  ENUM('DEBIT', 'CREDIT', 'GIFT') NOT NULL COMMENT 'Payment method - Card(Debit/Credit) or Gift Card',
    card_no     VARCHAR(30) NOT NULL COMMENT 'Card Number used for Credit/Debit Card transactions.',
    pay_date    DATETIME NOT NULL COMMENT 'Date of the payment.'
);


CREATE TABLE dsr_rental_service (
    service_id          BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for every service operation.',
    customer_id         BIGINT NOT NULL COMMENT 'Customer ID for the rental service',
    vehicle_id          BIGINT NOT NULL COMMENT 'Vehicle used for the rental service',
    pickup_date         DATETIME NOT NULL COMMENT 'Pickup Date for the service.',
    pickup_location_id  BIGINT NOT NULL COMMENT 'Pickup Office Location',
    dropoff_date        DATETIME COMMENT 'Drop off Date for the service.',
    dropoff_location_id BIGINT NOT NULL COMMENT 'Dropoff Office Location',
    start_odo           DECIMAL(9, 2) NOT NULL COMMENT 'Recorded odometer reading before start of the trip.',
    end_odo             DECIMAL(9, 2) COMMENT 'Recorded odometer reading at the end of the trip.',
    daily_limit         DECIMAL(9, 2) COMMENT 'Daily limit for the service.',
    service_status      VARCHAR(1) NOT NULL COMMENT 'Status for the service - Either Completed(C) or Pending(P)',
    coupon_id           BIGINT COMMENT 'Coupon ID used for the rental service'
);


-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE dsr_vehicle (
    vehicle_id        BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for vehicle(s).',
    location_id       BIGINT NOT NULL COMMENT 'Location ID for that vehicle.',
    class_id          BIGINT NOT NULL COMMENT 'Class ID for that vehicle.',
    make              VARCHAR(50) NOT NULL COMMENT 'Make of the vehicle.',
    model             VARCHAR(60) NOT NULL COMMENT 'Model description of the vehicle.',
    make_year         DATETIME NOT NULL COMMENT 'Year in which the model was made.',
    vin_no            VARCHAR(20) NOT NULL COMMENT 'Vehicle Identification Number.',
    liscense_plate_no VARCHAR(20) NOT NULL COMMENT 'License plate number for the particular vehicle.'
);


-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE dsr_vehicle_class (
    class_id     BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for a particular class of vehicles.',
    class        VARCHAR(30) NOT NULL COMMENT 'Class name/description of the vehicle type.',
    rent_charge  DECIMAL(9, 2) NOT NULL COMMENT 'Rent charged per day of usage.',
    extra_charge DECIMAL(9, 2) NOT NULL COMMENT 'Extra rent charge per day.'
);

-- CONSTRAINTS
ALTER TABLE dsr_coupon ADD CONSTRAINT chk_discount CHECK (discount <= 100);
ALTER TABLE dsr_coupon_indiv ADD CONSTRAINT chk_date CHECK (valid_to >= valid_from);
ALTER TABLE dsr_rental_service ADD CONSTRAINT chk_odo CHECK (end_odo >= start_odo);
ALTER TABLE dsr_rental_service ADD CONSTRAINT chk_service_date CHECK (dropoff_date >= pickup_date);

ALTER TABLE dsr_customer ADD CONSTRAINT ch_inh_dsr_customer CHECK ( customer_type IN ( 'C', 'I' ) );
ALTER TABLE dsr_coupon ADD CONSTRAINT ch_inh_dsr_coupon CHECK ( coupon_type IN ( 'C', 'I' ) );
ALTER TABLE dsr_rental_service ADD CONSTRAINT chk_service_status CHECK ( service_status IN ('P', 'C') );

ALTER TABLE dsr_coupon_corp ADD CONSTRAINT dsr_corpcoup_corp_fk FOREIGN KEY ( corp_id ) REFERENCES dsr_corporation ( corp_id );
ALTER TABLE dsr_coupon_corp ADD CONSTRAINT dsr_corpcoup_coupon_fk FOREIGN KEY ( coupon_id ) REFERENCES dsr_coupon ( coupon_id );
ALTER TABLE dsr_cust_corporate ADD CONSTRAINT dsr_corpcust_corp_fk FOREIGN KEY ( corp_id ) REFERENCES dsr_corporation ( corp_id );
ALTER TABLE dsr_cust_corporate ADD CONSTRAINT dsr_corpcust_cust_fk FOREIGN KEY ( customer_id ) REFERENCES dsr_customer ( customer_id );
ALTER TABLE dsr_coupon_indiv ADD CONSTRAINT dsr_indivcoup_coupon_fk FOREIGN KEY ( coupon_id ) REFERENCES dsr_coupon ( coupon_id );
ALTER TABLE dsr_cust_individual ADD CONSTRAINT dsr_indivcust_cust_fk FOREIGN KEY ( customer_id ) REFERENCES dsr_customer ( customer_id );
ALTER TABLE dsr_invoice ADD CONSTRAINT dsr_invce_rentsvc_fk FOREIGN KEY ( service_id ) REFERENCES dsr_rental_service ( service_id );
ALTER TABLE dsr_invc_payment ADD CONSTRAINT dsr_invcpay_invoice_fk FOREIGN KEY ( invoice_id ) REFERENCES dsr_invoice ( invoice_id );
ALTER TABLE dsr_invc_payment ADD CONSTRAINT dsr_invcpay_payment_fk FOREIGN KEY ( payment_id ) REFERENCES dsr_payment ( payment_id );
ALTER TABLE dsr_payment ADD CONSTRAINT dsr_payment_cust_fk FOREIGN KEY ( customer_id ) REFERENCES dsr_customer ( customer_id );
ALTER TABLE dsr_rental_service ADD CONSTRAINT dsr_rntsvc_coupon_fk FOREIGN KEY ( coupon_id ) REFERENCES dsr_coupon ( coupon_id );
ALTER TABLE dsr_rental_service ADD CONSTRAINT dsr_rntsvc_cust_fk FOREIGN KEY ( customer_id ) REFERENCES dsr_customer ( customer_id );
ALTER TABLE dsr_rental_service ADD CONSTRAINT dsr_rntsvc_drop_ofcloc_fk FOREIGN KEY ( dropoff_location_id ) REFERENCES dsr_office_location ( location_id );
ALTER TABLE dsr_rental_service ADD CONSTRAINT dsr_rntsvc_pick_ofcloc_fk FOREIGN KEY ( pickup_location_id ) REFERENCES dsr_office_location ( location_id );
ALTER TABLE dsr_rental_service ADD CONSTRAINT dsr_rntsvc_veh_fk FOREIGN KEY ( vehicle_id ) REFERENCES dsr_vehicle ( vehicle_id );
ALTER TABLE dsr_vehicle ADD CONSTRAINT dsr_veh_ofcloc_fk FOREIGN KEY ( location_id ) REFERENCES dsr_office_location ( location_id );
ALTER TABLE dsr_vehicle ADD CONSTRAINT dsr_veh_vehclass_fk FOREIGN KEY ( class_id ) REFERENCES dsr_vehicle_class ( class_id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
DROP TRIGGER IF EXISTS arc_fkarc_17_dsr_coupon_indiv_insert;
DROP TRIGGER IF EXISTS arc_fkarc_17_dsr_coupon_indiv_update;
DROP TRIGGER IF EXISTS arc_fkarc_17_dsr_coupon_corp_insert;
DROP TRIGGER IF EXISTS arc_fkarc_17_dsr_coupon_corp_update;
DROP TRIGGER IF EXISTS arc_fkarc_1_dsr_cust_corporate_insert;
DROP TRIGGER IF EXISTS arc_fkarc_1_dsr_cust_corporate_update;
DROP TRIGGER IF EXISTS arc_fkarc__dsr_cust_individual_insert;
DROP TRIGGER IF EXISTS arc_fkarc__dsr_cust_individual_update;
DROP TRIGGER IF EXISTS before_insert_dsr_rental_service;
DROP TRIGGER IF EXISTS before_insert_dsr_customer;
DROP TRIGGER IF EXISTS before_update_dsr_customer;
DROP TRIGGER IF EXISTS chk_individual_coupon_valid;
DROP TRIGGER IF EXISTS after_rental_service_update;


DELIMITER //

-- Triggers for dsr_coupon_indiv
CREATE TRIGGER arc_fkarc_17_dsr_coupon_indiv_insert BEFORE INSERT ON dsr_coupon_indiv
FOR EACH ROW
BEGIN
    DECLARE d VARCHAR(1);
    SELECT a.coupon_type INTO d FROM dsr_coupon a WHERE a.coupon_id = new.coupon_id;
    IF ( d IS NULL OR d <> 'I' ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK DSR_INDIVCOUP_COUPON_FK in Table DSR_COUPON_INDIV violates Arc constraint on Table DSR_COUPON - discriminator column coupon_type doesn''t have value ''I''';
    END IF;
END;
//

CREATE TRIGGER arc_fkarc_17_dsr_coupon_indiv_update BEFORE UPDATE ON dsr_coupon_indiv
FOR EACH ROW
BEGIN
    DECLARE d VARCHAR(1);
    SELECT a.coupon_type INTO d FROM dsr_coupon a WHERE a.coupon_id = new.coupon_id;
    IF ( d IS NULL OR d <> 'I' ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK DSR_INDIVCOUP_COUPON_FK in Table DSR_COUPON_INDIV violates Arc constraint on Table DSR_COUPON - discriminator column coupon_type doesn''t have value ''I''';
    END IF;
END;
//

-- Triggers for dsr_coupon_corp
CREATE TRIGGER arc_fkarc_17_dsr_coupon_corp_insert BEFORE INSERT ON dsr_coupon_corp
FOR EACH ROW
BEGIN
    DECLARE d VARCHAR(1);
    SELECT a.coupon_type INTO d FROM dsr_coupon a WHERE a.coupon_id = new.coupon_id;
    IF ( d IS NULL OR d <> 'C' ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK DSR_CORPCOUP_COUPON_FK in Table DSR_COUPON_CORP violates Arc constraint on Table DSR_COUPON - discriminator column coupon_type doesn''t have value ''C''';
    END IF;
END;
//

CREATE TRIGGER arc_fkarc_17_dsr_coupon_corp_update BEFORE UPDATE ON dsr_coupon_corp
FOR EACH ROW
BEGIN
    DECLARE d VARCHAR(1);
    SELECT a.coupon_type INTO d FROM dsr_coupon a WHERE a.coupon_id = new.coupon_id;
    IF ( d IS NULL OR d <> 'C' ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK DSR_CORPCOUP_COUPON_FK in Table DSR_COUPON_CORP violates Arc constraint on Table DSR_COUPON - discriminator column coupon_type doesn''t have value ''C''';
    END IF;
END;
//

-- Triggers for dsr_cust_corporate
CREATE TRIGGER arc_fkarc_1_dsr_cust_corporate_insert BEFORE INSERT ON dsr_cust_corporate
FOR EACH ROW
BEGIN
    DECLARE d VARCHAR(1);
    SELECT a.customer_type INTO d FROM dsr_customer a WHERE a.customer_id = new.customer_id;
    IF ( d IS NULL OR d <> 'C' ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK DSR_CORPCUST_CUST_FK in Table DSR_CUST_CORPORATE violates Arc constraint on Table DSR_CUSTOMER - discriminator column customer_type doesn''t have value ''C''';
    END IF;
END;
//

CREATE TRIGGER arc_fkarc_1_dsr_cust_corporate_update BEFORE UPDATE ON dsr_cust_corporate
FOR EACH ROW
BEGIN
    DECLARE d VARCHAR(1);
    SELECT a.customer_type INTO d FROM dsr_customer a WHERE a.customer_id = new.customer_id;
    IF ( d IS NULL OR d <> 'C' ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK DSR_CORPCUST_CUST_FK in Table DSR_CUST_CORPORATE violates Arc constraint on Table DSR_CUSTOMER - discriminator column customer_type doesn''t have value ''C''';
    END IF;
END;
//

-- Triggers for dsr_cust_individual
CREATE TRIGGER arc_fkarc__dsr_cust_individual_insert BEFORE INSERT ON dsr_cust_individual
FOR EACH ROW
BEGIN
    DECLARE d VARCHAR(1);
    SELECT a.customer_type INTO d FROM dsr_customer a WHERE a.customer_id = new.customer_id;
    IF ( d IS NULL OR d <> 'I' ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK DSR_INDIVCUST_CUST_FK in Table DSR_CUST_INDIVIDUAL violates Arc constraint on Table DSR_CUSTOMER - discriminator column customer_type doesn''t have value ''I''';
    END IF;
END;
//

CREATE TRIGGER arc_fkarc__dsr_cust_individual_update BEFORE UPDATE ON dsr_cust_individual
FOR EACH ROW
BEGIN
    DECLARE d VARCHAR(1);
    SELECT a.customer_type INTO d FROM dsr_customer a WHERE a.customer_id = new.customer_id;
    IF ( d IS NULL OR d <> 'I' ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK DSR_INDIVCUST_CUST_FK in Table DSR_CUST_INDIVIDUAL violates Arc constraint on Table DSR_CUSTOMER - discriminator column customer_type doesn''t have value ''I''';
    END IF;
END;
//

CREATE TRIGGER before_insert_dsr_rental_service
BEFORE INSERT ON dsr_rental_service
FOR EACH ROW
BEGIN
    DECLARE customer_type_var VARCHAR(1);
    DECLARE coupon_type_var VARCHAR(1);
    -- Get customer type
    SELECT customer_type INTO customer_type_var FROM dsr_customer WHERE customer_id = NEW.customer_id;
    -- Get coupon type
    SELECT coupon_type INTO coupon_type_var FROM dsr_coupon WHERE coupon_id = NEW.coupon_id;
    -- Check if customer type matches coupon type
    IF ( NEW.coupon_id IS NOT NULL AND customer_type_var <> coupon_type_var) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Customer type does not match Coupon type';
    END IF;
END;
//

-- Email check for address in Customer insert --
CREATE TRIGGER before_insert_dsr_customer
BEFORE INSERT ON dsr_customer
FOR EACH ROW
BEGIN
    IF NEW.email NOT REGEXP '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,4}$' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid email address';
    END IF;
END;
//

-- Update Trigger for Customer on email address -- 
CREATE TRIGGER before_update_dsr_customer
BEFORE UPDATE ON dsr_customer
FOR EACH ROW
BEGIN
    IF NEW.email NOT REGEXP '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,4}$' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid email address';
    END IF;
END;
//

-- Constraint for Individual Coupon to be valid
CREATE TRIGGER chk_individual_coupon_valid
BEFORE INSERT ON dsr_rental_service
FOR EACH ROW
BEGIN
	DECLARE coupon_type_val VARCHAR(1);
	DECLARE customer_type_val VARCHAR(1);
	DECLARE valid_to_val DATE;
    DECLARE pickup_date DATE;
    
	-- Get coupon type and validity dates
	SELECT 
		coup.coupon_type, 
		ci.valid_to
	INTO 
		coupon_type_val, 
		valid_to_val
	FROM 
		dsr_coupon coup
	JOIN 
		dsr_coupon_indiv ci ON coup.coupon_id = ci.coupon_id
        WHERE 
            coup.coupon_id = NEW.coupon_id;
	-- Get customer type
	SELECT 
		customer_type
	INTO 
		customer_type_val
	FROM 
		dsr_customer
	WHERE 
		customer_id = NEW.customer_id;
        -- Check if coupon type is individual and valid
        IF (NEW.coupon_id IS NOT NULL AND coupon_type_val = 'I' AND valid_to_val < NEW.pickup_date) THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Invalid Individual Coupon for the customer type or expired.';
        END IF;
END;
//

CREATE TRIGGER after_rental_service_update
AFTER UPDATE ON dsr_rental_service
FOR EACH ROW
BEGIN
    DECLARE rent_charge_v DECIMAL(9, 2);
    DECLARE extra_charge_v DECIMAL(9, 2);
    DECLARE total_amount_v DECIMAL(9, 2);
    DECLARE final_amount_v DECIMAL(9, 2);
    DECLARE coupon_discount_v DECIMAL(5, 2);
    IF NEW.service_status = 'C' AND OLD.service_status = 'P' AND NEW.end_odo IS NOT NULL AND NEW.dropoff_location_id IS NOT NULL THEN
        -- Fetch rent_charge and extra_charge based on the rental service vehicle class
        SELECT rent_charge, extra_charge INTO rent_charge_v, extra_charge_v
        FROM dsr_vehicle
        JOIN dsr_vehicle_class ON dsr_vehicle.class_id = dsr_vehicle_class.class_id
        WHERE dsr_vehicle.vehicle_id = NEW.vehicle_id;

        -- Calculate total amount based on the provided formula
        IF NEW.daily_limit IS NULL OR NEW.daily_limit = 0 THEN
            SET total_amount_v = (NEW.end_odo - NEW.start_odo) * rent_charge_v;
        ELSE
            SET total_amount_v = (NEW.end_odo - NEW.start_odo) * rent_charge_v
                              + GREATEST(NEW.end_odo - NEW.start_odo - NEW.daily_limit, 0) * extra_charge_v;
        END IF;

        -- Apply coupon discount
        IF NEW.coupon_id IS NOT NULL THEN

            -- Fetch coupon discount based on coupon_id
            SELECT discount INTO coupon_discount_v
            FROM dsr_coupon
            WHERE dsr_coupon.coupon_id = NEW.coupon_id;

            SET final_amount_v = total_amount_v - (total_amount_v * coupon_discount_v / 100);
        ELSE
            SET final_amount_v = total_amount_v;
        END IF;

        -- Insert entry into dsr_invoice table
        INSERT INTO dsr_invoice (service_id, invoice_date, invoice_amount)
        VALUES (NEW.service_id, NOW(), final_amount_v);
    END IF;
END
//
