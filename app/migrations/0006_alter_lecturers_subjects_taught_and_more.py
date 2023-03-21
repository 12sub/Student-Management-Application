# Generated by Django 4.1.7 on 2023-03-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_management_date_of_employment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturers',
            name='subjects_taught',
            field=models.CharField(choices=[('Mathematics', 'Mathematics'), ('English', 'English'), ('Chemistry', 'Chemistry'), ('Social Science', 'Social Science'), ('Agriculture', 'Agriculture'), ('Physics', 'Physics'), ('Biology', 'Biology'), ('Futher Mathematics', 'Futher Mathematics'), ('Phonetics', 'Phonetics'), ('Commerce', 'Commerce'), ('Geography', 'Geography'), ('Economics', 'Economics'), ('Computer Programming', 'Computer Programming'), ('ICT Services', 'ICT Services'), ('Electronics', 'Electronics'), ('Data Processing', 'Data Processing'), ('Yoruba', 'Yoruba'), ('Hausa', 'Hausa'), ('Igbo', 'Igbo'), ('Technical Drawing', 'Technical Drawing')], max_length=200),
        ),
        migrations.AlterField(
            model_name='management',
            name='profession',
            field=models.CharField(choices=[('Cleaner', 'Cleaner'), ('Secetary', 'Secetary'), ('Engineer', 'Engineer'), ('Principal', 'Principal'), ('Vice-Principal', 'Vice-Principal'), ('Board of Regents', 'Board of Regents'), ('ICT Specialist', 'ICT Specialist')], max_length=100),
        ),
    ]
