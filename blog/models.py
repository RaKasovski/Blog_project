from django.db import models
class Post(models.Model):
 	posts_image = models.ImageField(upload_to ="")
 	posts_text = models.CharField(max_length = 300)
 	posts_data_time = models.DateTimeField()
 	posts_title = models.CharField(max_length = 50)
