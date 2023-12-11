-- WITH INDEXING
"""
-> Limit: 100 row(s)  (cost=3.65 rows=34) (actual time=0.911..22.2 rows=34 loops=1)
    -> Filter: ((exists(select #2) is false or exists(select #3) is false or exists(select #4) is false) and (exists(select #5) is false or exists(select #6) is false or exists(select #7) is false))  (cost=3.65 rows=34) (actual time=0.91..22.2 rows=34 loops=1)
        -> Table scan on vehicle_vehicle  (cost=3.65 rows=34) (actual time=0.0483..0.0798 rows=34 loops=1)
        -> Select #2 (subquery in condition; dependent)
            -> Limit: 1 row(s)  (cost=4.07 rows=1) (actual time=0.04..0.0401 rows=1 loops=34)
                -> Filter: (U1.next_available_date > DATE'2021-07-15')  (cost=4.07 rows=37.5) (actual time=0.0398..0.0398 rows=1 loops=34)
                    -> Covering index lookup on U1 using vehicle_boo_vehicle_3b75a3_idx (vehicle_id_id=vehicle_vehicle.vehicle_id)  (cost=4.07 rows=112) (actual time=0.0235..0.0322 rows=72.6 loops=34)
        -> Select #3 (subquery in condition; dependent)
            -> Limit: 1 row(s)  (cost=22.9 rows=1) (actual time=0.353..0.353 rows=0 loops=34)
                -> Filter: (U1.payment_status = 'C')  (cost=22.9 rows=11.2) (actual time=0.353..0.353 rows=0 loops=34)
                    -> Index lookup on U1 using vehicle_boo_vehicle_be74b4_idx (vehicle_id_id=vehicle_vehicle.vehicle_id)  (cost=22.9 rows=112) (actual time=0.278..0.343 rows=119 loops=34)
        -> Select #4 (subquery in condition; dependent)
            -> Limit: 1 row(s)  (cost=4.07 rows=1) (never executed)
                -> Filter: (U1.pickup_date <= DATE'2021-07-15')  (cost=4.07 rows=37.5) (never executed)
                    -> Covering index lookup on U1 using vehicle_boo_vehicle_be74b4_idx (vehicle_id_id=vehicle_vehicle.vehicle_id)  (cost=4.07 rows=112) (never executed)
        -> Select #5 (subquery in condition; dependent)
            -> Limit: 1 row(s)  (cost=4.07 rows=1) (actual time=0.0473..0.0473 rows=1 loops=34)
                -> Filter: (U1.next_available_date > DATE'2021-07-25')  (cost=4.07 rows=37.5) (actual time=0.047..0.047 rows=1 loops=34)
                    -> Covering index lookup on U1 using vehicle_boo_vehicle_3b75a3_idx (vehicle_id_id=vehicle_vehicle.vehicle_id)  (cost=4.07 rows=112) (actual time=0.0254..0.038 rows=73.2 loops=34)
        -> Select #6 (subquery in condition; dependent)
            -> Limit: 1 row(s)  (cost=22.9 rows=1) (actual time=0.203..0.203 rows=0 loops=34)
                -> Filter: (U1.payment_status = 'C')  (cost=22.9 rows=11.2) (actual time=0.202..0.202 rows=0 loops=34)
                    -> Index lookup on U1 using vehicle_boo_vehicle_be74b4_idx (vehicle_id_id=vehicle_vehicle.vehicle_id)  (cost=22.9 rows=112) (actual time=0.151..0.193 rows=119 loops=34)
        -> Select #7 (subquery in condition; dependent)
            -> Limit: 1 row(s)  (cost=4.07 rows=1) (never executed)
                -> Filter: (U1.pickup_date <= DATE'2021-07-25')  (cost=4.07 rows=37.5) (never executed)
                    -> Covering index lookup on U1 using vehicle_boo_vehicle_be74b4_idx (vehicle_id_id=vehicle_vehicle.vehicle_id)  (cost=4.07 rows=112) (never executed)
"""
EXPLAIN ANALYZE
SELECT
vehicle_vehicle.vehicle_id
, vehicle_vehicle.location_id_id
, vehicle_vehicle.class_id_id
, vehicle_vehicle.make
, vehicle_vehicle.model
, vehicle_vehicle.vin_number
, vehicle_vehicle.license_plate_number
, vehicle_vehicle.make_year
, vehicle_vehicle.odo
, vehicle_vehicle.rating
, vehicle_vehicle.description FROM vehicle_vehicle WHERE NOT (
    (
        (
            EXISTS(
                SELECT (1) AS a FROM vehicle_booking U1 WHERE (U1.next_available_date > '2021-07-15' AND U1.vehicle_id_id = vehicle_vehicle.vehicle_id) LIMIT 1) AND EXISTS(
                SELECT (1) AS a FROM vehicle_booking U1 WHERE (U1.payment_status = 'C' AND U1.vehicle_id_id = vehicle_vehicle.vehicle_id) LIMIT 1) AND EXISTS(
                SELECT (1) AS a FROM vehicle_booking U1 WHERE (U1.pickup_date <= '2021-07-15' AND U1.vehicle_id_id = vehicle_vehicle.vehicle_id) LIMIT 1)) OR (EXISTS(
                SELECT (1) AS a FROM vehicle_booking U1 WHERE (U1.next_available_date > '2021-07-25' AND U1.vehicle_id_id = vehicle_vehicle.vehicle_id) LIMIT 1) AND EXISTS(
                SELECT (1) AS a FROM vehicle_booking U1 WHERE (U1.payment_status = 'C' AND U1.vehicle_id_id = vehicle_vehicle.vehicle_id) LIMIT 1) AND EXISTS(
                SELECT (1) AS a FROM vehicle_booking U1 WHERE (U1.pickup_date <= '2021-07-25' AND U1.vehicle_id_id = vehicle_vehicle.vehicle_id) LIMIT 1)
        )
    )
)
LIMIT 100;

