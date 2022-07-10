from django.db import models
from post.models import Post

class Comment(models.Model):
    id = models.BigAutoField(help_text="Comment ID", primary_key=True)
    writer = models.CharField(max_length=10)
    post_id = models.ForeignKey("post.Post",related_name="post", on_delete=models.CASCADE, db_column="post_id",default="")
    contents = models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.writer