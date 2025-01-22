import random
from vege.models import *
from django.core.management import BaseCommand
class Command(BaseCommand):
    help = "Create or Add Given Set of External Organization Names"

    def add_arguments(self, parser):
        parser.add_argument('--n', required=False, type=int)

    def handle(self, *args, **options):
        try:
            n = options['n'] if options['n'] else 100
            student_objs=Student.objects.all()
            for student in student_objs:
                subjects=Subject.objects.all()
                for subject in subjects:
                    SubjectMarks.objects.create(
                        subject=subject,
                        student=student,
                        marks=random.randint(0,100)
                    )
            print(f"Marks added for {n} Students")
        except Exception as e:
            print(e)