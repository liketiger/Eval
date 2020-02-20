from django.db import models
import django_filters

class ClassBlog(models.Model):
    강의명 = models.CharField(max_length=100, default='')
    교수명 = models.CharField(max_length=100, default='')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    평가내용 = models.TextField()

    def __str__(self):
        return self.강의명

class EvalFilter(django_filters.FilterSet):
    class Meta:
        model = ClassBlog
        fields = ['강의명', '교수명']
# Create your models here.
