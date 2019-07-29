# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agedisc(models.Model):
    number_1 = models.CharField(db_column='1', primary_key=True, max_length=20)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.CharField(db_column='2', max_length=20, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.CharField(db_column='3', max_length=20, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4 = models.CharField(db_column='4', max_length=20, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5 = models.CharField(db_column='5', max_length=20, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'AgeDisc'


class Android(models.Model):
    totaltime = models.BigIntegerField(primary_key=True)
    usernum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Android'


class Android4(models.Model):
    totaltime = models.BigIntegerField(primary_key=True)
    usernum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Android4'


class Android5(models.Model):
    totaltime = models.BigIntegerField(primary_key=True)
    usernum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Android5'


class Android6(models.Model):
    totaltime = models.BigIntegerField(primary_key=True)
    usernum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Android6'


class Android7(models.Model):
    totaltime = models.BigIntegerField(primary_key=True)
    usernum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Android7'


class Annualgender(models.Model):
    number_1 = models.IntegerField(db_column='1', primary_key=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.IntegerField(db_column='2', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'AnnualGender'


class Annualorshort(models.Model):
    number_1 = models.CharField(db_column='1', primary_key=True, max_length=255)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.CharField(db_column='2', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.CharField(db_column='3', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4 = models.CharField(db_column='4', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'AnnualOrShort'


class Authority(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    login = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Authority'


class Avaidockavg(models.Model):
    number_1 = models.CharField(db_column='1', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.CharField(db_column='2', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.CharField(db_column='3', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4 = models.AutoField(db_column='4', primary_key=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'AvaiDockAvg'


class Dur6Hours(models.Model):
    number_1 = models.CharField(db_column='1', primary_key=True, max_length=20)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.SmallIntegerField(db_column='2', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'Dur6hours'


class Gendertime(models.Model):
    number_1 = models.IntegerField(db_column='1', primary_key=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.CharField(db_column='2', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.IntegerField(db_column='3', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4 = models.CharField(db_column='4', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'GenderTime'


class Login3(models.Model):
    b3 = models.BigIntegerField(db_column='B3', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Login3'


class Login7(models.Model):
    date = models.DateField(primary_key=True)
    login = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Login7'


class Monavgunavbike(models.Model):
    number_1 = models.CharField(db_column='1', max_length=20, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.CharField(db_column='2', max_length=20, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.CharField(db_column='3', max_length=20, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'MonAvgUnavBike'


class Monavgunavpark(models.Model):
    number_1 = models.CharField(db_column='1', max_length=20, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.CharField(db_column='2', max_length=20, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.CharField(db_column='3', max_length=20, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4 = models.AutoField(db_column='4', primary_key=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'MonAvgUnavPark'


class Newolduser(models.Model):
    new = models.BigIntegerField(primary_key=True)
    old = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'NewOldUser'
        unique_together = (('new', 'old'),)


class Rainday(models.Model):
    number_3_20_2015 = models.IntegerField(db_column='3/20/2015', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_21_2015 = models.IntegerField(db_column='3/21/2015', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_22_2015 = models.IntegerField(db_column='3/22/2015', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_23_2015 = models.IntegerField(db_column='3/23/2015', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_24_2015 = models.IntegerField(db_column='3/24/2015', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_26_2015 = models.IntegerField(db_column='3/26/2015', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_27_2015 = models.IntegerField(db_column='3/27/2015', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'RainDay'


class Retentionrate(models.Model):
    day2 = models.CharField(primary_key=True, max_length=255)
    day3 = models.CharField(max_length=255, blank=True, null=True)
    day7 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RetentionRate'


#desc : year-month  rideNum_monthly
class Ridenummonthly(models.Model):
    number_1 = models.CharField(db_column='1', primary_key=True, max_length=20)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.CharField(db_column='2', max_length=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'RideNumMonthly'


#desc : station_id  Avg_availableBike  year-month
class Staavainum(models.Model):
    number_1 = models.SmallIntegerField(db_column='1', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.SmallIntegerField(db_column='2', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.CharField(db_column='3', primary_key=True, max_length=10)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'StaAvaiNum'


#desc : station_id  DockNum  date
class Staonline(models.Model):
    number_1 = models.CharField(db_column='1', primary_key=True, max_length=30)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.CharField(db_column='2', max_length=30, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.CharField(db_column='3', max_length=30, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'StaOnline'


class Sunday(models.Model):
    number_5_14_2015 = models.IntegerField(db_column='5/14/2015', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_15_2015 = models.IntegerField(db_column='5/15/2015', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_16_2015 = models.IntegerField(db_column='5/16/2015', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_17_2015 = models.IntegerField(db_column='5/17/2015', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_18_2015 = models.IntegerField(db_column='5/18/2015', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_19_2015 = models.IntegerField(db_column='5/19/2015', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_20_2015 = models.IntegerField(db_column='5/20/2015', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'SunDay'


class Topn(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    t = models.BigIntegerField(blank=True, null=True)
    times = models.IntegerField(blank=True, null=True)
    ft = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TopN'


class Topnnfo(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    t = models.BigIntegerField(blank=True, null=True)
    times = models.IntegerField(blank=True, null=True)
    ft = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TopNnfo'


# desc :
# ID  date  start_stationID  lat  long
# ID  date  end_stationID lat  long
class TripFlow(models.Model):
    id = models.BigAutoField(primary_key=True)
    number_1 = models.CharField(db_column='1', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.CharField(db_column='2', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.CharField(db_column='3', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4 = models.CharField(db_column='4', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5 = models.CharField(db_column='5', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'Trip_Flow'


class Userinfo(models.Model):
    totaluser = models.BigIntegerField(primary_key=True)
    totallog = models.BigIntegerField(blank=True, null=True)
    avgtime = models.BigIntegerField(blank=True, null=True)
    eachtime = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserInfo'


class Usertime(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    totaltime = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserTime'


#class AuthGroup(models.Model):
#    name = models.CharField(unique=True, max_length=150)
#
#    class Meta:
#        managed = False
#        db_table = 'auth_group'
#
#
#class AuthGroupPermissions(models.Model):
#    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#    class Meta:
#        managed = False
#        db_table = 'auth_group_permissions'
#        unique_together = (('group', 'permission'),)
#
#
#class AuthPermission(models.Model):
#    name = models.CharField(max_length=255)
#    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#    codename = models.CharField(max_length=100)
#
#    class Meta:
#        managed = False
#        db_table = 'auth_permission'
#        unique_together = (('content_type', 'codename'),)
#
#
#class AuthUser(models.Model):
#    password = models.CharField(max_length=128)
#    last_login = models.DateTimeField(blank=True, null=True)
#    is_superuser = models.IntegerField()
#    username = models.CharField(unique=True, max_length=150)
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=150)
#    email = models.CharField(max_length=254)
#    is_staff = models.IntegerField()
#    is_active = models.IntegerField()
#    date_joined = models.DateTimeField()
#
#    class Meta:
#        managed = False
#        db_table = 'auth_user'
#
#
#class AuthUserGroups(models.Model):
#    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#    class Meta:
#        managed = False
#        db_table = 'auth_user_groups'
#        unique_together = (('user', 'group'),)
#
#
#class AuthUserUserPermissions(models.Model):
#    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#    class Meta:
#        managed = False
#        db_table = 'auth_user_user_permissions'
#        unique_together = (('user', 'permission'),)


#class DjangoAdminLog(models.Model):
#    action_time = models.DateTimeField()
#    object_id = models.TextField(blank=True, null=True)
#    object_repr = models.CharField(max_length=200)
#    action_flag = models.PositiveSmallIntegerField()
#    change_message = models.TextField()
#    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#    class Meta:
#        managed = False
#        db_table = 'django_admin_log'
#
#
#class DjangoContentType(models.Model):
#    app_label = models.CharField(max_length=100)
#    model = models.CharField(max_length=100)
#
#    class Meta:
#        managed = False
#        db_table = 'django_content_type'
#        unique_together = (('app_label', 'model'),)
#
#
#class DjangoMigrations(models.Model):
#    app = models.CharField(max_length=255)
#    name = models.CharField(max_length=255)
#    applied = models.DateTimeField()
#
#    class Meta:
#        managed = False
#        db_table = 'django_migrations'
#
#
#class DjangoSession(models.Model):
#    session_key = models.CharField(primary_key=True, max_length=40)
#    session_data = models.TextField()
#    expire_date = models.DateTimeField()
#
#    class Meta:
#        managed = False
#        db_table = 'django_session'


class Gamep1(models.Model):
    num = models.BigAutoField(primary_key=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    sys = models.CharField(max_length=255, blank=True, null=True)
    ver = models.CharField(max_length=11, blank=True, null=True)
    t1 = models.CharField(max_length=255, blank=True, null=True)
    t2 = models.CharField(max_length=255, blank=True, null=True)
    dur = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gameP1'


class Gamep2(models.Model):
    num = models.BigAutoField(primary_key=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    sys = models.CharField(max_length=255, blank=True, null=True)
    ver = models.CharField(max_length=11, blank=True, null=True)
    t1 = models.CharField(max_length=255, blank=True, null=True)
    t2 = models.CharField(max_length=255, blank=True, null=True)
    dur = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gameP2'


class Gamep3(models.Model):
    num = models.BigAutoField(primary_key=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    sys = models.CharField(max_length=255, blank=True, null=True)
    ver = models.CharField(max_length=11, blank=True, null=True)
    t1 = models.CharField(max_length=255, blank=True, null=True)
    t2 = models.CharField(max_length=255, blank=True, null=True)
    dur = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gameP3'


class Gamep4(models.Model):
    num = models.BigAutoField(primary_key=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    sys = models.CharField(max_length=255, blank=True, null=True)
    ver = models.CharField(max_length=11, blank=True, null=True)
    t1 = models.CharField(max_length=255, blank=True, null=True)
    t2 = models.CharField(max_length=255, blank=True, null=True)
    dur = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gameP4'


class Gamep5(models.Model):
    num = models.BigAutoField(primary_key=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    sys = models.CharField(max_length=255, blank=True, null=True)
    ver = models.CharField(max_length=11, blank=True, null=True)
    t1 = models.CharField(max_length=255, blank=True, null=True)
    t2 = models.CharField(max_length=255, blank=True, null=True)
    dur = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gameP5'


class Gamep6(models.Model):
    num = models.BigAutoField(primary_key=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    sys = models.CharField(max_length=255, blank=True, null=True)
    ver = models.CharField(max_length=11, blank=True, null=True)
    t1 = models.CharField(max_length=255, blank=True, null=True)
    t2 = models.CharField(max_length=255, blank=True, null=True)
    dur = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gameP6'


class Gamep7(models.Model):
    num = models.BigAutoField(primary_key=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    sys = models.CharField(max_length=255, blank=True, null=True)
    ver = models.CharField(max_length=255, blank=True, null=True)
    t1 = models.CharField(max_length=255, blank=True, null=True)
    t2 = models.CharField(max_length=255, blank=True, null=True)
    dur = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gameP7'


class Ios(models.Model):
    totaltime = models.BigIntegerField(primary_key=True)
    usernum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iOS'


class Ios10(models.Model):
    totaltime = models.BigIntegerField(primary_key=True)
    usernum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iOS10'


class Ios11(models.Model):
    totaltime = models.BigIntegerField(primary_key=True)
    usernum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iOS11'


#class PollsChoice(models.Model):
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField()
#    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)
#
#    class Meta:
#        managed = False
#        db_table = 'polls_choice'
#
#
#class PollsQuestion(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField()
#
#    class Meta:
#        managed = False
#        db_table = 'polls_question'


#class Student(models.Model):
#    studentnum = models.CharField(db_column='studentNum', primary_key=True, max_length=15)  # Field name made lowercase.
#    name = models.CharField(max_length=20)
#    age = models.IntegerField()
#    sex = models.IntegerField()
#    mobile = models.CharField(unique=True, max_length=15)
#    createtime = models.DateTimeField(db_column='createTime')  # Field name made lowercase.
#    modifytime = models.DateTimeField(db_column='modifyTime')  # Field name made lowercase.
#
#    class Meta:
#        managed = False
#        db_table = 'student'
#
#
#class StudentUnion(models.Model):
#    id = models.IntegerField(primary_key=True)
#    unionname = models.CharField(db_column='unionName', max_length=20)  # Field name made lowercase.
#    unionnum = models.IntegerField(db_column='unionNum')  # Field name made lowercase.
#    unionroot = models.ForeignKey(Student, models.DO_NOTHING, db_column='unionRoot_id', unique=True)  # Field name made lowercase.
#
#    class Meta:
#        managed = False
#        db_table = 'student_union'
