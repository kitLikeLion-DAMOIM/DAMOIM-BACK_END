from signal import raise_signal
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, user_id,department,grade,phone,name, password):
        if not user_id:
            raise ValueError('must have user identity')
        if not department:
            raise ValueError('must have user department')
        if not grade:
            raise ValueError('must have user grade')
        if not phone:
            raise ValueError('must have user phone')
        if not name:
            raise ValueError('must have user name')
        if not password:
            raise ValueError('must have user password')
        user = self.model(
            user_id = user_id,
            department = department,
            grade = grade,
            phone = phone,
            name = name,
            password = password
        )
        user.save(using=self._db)
        return user

    # 관리자 user 생성
    # def create_superuser(self, email, nickname, name, password=None):
    #     user = self.create_user(
    #         email,
    #         password = password,
    #         nickname = nickname,
    #         name = name
    #     )
    #     user.is_admin = True
    #     user.save(using=self._db)
    #     return user

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=50,unique=True)
    name = models.CharField(default='', max_length=10, null=False, blank=False)
    department = models.CharField(max_length=50)
    grade = models.CharField(max_length=10)
    phone= models.CharField(max_length=20)
    is_auth=models.BooleanField(default=False)
    token = models.TextField(default='')

    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    
    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 nickname으로 설정
    USERNAME_FIELD = 'user_id'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.user_id

