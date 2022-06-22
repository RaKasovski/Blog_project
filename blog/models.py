from django.db import models
class Post(models.Model):
 	posts_image = models.ImageField(upload_to ="post_images")
 	posts_text = models.CharField(max_length = 300)
 	posts_data_time = models.DateTimeField()
 	posts_title = models.CharField(max_length = 50)

def __str__(self):
	return self.posts_title


def get_summery(self):
	return self.posts_text[:70]

