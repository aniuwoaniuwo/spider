from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
 
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)
	#def __str__(self):
     #   return self.title
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
 
    def my_property(self):
        return self.first_name + ' ' + self.last_name
    my_property.short_description = "Full name of the person"
 
    full_name = property(my_property)