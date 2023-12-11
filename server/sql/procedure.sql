-- Procedure
DELIMITER //

CREATE PROCEDURE DeleteStrayBookings()
BEGIN
    DECLARE cutoff_time DATETIME;
    SET cutoff_time = NOW() - INTERVAL 35 SECOND;
    
    DELETE FROM vehicle_booking 
    WHERE created_at <= cutoff_time 
    AND payment_status = 'P';
END //

DELIMITER ;

-- event
DELIMITER //

CREATE EVENT DeleteStrayBookingsEvent
ON SCHEDULE EVERY 1 MINUTE
DO
BEGIN
    CALL DeleteStrayBookings();
END //

DELIMITER ;
