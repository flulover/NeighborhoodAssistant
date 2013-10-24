from django.db import models


class login(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    telephone = models.CharField(max_length=16)
    password = models.CharField(max_length=16)

    class Meta:
        db_table = 'login'

class user(models.Model):
    name = models.CharField(max_length=32)
    user_type = models.CharField(max_length=16)
    email = models.CharField(max_length=64)
    telephone = models.CharField(max_length=16)
    create_time = models.DateField()
    qq = models.CharField(max_length=20)
    headshot = models.CharField(max_length=128)

    login = models.ForeignKey(login)
    login.primary_key = True;

    class Meta:
        db_table = 'user'

class merchant(models.Model):
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=12)
    description = models.CharField(max_length=256)
    telephone = models.CharField(max_length=16)
    fix_telephone = models.CharField(max_length=16)

    login = models.ForeignKey(login)
    login.primary_key = True

    class Meta:
        db_table = 'merchant'

class housing_estate(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=128)

    merchants = models.ManyToManyField(merchant)
    users = models.ManyToManyField(user)

    class Meta:
        db_table = 'housing_estate'

class user_define_merchant(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)

    user = models.ForeignKey(user)
    user.primary_key = True

    class Meta:
        db_table = 'user_define_merchant'

class user_search_history(models.Model):
    search_content = models.CharField(max_length=128)
    search_time = models.DateField()

    user = models.ForeignKey(user)
    user.primary_key = True

    class Meta:
        db_table = 'user_search_history'

class merchant_service_item(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    related_image = models.CharField(max_length=128)

    merchant = models.ForeignKey(merchant, primary_key=True)

    class Meta:
        db_table = 'merchant_service_item'

class merchant_statistical_data(models.Model):
    grade = models.IntegerField()
    viewed_times = models.IntegerField()
    called_times = models.IntegerField()

    merchant = models.ForeignKey(merchant, primary_key=True)

    class Meta:
        db_table = 'merchant_statistical_data'

class merchant_comment(models.Model):
    comment = models.CharField(max_length=128)
    comment_time = models.DateField()

    merchant = models.ForeignKey(merchant, primary_key=True)

    class Meta:
        db_table = 'merchant_comment'

class user_favourite_merchant(models.Model):
    user = models.ForeignKey(user)
    merchant = models.ForeignKey(merchant)

    class Meta:
        db_table = 'user_favourite_merchant'


