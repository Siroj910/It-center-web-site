from django.db import models


class Courses(models.Model):
    icon_message = models.CharField(max_length=20)
    course_name = models.CharField(max_length=200)
    technology = models.TextField(max_length=200)
    course_term = models.CharField(max_length=20)
    course_prize = models.CharField(max_length=200)

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = 'Course'


class Img(models.Model):
    img = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = 'Image'


class Mentors(models.Model):
    img_mentor = models.ImageField(upload_to='mentors/', blank=True)
    name = models.CharField(max_length=200)
    major = models.CharField(max_length=50)
    technology = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mentor'






