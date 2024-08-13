from database import db
from models.user import User


class Diet(db.Model):
    id = db.AutoField(primary_key=True)
    name = db.CharField(max_length=100)
    description = db.TextField()
    created_at = db.DateTimeField(auto_now_add=True)
    updated_at = db.DateTimeField(auto_now=True)
    off_the_diet = db.BooleanField(default=False)
    user = db.ForeignKey(User, on_delete=db.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Diet'
        verbose_name_plural = 'Diets'
        ordering = ['name']



