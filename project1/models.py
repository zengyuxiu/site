from django.db import models


# Create your models here.
class Android(models.Model):
    totaltime = models.BigIntegerField(primary_key=True)
    usernum = models.BigIntegerField(blank=True, null=True)

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    char_field_dict = {'TotalTime': 'totaltime', 'UserNumber': 'usernum'}

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    class Meta:
        managed = False
        db_table = 'Android'


class Android4(models.Model):
    totaltime = models.BigIntegerField(primary_key=True)
    usernum = models.BigIntegerField(blank=True, null=True)
    char_field_dict = {'TotalTime': 'totaltime', 'UserNumber': 'usernum'}

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    class Meta:
        managed = False
        db_table = 'Android4'


class Android5(models.Model):
    totaltime = models.BigIntegerField(primary_key=True)
    usernum = models.BigIntegerField(blank=True, null=True)
    char_field_dict = {'TotalTime': 'totaltime', 'UserNumber': 'usernum'}

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    class Meta:
        managed = False
        db_table = 'Android5'


class Android6(models.Model):
    totaltime = models.BigIntegerField(primary_key=True)
    usernum = models.BigIntegerField(blank=True, null=True)
    char_field_dict = {'TotalTime': 'totaltime', 'UserNumber': 'usernum'}

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    class Meta:
        managed = False
        db_table = 'Android6'


class Android7(models.Model):
    totaltime = models.BigIntegerField(primary_key=True)
    usernum = models.BigIntegerField(blank=True, null=True)
    char_field_dict = {'TotalTime': 'totaltime', 'UserNumber': 'usernum'}

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    class Meta:
        managed = False
        db_table = 'Android7'


class Login3(models.Model):
    b3 = models.BigIntegerField(db_column='B3', primary_key=True)  # Field name made lowercase.
    char_field_dict = {'b3': 'B3'}

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    class Meta:
        managed = False
        db_table = 'Login3'


class Login7(models.Model):
    date = models.DateField(primary_key=True)
    login = models.BigIntegerField(blank=True, null=True)
    char_field_dict = {'Date': 'date', 'Login': 'login'}

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    class Meta:
        managed = False
        db_table = 'Login7'


class Newolduser(models.Model):
    new = models.BigIntegerField(primary_key=True)
    old = models.BigIntegerField()
    char_field_dict = {'NewUser': 'new', 'OldUser': 'old'}

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    class Meta:
        managed = False
        db_table = 'NewOldUser'
        unique_together = (('new', 'old'),)


class Retentionrate(models.Model):
    day2 = models.CharField(primary_key=True, max_length=255)
    day3 = models.CharField(max_length=255, blank=True, null=True)
    day7 = models.CharField(max_length=255, blank=True, null=True)

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    char_field_dict = {'Retentionrate_in_2days': 'day2', 'Retentionrate_in_3days': 'day3',
                       'Retentionrate_in_7days': 'day7'}

    class Meta:
        managed = False
        db_table = 'RetentionRate'


class Topn(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    t = models.BigIntegerField(blank=True, null=True)
    times = models.IntegerField(blank=True, null=True)
    ft = models.CharField(max_length=255, blank=True, null=True)

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    char_field_dict = {'id': 'id', 't': 't', 'times': 'times',
                       'ft': 'ft'}

    class Meta:
        managed = False
        db_table = 'TopN'


class Topnnfo(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    t = models.BigIntegerField(blank=True, null=True)
    times = models.IntegerField(blank=True, null=True)
    ft = models.CharField(max_length=255, blank=True, null=True)

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    char_field_dict = {'id': 'id', 't': 't', 'times': 'times',
                       'ft': 'ft'}

    class Meta:
        managed = False
        db_table = 'TopNnfo'


class Userinfo(models.Model):
    totaluser = models.BigIntegerField(primary_key=True)
    totallog = models.BigIntegerField(blank=True, null=True)
    avgtime = models.BigIntegerField(blank=True, null=True)
    eachtime = models.BigIntegerField(blank=True, null=True)

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    char_field_dict = {'TotalUser': 'totaluser', 'TotalLog': 'totallog', 'AvgTime': 'avgtime',
                       'EachTime': 'eachtime'}

    class Meta:
        managed = False
        db_table = 'UserInfo'


class Usertime(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    totaltime = models.BigIntegerField(blank=True, null=True)

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    char_field_dict = {'ID': 'id', 'totaltime': 'totaltime'}

    class Meta:
        managed = False
        db_table = 'UserTime'


class Gamep1(models.Model):
    num = models.BigAutoField(primary_key=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    sys = models.CharField(max_length=255, blank=True, null=True)
    ver = models.CharField(max_length=11, blank=True, null=True)
    t1 = models.CharField(max_length=255, blank=True, null=True)
    t2 = models.CharField(max_length=255, blank=True, null=True)
    dur = models.BigIntegerField(blank=True, null=True)

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    char_field_dict = {'Number': 'num', 'ID': 'id', 'System': 'sys', 'Version': 'ver', 'T1': 't1', 'T2': 't2',
                       'Duration': 'dur'}

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

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    char_field_dict = {'Number': 'num', 'ID': 'id', 'System': 'sys', 'Version': 'ver', 'T1': 't1', 'T2': 't2',
                       'Duration': 'dur'}

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

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    char_field_dict = {'Number': 'num', 'ID': 'id', 'System': 'sys', 'Version': 'ver', 'T1': 't1', 'T2': 't2',
                       'Duration': 'dur'}

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

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    char_field_dict = {'Number': 'num', 'ID': 'id', 'System': 'sys', 'Version': 'ver', 'T1': 't1', 'T2': 't2',
                       'Duration': 'dur'}

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

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    char_field_dict = {'Number': 'num', 'ID': 'id', 'System': 'sys', 'Version': 'ver', 'T1': 't1', 'T2': 't2',
                       'Duration': 'dur'}

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

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    char_field_dict = {'Number': 'num', 'ID': 'id', 'System': 'sys', 'Version': 'ver', 'T1': 't1', 'T2': 't2',
                       'Duration': 'dur'}

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

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    char_field_dict = {'Number': 'num', 'ID': 'id', 'System': 'sys', 'Version': 'ver', 'T1': 't1', 'T2': 't2',
                       'Duration': 'dur'}

    class Meta:
        managed = False
        db_table = 'gameP7'


class Ios(models.Model):
    totaltime = models.BigIntegerField(primary_key=True)
    usernum = models.BigIntegerField(blank=True, null=True)

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    char_field_dict = {'TotalTime': 'totaltime', 'UserNumber': 'usernum'}

    class Meta:
        managed = False
        db_table = 'iOS'


class Ios10(models.Model):
    totaltime = models.BigIntegerField(primary_key=True)
    usernum = models.BigIntegerField(blank=True, null=True)

    def __data__(self):
        data_sets = []
        for char_field in self.char_field_dict.values():
            data_tulpe = self.objects.values_list(char_field)
            data_set = []
            for data in data_tulpe:
                data_set.append(data[-1])
            data_sets.append(data_set)
        return data_sets

    char_field_dict = {'TotalTime': 'totaltime', 'UserNumber': 'usernum'}

    class Meta:
        managed = False
        db_table = 'iOS10'


class Ios11(models.Model):
    totaltime = models.BigIntegerField(primary_key=True)
    usernum = models.BigIntegerField(blank=True, null=True)

    char_field_dict = {'TotalTime': 'totaltime', 'UserNumber': 'usernum'}

    class Meta:
        managed = False
        db_table = 'iOS11'
