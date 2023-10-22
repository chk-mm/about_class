from datetime import datetime


def send_sms(msg, phone):
    print(f'To: {phone}')
    print(f'{msg}')


def send_email(msg, email):
    print(f'To: {email}')
    print(f'{msg}')


class Patient:
    def __init__(self, fname, lname, title, birthdate, email, tel1, tel2):
        self.fname = fname
        self.lname = lname
        self.title = title
        self.birthdate = birthdate
        self.email = email
        self.tel1 = tel1
        self.tel2 = tel2

    def greeting(self):
        return f'Hello! {self.title} {self.fname}'

    def send_appointment_reminder(self, date):
        message = f'\t{date}\t How are you? {self.fname}'
        send_sms(message, self.tel1)
        send_email(message, self.email)

    def get_age(self):
        birth_year = self.birthdate.year
        birth_month = self.birthdate.month
        birth_day = self.birthdate.day

        today = datetime.now()
        curr_year = today.year
        curr_month = today.month
        curr_day = today.day

        days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if birth_day > curr_day:
            curr_month = curr_month - 1
            curr_day = curr_day + days_of_month[birth_month - 1]

        if birth_month > curr_month:
            curr_year = curr_year - 1
            curr_month = curr_month + 12

        year = curr_year - birth_year
        month = curr_month - birth_month
        day = curr_day - birth_day

        return f'{year}Y {month}M {day}D'

    def get_patient_profile(self):
        return (f'Name:\t{self.title} {self.fname} {self.lname}\n'
                f'Age:\t{self.get_age()}\n'
                f'Email:\t{self.email}\n'
                f'Tel:\t{self.tel1}, {self.tel2}')


patient1 = Patient(
    'John',
    'Doe',
    'Mr.',
    datetime(2000, 8, 13),  # if today is 2023/10/8, age is 23Y 1M 26D
    'john.doe@gmail.com',
    '+3345451555',
    '+6693932030',
)

patient2 = Patient(
    'Jane',
    'Doe',
    'Ms.',
    datetime(2000, 4, 23),  # if today is 2023/10/8, age is 23Y 5M 15D
    'jane.doe@gmail.com',
    '+3345451552',
    '+6693932032',
)

print(patient1.greeting())
patient1.send_appointment_reminder(datetime(2023, 10, 13, 13, 0))

print('Patient 1')
print(patient1.get_patient_profile())

print('Patient 2')
print(patient2.get_patient_profile())