-- WITHOUT INDEX
"""
-> Limit: 100 row(s)  (cost=3.65 rows=34) (actual time=4.05..115 rows=34 loops=1)
    -> Filter: ((exists(select #2) is false or exists(select #3) is false or exists(select #4) is false) and (exists(select #5) is false or exists(select #6) is false or exists(select #7) is false))  (cost=3.65 rows=34) (actual time=4.04..115 rows=34 loops=1)
        -> Table scan on vehicle_vehicle  (cost=3.65 rows=34) (actual time=0.0393..0.0704 rows=34 loops=1)
        -> Select #2 (subquery in condition; dependent)
            -> Limit: 1 row(s)  (cost=275 rows=1) (actual time=0.0567..0.0568 rows=1 loops=34)
                -> Filter: ((U1.next_available_date > DATE'2021-07-15') and (U1.vehicle_id_id = vehicle_vehicle.vehicle_id))  (cost=275 rows=127) (actual time=0.0565..0.0565 rows=1 loops=34)
                    -> Table scan on U1  (cost=275 rows=3823) (actual time=0.0273..0.0446 rows=83.2 loops=34)
        -> Select #3 (subquery in condition; dependent)
            -> Limit: 1 row(s)  (cost=355 rows=1) (actual time=1.65..1.65 rows=0 loops=34)
                -> Filter: ((U1.payment_status = 'C') and (U1.vehicle_id_id = vehicle_vehicle.vehicle_id))  (cost=355 rows=38.2) (actual time=1.65..1.65 rows=0 loops=34)
                    -> Table scan on U1  (cost=355 rows=3823) (actual time=0.0236..1.35 rows=4031 loops=34)
        -> Select #4 (subquery in condition; dependent)
            -> Limit: 1 row(s)  (cost=275 rows=1) (never executed)
                -> Filter: ((U1.pickup_date <= DATE'2021-07-15') and (U1.vehicle_id_id = vehicle_vehicle.vehicle_id))  (cost=275 rows=127) (never executed)
                    -> Table scan on U1  (cost=275 rows=3823) (never executed)
        -> Select #5 (subquery in condition; dependent)
            -> Limit: 1 row(s)  (cost=275 rows=1) (actual time=0.0522..0.0522 rows=1 loops=34)
                -> Filter: ((U1.next_available_date > DATE'2021-07-25') and (U1.vehicle_id_id = vehicle_vehicle.vehicle_id))  (cost=275 rows=127) (actual time=0.0519..0.0519 rows=1 loops=34)
                    -> Table scan on U1  (cost=275 rows=3823) (actual time=0.0238..0.0405 rows=83.4 loops=34)
        -> Select #6 (subquery in condition; dependent)
            -> Limit: 1 row(s)  (cost=355 rows=1) (actual time=1.62..1.62 rows=0 loops=34)
                -> Filter: ((U1.payment_status = 'C') and (U1.vehicle_id_id = vehicle_vehicle.vehicle_id))  (cost=355 rows=38.2) (actual time=1.62..1.62 rows=0 loops=34)
                    -> Table scan on U1  (cost=355 rows=3823) (actual time=0.0233..1.32 rows=4031 loops=34)
        -> Select #7 (subquery in condition; dependent)
            -> Limit: 1 row(s)  (cost=275 rows=1) (never executed)
                -> Filter: ((U1.pickup_date <= DATE'2021-07-25') and (U1.vehicle_id_id = vehicle_vehicle.vehicle_id))  (cost=275 rows=127) (never executed)
                    -> Table scan on U1  (cost=275 rows=3823) (never executed)
"""

