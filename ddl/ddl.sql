-- SQLINES DEMO *** le SQL Developer Data Modeler 23.1.0.087.0806
-- SQLINES DEMO *** -11-08 18:59:59 EST
-- SQLINES DEMO *** le Database 21c
-- SQLINES DEMO *** le Database 21c
-- SQLINES DEMO *** no DDL - MDSYS.SDO_GEOMETRY
-- SQLINES DEMO *** no DDL - XMLTYPE
-- SQLINES LICENSE FOR EVALUATION USE ONLY


CREATE TABLE address (
    address_id      BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for every customer.',
    address_street  VARCHAR(100) NOT NULL COMMENT 'Street for the address.',
    address_city    VARCHAR(30) NOT NULL COMMENT 'City of the address.',
    address_state   VARCHAR(20) NOT NULL COMMENT 'State of the address.',
    address_zipcode VARCHAR(7) NOT NULL COMMENT 'Zipcode of the address.',
    customer_id     BIGINT NOT NULL
);


-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE corporation (
    corp_id   BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for every corporation.',
    corp_name VARCHAR(50) NOT NULL COMMENT 'Name of the corporation.',
    reg_no    VARCHAR(50) NOT NULL COMMENT 'Registration Number for the corporation.'
);


-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE coupon (
    coupon_id   BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    coupon_type VARCHAR(6) NOT NULL COMMENT 'Type of Coupon - Individual (I) or Corporate(C)',
    discount    DECIMAL(3, 2) NOT NULL
);
ALTER TABLE coupon ADD CONSTRAINT ch_inh_coupon CHECK ( coupon_type IN ( 'C', 'I' ) );


-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE coupon_corp (
    coupon_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    corp_id   BIGINT
);


-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE coupon_indiv (
    coupon_id  BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    valid_from DATETIME NOT NULL,
    valid_to   DATETIME NOT NULL
);


-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE cust_corporate (
    customer_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for every customer.',
    emp_id      VARCHAR(10) NOT NULL COMMENT 'Employee ID for the corporate',
    corp_id     BIGINT
);


-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE cust_individual (
    customer_id         BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for every customer.',
    dl_no               VARCHAR(15) NOT NULL COMMENT 'Driver''s License Number for the Individual.',
    insurance_company   VARCHAR(50) NOT NULL COMMENT 'Insurance Company for the individual.',
    insurance_policy_no VARCHAR(50) NOT NULL COMMENT 'Individual''s insurance policy number.'
);


-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE customer (
    customer_id   BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for every customer.',
    customer_type VARCHAR(1) NOT NULL COMMENT 'Type of Customer - Individual(I) or Corporate(C).',
    first_name    VARCHAR(20) NOT NULL COMMENT 'First Name of the customer.',
    last_name     VARCHAR(20) NOT NULL COMMENT 'Last name of the customer.',
    email         VARCHAR(50) NOT NULL COMMENT 'Email for contact.',
    phone         VARCHAR(13) NOT NULL COMMENT 'Primary contact of the customer.'
);
ALTER TABLE customer ADD CONSTRAINT ch_inh_customer CHECK ( customer_type IN ( 'C', 'I' ) );


-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE invoice (
    invoice_id   BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for an invoice.',
    invoice_date DATETIME NOT NULL COMMENT 'Date on which the invoice was generated.',
    amount       DECIMAL(7, 2) NOT NULL COMMENT 'Final Calculate Amount for rental service.',
    service_id   BIGINT NOT NULL
);


-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE office_location (
    location_id     BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for officel locations.',
    address_street  VARCHAR(100) NOT NULL COMMENT 'Street address.	',
    address_city    VARCHAR(30) NOT NULL COMMENT 'City of the office.',
    address_state   VARCHAR(20) NOT NULL COMMENT 'State in which the office resides.',
    address_zipcode VARCHAR(7) NOT NULL COMMENT 'Zip code for the address.',
    phone           VARCHAR(13) NOT NULL COMMENT 'Primary contact number for the office.'
);


-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE payment (
    payment_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for every payment.',
    pay_method VARCHAR(30) NOT NULL COMMENT 'Payment method - Card(Debit/Credit), Gift Card, Cash etc.',
    card_no    VARCHAR(30) NOT NULL COMMENT 'Card Number used for Credit/Debit Card transactions.',
    pay_amount DECIMAL(7, 2) NOT NULL COMMENT 'Amount paid inclusive taxes.',
    pay_date   DATETIME NOT NULL COMMENT 'Date of the payment.',
    invoice_id BIGINT
);


-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE rental_service (
    service_id          BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for every service operation.',
    pickup_date         DATETIME NOT NULL COMMENT 'Pickup Date for the service.',
    dropoff_date        DATETIME COMMENT 'Drop off data for the service.',
    start_odo           DECIMAL(7, 2) NOT NULL COMMENT 'Recorded odometer reading before start of the trip.',
    end_odo             DECIMAL(7, 2) COMMENT 'Recorded odometer reading at the end of the trip.',
    daily_limit         DECIMAL(7, 2) COMMENT 'Daily limit for the service.',
    service_status      VARCHAR(1) NOT NULL,
    pickup_location_id  BIGINT,
    dropoff_location_id BIGINT,
    customer_id         BIGINT,
    vehicle_id          BIGINT,
    coupon_id           BIGINT
);


