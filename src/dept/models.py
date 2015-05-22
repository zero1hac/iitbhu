from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class department(models.Model):
    dept_code = models.CharField(max_length = 10, primary_key = True, blank = False)
    dept_name = models.CharField(max_length = 50, null = True, blank = True)
    dept_info = models.TextField()
    
    def __unicode__(self):
        return smart_unicode(self.dept_code)+' : '+smart_unicode(self.dept_name)
    

class faculty(models.Model):
    name = models.CharField(max_length = 50, null = True, blank = True)
    dept = models.CharField(max_length = 50, null = True, blank = True)
    designation = models.CharField(max_length = 20, null = True, blank = True)
    qualification = models.CharField(max_length = 100, null = True, blank = True)
    area_of_interest = models.CharField(max_length = 100, null = True, blank = True)
    contact = models.CharField(max_length = 50, null = True, blank = True)
    email = models.EmailField(null = False, blank = False)
    status = models.CharField(max_length = 10, null = True, blank = True)
    
    def __unicode__(self):
        return smart_unicode(self.name)+' : '+smart_unicode(self.email)


class student(models.Model):
    roll_no = models.CharField(max_length = 10, primary_key = True, blank = False)
    name = models.CharField(max_length = 50, null = False, blank = False)
    batch = models.CharField(max_length = 30, null = False, blank = False)
    email = models.EmailField(null = False, blank = False)

    def __unicode__(self):
        return smart_unicode(self.roll_no)+' : '+smart_unicode(self.name)
    
    
class staff(models.Model):
    name = models.CharField(max_length = 50, null = False, blank = False)
    dept = models.CharField(max_length = 50, null = False, blank = False)
    designation = models.CharField(max_length = 20, null = False, blank = False)
    email = models.EmailField()
    
    def __unicode__(self):
        return smart_unicode(self.name)+' : '+smart_unicode(self.email)
    
class notification(models.Model):
    notif_id = models.CharField(max_length = 30, primary_key = True, blank = False)
    title = models.CharField(max_length = 50, null = False, blank = False)
    description = models.CharField(max_length = 100, null = False, blank = False)
    date = models.DateTimeField(auto_now_add = True, auto_now = False)
        
    def __unicode__(self):
        return smart_unicode(self.notif_id)+' : '+smart_unicode(self.title)
    

class course(models.Model):
    s_no = models.IntegerField()
    course_id = models.CharField(max_length = 30, null = False, blank = False)
    course_name = models.CharField(max_length = 30, null = False, blank = False)
    degree = models.CharField(max_length = 30, null = False, blank = False)
    year = models.IntegerField()
    sem = models.IntegerField()
    credits = models.IntegerField()
    course_of_dept = models.CharField(max_length = 30, null = False, blank = False)
    course_in_dept = models.CharField(max_length = 100, null = False, blank = False)
    type = models.CharField(max_length = 30, null = False, blank = False)

    def __unicode__(self):
        return smart_unicode(self.course_id)+' : '+smart_unicode(self.course_name)


class gallery(models.Model):
    gallery_id = models.CharField(max_length = 30, primary_key = True, blank = False)
    name = models.CharField(max_length = 30, null = False, blank = False)
    description = models.CharField(max_length = 30, null = False, blank = False)
    
    def __unicode__(self):
        return smart_unicode(self.gallery_id)+' : '+smart_unicode(self.name)


class image(models.Model):
    image_id = models.CharField(max_length = 30, primary_key = True, blank = False)
    gallery_id = models.CharField(max_length = 30, null = False, blank = False)
    upload_date = models.DateTimeField(auto_now_add = True, auto_now = False)
    link = models.URLField()
    caption = models.CharField(max_length = 30, null = True, blank = True)
    
    def __unicode__(self):
        return smart_unicode(self.image_id)+' : '+smart_unicode(self.caption)





