EXPLAIN ANALYZE
SELECT
vehicle_vehicle.vehicle_id
, vehicle_vehicle.location_id_id
, vehicle_vehicle.class_id_id
, vehicle_vehicle.make
, vehicle_vehicle.model
, vehicle_vehicle.vin_number
, vehicle_vehicle.license_plate_number
, vehicle_vehicle.make_year
, vehicle_vehicle.odo
, vehicle_vehicle.rating
, vehicle_vehicle.description FROM vehicle_vehicle IGNORE INDEX
(
    vehicle_booking.vehicle_boo_vehicle_3b75a3_idx,
    vehicle_booking.vehicle_boo_vehicle_404ad7_idx,
    vehicle_booking.vehicle_boo_vehicle_be74b4_idx
)
WHERE NOT (
    (
        (
            EXISTS(
                SELECT (1) AS a FROM vehicle_booking U1 WHERE (U1.next_available_date > '2021-07-15' AND U1.vehicle_id_id = vehicle_vehicle.vehicle_id) LIMIT 1) AND EXISTS(
                SELECT (1) AS a FROM vehicle_booking U1 WHERE (U1.payment_status = 'C' AND U1.vehicle_id_id = vehicle_vehicle.vehicle_id) LIMIT 1) AND EXISTS(
                SELECT (1) AS a FROM vehicle_booking U1 WHERE (U1.pickup_date <= '2021-07-15' AND U1.vehicle_id_id = vehicle_vehicle.vehicle_id) LIMIT 1)) OR (EXISTS(
                SELECT (1) AS a FROM vehicle_booking U1 WHERE (U1.next_available_date > '2021-07-25' AND U1.vehicle_id_id = vehicle_vehicle.vehicle_id) LIMIT 1) AND EXISTS(
                SELECT (1) AS a FROM vehicle_booking U1 WHERE (U1.payment_status = 'C' AND U1.vehicle_id_id = vehicle_vehicle.vehicle_id) LIMIT 1) AND EXISTS(
                SELECT (1) AS a FROM vehicle_booking U1 WHERE (U1.pickup_date <= '2021-07-25' AND U1.vehicle_id_id = vehicle_vehicle.vehicle_id) LIMIT 1)
        )
    )
)
LIMIT 100;