-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE vehicle (
    vehicle_id        BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for vehicle(s).',
    location_id       BIGINT NOT NULL,
    class_id          BIGINT NOT NULL,
    make              VARCHAR(50) NOT NULL COMMENT 'Make of the vehicle.',
    model             VARCHAR(60) NOT NULL COMMENT 'Model description of the vehicle.',
    make_year         DATETIME NOT NULL COMMENT 'Year in which the model was made.',
    vin_no            VARCHAR(20) NOT NULL COMMENT 'Vehicle Identification Number.',
    liscense_plate_no VARCHAR(20) NOT NULL COMMENT 'License plate number for the particular vehicle.'
);


-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE vehicle_class (
    class_id     BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID for a particular class of vehicles.',
    class        VARCHAR(30) NOT NULL COMMENT 'Class name/description of the vehicle type.',
    rent_charge  DECIMAL(7, 2) NOT NULL COMMENT 'Rent charged per day of usage.',
    extra_charge DECIMAL(7, 2) NOT NULL COMMENT 'Extra rent charge per day.'
);


-- FOREIGN KEY CONSTRAINTS
ALTER TABLE address ADD CONSTRAINT addr_cust_fk FOREIGN KEY ( customer_id ) REFERENCES customer ( customer_id );
ALTER TABLE coupon_corp ADD CONSTRAINT corpcpn_corporation_fk FOREIGN KEY ( corp_id ) REFERENCES corporation ( corp_id );
ALTER TABLE coupon_corp ADD CONSTRAINT corpcpn_coupon_fk FOREIGN KEY ( coupon_id ) REFERENCES coupon ( coupon_id );
ALTER TABLE cust_corporate ADD CONSTRAINT cust_custcorp_fk FOREIGN KEY ( customer_id ) REFERENCES customer ( customer_id );
ALTER TABLE cust_individual ADD CONSTRAINT cust_individual_fk FOREIGN KEY ( customer_id ) REFERENCES customer ( customer_id );
ALTER TABLE cust_corporate ADD CONSTRAINT custcorp_corp_fk FOREIGN KEY ( corp_id ) REFERENCES corporation ( corp_id );
ALTER TABLE coupon_indiv ADD CONSTRAINT indivcpn_coupon_fk FOREIGN KEY ( coupon_id ) REFERENCES coupon ( coupon_id );
ALTER TABLE invoice ADD CONSTRAINT invce_rental_service_fk FOREIGN KEY ( service_id ) REFERENCES rental_service ( service_id );
ALTER TABLE payment ADD CONSTRAINT payment_invce_fk FOREIGN KEY ( invoice_id ) REFERENCES invoice ( invoice_id );
ALTER TABLE rental_service ADD CONSTRAINT rntal_service_cpn_fk FOREIGN KEY ( coupon_id ) REFERENCES coupon ( coupon_id );
ALTER TABLE rental_service ADD CONSTRAINT rntal_service_cust_fk FOREIGN KEY ( customer_id ) REFERENCES customer ( customer_id );
ALTER TABLE rental_service ADD CONSTRAINT rntal_service_ofc_loc_drop_fk FOREIGN KEY ( dropoff_location_id ) REFERENCES office_location ( location_id );
ALTER TABLE rental_service ADD CONSTRAINT rntal_service_ofc_loc_pick_fk FOREIGN KEY ( pickup_location_id ) REFERENCES office_location ( location_id );
ALTER TABLE rental_service ADD CONSTRAINT rntal_service_vehicle_fk FOREIGN KEY ( vehicle_id ) REFERENCES vehicle ( vehicle_id );
ALTER TABLE vehicle ADD CONSTRAINT vehicle_class_fk FOREIGN KEY ( class_id ) REFERENCES vehicle_class ( class_id );
ALTER TABLE vehicle ADD CONSTRAINT vehicle_ofc_loc_fk FOREIGN KEY ( location_id ) REFERENCES office_location ( location_id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
DROP TRIGGER IF EXISTS arc_fkarc_5_coupon_indiv_insert;
DROP TRIGGER IF EXISTS arc_fkarc_5_coupon_indiv_update;
DROP TRIGGER IF EXISTS arc_fkarc_5_coupon_corp_insert;
DROP TRIGGER IF EXISTS arc_fkarc_5_coupon_corp_update;
DROP TRIGGER IF EXISTS arc_fkarc_6_cust_corporate_insert;
DROP TRIGGER IF EXISTS arc_fkarc_6_cust_corporate_update;
DROP TRIGGER IF EXISTS arc_fkarc_6_cust_individual_insert;
DROP TRIGGER IF EXISTS arc_fkarc_6_cust_individual_update;

DELIMITER //

CREATE TRIGGER arc_fkarc_5_coupon_indiv_insert BEFORE INSERT ON coupon_indiv
FOR EACH ROW
BEGIN
    DECLARE d CHAR(6);
    SELECT a.coupon_type INTO d FROM coupon a WHERE a.coupon_id = NEW.coupon_id;
    IF d IS NULL OR d <> 'I' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK INDIVCPN_COUPON_FK in Table COUPON_INDIV violates Arc constraint on Table COUPON - discriminator column coupon_type doesn''t have value ''I''';
    END IF;
END;
//

DELIMITER ;

DELIMITER //

CREATE TRIGGER arc_fkarc_5_coupon_indiv_update BEFORE UPDATE ON coupon_indiv
FOR EACH ROW
BEGIN
    DECLARE d CHAR(6);
    SELECT a.coupon_type INTO d FROM coupon a WHERE a.coupon_id = NEW.coupon_id;
    IF d IS NULL OR d <> 'I' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK INDIVCPN_COUPON_FK in Table COUPON_INDIV violates Arc constraint on Table COUPON - discriminator column coupon_type doesn''t have value ''I''';
    END IF;
END;
//

DELIMITER ;

DELIMITER //

CREATE TRIGGER arc_fkarc_5_coupon_corp_insert BEFORE INSERT ON coupon_corp
FOR EACH ROW
BEGIN
    DECLARE d CHAR(6);
    SELECT a.coupon_type INTO d FROM coupon a WHERE a.coupon_id = NEW.coupon_id;
    IF d IS NULL OR d <> 'C' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK CORPCPN_COUPON_FK in Table COUPON_CORP violates Arc constraint on Table COUPON - discriminator column coupon_type doesn''t have value ''C''';
    END IF;
END;
//

DELIMITER ;

DELIMITER //

CREATE TRIGGER arc_fkarc_5_coupon_corp_update BEFORE UPDATE ON coupon_corp
FOR EACH ROW
BEGIN
    DECLARE d CHAR(6);
    SELECT a.coupon_type INTO d FROM coupon a WHERE a.coupon_id = NEW.coupon_id;
    IF d IS NULL OR d <> 'C' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK CORPCPN_COUPON_FK in Table COUPON_CORP violates Arc constraint on Table COUPON - discriminator column coupon_type doesn''t have value ''C''';
    END IF;
END;
//

DELIMITER ;

DELIMITER //

CREATE TRIGGER arc_fkarc_6_cust_corporate_insert BEFORE INSERT ON cust_corporate
FOR EACH ROW
BEGIN
    DECLARE d CHAR(1);
    SELECT a.customer_type INTO d FROM customer a WHERE a.customer_id = NEW.customer_id;
    IF d IS NULL OR d <> 'C' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK CUST_CUSTCORP_FK in Table CUST_CORPORATE violates Arc constraint on Table CUSTOMER - discriminator column customer_type doesn''t have value ''C''';
    END IF;
END;
//

DELIMITER ;

DELIMITER //

CREATE TRIGGER arc_fkarc_6_cust_corporate_update BEFORE UPDATE ON cust_corporate
FOR EACH ROW
BEGIN
    DECLARE d CHAR(1);
    SELECT a.customer_type INTO d FROM customer a WHERE a.customer_id = NEW.customer_id;
    IF d IS NULL OR d <> 'C' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK CUST_CUSTCORP_FK in Table CUST_CORPORATE violates Arc constraint on Table CUSTOMER - discriminator column customer_type doesn''t have value ''C''';
    END IF;
END;
//

DELIMITER ;

DELIMITER //

CREATE TRIGGER arc_fkarc_6_cust_individual_insert BEFORE INSERT ON cust_individual
FOR EACH ROW
BEGIN
    DECLARE d CHAR(1);
    SELECT a.customer_type INTO d FROM customer a WHERE a.customer_id = NEW.customer_id;
    IF d IS NULL OR d <> 'I' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK CUST_INDIVIDUAL_FK in Table CUST_INDIVIDUAL violates Arc constraint on Table CUSTOMER - discriminator column customer_type doesn''t have value ''I''';
    END IF;
END;
//

DELIMITER ;

DELIMITER //

CREATE TRIGGER arc_fkarc_6_cust_individual_update BEFORE UPDATE ON cust_individual
FOR EACH ROW
BEGIN
    DECLARE d CHAR(1);
    SELECT a.customer_type INTO d FROM customer a WHERE a.customer_id = NEW.customer_id;
    IF d IS NULL OR d <> 'I' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FK CUST_INDIVIDUAL_FK in Table CUST_INDIVIDUAL violates Arc constraint on Table CUSTOMER - discriminator column customer_type doesn''t have value ''I''';
    END IF;
END;
//

DELIMITER ;


-- SQLINES DEMO *** per Data Modeler Summary Report: 
-- 
-- SQLINES DEMO ***                        14
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                        32
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO *** DY                      0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         4
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***  TYPE                   0
-- SQLINES DEMO ***  TYPE                   0
-- SQLINES DEMO ***  TYPE BODY              0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO *** EGMENT                  0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO *** ED VIEW                 0
-- SQLINES DEMO *** ED VIEW LOG             0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- 
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- 
-- SQLINES DEMO ***                         0
-- 
-- SQLINES DEMO ***                         0
-- SQLINES DEMO *** A                       0
-- SQLINES DEMO *** T                       0
-- 
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
