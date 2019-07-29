from django.db import models


# Create your models here.
# desc :
# male 0-20,21-40,41-60,61-80
# female 0-20,21-40,41-60,61-80
class Agedisc(models.Model):
    number_1 = models.CharField(db_column='1', primary_key=True,
                                max_length=20)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.CharField(db_column='2', max_length=20, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.CharField(db_column='3', max_length=20, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4 = models.CharField(db_column='4', max_length=20, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5 = models.CharField(db_column='5', max_length=20, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.

    char_field_dict = {'性别': 'number_1', '0~20': 'number_2', '21~40': 'number_3', '41~60': 'number_4',
                       '61~80': 'number_5'}

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
        db_table = 'AgeDisc'


# desc :
class Annualgender(models.Model):
    number_1 = models.IntegerField(db_column='1',
                                   primary_key=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.IntegerField(db_column='2', blank=True,
                                   null=True)  # Field renamed because it wasn't a valid Python identifier.
    char_field_dict = {'男会员': 'number_1', '女会员': 'number_2'}

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
        db_table = 'AnnualGender'


# desc :year-month  Annualuser  Short-termuser  Short-termuser/Annualuser
class Annualorshort(models.Model):
    number_1 = models.CharField(db_column='1', primary_key=True,
                                max_length=255)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.CharField(db_column='2', max_length=255, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.CharField(db_column='3', max_length=255, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4 = models.CharField(db_column='4', max_length=255, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.

    char_field_dict = {'year-month': 'number_1', 'AnnualUser': 'number_2', 'Short_TermUser': 'number_3',
                       'Short-TermUser/AnnualUser': 'number_4'}

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
        db_table = 'AnnualOrShort'


# desc : station_id  availableDock  year-month 最后一个自增 略去
class Avaidockavg(models.Model):
    number_1 = models.CharField(db_column='1', max_length=255, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.CharField(db_column='2', max_length=255, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.CharField(db_column='3', max_length=255, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4 = models.AutoField(db_column='4',
                                primary_key=True)  # Field renamed because it wasn't a valid Python identifier.

    char_field_dict = {'station_id': 'number_1', 'AvailabelDock': 'number_2', 'year-month': 'number_3'}

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
        db_table = 'AvaiDockAvg'


# static sql_error
# desc : depart 24h into 4 parts:# 0-6# 6-12# 12-18# 18-24
class Dur6Hours(models.Model):
    number_1 = models.CharField(db_column='1', primary_key=True,
                                max_length=20)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.SmallIntegerField(db_column='2', blank=True,
                                        null=True)  # Field renamed because it wasn't a valid Python identifier.
    char_field_dict = {'男骑行者数': 'number_1', '男骑行者_总时长（h）': 'number_2', '女骑行者数': 'number_3', '女骑行者_总时长（h）': 'number_4'}

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
        db_table = 'Dur6hours'


# desc :男骑行者数，总时长（小时），女骑行者，总时长
class Gendertime(models.Model):
    number_1 = models.IntegerField(db_column='1',
                                   primary_key=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.CharField(db_column='2', max_length=255, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.IntegerField(db_column='3', blank=True,
                                   null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4 = models.CharField(db_column='4', max_length=255, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    char_field_dict = {'男骑行者数': 'number_1', '男骑行者_总时长（h）': 'number_2', '女骑行者数': 'number_3', '女骑行者_总时长（h）': 'number_4'}

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
        db_table = 'GenderTime'


# desc :站台，一个月中平均每天损坏车数，月份
class Monavgunavbike(models.Model):
    number_1 = models.CharField(db_column='1', max_length=20, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.CharField(db_column='2', max_length=20, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.CharField(db_column='3', max_length=20, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.

    char_field_dict = {'站台': 'number_1', '一个月中平均每天损坏车数': 'number_2', '月份': 'number_3'}

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
        db_table = 'MonAvgUnavBike'


# desc :
# MonAvgUnavBike
# 站台，一个月中平均每天损坏车位数，月份
class Monavgunavpark(models.Model):
    number_1 = models.CharField(db_column='1', max_length=20, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.CharField(db_column='2', max_length=20, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.CharField(db_column='3', max_length=20, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4 = models.AutoField(db_column='4',
                                primary_key=True)  # Field renamed because it wasn't a valid Python identifier.

    char_field_dict = {'站台': 'number_1', '一个月中平均每天损坏车位数': 'number_2', '月份': 'number_3'}

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
        db_table = 'MonAvgUnavPark'


# desc : 3/19 3/20 3/21 3/22 3/23 3/24 3/25
class Rainday(models.Model):
    number_3_20_2015 = models.IntegerField(db_column='3/20/2015',
                                           primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_21_2015 = models.IntegerField(db_column='3/21/2015', blank=True,
                                           null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_22_2015 = models.IntegerField(db_column='3/22/2015', blank=True,
                                           null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_23_2015 = models.IntegerField(db_column='3/23/2015', blank=True,
                                           null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_24_2015 = models.IntegerField(db_column='3/24/2015', blank=True,
                                           null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_26_2015 = models.IntegerField(db_column='3/26/2015', blank=True,
                                           null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_27_2015 = models.IntegerField(db_column='3/27/2015', blank=True,
                                           null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    char_field_dict = {'3/20': 'number_3_20_2015', '3/21': 'number_3_21_2015', '3/22': 'number_3_22_2015',
                       '3/23': 'number_3_23_2015', '3/24': 'number_3_24_2015', '3/25': 'number_3_23_2015',
                       '3/26': 'number_3_26_2015', '3/27': 'number_3_27_2015'}

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
        db_table = 'RainDay'


# desc : year-month  rideNum_monthly
class Ridenummonthly(models.Model):
    number_1 = models.CharField(db_column='1', primary_key=True,
                                max_length=20)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.CharField(db_column='2', max_length=10, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.

    char_field_dict = {'year-month': 'number_1', 'rideNum_month': 'number_2'}

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
        db_table = 'RideNumMonthly'


# desc : station_id  Avg_availableBike  year-month
class Staavainum(models.Model):
    number_1 = models.SmallIntegerField(db_column='1', blank=True,
                                        null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.SmallIntegerField(db_column='2', blank=True,
                                        null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.CharField(db_column='3', primary_key=True,
                                max_length=10)  # Field renamed because it wasn't a valid Python identifier.
    char_field_dict = {'station_id': 'number_1', 'AvgAvaliableBike': 'number_2', 'year-month': 'number_3'}

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
        db_table = 'StaAvaiNum'


# desc : station_id  DockNum  date
class Staonline(models.Model):
    number_1 = models.CharField(db_column='1', primary_key=True,
                                max_length=30)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.CharField(db_column='2', max_length=30, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.CharField(db_column='3', max_length=30, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.

    char_field_dict = {'station_id': 'number_1', 'DockNum': 'number_2', 'date': 'number_3'}

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
        db_table = 'StaOnline'


# desc : 5/14 5/15 5/16 5/17 5/18 5/19 5/20
class Sunday(models.Model):
    number_5_14_2015 = models.IntegerField(db_column='5/14/2015',
                                           primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_15_2015 = models.IntegerField(db_column='5/15/2015', blank=True,
                                           null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_16_2015 = models.IntegerField(db_column='5/16/2015', blank=True,
                                           null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_17_2015 = models.IntegerField(db_column='5/17/2015', blank=True,
                                           null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_18_2015 = models.IntegerField(db_column='5/18/2015', blank=True,
                                           null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_19_2015 = models.IntegerField(db_column='5/19/2015', blank=True,
                                           null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_20_2015 = models.IntegerField(db_column='5/20/2015', blank=True,
                                           null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    char_field_dict = {'5/14': 'number_5_14_2015', '5/15': 'number_5_15_2015', '5/16': 'number_5_16_2015',
                       '5/17': 'number_5_17_2015', '5/18': 'number_5_18_2015', '5/19': 'number_5_19_2015',
                       '5/20': 'number_5_20_2015'}

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
        db_table = 'SunDay'


# desc :
# ID  date  start_stationID  lat  long
# ID  date  end_stationID lat  long
class TripFlow(models.Model):
    id = models.BigAutoField(primary_key=True)
    number_1 = models.CharField(db_column='1', max_length=255, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.CharField(db_column='2', max_length=255, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.CharField(db_column='3', max_length=255, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4 = models.CharField(db_column='4', max_length=255, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5 = models.CharField(db_column='5', max_length=255, blank=True,
                                null=True)  # Field renamed because it wasn't a valid Python identifier.

    char_field_dict = {'ID': 'number_1', 'date': 'number_2', 'start/end_stationID': 'number_3', 'lat': 'number_4',
                       'long': 'number_5'}

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
        db_table = 'Trip_Flow'
