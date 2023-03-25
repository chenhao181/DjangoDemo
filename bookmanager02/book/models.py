from django.db import models

# Create your models here.


class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name='名字')
    pub_date = models.DateField(null=True)
    readCount = models.IntegerField(default=0)
    commentCount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '书籍管理'

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female'),
    )
    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    descriptions = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)

    # 外键
    # 系统会自动为外键添加 _id
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'

    def __str__(self):
        return self.name



