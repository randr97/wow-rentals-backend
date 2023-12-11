-- Note this is a django managed database and hence django also manages prefixes of tables

-- dsr_wowdb.auth_group definition

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.django_content_type definition

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.django_migrations definition

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.django_session definition

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.swimlane_corporation definition

CREATE TABLE `swimlane_corporation` (
  `corp_id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `registration_number` varchar(100) NOT NULL,
  `domain` varchar(100) NOT NULL,
  PRIMARY KEY (`corp_id`),
  KEY `swimlane_co_domain_549738_idx` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.swimlane_coupon definition

CREATE TABLE `swimlane_coupon` (
  `coupon_id` bigint NOT NULL AUTO_INCREMENT,
  `coupon_code` varchar(10) NOT NULL,
  `coupon_type` varchar(1) NOT NULL,
  `discount` decimal(5,2) NOT NULL,
  `is_valid` tinyint(1) NOT NULL,
  PRIMARY KEY (`coupon_id`),
  UNIQUE KEY `coupon_code` (`coupon_code`),
  KEY `swimlane_co_coupon__b6bd8d_idx` (`coupon_code`),
  KEY `swimlane_co_coupon__82dbcc_idx` (`coupon_id`,`coupon_code`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.users_management_user definition

CREATE TABLE `users_management_user` (
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `customer_id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `user_type` varchar(1) NOT NULL,
  `address_street` varchar(100) NOT NULL,
  `address_city` varchar(100) NOT NULL,
  `address_state` varchar(100) NOT NULL,
  `address_zipcode` varchar(100) NOT NULL,
  PRIMARY KEY (`customer_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.vehicle_officelocation definition

CREATE TABLE `vehicle_officelocation` (
  `location_id` bigint NOT NULL AUTO_INCREMENT,
  `address_street` varchar(100) NOT NULL,
  `address_city` varchar(100) NOT NULL,
  `address_state` varchar(100) NOT NULL,
  `address_zipcode` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  PRIMARY KEY (`location_id`),
  KEY `vehicle_off_address_f10625_idx` (`address_city`),
  KEY `vehicle_off_address_0e768a_idx` (`address_street`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.vehicle_vehicleclass definition

CREATE TABLE `vehicle_vehicleclass` (
  `class_id` bigint NOT NULL AUTO_INCREMENT,
  `vehicle_class` varchar(100) NOT NULL,
  `rent_charge` decimal(10,2) NOT NULL,
  `extra_charge` decimal(10,2) NOT NULL,
  PRIMARY KEY (`class_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.auth_permission definition

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.django_admin_log definition

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_users_man` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_man` FOREIGN KEY (`user_id`) REFERENCES `users_management_user` (`customer_id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.swimlane_couponcorporate definition

CREATE TABLE `swimlane_couponcorporate` (
  `coupon_id_id` bigint NOT NULL,
  `corp_id_id` bigint NOT NULL,
  PRIMARY KEY (`coupon_id_id`),
  KEY `swimlane_couponcorpo_corp_id_id_2464cda9_fk_swimlane_` (`corp_id_id`),
  CONSTRAINT `swimlane_couponcorpo_corp_id_id_2464cda9_fk_swimlane_` FOREIGN KEY (`corp_id_id`) REFERENCES `swimlane_corporation` (`corp_id`),
  CONSTRAINT `swimlane_couponcorpo_coupon_id_id_4b7804c1_fk_swimlane_` FOREIGN KEY (`coupon_id_id`) REFERENCES `swimlane_coupon` (`coupon_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.swimlane_couponindividual definition

CREATE TABLE `swimlane_couponindividual` (
  `coupon_id_id` bigint NOT NULL,
  `valid_from` date NOT NULL,
  `valid_to` date NOT NULL,
  PRIMARY KEY (`coupon_id_id`),
  CONSTRAINT `swimlane_couponindiv_coupon_id_id_36cf057f_fk_swimlane_` FOREIGN KEY (`coupon_id_id`) REFERENCES `swimlane_coupon` (`coupon_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.swimlane_customercorporate definition

CREATE TABLE `swimlane_customercorporate` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `emp_id` varchar(100) NOT NULL,
  `corp_id_id` bigint NOT NULL,
  `customer_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `customer_id_id` (`customer_id_id`),
  KEY `swimlane_customercor_corp_id_id_5a9bc9fc_fk_swimlane_` (`corp_id_id`),
  CONSTRAINT `swimlane_customercor_corp_id_id_5a9bc9fc_fk_swimlane_` FOREIGN KEY (`corp_id_id`) REFERENCES `swimlane_corporation` (`corp_id`),
  CONSTRAINT `swimlane_customercor_customer_id_id_4ad6f406_fk_users_man` FOREIGN KEY (`customer_id_id`) REFERENCES `users_management_user` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.swimlane_customerindividual definition

CREATE TABLE `swimlane_customerindividual` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `dl_number` varchar(100) NOT NULL,
  `insurance_company` varchar(100) NOT NULL,
  `insurance_policy_no` varchar(100) NOT NULL,
  `customer_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `customer_id_id` (`customer_id_id`),
  CONSTRAINT `swimlane_customerind_customer_id_id_5d0b1632_fk_users_man` FOREIGN KEY (`customer_id_id`) REFERENCES `users_management_user` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.swimlane_payment definition

CREATE TABLE `swimlane_payment` (
  `payment_id` bigint NOT NULL AUTO_INCREMENT,
  `payment_method` varchar(1) NOT NULL,
  `card_number` varchar(100) NOT NULL,
  `is_valid` tinyint(1) NOT NULL,
  `card_name` varchar(100) NOT NULL,
  `card_exp_date` date NOT NULL,
  `card_zipcode` varchar(5) NOT NULL,
  `customer_id_id` bigint NOT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `swimlane_payment_customer_id_id_e2997d01_fk_users_man` (`customer_id_id`),
  CONSTRAINT `swimlane_payment_customer_id_id_e2997d01_fk_users_man` FOREIGN KEY (`customer_id_id`) REFERENCES `users_management_user` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.users_management_user_groups definition

CREATE TABLE `users_management_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_management_user_groups_user_id_group_id_10b04da8_uniq` (`user_id`,`group_id`),
  KEY `users_management_user_groups_group_id_91f48f20_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_management_use_user_id_716c5d67_fk_users_man` FOREIGN KEY (`user_id`) REFERENCES `users_management_user` (`customer_id`),
  CONSTRAINT `users_management_user_groups_group_id_91f48f20_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.users_management_user_user_permissions definition

CREATE TABLE `users_management_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_management_user_us_user_id_permission_id_c2d870b3_uniq` (`user_id`,`permission_id`),
  KEY `users_management_use_permission_id_d224a626_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_management_use_permission_id_d224a626_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_management_use_user_id_2804ce58_fk_users_man` FOREIGN KEY (`user_id`) REFERENCES `users_management_user` (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.vehicle_vehicle definition

CREATE TABLE `vehicle_vehicle` (
  `vehicle_id` bigint NOT NULL AUTO_INCREMENT,
  `make` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  `vin_number` varchar(100) NOT NULL,
  `license_plate_number` varchar(100) NOT NULL,
  `make_year` date NOT NULL,
  `odo` decimal(10,2) NOT NULL,
  `class_id_id` bigint DEFAULT NULL,
  `location_id_id` bigint NOT NULL,
  `description` varchar(255) NOT NULL,
  `rating` int NOT NULL,
  PRIMARY KEY (`vehicle_id`),
  KEY `vehicle_vehicle_class_id_id_1d3e9c2c_fk_vehicle_v` (`class_id_id`),
  KEY `vehicle_vehicle_location_id_id_4647003e_fk_vehicle_o` (`location_id_id`),
  CONSTRAINT `vehicle_vehicle_class_id_id_1d3e9c2c_fk_vehicle_v` FOREIGN KEY (`class_id_id`) REFERENCES `vehicle_vehicleclass` (`class_id`),
  CONSTRAINT `vehicle_vehicle_location_id_id_4647003e_fk_vehicle_o` FOREIGN KEY (`location_id_id`) REFERENCES `vehicle_officelocation` (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.auth_group_permissions definition

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.vehicle_booking definition

CREATE TABLE `vehicle_booking` (
  `booking_id` bigint NOT NULL AUTO_INCREMENT,
  `pickup_date` date NOT NULL,
  `dropoff_date` date NOT NULL,
  `start_odo` decimal(10,2) DEFAULT NULL,
  `end_odo` decimal(10,2) DEFAULT NULL,
  `daily_limit` decimal(10,2) NOT NULL,
  `trip_status` varchar(1) NOT NULL,
  `next_available_date` date DEFAULT NULL,
  `payment_status` varchar(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `coupon_id_id` bigint DEFAULT NULL,
  `customer_id_id` bigint DEFAULT NULL,
  `dropoff_location_id` bigint DEFAULT NULL,
  `pickup_location_id` bigint DEFAULT NULL,
  `vehicle_id_id` bigint DEFAULT NULL,
  PRIMARY KEY (`booking_id`),
  KEY `vehicle_booking_coupon_id_id_4945ccde_fk_swimlane_` (`coupon_id_id`),
  KEY `vehicle_booking_customer_id_id_89087cc3_fk_users_man` (`customer_id_id`),
  KEY `vehicle_booking_dropoff_location_id_85632d86_fk_vehicle_o` (`dropoff_location_id`),
  KEY `vehicle_booking_pickup_location_id_627a94a6_fk_vehicle_o` (`pickup_location_id`),
  KEY `vehicle_boo_vehicle_be74b4_idx` (`vehicle_id_id`,`pickup_date`),
  KEY `vehicle_boo_vehicle_404ad7_idx` (`vehicle_id_id`,`dropoff_date`),
  KEY `vehicle_boo_vehicle_3b75a3_idx` (`vehicle_id_id`,`next_available_date`),
  CONSTRAINT `vehicle_booking_coupon_id_id_4945ccde_fk_swimlane_` FOREIGN KEY (`coupon_id_id`) REFERENCES `swimlane_coupon` (`coupon_id`),
  CONSTRAINT `vehicle_booking_customer_id_id_89087cc3_fk_users_man` FOREIGN KEY (`customer_id_id`) REFERENCES `users_management_user` (`customer_id`),
  CONSTRAINT `vehicle_booking_dropoff_location_id_85632d86_fk_vehicle_o` FOREIGN KEY (`dropoff_location_id`) REFERENCES `vehicle_officelocation` (`location_id`),
  CONSTRAINT `vehicle_booking_pickup_location_id_627a94a6_fk_vehicle_o` FOREIGN KEY (`pickup_location_id`) REFERENCES `vehicle_officelocation` (`location_id`),
  CONSTRAINT `vehicle_booking_vehicle_id_id_9344bcf4_fk_vehicle_v` FOREIGN KEY (`vehicle_id_id`) REFERENCES `vehicle_vehicle` (`vehicle_id`)
) ENGINE=InnoDB AUTO_INCREMENT=101606 DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.vehicle_booking_payment definition

CREATE TABLE `vehicle_booking_payment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `booking_id` bigint NOT NULL,
  `payment_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vehicle_booking_payment_booking_id_payment_id_1b74e49c_uniq` (`booking_id`,`payment_id`),
  KEY `vehicle_booking_paym_payment_id_75433023_fk_swimlane_` (`payment_id`),
  CONSTRAINT `vehicle_booking_paym_booking_id_2f6cf3a0_fk_vehicle_b` FOREIGN KEY (`booking_id`) REFERENCES `vehicle_booking` (`booking_id`),
  CONSTRAINT `vehicle_booking_paym_payment_id_75433023_fk_swimlane_` FOREIGN KEY (`payment_id`) REFERENCES `swimlane_payment` (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1770 DEFAULT CHARSET=utf8mb3;


-- dsr_wowdb.vehicle_invoice definition

CREATE TABLE `vehicle_invoice` (
  `invoice_id` bigint NOT NULL AUTO_INCREMENT,
  `total` decimal(10,2) NOT NULL,
  `bill_to_address` varchar(255) NOT NULL,
  `dropoff_location` varchar(255) NOT NULL,
  `ship_to_address` varchar(255) NOT NULL,
  `booking_id_id` bigint DEFAULT NULL,
  `taxes` decimal(10,2) NOT NULL,
  PRIMARY KEY (`invoice_id`),
  UNIQUE KEY `booking_id_id` (`booking_id_id`),
  CONSTRAINT `vehicle_invoice_booking_id_id_37732579_fk_vehicle_b` FOREIGN KEY (`booking_id_id`) REFERENCES `vehicle_booking` (`booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2666 DEFAULT CHARSET=utf8mb3;
