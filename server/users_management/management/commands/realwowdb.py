import random
from datetime import datetime, timedelta
from decimal import Decimal

from django.core.management.base import BaseCommand
from faker import Faker

from swimlane.models import (Corporation, Coupon, CouponCorporate,
                             CouponIndividual, CustomerCorporate,
                             CustomerIndividual, Payment)
from users_management.models import User
from vehicle.models import Booking, OfficeLocation, Vehicle, VehicleClass

from .utils import get_random_string


class Command(BaseCommand):
    help = "Adds default users"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # faker
        fake = Faker()

        # Dummy user creations
        users = [
            User(customer_id=1, is_active=True, user_type='I', first_name='Ava', last_name='Williams', email='ava.williams@hotmail.com', phone='555-1001', address_street='101 Maple Dr', address_city='Austin', address_state='TX', address_zipcode='73301'),
            User(customer_id=2, is_active=True, user_type='I', first_name='Miguel', last_name='Hernandez', email='miguel.hernandez@dailybuzz.com', phone='555-1002', address_street='202 Oak St', address_city='Miami', address_state='FL', address_zipcode='33101'),
            User(customer_id=3, is_active=True, user_type='I', first_name='Sarah', last_name='Johnson', email='sarah.johnson@outlook.com', phone='555-1003', address_street='303 Pine St', address_city='Denver', address_state='CO', address_zipcode='80201'),
            User(customer_id=4, is_active=True, user_type='I', first_name='James', last_name='Wilson', email='james.wilson@yahooinc.com', phone='555-1004', address_street='404 Birch Rd', address_city='Atlanta', address_state='GA', address_zipcode='30301'),
            User(customer_id=5, is_active=True, user_type='I', first_name='Emily', last_name='Davis', email='emily.davis@techmail.com', phone='555-1005', address_street='505 Cedar Ln', address_city='Portland', address_state='OR', address_zipcode='97201'),
            User(customer_id=6, is_active=True, user_type='I', first_name='Daniel', last_name='Martinez', email='daniel.martinez@socialhub.com', phone='555-1006', address_street='606 Oak Ave', address_city='Las Vegas', address_state='NV', address_zipcode='89101'),
            User(customer_id=7, is_active=True, user_type='I', first_name='Olivia', last_name='Brown', email='olivia.brown@livemail.com', phone='555-1007', address_street='707 Elm St', address_city='Chicago', address_state='IL', address_zipcode='60601'),
            User(customer_id=8, is_active=True, user_type='I', first_name='Lucas', last_name='Gonzalez', email='lucas.gonzalez@hotmail.com', phone='555-1008', address_street='808 Maple Ave', address_city='Phoenix', address_state='AZ', address_zipcode='85001'),
            User(customer_id=9, is_active=True, user_type='I', first_name='Sophia', last_name='Lopez', email='sophia.lopez@worldnet.com', phone='555-1009', address_street='909 Walnut St', address_city='Philadelphia', address_state='PA', address_zipcode='19101'),
            User(customer_id=10, is_active=True, user_type='I', first_name='Ethan', last_name='Taylor', email='ethan.taylor@globalnet.com', phone='555-1010', address_street='1010 Cherry Blvd', address_city='San Antonio', address_state='TX', address_zipcode='78201'),
            User(customer_id=11, is_active=True, user_type='I', first_name='Isabella', last_name='Anderson', email='isabella.anderson@hotmail.com', phone='555-1011', address_street='1111 Pine Knoll Dr', address_city='San Diego', address_state='CA', address_zipcode='92101'),
            User(customer_id=12, is_active=True, user_type='I', first_name='Matthew', last_name='Lee', email='matthew.lee@hotmail.com', phone='555-1012', address_street='1212 Oakdale Rd', address_city='Dallas', address_state='TX', address_zipcode='75201'),
            User(customer_id=13, is_active=True, user_type='I', first_name='Chloe', last_name='Kim', email='chloe.kim@webmail.com', phone='555-1013', address_street='1313 Birchfield St', address_city='San Jose', address_state='CA', address_zipcode='95101'),
            User(customer_id=14, is_active=True, user_type='I', first_name='William', last_name='Clark', email='william.clark@hotmail.com', phone='555-1014', address_street='1414 Cedar Ln', address_city='Jacksonville', address_state='FL', address_zipcode='32201'),
            User(customer_id=15, is_active=True, user_type='I', first_name='Madison', last_name='Garcia', email='madison.garcia@gmail.com', phone='555-1015', address_street='1515 Spruce St', address_city='Fort Worth', address_state='TX', address_zipcode='76101'),
            User(customer_id=16, is_active=True, user_type='I', first_name='Alexander', last_name='Rodriguez', email='alexander.rodriguez@hotmail.com', phone='555-1016', address_street='1616 Pineview Ave', address_city='Columbus', address_state='OH', address_zipcode='43201'),
            User(customer_id=17, is_active=True, user_type='I', first_name='Grace', last_name='Martinez', email='grace.martinez@hotmail.com', phone='555-1017', address_street='1717 Oakwood Dr', address_city='Charlotte', address_state='NC', address_zipcode='28201'),
            User(customer_id=18, is_active=True, user_type='I', first_name='Ryan', last_name='Hernandez', email='ryan.hernandez@hotmail.com', phone='555-1018', address_street='1818 Maplecrest Rd', address_city='Indianapolis', address_state='IN', address_zipcode='46201'),
            User(customer_id=19, is_active=True, user_type='I', first_name='Ella', last_name='Martinez', email='ella.martinez@hotmail.com', phone='555-1019', address_street='1919 Elmtree Park Dr', address_city='Austin', address_state='TX', address_zipcode='78701'),
            User(customer_id=20, is_active=True, user_type='I', first_name='Benjamin', last_name='Hernandez', email='benjamin.hernandez@hotmail.com', phone='555-1020', address_street='2020 Birchwood Ave', address_city='San Francisco', address_state='CA', address_zipcode='94101'),
            User(customer_id=21, is_active=True, user_type='C', first_name='Charlotte', last_name='Wilson', email='charlotte.wilson@netflix.com', phone='555-1021', address_street='2101 Corporate Blvd', address_city='Houston', address_state='TX', address_zipcode='77001'),
            User(customer_id=22, is_active=True, user_type='C', first_name='Oliver', last_name='Moore', email='oliver.moore@bizmail.com', phone='555-1022', address_street='2202 Business Park Dr', address_city='Chicago', address_state='IL', address_zipcode='60601'),
            User(customer_id=23, is_active=True, user_type='C', first_name='Sophie', last_name='Taylor', email='sophie.taylor@netflix.com', phone='555-1023', address_street='2303 Industrial Rd', address_city='Phoenix', address_state='AZ', address_zipcode='85001'),
            User(customer_id=24, is_active=True, user_type='C', first_name='Jack', last_name='Brown', email='jack.brown@company.com', phone='555-1024', address_street='2404 Commerce Ave', address_city='Philadelphia', address_state='PA', address_zipcode='19101'),
            User(customer_id=25, is_active=True, user_type='C', first_name='Amelia', last_name='Davis', email='amelia.davis@trade.com', phone='555-1025', address_street='2505 Market St', address_city='San Antonio', address_state='TX', address_zipcode='78201'),
            User(customer_id=26, is_active=True, user_type='C', first_name='Noah', last_name='Miller', email='noah.miller@industry.com', phone='555-1026', address_street='2606 Enterprise Ln', address_city='San Diego', address_state='CA', address_zipcode='92101'),
            User(customer_id=27, is_active=True, user_type='C', first_name='Mia', last_name='Lee', email='mia.lee@commercial.com', phone='555-1027', address_street='2707 Trade Center Way', address_city='Dallas', address_state='TX', address_zipcode='75201'),
            User(customer_id=28, is_active=True, user_type='C', first_name='Henry', last_name='Gonzalez', email='henry.gonzalez@netflix.com', phone='555-1028', address_street='2808 Capital Dr', address_city='San Jose', address_state='CA', address_zipcode='95101'),
            User(customer_id=29, is_active=True, user_type='C', first_name='Zoe', last_name='Anderson', email='zoe.anderson@profession.com', phone='555-1029', address_street='2909 Corporate Plaza', address_city='Jacksonville', address_state='FL', address_zipcode='32201'),
            User(customer_id=30, is_active=True, user_type='C', first_name='Gabriel', last_name='Martinez', email='gabriel.martinez@netflix.com', phone='555-1030', address_street='3010 Innovation Blvd', address_city='Fort Worth', address_state='TX', address_zipcode='76101'),
            User(customer_id=31, is_active=True, user_type='C', first_name='Lucy', last_name='Clark', email='lucy.clark@corporation.com', phone='555-1031', address_street='3111 Industrial Park Ave', address_city='Columbus', address_state='OH', address_zipcode='43201'),
            User(customer_id=32, is_active=True, user_type='C', first_name='Samuel', last_name='Rodriguez', email='samuel.rodriguez@businessworld.com', phone='555-1032', address_street='3222 Commerce Rd', address_city='Charlotte', address_state='NC', address_zipcode='28201'),
            User(customer_id=33, is_active=True, user_type='C', first_name='Lily', last_name='Garcia', email='lily.garcia@biznet.com', phone='555-1033', address_street='3333 Corporate Circle', address_city='Indianapolis', address_state='IN', address_zipcode='46201'),
            User(customer_id=34, is_active=True, user_type='C', first_name='David', last_name='Martinez', email='david.martinez@netflix.com', phone='555-1034', address_street='3444 Business Way', address_city='Austin', address_state='TX', address_zipcode='78701'),
            User(customer_id=35, is_active=True, user_type='C', first_name='Evelyn', last_name='Wilson', email='evelyn.wilson@tradecorp.com', phone='555-1035', address_street='3555 Entrepreneur Ave', address_city='San Francisco', address_state='CA', address_zipcode='94101'),
            User(customer_id=36, is_active=True, user_type='C', first_name='Joseph', last_name='Anderson', email='joseph.anderson@commercenet.com', phone='555-1036', address_street='3666 Market Place Blvd', address_city='Houston', address_state='TX', address_zipcode='77001'),
            User(customer_id=37, is_active=True, user_type='C', first_name='Abigail', last_name='Thomas', email='abigail.thomas@bizhub.com', phone='555-1037', address_street='3777 Capital City Ln', address_city='Chicago', address_state='IL', address_zipcode='60601'),
            User(customer_id=38, is_active=True, user_type='C', first_name='Michael', last_name='Brown', email='michael.brown@enterprisehub.com', phone='555-1038', address_street='3888 Innovation Dr', address_city='Phoenix', address_state='AZ', address_zipcode='85001'),
            User(customer_id=39, is_active=True, user_type='C', first_name='Anna', last_name='Davis', email='anna.davis@corpbiz.com', phone='555-1039', address_street='3999 Business Park Dr', address_city='Philadelphia', address_state='PA', address_zipcode='19101'),
            User(customer_id=40, is_active=True, user_type='C', first_name='Christopher', last_name='Garcia', email='christopher.garcia@industrialnet.com', phone='555-1040', address_street='4000 Commerce Ct', address_city='San Antonio', address_state='TX', address_zipcode='78201'),
        ]
        for u in users:
            u.save()

        admin = {
                    "customer_id": 47,
                    "email": "admin@gmail.com",
                    "phone": "7325229576",
                    "first_name": "admin",
                    "last_name": "admin",
                    "password": "password",
                    "address_street": "544 Bay-ridge Pkwy",
                    "address_city": "Brooklyn",
                    "address_state": "NY",
                    "address_zipcode": "11209",
                    "user_type": "I",
                }

        u = User(is_superuser=True, is_staff=True, **admin)
        u.set_password(admin['password'])
        u.save()

        corps = [
            Corporation(corp_id=1, name='NextGen Innovations Inc.', registration_number='NGI123456', domain='nextgeninnovations.com'),
            Corporation(corp_id=2, name='American Global Logistics LLC', registration_number='AGL7890', domain='americangloballogistics.com'),
            Corporation(corp_id=3, name='United Financial Group Ltd.', registration_number='UFGABCDE', domain='unitedfinancialgroup.com'),
            Corporation(corp_id=4, name='HealthFirst Providers LLC', registration_number='HFP123', domain='healthfirstproviders.com'),
            Corporation(corp_id=5, name='EcoEnergy Dynamics Inc.', registration_number='EEDXYZ789', domain='ecoenergydynamics.com'),
            Corporation(corp_id=6, name='TechFrontier Innovations Corp.', registration_number='TFI123457', domain='techfrontierinnovations.com'),
            Corporation(corp_id=7, name='Continental Logistics Solutions LLC', registration_number='CLS7891', domain='continentallogistics.com'),
            Corporation(corp_id=8, name='Capital Finance Advisors Ltd.', registration_number='CFAABCDF', domain='capitalfinanceadvisors.com'),
            Corporation(corp_id=9, name='Total Healthcare Services LLC', registration_number='THS123', domain='totalhealthcareservices.com'),
            Corporation(corp_id=10, name='Dynamic Energy Systems Corp.', registration_number='DESXYZ790', domain='dynamicenergysystems.com'),
            Corporation(corp_id=11, name='Innovation Tech Works Inc.', registration_number='ITW123458', domain='innovationtechworks.com'),
            Corporation(corp_id=12, name='Nationwide Logistics Group LLC', registration_number='NLG7892', domain='nationwidelogisticsgroup.com'),
            Corporation(corp_id=13, name='Secure Finance Management Ltd.', registration_number='SFMABCDG', domain='securefinancemanagement.com'),
            Corporation(corp_id=14, name='Primary Health Providers LLC', registration_number='PHP123', domain='primaryhealthproviders.com'),
            Corporation(corp_id=15, name='Renewable Energy Dynamics Corp.', registration_number='REDXYZ791', domain='renewableenergydynamics.com'),

        ]
        for c in corps:
            c.save()

        cust_corp = [
            CustomerCorporate(customer_id=User.objects.get(pk=24), emp_id='EMP024', corp_id=Corporation.objects.get(pk=1)),
            CustomerCorporate(customer_id=User.objects.get(pk=25), emp_id='EMP025', corp_id=Corporation.objects.get(pk=2)),
            CustomerCorporate(customer_id=User.objects.get(pk=26), emp_id='EMP026', corp_id=Corporation.objects.get(pk=3)),
            CustomerCorporate(customer_id=User.objects.get(pk=27), emp_id='EMP027', corp_id=Corporation.objects.get(pk=4)),
            CustomerCorporate(customer_id=User.objects.get(pk=28), emp_id='EMP028', corp_id=Corporation.objects.get(pk=5)),
            CustomerCorporate(customer_id=User.objects.get(pk=29), emp_id='EMP029', corp_id=Corporation.objects.get(pk=6)),
            CustomerCorporate(customer_id=User.objects.get(pk=30), emp_id='EMP030', corp_id=Corporation.objects.get(pk=7)),
            CustomerCorporate(customer_id=User.objects.get(pk=31), emp_id='EMP031', corp_id=Corporation.objects.get(pk=8)),
            CustomerCorporate(customer_id=User.objects.get(pk=32), emp_id='EMP032', corp_id=Corporation.objects.get(pk=9)),
            CustomerCorporate(customer_id=User.objects.get(pk=33), emp_id='EMP033', corp_id=Corporation.objects.get(pk=10)),
            CustomerCorporate(customer_id=User.objects.get(pk=34), emp_id='EMP034', corp_id=Corporation.objects.get(pk=11)),
            CustomerCorporate(customer_id=User.objects.get(pk=35), emp_id='EMP035', corp_id=Corporation.objects.get(pk=12)),
            CustomerCorporate(customer_id=User.objects.get(pk=36), emp_id='EMP036', corp_id=Corporation.objects.get(pk=13)),
            CustomerCorporate(customer_id=User.objects.get(pk=37), emp_id='EMP037', corp_id=Corporation.objects.get(pk=14)),
            CustomerCorporate(customer_id=User.objects.get(pk=38), emp_id='EMP038', corp_id=Corporation.objects.get(pk=15)),
            CustomerCorporate(customer_id=User.objects.get(pk=39), emp_id='EMP039', corp_id=Corporation.objects.get(pk=1)),
            CustomerCorporate(customer_id=User.objects.get(pk=40), emp_id='EMP040', corp_id=Corporation.objects.get(pk=2)),
        ]
        for i, cc in enumerate(cust_corp):
            cc.pk = i + 1
            cc.save()

        cust_indv = [
            CustomerIndividual(customer_id=User.objects.get(pk=1), dl_number='DL1234561', insurance_company='State Farm', insurance_policy_no='POLICY1231'),
            CustomerIndividual(customer_id=User.objects.get(pk=2), dl_number='DL7890122', insurance_company='Geico', insurance_policy_no='POLICY4562'),
            CustomerIndividual(customer_id=User.objects.get(pk=3), dl_number='DL3456783', insurance_company='Allstate', insurance_policy_no='POLICY7893'),
            CustomerIndividual(customer_id=User.objects.get(pk=4), dl_number='DL9012344', insurance_company='Progressive', insurance_policy_no='POLICYABC4'),
            CustomerIndividual(customer_id=User.objects.get(pk=5), dl_number='DL5678905', insurance_company='Liberty Mutual', insurance_policy_no='POLICYDEF5'),
            CustomerIndividual(customer_id=User.objects.get(pk=6), dl_number='DL1111116', insurance_company='Farmers Insurance', insurance_policy_no='POLICY1116'),
            CustomerIndividual(customer_id=User.objects.get(pk=7), dl_number='DL3333337', insurance_company='Nationwide', insurance_policy_no='POLICY3337'),
            CustomerIndividual(customer_id=User.objects.get(pk=8), dl_number='DL5555558', insurance_company='USAA', insurance_policy_no='POLICY5558'),
            CustomerIndividual(customer_id=User.objects.get(pk=9), dl_number='DL7777779', insurance_company='Travelers', insurance_policy_no='POLICY7779'),
            CustomerIndividual(customer_id=User.objects.get(pk=10), dl_number='DL99999910', insurance_company='American Family Insurance', insurance_policy_no='POLICY99910'),
            CustomerIndividual(customer_id=User.objects.get(pk=11), dl_number='DL12345611', insurance_company='Erie Insurance', insurance_policy_no='POLICY12311'),
            CustomerIndividual(customer_id=User.objects.get(pk=12), dl_number='DL78901212', insurance_company='State Farm', insurance_policy_no='POLICY45612'),
            CustomerIndividual(customer_id=User.objects.get(pk=13), dl_number='DL34567813', insurance_company='Geico', insurance_policy_no='POLICY78913'),
            CustomerIndividual(customer_id=User.objects.get(pk=14), dl_number='DL90123414', insurance_company='Allstate', insurance_policy_no='POLICYABC14'),
            CustomerIndividual(customer_id=User.objects.get(pk=15), dl_number='DL56789015', insurance_company='Progressive', insurance_policy_no='POLICYDEF15'),
            CustomerIndividual(customer_id=User.objects.get(pk=16), dl_number='DL11111116', insurance_company='Liberty Mutual', insurance_policy_no='POLICY11116'),
            CustomerIndividual(customer_id=User.objects.get(pk=17), dl_number='DL33333317', insurance_company='Farmers Insurance', insurance_policy_no='POLICY33317'),
            CustomerIndividual(customer_id=User.objects.get(pk=18), dl_number='DL55555518', insurance_company='Nationwide', insurance_policy_no='POLICY55518'),
            CustomerIndividual(customer_id=User.objects.get(pk=19), dl_number='DL77777719', insurance_company='USAA', insurance_policy_no='POLICY77719'),
            CustomerIndividual(customer_id=User.objects.get(pk=20), dl_number='DL99999920', insurance_company='Travelers', insurance_policy_no='POLICY99920'),
        ]
        for i, ci in enumerate(cust_indv):
            ci.pk = i + 1
            ci.save()

        vehicle_class = [
            VehicleClass(vehicle_class='Sedan', rent_charge=50.00, extra_charge=5.00),
            VehicleClass(vehicle_class='SUV', rent_charge=70.00, extra_charge=7.00),
            VehicleClass(vehicle_class='Truck', rent_charge=80.00, extra_charge=8.00),
            VehicleClass(vehicle_class='Compact Car', rent_charge=45.00, extra_charge=4.50),
            VehicleClass(vehicle_class='Luxury Car', rent_charge=100.00, extra_charge=10.00),
            VehicleClass(vehicle_class='Convertible', rent_charge=85.00, extra_charge=8.50),
            VehicleClass(vehicle_class='Sports Car', rent_charge=120.00, extra_charge=12.00),
            VehicleClass(vehicle_class='Minivan', rent_charge=65.00, extra_charge=6.50),
            VehicleClass(vehicle_class='Electric Car', rent_charge=75.00, extra_charge=7.50),
            VehicleClass(vehicle_class='Hybrid', rent_charge=70.00, extra_charge=7.00),
        ]
        for i, v in enumerate(vehicle_class):
            v.pk = i + 1
            v.save()
        print('*' * 10)
        print('Created vehicle class')
        print(VehicleClass.objects.all())

        office_location = [
            OfficeLocation(address_street='350 5th Ave', address_city='New York', address_state='NY', address_zipcode='10118', phone='212-555-0300'),
            OfficeLocation(address_street='100 Legends Way', address_city='Boston', address_state='MA', address_zipcode='02114', phone='617-555-1500'),
            OfficeLocation(address_street='700 Penn St', address_city='Philadelphia', address_state='PA', address_zipcode='19130', phone='215-555-1800'),
            OfficeLocation(address_street='100 Market St', address_city='San Francisco', address_state='CA', address_zipcode='94105', phone='415-555-0100'),
            # OfficeLocation(address_street='233 S Wacker Dr', address_city='Chicago', address_state='IL', address_zipcode='60606', phone='312-555-0200'),
            # OfficeLocation(address_street='600 Congress Ave', address_city='Austin', address_state='TX', address_zipcode='78701', phone='512-555-0400'),
            # OfficeLocation(address_street='400 Broad St', address_city='Seattle', address_state='WA', address_zipcode='98109', phone='206-555-0500'),
            # OfficeLocation(address_street='1300 Pennsylvania Ave NW', address_city='Washington', address_state='DC', address_zipcode='20004', phone='202-555-0600'),
            # OfficeLocation(address_street='150 2nd Ave N', address_city='Nashville', address_state='TN', address_zipcode='37201', phone='615-555-0700'),
            # OfficeLocation(address_street='601 Biscayne Blvd', address_city='Miami', address_state='FL', address_zipcode='33132', phone='305-555-0800'),
            # OfficeLocation(address_street='100 Universal City Plaza', address_city='Los Angeles', address_state='CA', address_zipcode='91608', phone='818-555-0900'),
            # OfficeLocation(address_street='4200 Conroy Rd', address_city='Orlando', address_state='FL', address_zipcode='32839', phone='407-555-1000'),
            # OfficeLocation(address_street='800 Bagby St', address_city='Houston', address_state='TX', address_zipcode='77002', phone='713-555-1100'),
            # OfficeLocation(address_street='45 Ivan Allen Jr Blvd NW', address_city='Atlanta', address_state='GA', address_zipcode='30308', phone='404-555-1200'),
            # OfficeLocation(address_street='1 Cardinals Dr', address_city='Glendale', address_state='AZ', address_zipcode='85305', phone='623-555-1300'),
            # OfficeLocation(address_street='800 Elysian Park Ave', address_city='Los Angeles', address_state='CA', address_zipcode='90012', phone='213-555-1400'),
            # OfficeLocation(address_street='401 Biscayne Blvd', address_city='Miami', address_state='FL', address_zipcode='33132', phone='305-555-1600'),
            # OfficeLocation(address_street='1510 Polk St', address_city='Houston', address_state='TX', address_zipcode='77002', phone='713-555-1700'),
            # OfficeLocation(address_street='2655 Richmond Ave', address_city='Staten Island', address_state='NY', address_zipcode='10314', phone='718-555-1900'),
            # OfficeLocation(address_street='333 W Camden St', address_city='Baltimore', address_state='MD', address_zipcode='21201', phone='410-555-2000'),
            # OfficeLocation(address_street='501 Crawford St', address_city='Houston', address_state='TX', address_zipcode='77002', phone='713-555-2100'),
            # OfficeLocation(address_street='1500 Sugar Bowl Dr', address_city='New Orleans', address_state='LA', address_zipcode='70112', phone='504-555-2200'),
            # OfficeLocation(address_street='1265 Lombardi Ave', address_city='Green Bay', address_state='WI', address_zipcode='54304', phone='920-555-2300'),
            # OfficeLocation(address_street='1 Titans Way', address_city='Nashville', address_state='TN', address_zipcode='37213', phone='615-555-2400'),
        ]
        for i, ol in enumerate(office_location):
            ol.pk = i + 1
            ol.save()

        print('*' * 10)
        print('Created office location')
        print(OfficeLocation.objects.all())

        coupon = [
            Coupon(coupon_type='C', discount=25.00),
            Coupon(coupon_type='C', discount=30.00),
            Coupon(coupon_type='C', discount=35.00),
            Coupon(coupon_type='C', discount=40.00),
            Coupon(coupon_type='C', discount=45.00),
            Coupon(coupon_type='C', discount=50.00),
            Coupon(coupon_type='C', discount=55.00),
            Coupon(coupon_type='C', discount=60.00),
            Coupon(coupon_type='C', discount=65.00),
            Coupon(coupon_type='C', discount=70.00),
            Coupon(coupon_type='C', discount=75.00),
            Coupon(coupon_type='C', discount=80.00),
            Coupon(coupon_type='C', discount=85.00),
            Coupon(coupon_type='C', discount=90.00),
            Coupon(coupon_type='C', discount=95.00),
            Coupon(coupon_type='I', discount=5.00),
            Coupon(coupon_type='I', discount=10.00),
            Coupon(coupon_type='I', discount=15.00),
            Coupon(coupon_type='I', discount=5.00),
            Coupon(coupon_type='I', discount=10.00),
            Coupon(coupon_type='I', discount=15.00),
            Coupon(coupon_type='I', discount=5.00),
            Coupon(coupon_type='I', discount=10.00),
            Coupon(coupon_type='I', discount=15.00),
            Coupon(coupon_type='I', discount=20.00),
        ]
        for i, c in enumerate(coupon):
            c.pk = i + 1
            c.is_valid = True
            c.coupon_code = get_random_string(5).upper()
            c.save()

        vehicles = [
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Toyota-Camry.jpg', make='Toyota', model='Camry', make_year='2017-05-12', vin_number='VIN1CAMRY', license_plate_number='CAM1234', description="The Toyota Camry is a reliable and popular midsize sedan known for its comfortable ride, spacious interior, and fuel efficiency. It features modern technology and safety features, making it a practical choice for daily commuting.", class_id=VehicleClass.objects.get(vehicle_class="Sedan")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Honda-CRV.jpg', make='Honda', model='CRV', make_year='2013-08-19', vin_number='VIN2CRV', license_plate_number='CRV5678', description="The Honda CRV is a versatile and compact SUV that combines fuel efficiency with a spacious interior. It's known for its smooth ride, practical features, and advanced safety technologies, making it an ideal choice for families and adventurers.", class_id=VehicleClass.objects.get(vehicle_class="SUV")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Ford-F-150.jpg', make='Ford', model='F-150', make_year='2015-04-23', vin_number='VIN3F150', license_plate_number='F150123', description="The Ford F-150 is a rugged and powerful full-size pickup truck, recognized for its towing capacity, durability, and innovative features. It caters to both work and recreational needs, making it a top choice in the truck category.", class_id=VehicleClass.objects.get(vehicle_class="Truck")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Chevrolet-Malibu.jpg', make='Chevrolet', model='Malibu', make_year='2010-12-11', vin_number='VIN4MALIB', license_plate_number='MAL4567', description="The Chevrolet Malibu is a stylish and efficient midsize sedan offering a comfortable ride and modern technology. With a focus on fuel economy and safety features, the Malibu is a popular choice for daily commuting and family drives.", class_id=VehicleClass.objects.get(vehicle_class="Sedan")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Tesla-Model-3.jpg', make='Tesla', model='Model 3', make_year='2020-01-05', vin_number='VIN5MOD3', license_plate_number='MOD3789', description="The Tesla Model 3 is an electric car known for its cutting-edge technology, impressive acceleration, and long-range capabilities. It represents the future of electric vehicles, combining sustainability with high-performance driving.", class_id=VehicleClass.objects.get(vehicle_class="Electric Car")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Nissan-Altima.jpg', make='Nissan', model='Altima', make_year='2014-07-30', vin_number='VIN6ALTM', license_plate_number='ALT4561', description="The Nissan Altima is a well-rounded midsize sedan offering a comfortable interior, advanced safety features, and efficient performance. It appeals to those seeking a reliable and stylish sedan for everyday use.", class_id=VehicleClass.objects.get(vehicle_class="Sedan")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Subaru-Outback.jpg', make='Subaru', model='Outback', make_year='2016-09-16', vin_number='VIN7OUTB', license_plate_number='OUT7892', description="The Subaru Outback is a versatile crossover SUV with off-road capabilities and a spacious interior. Known for its rugged design, all-wheel-drive system, and practical features, the Outback is suitable for various lifestyles.", class_id=VehicleClass.objects.get(vehicle_class="SUV")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Jeep-Wrangler.jpg', make='Jeep', model='Wrangler', make_year='2018-03-21', vin_number='VIN8WRNG', license_plate_number='WRN0123', description="The Jeep Wrangler is an iconic and off-road-capable SUV with a distinctive design. Known for its ruggedness and open-air driving experience, the Wrangler is a favorite among adventure enthusiasts.", class_id=VehicleClass.objects.get(vehicle_class="SUV")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Hyundai-Sonata.jpg', make='Hyundai', model='Sonata', make_year='2011-11-29', vin_number='VIN9SONT', license_plate_number='SON4564', description="The Hyundai Sonata is a stylish and well-equipped midsize sedan offering a smooth ride, advanced technology, and safety features. It caters to those seeking a balance of comfort and modern amenities.", class_id=VehicleClass.objects.get(vehicle_class="Sedan")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/BMW-X5.jpg', make='BMW', model='X5', make_year='2019-02-14', vin_number='VIN10X5', license_plate_number='BMW7895', description="The BMW X5 is a luxury midsize SUV known for its sophisticated design, powerful performance, and high-end interior features. It combines sportiness with comfort, making it a desirable choice in the luxury SUV segment.", class_id=VehicleClass.objects.get(vehicle_class="SUV")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Mercedes-Benz-C-Class.jpg', make='Mercedes-Benz', model='C-Class', make_year='2012-06-07', vin_number='VIN11CCL', license_plate_number='MBZ1236', description="The Mercedes-Benz C-Class is a luxurious compact car known for its elegant design, premium interior, and advanced technology features. With a focus on performance and comfort, the C-Class is a symbol of sophistication.", class_id=VehicleClass.objects.get(vehicle_class="Luxury Car")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Audi-Q5.jpg', make='Audi', model='Q5', make_year='2018-10-22', vin_number='VIN12Q5', license_plate_number='AUD7897', description="The Audi Q5 is a stylish and well-crafted luxury SUV with a spacious interior and advanced tech features. Known for its smooth ride and refined design, the Q5 is a popular choice in the premium SUV category.", class_id=VehicleClass.objects.get(vehicle_class="SUV")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Kia-Sorento.jpg', make='Kia', model='Sorento', make_year='2014-03-15', vin_number='VIN13SOR', license_plate_number='KIA0128', description="The Kia Sorento is a versatile midsize SUV offering a comfortable ride, modern features, and a spacious interior. With a reputation for reliability, the Sorento appeals to families and those seeking practicality.", class_id=VehicleClass.objects.get(vehicle_class="SUV")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Mazda-CX-5.jpg', make='Mazda', model='CX-5', make_year='2016-05-21', vin_number='VIN14CX5', license_plate_number='MAZ4569', description="The Mazda CX-5 is a stylish and sporty compact SUV known for its dynamic performance and upscale interior. Combining driving enjoyment with practicality, the CX-5 is a standout in its category.", class_id=VehicleClass.objects.get(vehicle_class="SUV")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Volvo-XC90.jpg', make='Volvo', model='XC90', make_year='2011-07-08', vin_number='VIN15XC9', license_plate_number='VOL7890', description="The Volvo XC90 is a luxury midsize SUV that emphasizes safety, comfort, and Scandinavian design. With a spacious interior and advanced safety features, the XC90 caters to those seeking a premium family SUV.", class_id=VehicleClass.objects.get(vehicle_class="Luxury Car")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Jaguar-F-Pace.jpg', make='Jaguar', model='F-Pace', make_year='2017-09-28', vin_number='VIN16FPC', license_plate_number='JAG1231', description="The Jaguar F-Pace is a luxurious and performance-oriented SUV with a distinctive design and powerful engines. Combining elegance with sportiness, the F-Pace is a top choice for those seeking a premium driving experience.", class_id=VehicleClass.objects.get(vehicle_class="Luxury Car")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Lexus-RX.jpg', make='Lexus', model='RX', make_year='2015-08-17', vin_number='VIN17LEX', license_plate_number='LEX4562', description="The Lexus RX is a luxury midsize SUV known for its smooth ride, high-quality interior, and advanced safety features. With a focus on comfort and refinement, the RX stands out in the luxury SUV segment.", class_id=VehicleClass.objects.get(vehicle_class="Luxury Car")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Porsche-Cayenne.jpg', make='Porsche', model='Cayenne', make_year='2019-04-03', vin_number='VIN18CAY', license_plate_number='POR7893', description="The Porsche Cayenne is a high-performance luxury SUV with a sporty design and powerful engines. Combining luxury with driving dynamics, the Cayenne is a symbol of Porsche's commitment to sporty SUVs.", class_id=VehicleClass.objects.get(vehicle_class="Luxury Car")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Land-Rover-Discovery.jpg', make='Land Rover', model='Discovery', make_year='2012-12-20', vin_number='VIN19DIS', license_plate_number='LRV0124', description="The Land Rover Discovery is a rugged and capable midsize SUV with off-road prowess and a spacious interior. Known for its versatility, the Discovery is suitable for both urban and adventurous lifestyles.", class_id=VehicleClass.objects.get(vehicle_class="SUV")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Buick-Enclave.jpg', make='Buick', model='Enclave', make_year='2013-02-26', vin_number='VIN20ENV', license_plate_number='BUK7894', description="The Buick Enclave is a midsize luxury SUV offering a comfortable and refined ride, a spacious interior, and modern tech features. With a focus on comfort and style, the Enclave caters to those seeking a premium SUV experience.", class_id=VehicleClass.objects.get(vehicle_class="Luxury Car")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/GMC-Terrain.jpg', make='GMC', model='Terrain', make_year='2016-11-09', vin_number='VIN21TER', license_plate_number='GMC1235', description="The GMC Terrain is a compact SUV known for its bold design, practical features, and a comfortable interior. With a focus on versatility, the Terrain is suitable for various lifestyles and preferences.", class_id=VehicleClass.objects.get(vehicle_class="SUV")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Cadillac-XT5.jpg', make='Cadillac', model='XT5', make_year='2020-06-30', vin_number='VIN22XT5', license_plate_number='CAD7896', description="The Cadillac XT5 is a midsize luxury SUV with a distinctive design, premium features, and advanced safety technologies. Combining elegance with performance, the XT5 represents Cadillac's commitment to luxury.", class_id=VehicleClass.objects.get(vehicle_class="Luxury Car")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Lincoln-Navigator.jpg', make='Lincoln', model='Navigator', make_year='2011-10-13', vin_number='VIN23NAV', license_plate_number='LIN0127', description="The Lincoln Navigator is a full-size luxury SUV offering a spacious and opulent interior, advanced technology, and a smooth ride. With a focus on luxury and comfort, the Navigator stands out in its category.", class_id=VehicleClass.objects.get(vehicle_class="Luxury Car")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Infiniti-QX60.jpg', make='Infiniti', model='QX60', make_year='2014-08-22', vin_number='VIN24QX6', license_plate_number='INF4560', description="The Infiniti QX60 is a midsize luxury SUV known for its stylish design, a comfortable ride, and advanced tech features. Catering to families and those seeking a premium driving experience, the QX60 combines elegance with practicality.", class_id=VehicleClass.objects.get(vehicle_class="Luxury Car")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Dodge-Charger.jpg', make='Dodge', model='Charger', make_year='2019-03-15', vin_number='VIN25CHRG', license_plate_number='DOD2517', description="The Dodge Charger is a powerful and iconic full-size sedan with a muscular design and high-performance engines. Known for its aggressive styling and dynamic driving experience, the Charger is a symbol of American muscle cars.", class_id=VehicleClass.objects.get(vehicle_class="Sports Car")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Chevrolet-Colorado.jpg', make='Chevrolet', model='Colorado', make_year='2018-07-22', vin_number='VIN26COLR', license_plate_number='CHE2620', description="The Chevrolet Colorado is a midsize pickup truck known for its versatility, capable towing, and practical features. Whether for work or recreation, the Colorado caters to those seeking a capable and compact truck.", class_id=VehicleClass.objects.get(vehicle_class="Truck")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Ford-Focus.jpg', make='Ford', model='Focus', make_year='2017-11-30', vin_number='VIN27FOCS', license_plate_number='FOR2732', description="The Ford Focus is a compact car offering a balance of efficiency, practicality, and modern features. Known for its nimble handling and diverse model range, the Focus is a popular choice in the compact car category.", class_id=VehicleClass.objects.get(vehicle_class="Compact Car")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Lexus-ES.jpg', make='Lexus', model='ES', make_year='2016-05-19', vin_number='VIN28LEXS', license_plate_number='LEX2845', description="The Lexus ES is a midsize luxury sedan known for its smooth ride, upscale interior, and advanced technology features. Combining comfort with sophistication, the ES represents Lexus's commitment to luxury sedans.", class_id=VehicleClass.objects.get(vehicle_class="Luxury Car")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Toyota-RAV4.jpg', make='Toyota', model='RAV4', make_year='2015-02-14', vin_number='VIN29RAV4', license_plate_number='TOY2956', description="The Toyota RAV4 is a popular and reliable compact SUV known for its practicality, fuel efficiency, and versatile features. With a spacious interior and advanced safety technologies, the RAV4 is a top choice in the compact SUV segment.", class_id=VehicleClass.objects.get(vehicle_class="SUV")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Honda-Pilot.jpg', make='Honda', model='Pilot', make_year='2020-08-08', vin_number='VIN30PLT', license_plate_number='HON3069', description="The Honda Pilot is a midsize SUV offering a spacious interior, advanced safety features, and a comfortable ride. Known for its family-friendly design and reliability, the Pilot caters to those with active lifestyles.", class_id=VehicleClass.objects.get(vehicle_class="SUV")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Jeep-Cherokee.jpg', make='Jeep', model='Cherokee', make_year='2014-12-25', vin_number='VIN31CHRK', license_plate_number='JEP3170', description="The Jeep Cherokee is a compact SUV with a rugged design and off-road capabilities. Known for its versatility and iconic Jeep styling, the Cherokee appeals to those seeking both urban and adventurous driving experiences.", class_id=VehicleClass.objects.get(vehicle_class="SUV")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Nissan-Maxima.jpg', make='Nissan', model='Maxima', make_year='2013-09-10', vin_number='VIN32MAX', license_plate_number='NIS3281', description="The Nissan Maxima is a sporty and stylish full-size sedan offering a powerful V6 engine, upscale features, and a driver-focused design. Combining performance with comfort, the Maxima is a standout in the sedan category.", class_id=VehicleClass.objects.get(vehicle_class="Sedan")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Audi-A4.jpg', make='Audi', model='A4', make_year='2012-06-03', vin_number='VIN33AUD4', license_plate_number='AUD3392', description="The Audi A4 is a luxury compact sedan known for its refined design, advanced technology, and sporty performance. With a focus on driving dynamics and upscale features, the A4 is a strong contender in its class.", class_id=VehicleClass.objects.get(vehicle_class="Luxury Car")),
            Vehicle(url='https://wowdb-ui-onhsmaymgq-uc.a.run.app/static/cars/Volkswagen-Golf.jpg', make='Volkswagen', model='Golf', make_year='2011-01-17', vin_number='VIN34GLF', license_plate_number='VOL3410', description="The Volkswagen Golf is a versatile and practical compact car known for its solid build quality, efficient engines, and a well-designed interior. With various models and configurations, the Golf caters to diverse preferences.", class_id=VehicleClass.objects.get(vehicle_class="Compact Car")),
        ]
        ct = 1
        for j in range(1, 101):
            for i, v in enumerate(vehicles):
                v.pk = ct
                ct += 1
                v.rating = int(random.uniform(1.7, 5))
                # v.description = get_text_from_ai(f'{v.make}, {v.model}')
                v.odo = random.uniform(10000, 100000)
                v.location_id = OfficeLocation.objects.get(pk=int(random.uniform(1, 4)))
                # v.class_id = get_vehicle_class_from_ai(f'{v.make}, {v.model}')
                v.save()

        print('*' * 10)
        print('Created vehicles')
        print(Vehicle.objects.all())

        coupon_corp = [
            CouponCorporate(coupon_id=Coupon.objects.get(pk=1), corp_id=Corporation.objects.get(pk=1)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=2), corp_id=Corporation.objects.get(pk=2)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=3), corp_id=Corporation.objects.get(pk=3)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=4), corp_id=Corporation.objects.get(pk=4)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=5), corp_id=Corporation.objects.get(pk=5)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=6), corp_id=Corporation.objects.get(pk=6)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=7), corp_id=Corporation.objects.get(pk=7)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=8), corp_id=Corporation.objects.get(pk=8)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=9), corp_id=Corporation.objects.get(pk=9)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=10), corp_id=Corporation.objects.get(pk=10)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=11), corp_id=Corporation.objects.get(pk=11)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=12), corp_id=Corporation.objects.get(pk=12)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=13), corp_id=Corporation.objects.get(pk=13)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=14), corp_id=Corporation.objects.get(pk=14)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=15), corp_id=Corporation.objects.get(pk=15)),
        ]
        for i, cc in enumerate(coupon_corp):
            cc.save()

        coupon_inv = [
            CouponIndividual(coupon_id=Coupon.objects.get(pk=16), valid_from='2023-01-01', valid_to='2023-12-31'),
            CouponIndividual(coupon_id=Coupon.objects.get(pk=17), valid_from='2023-01-01', valid_to='2023-12-31'),
            CouponIndividual(coupon_id=Coupon.objects.get(pk=18), valid_from='2023-01-02', valid_to='2023-12-01'),
            CouponIndividual(coupon_id=Coupon.objects.get(pk=19), valid_from='2023-01-02', valid_to='2023-12-01'),
            CouponIndividual(coupon_id=Coupon.objects.get(pk=20), valid_from='2023-01-03', valid_to='2023-12-02'),
            CouponIndividual(coupon_id=Coupon.objects.get(pk=21), valid_from='2023-01-03', valid_to='2023-12-02'),
            CouponIndividual(coupon_id=Coupon.objects.get(pk=22), valid_from='2023-01-04', valid_to='2023-12-03'),
            CouponIndividual(coupon_id=Coupon.objects.get(pk=23), valid_from='2023-01-04', valid_to='2023-12-03'),
            CouponIndividual(coupon_id=Coupon.objects.get(pk=24), valid_from='2023-01-05', valid_to='2023-12-04'),
            CouponIndividual(coupon_id=Coupon.objects.get(pk=25), valid_from='2023-01-05', valid_to='2023-12-04'),
        ]
        for i, ci in enumerate(coupon_inv):
            ci.save()

        payment = [
            Payment(card_name='Ava Williams', card_zipcode='73301', payment_method='C', card_number='4532-5611-1234-7890', card_exp_date=datetime.strptime('2024-09-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=1)),
            Payment(card_name='Miguel Hernandez', card_zipcode='33101', payment_method='D', card_number='4539-4512-7890-1234', card_exp_date=datetime.strptime('2024-10-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=2)),
            Payment(card_name='Sarah Johnson', card_zipcode='80201', payment_method='C', card_number='4929-1234-5678-9012', card_exp_date=datetime.strptime('2024-12-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=3)),
            Payment(card_name='James Wilson', card_zipcode='30301', payment_method='D', card_number='4716-4123-5678-9012', card_exp_date=datetime.strptime('2023-01-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=4)),
            Payment(card_name='Emily Davis', card_zipcode='97201', payment_method='G', card_number='5291-2345-6789-0123', card_exp_date=datetime.strptime('2024-02-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=5)),
            Payment(card_name='Daniel Martinez', card_zipcode='89101', payment_method='C', card_number='6011-1234-5678-9012', card_exp_date=datetime.strptime('2024-03-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=6)),
            Payment(card_name='Olivia Brown', card_zipcode='60601', payment_method='D', card_number='3569-1234-5678-9012', card_exp_date=datetime.strptime('2024-04-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=7)),
            Payment(card_name='Lucas Gonzalez', card_zipcode='85001', payment_method='C', card_number='6011-5678-1234-9012', card_exp_date=datetime.strptime('2024-05-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=8)),
            Payment(card_name='Sophia Lopez', card_zipcode='19101', payment_method='G', card_number='3056-7890-1234-5678', card_exp_date=datetime.strptime('2024-06-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=9)),
            Payment(card_name='Ethan Taylor', card_zipcode='78201', payment_method='D', card_number='6011-9012-3456-7890', card_exp_date=datetime.strptime('2024-07-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=10)),
            Payment(card_name='Isabella Anderson', card_zipcode='92101', payment_method='C', card_number='4485-1234-5678-9101', card_exp_date=datetime.strptime('2025-08-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=11)),
            Payment(card_name='Matthew Lee', card_zipcode='75201', payment_method='D', card_number='4789-2345-6789-0123', card_exp_date=datetime.strptime('2025-07-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=12)),
            Payment(card_name='Chloe Kim', card_zipcode='95101', payment_method='C', card_number='5241-3456-7890-1234', card_exp_date=datetime.strptime('2025-06-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=13)),
            Payment(card_name='William Clark', card_zipcode='32201', payment_method='G', card_number='3569-4567-8901-2345', card_exp_date=datetime.strptime('2025-05-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=14)),
            Payment(card_name='Madison Garcia', card_zipcode='76101', payment_method='D', card_number='6011-5678-9012-3456', card_exp_date=datetime.strptime('2025-04-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=15)),
            Payment(card_name='Alexander Rodriguez', card_zipcode='43201', payment_method='C', card_number='4532-6789-0123-4567', card_exp_date=datetime.strptime('2025-03-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=16)),
            Payment(card_name='Grace Martinez', card_zipcode='28201', payment_method='G', card_number='4716-7890-1234-5678', card_exp_date=datetime.strptime('2025-02-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=17)),
            Payment(card_name='Ryan Hernandez', card_zipcode='46201', payment_method='D', card_number='4929-8901-2345-6789', card_exp_date=datetime.strptime('2025-01-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=18)),
            Payment(card_name='Ella Martinez', card_zipcode='78701', payment_method='C', card_number='4539-0123-4567-8901', card_exp_date=datetime.strptime('2024-12-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=19)),
            Payment(card_name='Benjamin Hernandez', card_zipcode='94101', payment_method='D', card_number='4716-2345-6789-0123', card_exp_date=datetime.strptime('2024-11-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=20)),
            Payment(card_name='Charlotte Wilson', card_zipcode='77001', payment_method='D', card_number='4123-4567-8901-2345', card_exp_date=datetime.strptime('2025-10-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=21)),
            Payment(card_name='Oliver Moore', card_zipcode='60601', payment_method='G', card_number='3782-7890-1234-5678', card_exp_date=datetime.strptime('2025-09-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=22)),
            Payment(card_name='Sophie Taylor', card_zipcode='85001', payment_method='C', card_number='6014-8901-2345-6789', card_exp_date=datetime.strptime('2025-08-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=23)),
            Payment(card_name='Jack Brown', card_zipcode='19101', payment_method='D', card_number='4532-0123-4567-8901', card_exp_date=datetime.strptime('2025-07-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=24)),
            Payment(card_name='Amelia Davis', card_zipcode='78201', payment_method='G', card_number='4716-2345-6789-0123', card_exp_date=datetime.strptime('2025-06-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=25)),
            Payment(card_name='Noah Miller', card_zipcode='92101', payment_method='C', card_number='4929-4567-8901-2345', card_exp_date=datetime.strptime('2025-05-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=26)),
            Payment(card_name='Mia Lee', card_zipcode='75201', payment_method='D', card_number='4539-6789-0123-4567', card_exp_date=datetime.strptime('2025-04-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=27)),
            Payment(card_name='Henry Gonzalez', card_zipcode='95101', payment_method='G', card_number='4123-8901-2345-6789', card_exp_date=datetime.strptime('2025-03-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=28)),
            Payment(card_name='Zoe Anderson', card_zipcode='32201', payment_method='C', card_number='3782-0123-4567-8901', card_exp_date=datetime.strptime('2025-02-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=29)),
            Payment(card_name='Gabriel Martinez', card_zipcode='76101', payment_method='D', card_number='6014-2345-6789-0123', card_exp_date=datetime.strptime('2025-01-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=30)),
        ]
        for i, p in enumerate(payment):
            p.pk = i + 1
            p.save()

        vehicles = [v.pk for v in Vehicle.objects.all()]
        offices = [o.pk for o in OfficeLocation.objects.all()]
        users = []
        for u in User.objects.all():
            if Payment.objects.filter(customer_id=u.customer_id).exists():
                users.append(u.pk)
        # corp_coupon = [c.pk for c in CouponCorporate.objects.all()]
        inv_coupon = [c.pk for c in CouponIndividual.objects.filter(valid_to__gt=datetime.now())]

        for i in range(5000):
            print(i)
            v = Vehicle.objects.get(pk=random.choice(vehicles))
            b = Booking(
                pk=i + 100000,
                pickup_date=fake.date_between_dates(date_start=datetime(2020, 1, 1), date_end=datetime(2023, 10, 1)),
                pickup_location=v.location_id,
                dropoff_location=OfficeLocation.objects.get(pk=random.choice([v.location_id.pk] * 10 + offices)),
                start_odo=v.odo,
                end_odo=v.odo + Decimal(random.uniform(100, 1000)),
                daily_limit=100,
                trip_status='O',
                customer_id=User.objects.get(pk=random.choice(users)),
                vehicle_id=v,
                coupon_id=None,
            )
            if b.customer_id.user_type == 'C':
                b.coupon_id = None
            else:
                b.coupon_id = Coupon.objects.get(pk=random.choice(inv_coupon))
            b.dropoff_date = b.pickup_date + timedelta(days=int(random.uniform(1, 9)))
            b.save()
            b.payment.set(Payment.objects.filter(customer_id=b.customer_id.pk))
            b.trip_status = 'C'
            b.save()

        self.stdout.write(
            self.style.SUCCESS('Booking bulk created')
        )
