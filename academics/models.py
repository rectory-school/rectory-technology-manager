from django.db import models

# Create your models here.
class StudentPermRec(models.Model):
  student_id = models.CharField(max_length=8, unique=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  nickname = models.CharField(max_length=50, blank=True)
  email = models.EmailField(max_length=254, blank=True)
  
  class Meta:
    ordering = ['last_name', 'first_name', 'nickname']
    verbose_name = 'student'
    verbose_name_plural = 'students'
  
  @property
  def name(self):
    if self.nickname and self.nickname != self.first_name:
      return "{first} ({nick}) {last}".format(first=self.first_name, last=self.last_name, nick=self.nickname)
    
    return "{first} {last}".format(first=self.first_name, last=self.last_name, nick=self.nickname)
  
  def __str__(self):
    return self.name
  
class Family(models.Model):
  family_id = models.CharField(max_length=8, unique=True)
  
class StudentFamily(models.Model):
  student = models.ForeignKey(StudentPermRec)
  family = models.ForeignKey(Family)
  family_number = models.IntegerField()
  
class FamilyMember(models.Model):
  first = models.CharField(max_length=20)
  last = models.CharField(max_length=20)
  email = models.EmailField(max_length=254, blank=True)
  phone = models.CharField(max_length=20, blank=True)
  
  FAMILYRELATIONSHIPCHOICES = (('Pa', 'Parent A'), ('Pb', 'Parent B'))
  
  family = models.ForeignKey(Family)
  relationship = models.CharField(max_length=max([len(o[0]) for o in FAMILYRELATIONSHIPCHOICES]), choices=FAMILYRELATIONSHIPCHOICES)