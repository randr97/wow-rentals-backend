import random
from datetime import datetime
from django.core.management.base import BaseCommand

from swimlane.models import Corporation, CustomerCorporate, CustomerIndividual, Coupon, CouponCorporate, CouponIndividual, Payment
from users_management.models import User
from vehicle.models import OfficeLocation, Vehicle, VehicleClass


class Command(BaseCommand):
    help = "Adds default users"

    def add_arguments(self, parser):
        # parser.add_argument("poll_ids", nargs="+", type=int)
        pass

    def handle(self, *args, **options):
        # Dummy user creations
        users = [
            User(customer_id=1, is_active=True, user_type='I', first_name='John', last_name='Doe', email='john.doe@example.com', phone='555-1234', address_street='123 Main St', address_city='Anytown', address_state='CA', address_zipcode='12345'),
            User(customer_id=2, is_active=True, user_type='I', first_name='Alice', last_name='Smith', email='alice.smith@example.com', phone='555-9876', address_street='789 Oak St', address_city='Nowhere', address_state='TX', address_zipcode='98765'),
            User(customer_id=3, is_active=True, user_type='I', first_name='Eva', last_name='Miller', email='eva.miller@example.com', phone='555-1357', address_street='987 Maple St', address_city='Nowhere', address_state='TX', address_zipcode='75309'),
            User(customer_id=4, is_active=True, user_type='I', first_name='Charlie', last_name='Brown', email='charlie.brown@example.com', phone='555-5678', address_street='741 Birch St', address_city='Anytown', address_state='CA', address_zipcode='95124'),
            User(customer_id=5, is_active=True, user_type='I', first_name='Grace', last_name='Taylor', email='grace.taylor@example.com', phone='555-9876', address_street='963 Oak St', address_city='Nowhere', address_state='TX', address_zipcode='15973'),
            User(customer_id=6, is_active=True, user_type='I', first_name='David', last_name='Jones', email='david.jones@example.com', phone='555-8642', address_street='147 Walnut St', address_city='Anytown', address_state='CA', address_zipcode='25836'),
            User(customer_id=7, is_active=True, user_type='I', first_name='Sophie', last_name='White', email='sophie.white@example.com', phone='555-8790', address_street='582 Cedar St', address_city='Nowhere', address_state='TX', address_zipcode='47102'),
            User(customer_id=8, is_active=True, user_type='I', first_name='Michael', last_name='Johnson', email='michael.johnson@example.com', phone='555-2468', address_street='369 Pine St', address_city='Anytown', address_state='CA', address_zipcode='36914'),
            User(customer_id=9, is_active=True, user_type='I', first_name='Emma', last_name='Brown', email='emma.brown@example.com', phone='555-9876', address_street='654 Elm St', address_city='Nowhere', address_state='TX', address_zipcode='85203'),
            User(customer_id=10, is_active=True, user_type='I', first_name='Oliver', last_name='Clark', email='oliver.clark@example.com', phone='555-7531', address_street='951 Oak St', address_city='Nowhere', address_state='TX', address_zipcode='14785'),
            User(customer_id=11, is_active=True, user_type='I', first_name='Sophia', last_name='Davis', email='sophia.davis@example.com', phone='555-3698', address_street='258 Maple St', address_city='Anytown', address_state='CA', address_zipcode='63214'),
            User(customer_id=12, is_active=True, user_type='I', first_name='Jack', last_name='Hall', email='jack.hall@example.com', phone='555-9876', address_street='753 Birch St', address_city='Nowhere', address_state='TX', address_zipcode='95136'),
            User(customer_id=13, is_active=True, user_type='I', first_name='Isabella', last_name='Moore', email='isabella.moore@example.com', phone='555-1478', address_street='147 Cedar St', address_city='Anytown', address_state='CA', address_zipcode='75321'),
            User(customer_id=14, is_active=True, user_type='I', first_name='William', last_name='King', email='william.king@example.com', phone='555-9876', address_street='369 Oak St', address_city='Nowhere', address_state='TX', address_zipcode='36587'),
            User(customer_id=15, is_active=True, user_type='I', first_name='Ava', last_name='Martin', email='ava.martin@example.com', phone='555-8520', address_street='852 Pine St', address_city='Anytown', address_state='CA', address_zipcode='14785'),
            User(customer_id=16, is_active=True, user_type='I', first_name='Mia', last_name='Taylor', email='mia.taylor@example.com', phone='555-9876', address_street='147 Maple St', address_city='Nowhere', address_state='TX', address_zipcode='63214'),
            User(customer_id=17, is_active=True, user_type='I', first_name='James', last_name='Smith', email='james.smith@example.com', phone='555-9632', address_street='632 Oak St', address_city='Nowhere', address_state='TX', address_zipcode='95136'),
            User(customer_id=18, is_active=True, user_type='I', first_name='Charlotte', last_name='Brown', email='charlotte.brown@example.com', phone='555-3214', address_street='369 Elm St', address_city='Anytown', address_state='CA', address_zipcode='36587'),
            User(customer_id=19, is_active=True, user_type='I', first_name='Benjamin', last_name='Miller', email='benjamin.miller@example.com', phone='555-9876', address_street='147 Birch St', address_city='Nowhere', address_state='TX', address_zipcode='14785'),
            User(customer_id=20, is_active=True, user_type='I', first_name='Amelia', last_name='Johnson', email='amelia.johnson@example.com', phone='555-4567', address_street='753 Cedar St', address_city='Anytown', address_state='CA', address_zipcode='63214'),
            User(customer_id=21, is_active=True, user_type='I', first_name='Ethan', last_name='White', email='ethan.white@example.com', phone='555-9876', address_street='147 Pine St', address_city='Nowhere', address_state='TX', address_zipcode='36587'),
            User(customer_id=22, is_active=True, user_type='I', first_name='Liam', last_name='Jones', email='liam.jones@example.com', phone='555-8741', address_street='369 Maple St', address_city='Anytown', address_state='CA', address_zipcode='14785'),
            User(customer_id=23, is_active=True, user_type='I', first_name='Aria', last_name='Smith', email='aria.smith@example.com', phone='555-9876', address_street='632 Birch St', address_city='Nowhere', address_state='TX', address_zipcode='63214'),
            User(customer_id=24, is_active=True, user_type='C', first_name='Harper', last_name='Taylor', email='harper.taylor@example.com', phone='555-3698', address_street='147 Cedar St', address_city='Anytown', address_state='CA', address_zipcode='36587'),
            User(customer_id=25, is_active=True, user_type='C', first_name='Sebastian', last_name='Brown', email='sebastian.brown@example.com', phone='555-9876', address_street='753 Oak St', address_city='Nowhere', address_state='TX', address_zipcode='14785'),
            User(customer_id=26, is_active=True, user_type='C', first_name='Luna', last_name='Clark', email='luna.clark@example.com', phone='555-6321', address_street='369 Pine St', address_city='Anytown', address_state='CA', address_zipcode='63214'),
            User(customer_id=27, is_active=True, user_type='C', first_name='Jackson', last_name='King', email='jackson.king@example.com', phone='555-9876', address_street='147 Elm St', address_city='Nowhere', address_state='TX', address_zipcode='36587'),
            User(customer_id=28, is_active=True, user_type='C', first_name='Madison', last_name='Martin', email='madison.martin@example.com', phone='555-9876', address_street='632 Oak St', address_city='Anytown', address_state='CA', address_zipcode='14785'),
            User(customer_id=29, is_active=True, user_type='C', first_name='Grayson', last_name='Johnson', email='grayson.johnson@example.com', phone='555-1478', address_street='369 Cedar St', address_city='Nowhere', address_state='TX', address_zipcode='63214'),
            User(customer_id=30, is_active=True, user_type='C', first_name='Ella', last_name='Moore', email='ella.moore@example.com', phone='555-9876', address_street='147 Pine St', address_city='Anytown', address_state='CA', address_zipcode='36587'),
            User(customer_id=31, is_active=True, user_type='C', first_name='Aiden', last_name='Hall', email='aiden.hall@example.com', phone='555-8520', address_street='632 Maple St', address_city='Nowhere', address_state='TX', address_zipcode='14785'),
            User(customer_id=32, is_active=True, user_type='C', first_name='Scarlett', last_name='Davis', email='scarlett.davis@example.com', phone='555-9876', address_street='369 Birch St', address_city='Anytown', address_state='CA', address_zipcode='63214'),
            User(customer_id=33, is_active=True, user_type='C', first_name='Lucas', last_name='White', email='lucas.white@example.com', phone='555-9632', address_street='147 Cedar St', address_city='Nowhere', address_state='TX', address_zipcode='36587'),
            User(customer_id=34, is_active=True, user_type='C', first_name='Chloe', last_name='Smith', email='chloe.smith@example.com', phone='555-9876', address_street='632 Oak St', address_city='Anytown', address_state='CA', address_zipcode='14785'),
            User(customer_id=35, is_active=True, user_type='C', first_name='Carter', last_name='Brown', email='carter.brown@example.com', phone='555-3214', address_street='369 Pine St', address_city='Nowhere', address_state='TX', address_zipcode='63214'),
            User(customer_id=36, is_active=True, user_type='C', first_name='Penelope', last_name='Miller', email='penelope.miller@example.com', phone='555-9876', address_street='147 Elm St', address_city='Anytown', address_state='CA', address_zipcode='36587'),
            User(customer_id=37, is_active=True, user_type='C', first_name='Daniel', last_name='Johnson', email='daniel.johnson@example.com', phone='555-8741', address_street='632 Cedar St', address_city='Nowhere', address_state='TX', address_zipcode='14785'),
            User(customer_id=38, is_active=True, user_type='C', first_name='Madelyn', last_name='Taylor', email='madelyn.taylor@example.com', phone='555-9876', address_street='369 Oak St', address_city='Anytown', address_state='CA', address_zipcode='63214'),
            User(customer_id=39, is_active=True, user_type='C', first_name='Logan', last_name='Clark', email='logan.clark@example.com', phone='555-3698', address_street='147 Birch St', address_city='Nowhere', address_state='TX', address_zipcode='36587'),
            User(customer_id=40, is_active=True, user_type='C', first_name='Riley', last_name='King', email='riley.king@example.com', phone='555-9876', address_street='632 Maple St', address_city='Anytown', address_state='CA', address_zipcode='14785'),
            User(customer_id=41, is_active=True, user_type='C', first_name='Evelyn', last_name='Martin', email='evelyn.martin@example.com', phone='555-6321', address_street='369 Cedar St', address_city='Nowhere', address_state='TX', address_zipcode='63214'),
            User(customer_id=42, is_active=True, user_type='C', first_name='Mason', last_name='Moore', email='mason.moore@example.com', phone='555-9876', address_street='147 Pine St', address_city='Anytown', address_state='CA', address_zipcode='36587'),
            User(customer_id=43, is_active=True, user_type='C', first_name='Eleanor', last_name='Hall', email='eleanor.hall@example.com', phone='555-8520', address_street='632 Oak St', address_city='Nowhere', address_state='TX', address_zipcode='14785'),
            User(customer_id=44, is_active=True, user_type='C', first_name='Ian', last_name='Davis', email='ian.davis@example.com', phone='555-9876', address_street='369 Elm St', address_city='Anytown', address_state='CA', address_zipcode='63214'),
            User(customer_id=45, is_active=True, user_type='C', first_name='Zoe', last_name='White', email='zoe.white@example.com', phone='555-9632', address_street='147 Cedar St', address_city='Nowhere', address_state='TX', address_zipcode='36587'),
            User(customer_id=46, is_active=True, user_type='C', first_name='Nathan', last_name='Smith', email='nathan.smith@example.com', phone='555-9876', address_street='632 Birch St', address_city='Anytown', address_state='CA', address_zipcode='14785'),
            User(customer_id=47, is_active=True, user_type='C', first_name='Aubrey', last_name='Brown', email='aubrey.brown@example.com', phone='555-3214', address_street='369 Pine St', address_city='Nowhere', address_state='TX', address_zipcode='63214'),
        ]
        for u in users:
            u.save()

        # Admin user creation
        admin = {
            "customer_id": 47,
            "email": "admin@gmail.com",
            "phone": "7325229576",
            "first_name": "Rohit",
            "last_name": "Shrothrium Srinath",
            "password": "password",
            "address_street": "544 Bayridge Pkwy",
            "address_city": "Brooklyn",
            "address_state": "NY",
            "address_zipcode": "11209"
        }

        u = User(is_superuser=True, is_staff=True, **admin)
        u.set_password(admin['password'])
        u.save()

        # Create corporation
        corps = [
            Corporation(corp_id=1, name='Tech Innovations Inc.', registration_number='Tech123456', domain='example.com'),
            Corporation(corp_id=2, name='Global Logistics Co.', registration_number='Logistics7890', domain='example.com'),
            Corporation(corp_id=3, name='Finance Solutions Ltd.', registration_number='FinanceABCDE', domain='example.com'),
            Corporation(corp_id=4, name='HealthCare Providers LLC', registration_number='HealthCare123', domain='example.com'),
            Corporation(corp_id=5, name='Energy Dynamics Corp.', registration_number='EnergyXYZ789', domain='example.com'),
            Corporation(corp_id=6, name='Tech Innovations Inc. 2', registration_number='Tech123457', domain='example.com'),
            Corporation(corp_id=7, name='Global Logistics Co. 2', registration_number='Logistics7891', domain='example.com'),
            Corporation(corp_id=8, name='Finance Solutions Ltd. 2', registration_number='FinanceABCDF', domain='example.com'),
            Corporation(corp_id=9, name='HealthCare Providers LLC 2', registration_number='HealthCare124', domain='example.com'),
            Corporation(corp_id=10, name='Energy Dynamics Corp. 2', registration_number='EnergyXYZ790', domain='example.com'),
            Corporation(corp_id=11, name='Tech Innovations Inc. 3', registration_number='Tech123458', domain='example.com'),
            Corporation(corp_id=12, name='Global Logistics Co. 3', registration_number='Logistics7892', domain='example.com'),
            Corporation(corp_id=13, name='Finance Solutions Ltd. 3', registration_number='FinanceABCDG', domain='example.com'),
            Corporation(corp_id=14, name='HealthCare Providers LLC 3', registration_number='HealthCare125', domain='example.com'),
            Corporation(corp_id=15, name='Energy Dynamics Corp. 3', registration_number='EnergyXYZ791', domain='example.com'),
            Corporation(corp_id=16, name='Infra Mart Energy Dynamics Corp. 6', registration_number='Infra-EnergyXYZ793', domain='example.com'),
            Corporation(corp_id=17, name='Adani Infra Mart Finance Solutions Ltd.', registration_number='Adani-FinanceABCDE', domain='example.com'),
            Corporation(
                corp_id=18, name='Reliance Infra Mart HealthCare Providers LLC', registration_number='Reliance-HealthCare123', domain='example.com'),
            Corporation(corp_id=19, name='Tata Infra Mart Energy Dynamics Corp. 7', registration_number='Tata-EnergyXYZ789', domain='example.com'),
            Corporation(corp_id=20, name='Infy Infra Mart Tech Innovations Inc. 2', registration_number='Infy-Tech123457', domain='example.com'),
            Corporation(
                corp_id=21, name='Google Infra Mart Global Logistics Co. 2', registration_number='Google-Logistics7891', domain='example.com'),
            Corporation(corp_id=22, name='FB Infra Mart Finance Solutions Ltd. 2', registration_number='FB-FinanceABCDF', domain='example.com'),
        ]
        for c in corps:
            c.save()

        cust_corp = [
            CustomerCorporate(customer_id=User.objects.get(pk=24), emp_id='EMP002', corp_id=Corporation.objects.get(pk=1)),
            CustomerCorporate(customer_id=User.objects.get(pk=25), emp_id='EMP004', corp_id=Corporation.objects.get(pk=1)),
            CustomerCorporate(customer_id=User.objects.get(pk=26), emp_id='EMP006', corp_id=Corporation.objects.get(pk=1)),
            CustomerCorporate(customer_id=User.objects.get(pk=27), emp_id='EMP008', corp_id=Corporation.objects.get(pk=2)),
            CustomerCorporate(customer_id=User.objects.get(pk=28), emp_id='EMP010', corp_id=Corporation.objects.get(pk=2)),
            CustomerCorporate(customer_id=User.objects.get(pk=29), emp_id='EMP012', corp_id=Corporation.objects.get(pk=2)),
            CustomerCorporate(customer_id=User.objects.get(pk=30), emp_id='EMP014', corp_id=Corporation.objects.get(pk=3)),
            CustomerCorporate(customer_id=User.objects.get(pk=31), emp_id='EMP016', corp_id=Corporation.objects.get(pk=3)),
            CustomerCorporate(customer_id=User.objects.get(pk=32), emp_id='EMP018', corp_id=Corporation.objects.get(pk=3)),
            CustomerCorporate(customer_id=User.objects.get(pk=33), emp_id='EMP020', corp_id=Corporation.objects.get(pk=4)),
            CustomerCorporate(customer_id=User.objects.get(pk=34), emp_id='EMP022', corp_id=Corporation.objects.get(pk=5)),
            CustomerCorporate(customer_id=User.objects.get(pk=35), emp_id='EMP004', corp_id=Corporation.objects.get(pk=1)),
            CustomerCorporate(customer_id=User.objects.get(pk=36), emp_id='EMP006', corp_id=Corporation.objects.get(pk=1)),
            CustomerCorporate(customer_id=User.objects.get(pk=37), emp_id='EMP008', corp_id=Corporation.objects.get(pk=2)),
            CustomerCorporate(customer_id=User.objects.get(pk=38), emp_id='EMP010', corp_id=Corporation.objects.get(pk=2)),
            CustomerCorporate(customer_id=User.objects.get(pk=39), emp_id='EMP012', corp_id=Corporation.objects.get(pk=2)),
            CustomerCorporate(customer_id=User.objects.get(pk=40), emp_id='EMP014', corp_id=Corporation.objects.get(pk=3)),
            CustomerCorporate(customer_id=User.objects.get(pk=41), emp_id='EMP016', corp_id=Corporation.objects.get(pk=3)),
            CustomerCorporate(customer_id=User.objects.get(pk=42), emp_id='EMP018', corp_id=Corporation.objects.get(pk=3)),
            CustomerCorporate(customer_id=User.objects.get(pk=43), emp_id='EMP020', corp_id=Corporation.objects.get(pk=4)),
            CustomerCorporate(customer_id=User.objects.get(pk=44), emp_id='EMP022', corp_id=Corporation.objects.get(pk=5)),
        ]
        for i, cc in enumerate(cust_corp):
            cc.pk = i + 1
            cc.save()

        cust_indv = [
            CustomerIndividual(customer_id=User.objects.get(pk=1), dl_number='DL1234561', insurance_company='ABC Insurance', insurance_policy_no='POLICY1231'),
            CustomerIndividual(customer_id=User.objects.get(pk=2), dl_number='DL7890122', insurance_company='XYZ Insurance', insurance_policy_no='POLICY4562'),
            CustomerIndividual(customer_id=User.objects.get(pk=3), dl_number='DL3456783', insurance_company='123 Insurance', insurance_policy_no='POLICY7893'),
            CustomerIndividual(customer_id=User.objects.get(pk=4), dl_number='DL9012344', insurance_company='456 Insurance', insurance_policy_no='POLICYABC4'),
            CustomerIndividual(customer_id=User.objects.get(pk=5), dl_number='DL5678905', insurance_company='789 Insurance', insurance_policy_no='POLICYDEF5'),
            CustomerIndividual(customer_id=User.objects.get(pk=6), dl_number='DL1111116', insurance_company='AAA Insurance', insurance_policy_no='POLICY1116'),
            CustomerIndividual(customer_id=User.objects.get(pk=7), dl_number='DL3333337', insurance_company='CCC Insurance', insurance_policy_no='POLICY3337'),
            CustomerIndividual(customer_id=User.objects.get(pk=8), dl_number='DL5555558', insurance_company='EEE Insurance', insurance_policy_no='POLICY5558'),
            CustomerIndividual(customer_id=User.objects.get(pk=9), dl_number='DL7777779', insurance_company='GGG Insurance', insurance_policy_no='POLICY7779'),
            CustomerIndividual(customer_id=User.objects.get(pk=10), dl_number='DL99999910', insurance_company='III Insurance', insurance_policy_no='POLICY99910'),
            CustomerIndividual(customer_id=User.objects.get(pk=11), dl_number='DL12345611', insurance_company='ABC Insurance', insurance_policy_no='POLICY12311'),
            CustomerIndividual(customer_id=User.objects.get(pk=12), dl_number='DL78901212', insurance_company='XYZ Insurance', insurance_policy_no='POLICY45612'),
            CustomerIndividual(customer_id=User.objects.get(pk=13), dl_number='DL34567813', insurance_company='123 Insurance', insurance_policy_no='POLICY78913'),
            CustomerIndividual(customer_id=User.objects.get(pk=14), dl_number='DL90123414', insurance_company='456 Insurance', insurance_policy_no='POLICYABC14'),
            CustomerIndividual(customer_id=User.objects.get(pk=15), dl_number='DL56789015', insurance_company='789 Insurance', insurance_policy_no='POLICYDEF15'),
            CustomerIndividual(customer_id=User.objects.get(pk=16), dl_number='DL11111116', insurance_company='AAA Insurance', insurance_policy_no='POLICY11116'),
            CustomerIndividual(customer_id=User.objects.get(pk=17), dl_number='DL33333317', insurance_company='CCC Insurance', insurance_policy_no='POLICY33317'),
            CustomerIndividual(customer_id=User.objects.get(pk=18), dl_number='DL55555518', insurance_company='EEE Insurance', insurance_policy_no='POLICY55518'),
            CustomerIndividual(customer_id=User.objects.get(pk=19), dl_number='DL77777719', insurance_company='GGG Insurance', insurance_policy_no='POLICY77719'),
            CustomerIndividual(customer_id=User.objects.get(pk=20), dl_number='DL99999920', insurance_company='III Insurance', insurance_policy_no='POLICY99920'),
            CustomerIndividual(customer_id=User.objects.get(pk=21), dl_number='DL12345621', insurance_company='ABC Insurance', insurance_policy_no='POLICY12321'),
            CustomerIndividual(customer_id=User.objects.get(pk=22), dl_number='DL78901222', insurance_company='XYZ Insurance', insurance_policy_no='POLICY45622'),
            CustomerIndividual(customer_id=User.objects.get(pk=23), dl_number='DL34567823', insurance_company='123 Insurance', insurance_policy_no='POLICY78923'),
        ]
        for i, ci in enumerate(cust_indv):
            ci.pk = i + 1
            ci.save()

        # create vehicle class
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

        # office location
        office_location = [
            OfficeLocation(address_street='123 Main St', address_city='Cityville', address_state='StateA', address_zipcode='12345', phone='555-111-1111'),
            OfficeLocation(address_street='456 Oak Ave', address_city='Townburg', address_state='StateB', address_zipcode='56789', phone='555-222-2222'),
            OfficeLocation(address_street='789 Pine Rd', address_city='Villagetown', address_state='StateC', address_zipcode='10111', phone='555-333-3333'),
            OfficeLocation(address_street='321 Maple Blvd', address_city='Cityopolis', address_state='StateD', address_zipcode='31415', phone='555-444-4444'),
            OfficeLocation(address_street='654 Birch Lane', address_city='Townsville', address_state='StateE', address_zipcode='92638', phone='555-555-5555'),
            OfficeLocation(address_street='987 Cedar St', address_city='Hamletville', address_state='StateF', address_zipcode='13579', phone='555-666-6666'),
            OfficeLocation(address_street='159 Redwood Ave', address_city='Ruraltown', address_state='StateG', address_zipcode='24680', phone='555-777-7777'),
            OfficeLocation(address_street='753 Elm Rd', address_city='Suburbia', address_state='StateH', address_zipcode='97531', phone='555-888-8888'),
            OfficeLocation(address_street='246 Walnut Blvd', address_city='Metropolis', address_state='StateI', address_zipcode='86420', phone='555-999-9999'),
            OfficeLocation(address_street='802 Pine Lane', address_city='Cityscape', address_state='StateJ', address_zipcode='75309', phone='555-000-0000'),
            OfficeLocation(address_street='364 Cedar St', address_city='Villageville', address_state='StateK', address_zipcode='46802', phone='555-112-2334'),
            OfficeLocation(address_street='951 Birch Ave', address_city='Hamletburg', address_state='StateL', address_zipcode='98765', phone='555-443-3221'),
            OfficeLocation(address_street='573 Maple Rd', address_city='Townsville', address_state='StateM', address_zipcode='11223', phone='555-554-4332'),
            OfficeLocation(address_street='210 Oak Blvd', address_city='Suburbopolis', address_state='StateN', address_zipcode='33445', phone='555-665-5443'),
            OfficeLocation(address_street='846 Pine Lane', address_city='Cityburg', address_state='StateO', address_zipcode='55667', phone='555-776-6554'),
            OfficeLocation(address_street='479 Elm Rd', address_city='Villagescape', address_state='StateP', address_zipcode='77889', phone='555-887-5665'),
            OfficeLocation(address_street='632 Redwood Ave', address_city='Metrotown', address_state='StateQ', address_zipcode='99000', phone='555-998-4776'),
            OfficeLocation(address_street='268 Walnut St', address_city='Ruralburg', address_state='StateR', address_zipcode='11222', phone='555-009-3887'),
            OfficeLocation(address_street='713 Cedar Ave', address_city='Cityville', address_state='StateS', address_zipcode='33444', phone='555-210-2998'),
            OfficeLocation(address_street='345 Oak Rd', address_city='Townburg', address_state='StateT', address_zipcode='55666', phone='555-321-1009'),
            OfficeLocation(address_street='908 Pine Blvd', address_city='Villagetown', address_state='StateU', address_zipcode='77888', phone='555-432-2110'),
            OfficeLocation(address_street='531 Maple Lane', address_city='Cityopolis', address_state='StateV', address_zipcode='99000', phone='555-543-3221'),
            OfficeLocation(address_street='174 Birch St', address_city='Townsville', address_state='StateW', address_zipcode='11222', phone='555-654-4332'),
            OfficeLocation(address_street='789 Redwood Ave', address_city='Villagescape', address_state='StateX', address_zipcode='33445', phone='555-765-5443'),
        ]
        for i, ol in enumerate(office_location):
            ol.pk = i + 1
            ol.save()
        print('*' * 10)
        print('Created office location')
        print(OfficeLocation.objects.all())

        # create vehicle
        vehicles = [
            Vehicle(location_id=OfficeLocation.objects.get(pk=1), class_id=VehicleClass.objects.get(pk=1), make='Toyota', model='Camry', make_year='2022-01-01', vin_number='VIN123456', license_plate_number='ABC123', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=2), class_id=VehicleClass.objects.get(pk=2), make='Honda', model='CRV', make_year='2022-01-01', vin_number='VIN789012', license_plate_number='XYZ456', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=3), class_id=VehicleClass.objects.get(pk=3), make='Ford', model='F-150', make_year='2022-01-01', vin_number='VIN345678', license_plate_number='123DEF', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=4), class_id=VehicleClass.objects.get(pk=4), make='Chevrolet', model='Malibu', make_year='2022-01-01', vin_number='VIN901234', license_plate_number='456GHI', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=5), class_id=VehicleClass.objects.get(pk=5), make='Tesla', model='Model 3', make_year='2022-01-01', vin_number='VIN567890', license_plate_number='789JKL', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=6), class_id=VehicleClass.objects.get(pk=1), make='Nissan', model='Altima', make_year='2022-01-01', vin_number='VIN012345', license_plate_number='MNO987', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=7), class_id=VehicleClass.objects.get(pk=2), make='Subaru', model='Outback', make_year='2022-01-01', vin_number='VIN678901', license_plate_number='PQR654', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=8), class_id=VehicleClass.objects.get(pk=3), make='Jeep', model='Wrangler', make_year='2022-01-01', vin_number='VIN234567', license_plate_number='STU321', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=9), class_id=VehicleClass.objects.get(pk=4), make='Hyundai', model='Sonata', make_year='2022-01-01', vin_number='VIN890123', license_plate_number='VWX987', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=10), class_id=VehicleClass.objects.get(pk=5), make='BMW', model='X5', make_year='2022-01-01', vin_number='VIN456789', license_plate_number='YZA123', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=10), class_id=VehicleClass.objects.get(pk=1), make='Mercedes-Benz', model='C-Class', make_year='2022-01-01', vin_number='VIN012345', license_plate_number='BCD456', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=20), class_id=VehicleClass.objects.get(pk=2), make='Audi', model='Q5', make_year='2022-01-01', vin_number='VIN678901', license_plate_number='EFG789', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=3), class_id=VehicleClass.objects.get(pk=3), make='Kia', model='Sorento', make_year='2022-01-01', vin_number='VIN234567', license_plate_number='HIJ012', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=4), class_id=VehicleClass.objects.get(pk=4), make='Mazda', model='CX-5', make_year='2022-01-01', vin_number='VIN890123', license_plate_number='KLM345', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=5), class_id=VehicleClass.objects.get(pk=5), make='Volvo', model='XC90', make_year='2022-01-01', vin_number='VIN456789', license_plate_number='NOP678', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=6), class_id=VehicleClass.objects.get(pk=1), make='Jaguar', model='F-Pace', make_year='2022-01-01', vin_number='VIN012345', license_plate_number='QRS901', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=7), class_id=VehicleClass.objects.get(pk=2), make='Lexus', model='RX', make_year='2022-01-01', vin_number='VIN678901', license_plate_number='TUV234', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=8), class_id=VehicleClass.objects.get(pk=3), make='Porsche', model='Cayenne', make_year='2022-01-01', vin_number='VIN234567', license_plate_number='WXY567', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=9), class_id=VehicleClass.objects.get(pk=4), make='Land Rover', model='Discovery', make_year='2022-01-01', vin_number='VIN890123', license_plate_number='ZAB890', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=20), class_id=VehicleClass.objects.get(pk=5), make='Buick', model='Enclave', make_year='2022-01-01', vin_number='VIN456789', license_plate_number='CDE123', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=1), class_id=VehicleClass.objects.get(pk=1), make='GMC', model='Terrain', make_year='2022-01-01', vin_number='VIN012345', license_plate_number='FGH456', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=20), class_id=VehicleClass.objects.get(pk=2), make='Cadillac', model='XT5', make_year='2022-01-01', vin_number='VIN678901', license_plate_number='IJK789', odo=random.uniform(27000, 100000)),
            Vehicle(location_id=OfficeLocation.objects.get(pk=3), class_id=VehicleClass.objects.get(pk=3), make='Lincoln', model='Navigator', make_year='2022-01-01', vin_number='VIN234567', license_plate_number='LMN012', odo=random.uniform(27000, 100000)),
        ]
        for i, v in enumerate(vehicles):
            v.pk = i + 1
            v.save()

        print('*' * 10)
        print('Created vehicles')
        print(Vehicle.objects.all())

        coupon = [
            Coupon(coupon_type='I', discount=10.05),
            Coupon(coupon_type='I', discount=10.1),
            Coupon(coupon_type='I', discount=10.05),
            Coupon(coupon_type='I', discount=10.1),
            Coupon(coupon_type='I', discount=20.05),
            Coupon(coupon_type='I', discount=20.1),
            Coupon(coupon_type='I', discount=20.05),
            Coupon(coupon_type='I', discount=20.1),
            Coupon(coupon_type='I', discount=20.05),
            Coupon(coupon_type='I', discount=20.1),
            Coupon(coupon_type='C', discount=20.1),
            Coupon(coupon_type='C', discount=99.99),
            Coupon(coupon_type='C', discount=30.2),
            Coupon(coupon_type='C', discount=30.1),
            Coupon(coupon_type='C', discount=30.15),
            Coupon(coupon_type='C', discount=30.2),
            Coupon(coupon_type='C', discount=40.1),
            Coupon(coupon_type='C', discount=40.15),
            Coupon(coupon_type='C', discount=40.2),
            Coupon(coupon_type='C', discount=40.1),
            Coupon(coupon_type='C', discount=40.15),
            Coupon(coupon_type='C', discount=40.2),
            Coupon(coupon_type='C', discount=40.1),
            Coupon(coupon_type='C', discount=50.15),
            Coupon(coupon_type='C', discount=70.2),
        ]
        for i, c in enumerate(coupon):
            c.pk = i + 1
            c.is_valid = True
            c.save()

        coupon_corp = [
            CouponCorporate(coupon_id=Coupon.objects.get(pk=11), corp_id=Corporation.objects.get(pk=1)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=12), corp_id=Corporation.objects.get(pk=2)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=13), corp_id=Corporation.objects.get(pk=3)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=14), corp_id=Corporation.objects.get(pk=4)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=15), corp_id=Corporation.objects.get(pk=5)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=16), corp_id=Corporation.objects.get(pk=6)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=17), corp_id=Corporation.objects.get(pk=7)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=18), corp_id=Corporation.objects.get(pk=8)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=19), corp_id=Corporation.objects.get(pk=9)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=20), corp_id=Corporation.objects.get(pk=10)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=21), corp_id=Corporation.objects.get(pk=11)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=22), corp_id=Corporation.objects.get(pk=12)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=23), corp_id=Corporation.objects.get(pk=13)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=24), corp_id=Corporation.objects.get(pk=14)),
            CouponCorporate(coupon_id=Coupon.objects.get(pk=25), corp_id=Corporation.objects.get(pk=15)),
        ]
        for i, cc in enumerate(coupon_corp):
            cc.save()

        coupon_inv = [
            CouponIndividual(coupon_id=Coupon.objects.get(pk=1), valid_from='2023-01-01', valid_to='2023-12-31'),
            CouponIndividual(coupon_id=Coupon.objects.get(pk=2), valid_from='2023-01-01', valid_to='2023-12-31'),
            CouponIndividual(coupon_id=Coupon.objects.get(pk=3), valid_from='2023-01-02', valid_to='2023-12-01'),
            CouponIndividual(coupon_id=Coupon.objects.get(pk=4), valid_from='2023-01-02', valid_to='2023-12-01'),
            CouponIndividual(coupon_id=Coupon.objects.get(pk=5), valid_from='2023-01-03', valid_to='2023-12-02'),
            CouponIndividual(coupon_id=Coupon.objects.get(pk=6), valid_from='2023-01-03', valid_to='2023-12-02'),
            CouponIndividual(coupon_id=Coupon.objects.get(pk=7), valid_from='2023-01-04', valid_to='2023-12-03'),
            CouponIndividual(coupon_id=Coupon.objects.get(pk=8), valid_from='2023-01-04', valid_to='2023-12-03'),
            CouponIndividual(coupon_id=Coupon.objects.get(pk=9), valid_from='2023-01-05', valid_to='2023-12-04'),
            CouponIndividual(coupon_id=Coupon.objects.get(pk=10), valid_from='2023-01-05', valid_to='2023-12-04'),
        ]
        for i, ci in enumerate(coupon_inv):
            ci.save()

        payment = [
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='D', card_number='4444-5555-6666-7777', card_exp_date=datetime.strptime('2023-09-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=6)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='D', card_number='7777-8888-9999-0000', card_exp_date=datetime.strptime('2023-10-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=7)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='C', card_number='1234-5678-9012-3456', card_exp_date=datetime.strptime('2023-12-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=8)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='C', card_number='9876-5432-1098-7654', card_exp_date=datetime.strptime('2024-01-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=9)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='C', card_number='1111-2222-3333-4444', card_exp_date=datetime.strptime('2024-03-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=10)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='C', card_number='5555-6666-7777-8888', card_exp_date=datetime.strptime('2024-04-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=27)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='C', card_number='9999-0000-1111-2222', card_exp_date=datetime.strptime('2024-05-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=30)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='G', card_number='33335555', card_exp_date=datetime.strptime('2024-06-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=31)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='C', card_number='4444-5555-6666-7777', card_exp_date=datetime.strptime('2024-07-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=34)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='C', card_number='7777-8888-9999-0000', card_exp_date=datetime.strptime('2024-08-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=35)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='D', card_number='1234-5678-9012-3456', card_exp_date=datetime.strptime('2023-01-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=1)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='G', card_number='88882222', card_exp_date=datetime.strptime('2023-11-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=7)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='D', card_number='9876-5432-1098-7654', card_exp_date=datetime.strptime('2023-03-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=2)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='G', card_number='1222444', card_exp_date=datetime.strptime('2023-04-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=2)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='D', card_number='1111-2222-3333-4444', card_exp_date=datetime.strptime('2023-05-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=2)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='D', card_number='5555-6666-7777-8888', card_exp_date=datetime.strptime('2023-06-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=3)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='D', card_number='9999-0000-1111-2222', card_exp_date=datetime.strptime('2023-07-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=4)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='G', card_number='33335555', card_exp_date=datetime.strptime('2023-08-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=5)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='G', card_number='1222444', card_exp_date=datetime.strptime('2024-02-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=10)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='C', card_number='1111-2222-3333-4444', card_exp_date=datetime.strptime('2024-03-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=11)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='C', card_number='5555-6666-7777-8888', card_exp_date=datetime.strptime('2024-04-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=12)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='C', card_number='9999-0000-1111-2222', card_exp_date=datetime.strptime('2024-05-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=13)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='G', card_number='33335555', card_exp_date=datetime.strptime('2024-06-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=14)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='C', card_number='4444-5555-6666-7777', card_exp_date=datetime.strptime('2024-07-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=15)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='C', card_number='7777-8888-9999-0000', card_exp_date=datetime.strptime('2024-08-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=16)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='G', card_number='88882222', card_exp_date=datetime.strptime('2024-09-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=17)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='D', card_number='1234-5678-9012-3456', card_exp_date=datetime.strptime('2024-10-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=18)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='C', card_number='9876-5432-1098-7654', card_exp_date=datetime.strptime('2024-11-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=19)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='G', card_number='1222444', card_exp_date=datetime.strptime('2024-12-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=20)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='D', card_number='1111-2222-3333-4444', card_exp_date=datetime.strptime('2025-01-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=20)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='G', card_number='88882222', card_exp_date=datetime.strptime('2024-09-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=17)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='D', card_number='1234-5678-9012-3456', card_exp_date=datetime.strptime('2024-10-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=18)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='C', card_number='9876-5432-1098-7654', card_exp_date=datetime.strptime('2024-11-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=19)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='G', card_number='1222444', card_exp_date=datetime.strptime('2024-12-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=20)),
            Payment(card_name='Rohit Card', card_zipcode='11209', payment_method='D', card_number='1111-2222-3333-4444', card_exp_date=datetime.strptime('2025-01-15', '%Y-%m-%d').date(), customer_id=User.objects.get(pk=20)),
        ]
        for i, p in enumerate(payment):
            p.pk = i + 1
            p.save()

        self.stdout.write(
            self.style.SUCCESS('DB setup successful')
        )
