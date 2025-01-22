import random

from click import option
from django.core.management import BaseCommand
from faker import Faker

from  vege.models import *


class Command(BaseCommand):
    help = "Create or Add Given Set of External Organization Names"

    def add_arguments(self, parser):
        parser.add_argument('--n', required=False, type=int)

    def handle(self, *args, **options):
        fake = Faker()
        try:
            n = options['n'] if options['n'] else 100
            for i in range(0, n):
                department_objs = Department.objects.all()
                random_index = random.randint(0, len(department_objs) - 1)

                department = department_objs[random_index]
                student_id = f"STU_0{random.randint(100, 999)}"
                student_name = fake.name()
                student_email = fake.email()
                student_age = random.randint(20, 30)
                student_address = fake.address()

                student_id_obj = StudentId.objects.create(student_id=student_id)

                student_obj = Student.objects.create(
                    department=department,
                    student_id=student_id_obj,
                    student_name=student_name,
                    student_email=student_email,
                    student_age=student_age,
                    student_address=student_address
                )
            print(f"Successfully created {n} objects")

        except Exception as e:
            return e.__str__()
