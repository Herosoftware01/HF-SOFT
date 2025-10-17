from django.db import models

# Create your models here.
class AttUnt(models.Model):
    rowno = models.BigIntegerField(db_column='RowNo',primary_key=True)  # Field name made lowercase.
    Date = models.DateTimeField(blank=True, null=True,db_column='dt')
    dept = models.CharField(db_column='DEPT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    onroll = models.IntegerField(blank=True, null=True)
    present = models.IntegerField(blank=True, null=True)
    absent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vue_att_unt'


class VueOverall1(models.Model):
    o_ordqty = models.IntegerField(blank=True, null=True)
    o_merch = models.CharField(max_length=35, blank=True, null=True)
    Image = models.CharField(max_length=82, blank=True, null=True,db_column='filnam')
    unit = models.CharField(max_length=50)
    jobno = models.CharField(max_length=50,primary_key=True)
    topbottom_des = models.CharField(db_column='TopBottom_des', max_length=50, blank=True, null=True)  # Field name made lowercase.
    clr = models.CharField(max_length=50, blank=True, null=True)
    bc = models.IntegerField(blank=True, null=True)
    sew = models.IntegerField(blank=True, null=True)
    tc = models.IntegerField(blank=True, null=True)
    fc = models.IntegerField(blank=True, null=True)
    ir = models.IntegerField(blank=True, null=True)
    pac = models.IntegerField(blank=True, null=True)
    # o_buyer = models.CharField(db_column='o_Buyer', max_length=40, blank=True, null=True)  # Field name made lowercase.
    # stylename = models.CharField(db_column='StyleName', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vue_overall1'


class BillAge(models.Model):
    no = models.IntegerField(db_column='No', primary_key=True)  # Field name made lowercase.
    edate = models.DateTimeField(db_column='EDate')  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate')  # Field name made lowercase.
    billno = models.CharField(db_column='BillNo', max_length=50)  # Field name made lowercase.
    module = models.CharField(db_column='Module', max_length=50, blank=True, null=True)  # Field name made lowercase.
    suppliers = models.CharField(db_column='Suppliers', max_length=35, blank=True, null=True)  # Field name made lowercase.
    employees = models.CharField(db_column='Employees', max_length=35, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    billpassed = models.SmallIntegerField(db_column='BillPassed')  # Field name made lowercase.
    br_ageing = models.IntegerField(db_column='BR Ageing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billdate_ageing = models.IntegerField(db_column='BillDate Ageing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'bill_age'

    
class ResignDtls(models.Model):
    slno = models.BigIntegerField(db_column='SlNo', primary_key=True)  # Field name made lowercase.
    code = models.IntegerField()
    photo = models.CharField(max_length=400, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    dept = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(db_column='Category', max_length=50, blank=True, null=True)  # Field name made lowercase.
    joindt = models.DateTimeField(db_column='JoinDt', blank=True, null=True)  # Field name made lowercase.
    resigndt = models.DateTimeField(db_column='resignDt', blank=True, null=True)  # Field name made lowercase.
    days_worked = models.IntegerField(db_column='Days_Worked', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vue_resign_Dtls'