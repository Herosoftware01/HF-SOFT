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