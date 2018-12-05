from django.db import models

# Create your models here.
class person(models.Model):
	name=models.CharField(max_length=30)
	age=models.IntegerField()
	
	#pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
    #update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)
	def __str__(self):
		return self.name