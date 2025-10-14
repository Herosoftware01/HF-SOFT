from django.db import models
from datetime import date


class JobAllocation(models.Model):
    machine_id = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    emp_name_1 = models.CharField(max_length=100, blank=True)
    emp_id1 = models.CharField(max_length=20, blank=True)
    emp_name_2 = models.CharField(max_length=100, blank=True)
    emp_id2 = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"Machine {self.machine_id} - {self.date}"


class Punchdtls1(models.Model):
    unitname = models.CharField(db_column='Unitname', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dt = models.DateTimeField(blank=True, null=True)
    shift = models.IntegerField(blank=True, null=True)
    intime = models.DateTimeField(blank=True, null=True)
    outtime = models.DateTimeField(blank=True, null=True)
    sl = models.IntegerField(blank=True, null=True)
    # id = models.IntegerField(blank=True, null=True)
    id = models.ForeignKey(
            'Empwisesal',
            on_delete=models.DO_NOTHING,
            to_field='code',
            db_column='id',
            blank=True,
            null=True
        )
    latemin = models.IntegerField(blank=True, null=True)
    wrk_cat = models.CharField(max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    a_intime = models.DateTimeField(blank=True, null=True)
    a_outtime = models.DateTimeField(blank=True, null=True)
    o_intime = models.DateTimeField(blank=True, null=True)
    o_outtime = models.DateTimeField(blank=True, null=True)
    br_out = models.DateTimeField(blank=True, null=True)
    br_in = models.DateTimeField(blank=True, null=True)
    br_out1 = models.DateTimeField(blank=True, null=True)
    br_in1 = models.DateTimeField(blank=True, null=True)
    id1 = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'PunchDtls1'


class Empwisesal(models.Model):
    dept = models.CharField(max_length=50, blank=True, null=True)
    code = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    salary = models.DecimalField(db_column='Salary', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    night = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    sl = models.IntegerField(blank=True, null=True)
    orissa = models.CharField(max_length=3,blank=True, null=True)
    grp1 = models.IntegerField(blank=True, null=True)
    grp2 = models.IntegerField(blank=True, null=True)
    wrkunit = models.CharField(max_length=50,blank=True, null=True)
    prs = models.CharField(max_length=5000,blank=True, null=True)
    disprs = models.CharField(max_length=5000,blank=True, null=True)
    hostel = models.CharField(db_column='Hostel', max_length=50,blank=True, null=True)  # Field name made lowercase.
    roomdtls = models.CharField(db_column='Roomdtls', max_length=50,blank=True, null=True)  # Field name made lowercase.
    shift_contract = models.CharField(db_column='Shift_Contract', max_length=1,blank=True, null=True)  # Field name made lowercase.
    reportsl = models.IntegerField(db_column='Reportsl', blank=True, null=True)  # Field name made lowercase.
    intercom = models.CharField(max_length=50,blank=True, null=True)
    mobile = models.CharField(max_length=50,blank=True, null=True)
    attach = models.CharField(max_length=1550,blank=True, null=True)
    status = models.CharField(max_length=25,blank=True, null=True)
    bank = models.CharField(db_column='Bank', max_length=200,blank=True, null=True)  # Field name made lowercase.
    accountdetails = models.CharField(db_column='Accountdetails', max_length=200,blank=True, null=True)  # Field name made lowercase.
    grp3 = models.IntegerField(blank=True, null=True)
    salary1 = models.DecimalField(db_column='Salary1', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    otallowed = models.CharField(max_length=3,blank=True, null=True)
    branch = models.CharField(max_length=50,blank=True, null=True)
    badd = models.CharField(max_length=200,blank=True, null=True)
    ifscno = models.CharField(max_length=200,blank=True, null=True)
    bank1 = models.CharField(max_length=200,blank=True, null=True)
    branch1 = models.CharField(max_length=200,blank=True, null=True)
    badd1 = models.CharField(max_length=200,blank=True, null=True)
    ifscno1 = models.CharField(max_length=200,blank=True, null=True)
    accountdetails1 = models.CharField(db_column='Accountdetails1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bact = models.IntegerField(blank=True, null=True)
    qualification = models.CharField(db_column='Qualification', max_length=50, blank=True, null=True)  # Field name made lowercase.
    jdt = models.DateTimeField(blank=True, null=True)
    joindt = models.DateTimeField(db_column='JoinDt', blank=True, null=True)  # Field name made lowercase.
    resigndt = models.DateTimeField(db_column='resignDt', blank=True, null=True)  # Field name made lowercase.
    rdt = models.DateTimeField(blank=True, null=True)
    rsysdt = models.DateTimeField(blank=True, null=True)
    grp4 = models.IntegerField(blank=True, null=True)
    pftype = models.CharField(max_length=10,blank=True, null=True)
    curwrkunit = models.CharField(db_column='CurWrkUnit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(max_length=1,blank=True, null=True)
    inch = models.CharField(max_length=3,blank=True, null=True)
    nattgrp = models.CharField(max_length=20,blank=True, null=True)
    northindian = models.CharField(max_length=3,blank=True, null=True)
    inspection = models.CharField(db_column='Inspection', max_length=3,blank=True, null=True)  # Field name made lowercase.
    ins_incharge = models.CharField(db_column='Ins_Incharge', max_length=100,blank=True, null=True)  # Field name made lowercase.
    atharrecd = models.CharField(max_length=3,blank=True, null=True)
    atharcdob = models.CharField(max_length=3,blank=True, null=True)
    aempwatch = models.CharField(max_length=3,blank=True, null=True)
    photo = models.CharField(max_length=400,blank=True, null=True)
    empprs = models.CharField(db_column='Empprs', max_length=80,blank=True, null=True)  # Field name made lowercase.
    skilled = models.CharField(db_column='Skilled', max_length=10,blank=True, null=True)  # Field name made lowercase.
    ej = models.DateTimeField(blank=True, null=True)
    vanno = models.CharField(max_length=25,blank=True, null=True)
    esino = models.CharField(max_length=50,blank=True, null=True)
    pfno = models.CharField(max_length=50,blank=True, null=True)
    ladd1 = models.CharField(db_column='LADD1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    padd1 = models.CharField(db_column='PADD1', max_length=50,blank=True, null=True)  # Field name made lowercase.
    padd2 = models.CharField(db_column='PADD2', max_length=50,blank=True, null=True)  # Field name made lowercase.
    pcity = models.CharField(db_column='PCITY', max_length=50,blank=True, null=True)  # Field name made lowercase.
    pstate = models.CharField(db_column='PSTATE', max_length=50,blank=True, null=True)  # Field name made lowercase.
    ppincode = models.CharField(db_column='PPINCODE', max_length=50,blank=True, null=True)  # Field name made lowercase.
    emc = models.CharField(db_column='EMC', max_length=50,blank=True, null=True)  # Field name made lowercase.
    ladd2 = models.CharField(db_column='LADD2', max_length=50,blank=True, null=True)  # Field name made lowercase.
    lcity = models.CharField(db_column='LCITY', max_length=50,blank=True, null=True)  # Field name made lowercase.
    lstate = models.CharField(db_column='LSTATE', max_length=50,blank=True, null=True)  # Field name made lowercase.
    lpincode = models.CharField(db_column='LPINCODE', max_length=50,blank=True, null=True)  # Field name made lowercase.
    hra_per = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    hra_amt = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    relation = models.CharField(max_length=20,blank=True, null=True)
    emc_pers = models.CharField(max_length=100,blank=True, null=True)
    pcsrate = models.CharField(db_column='Pcsrate', max_length=3,blank=True, null=True)  # Field name made lowercase.
    p_inch = models.IntegerField(db_column='P_Inch', blank=True, null=True)  # Field name made lowercase.
    l = models.CharField(max_length=150,blank=True, null=True)
    grpnew = models.IntegerField(db_column='grpNew', blank=True, null=True)  # Field name made lowercase.
    mon_lab = models.CharField(db_column='Mon_Lab', max_length=1,blank=True, null=True)  # Field name made lowercase.
    comm_lab = models.CharField(db_column='Comm_Lab', max_length=1,blank=True, null=True)  # Field name made lowercase.
    comm_amt = models.DecimalField(db_column='Comm_Amt', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    comm_grp = models.CharField(db_column='Comm_grp', max_length=10,blank=True, null=True)  # Field name made lowercase.
    pcat = models.IntegerField(blank=True, null=True)
    dcs = models.IntegerField(blank=True, null=True)
    bg = models.CharField(max_length=50,blank=True, null=True)
    approved = models.CharField(db_column='Approved', max_length=1,blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(max_length=30,blank=True, null=True)
    tasstaff = models.CharField(max_length=3,blank=True, null=True)
    monthlysalary = models.CharField(db_column='MonthlySalary', max_length=1,blank=True, null=True)  # Field name made lowercase.
    mjoindt = models.DateField(blank=True, null=True)
    # ncat = models.ForeignKey('MempCategory', models.DO_NOTHING, blank=True, null=True)
    mcategory = models.CharField(max_length=50,blank=True, null=True)
    vc = models.TextField()  # This field type is a guess.
    id = models.AutoField(primary_key=True)
    aliasname = models.CharField(max_length=50,blank=True, null=True)
    whatsappgrp = models.CharField(db_column='WhatsappGrp', max_length=2000,blank=True, null=True)  # Field name made lowercase.
    createddt = models.DateTimeField(blank=True, null=True)
    modifieddt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EmpwiseSal'



class VueRl001(models.Model):
    rowno = models.BigIntegerField(db_column='RowNo', primary_key=True)  # Field name made lowercase.
    dt = models.DateTimeField()
    ty = models.CharField(max_length=8)
    dc = models.CharField(max_length=25, blank=True, null=True)
    rlno = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    colour = models.IntegerField()
    fabdescr = models.IntegerField()
    fab = models.CharField(max_length=35)
    diaid = models.IntegerField()
    dia = models.CharField(max_length=35)
    weight = models.DecimalField(max_digits=18, decimal_places=3)
    mtr = models.DecimalField(max_digits=18, decimal_places=2)
    lotno = models.CharField(max_length=10, blank=True, null=True)
    jobno = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'vue_rl001'



class mastermistakes(models.Model):
    choice=(
        ('C','Count'),
        ('M','Meter'),
        ('P','Popup'),)
    ty = models.CharField(max_length=1)
    dt = models.DateTimeField()
    mist1_eng = models.CharField(db_column='Mist1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mist2_eng = models.CharField(db_column='Mist2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mist3_eng = models.CharField(db_column='Mist3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mist4_eng = models.CharField(db_column='Mist4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mist5_eng = models.CharField(db_column='Mist5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mist6_eng = models.CharField(max_length=50, blank=True, null=True)
    mist7_eng = models.CharField(max_length=50, blank=True, null=True)
    mist8_eng = models.CharField(max_length=50, blank=True, null=True)
    mist9_eng = models.CharField(max_length=50, blank=True, null=True)
    mist10_eng = models.CharField(max_length=50, blank=True, null=True)
    mist11_eng = models.CharField(db_column='MIST11', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mist12_eng = models.CharField(db_column='MIST12', max_length=50,blank=True, null=True)  # Field name made lowercase.
    m1_choice = models.CharField(max_length=1, choices=choice, blank=True, null=True)
    m2_choice = models.CharField(max_length=1, choices=choice, blank=True, null=True)
    m3_choice = models.CharField(max_length=1, choices=choice, blank=True, null=True)
    m4_choice = models.CharField(max_length=1, choices=choice, blank=True, null=True)
    m5_choice = models.CharField(max_length=1, choices=choice, blank=True, null=True)
    m6_choice = models.CharField(max_length=1, choices=choice, blank=True, null=True)
    m7_choice = models.CharField(max_length=1, choices=choice, blank=True, null=True)
    m8_choice = models.CharField(max_length=1, choices=choice, blank=True, null=True)
    m9_choice = models.CharField(max_length=1, choices=choice, blank=True, null=True)
    m10_choice = models.CharField(max_length=1, choices=choice, blank=True, null=True)
    m11_choice = models.CharField(max_length=1, choices=choice, blank=True, null=True)
    m12_choice = models.CharField(max_length=1, choices=choice, blank=True, null=True)
    mist1_ta = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    mist2_ta = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    mist3_ta = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    mist4_ta = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    mist5_ta = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    mist6_ta = models.CharField(max_length=50, blank=True, null=True)
    mist7_ta = models.CharField(max_length=50,blank=True, null=True)
    mist8_ta = models.CharField(max_length=50, blank=True, null=True)
    mist9_ta = models.CharField(max_length=50,blank=True, null=True)
    mist10_ta = models.CharField(max_length=50,blank=True, null=True)
    mist11_ta = models.CharField(max_length=50,blank=True, null=True)  # Field name made lowercase.
    mist12_ta = models.CharField( max_length=50,blank=True, null=True)  # Field name made lowercase.
    mist1_hin = models.CharField( max_length=50,blank=True, null=True)  # Field name made lowercase.
    mist2_hin = models.CharField(max_length=50,blank=True, null=True)  # Field name made lowercase.
    mist3_hin = models.CharField(max_length=50,blank=True, null=True)  # Field name made lowercase.
    mist4_hin = models.CharField( max_length=50,blank=True, null=True)  # Field name made lowercase.
    mist5_hin = models.CharField(max_length=50,blank=True, null=True)  # Field name made lowercase.
    mist6_hin = models.CharField(max_length=50, blank=True, null=True)
    mist7_hin = models.CharField(max_length=50,blank=True, null=True)
    mist8_hin = models.CharField(max_length=50,blank=True, null=True)
    mist9_hin = models.CharField(max_length=50,blank=True, null=True)
    mist10_hin = models.CharField(max_length=50,blank=True, null=True)
    mist11_hin = models.CharField(max_length=50,blank=True, null=True)  # Field name made lowercase.
    mist12_hin = models.CharField(max_length=50,blank=True, null=True)  # Field name made lowercase.
    mist1_img = models.ImageField(upload_to='mistake_images/', blank=True, null=True)
    mist2_img = models.ImageField(upload_to='mistake_images/', blank=True, null=True)
    mist3_img = models.ImageField(upload_to='mistake_images/', blank=True, null=True)
    mist4_img = models.ImageField(upload_to='mistake_images/', blank=True, null=True)
    mist5_img = models.ImageField(upload_to='mistake_images/', blank=True, null=True)
    mist6_img = models.ImageField(upload_to='mistake_images/', blank=True, null=True)
    mist7_img = models.ImageField(upload_to='mistake_images/', blank=True, null=True)
    mist8_img = models.ImageField(upload_to='mistake_images/', blank=True, null=True)
    mist9_img = models.ImageField(upload_to='mistake_images/', blank=True, null=True)
    mist10_img = models.ImageField(upload_to='mistake_images/', blank=True, null=True)
    mist11_img = models.ImageField(upload_to='mistake_images/', blank=True, null=True)
    mist12_img = models.ImageField(upload_to='mistake_images/', blank=True, null=True)
    m1 = models.IntegerField(blank=True, null=True,db_column='M1')  # Field name made lowercase.
    m2 = models.IntegerField(blank=True, null=True,db_column='M2')  # Field name made lowercase.
    m3 = models.IntegerField(blank=True, null=True,db_column='M3')  # Field name made lowercase.
    m4 = models.IntegerField(blank=True, null=True,db_column='M4')  # Field name made lowercase.
    m5 = models.IntegerField(blank=True, null=True,db_column='M5')  # Field name made lowercase.
    m6 = models.IntegerField(blank=True, null=True,db_column='M6')
    m7 = models.IntegerField(blank=True, null=True,db_column='M7')
    m8 = models.IntegerField(blank=True, null=True,db_column='M8')
    m9 = models.IntegerField(blank=True, null=True,db_column='M9')
    m10 = models.IntegerField(blank=True, null=True,db_column='M10')
    m11 = models.IntegerField(blank=True, null=True,db_column='M11')  # Field name made lowercase.
    m12 = models.IntegerField(blank=True, null=True,db_column='M12')  # Field name made lowercase.



class VueOrdersinhand(models.Model):
    uom = models.CharField(max_length=5, blank=True, null=True)
    fdeldt = models.CharField(max_length=30, blank=True, null=True)
    img = models.CharField(max_length=82, blank=True, null=True)
    director = models.CharField(max_length=35)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    con = models.CharField(db_column='Con', max_length=193, blank=True, null=True)  # Field name made lowercase.
    o_filnam = models.CharField(max_length=8000, blank=True, null=True)
    o_styledesc = models.CharField(db_column='o_StyleDesc', max_length=35, blank=True, null=True)  # Field name made lowercase.
    o_week = models.CharField(max_length=750)
    o_wk = models.CharField(max_length=1)
    o_01_prn = models.CharField(max_length=750)
    o_03_emb = models.CharField(db_column='o_03_Emb', max_length=750)  # Field name made lowercase.
    o_ordtype = models.CharField(db_column='o_OrdType', max_length=6)  # Field name made lowercase.
    o_orderno = models.CharField(db_column='o_Orderno', max_length=50)  # Field name made lowercase.
    o_finaldelvdate = models.DateField(db_column='o_FinalDelvdate', blank=True, null=True)  # Field name made lowercase.
    o_buyer = models.CharField(db_column='o_Buyer', max_length=40, blank=True, null=True)  # Field name made lowercase.
    o_merch = models.CharField(max_length=35, blank=True, null=True)
    o_ordqty = models.IntegerField(blank=True, null=True)
    o_productionunit = models.CharField(db_column='o_ProductionUnit', max_length=35)  # Field name made lowercase.
    o_prodtype = models.CharField(db_column='o_ProdType', max_length=7)  # Field name made lowercase.
    o_buy = models.CharField(db_column='o_Buy', max_length=5, blank=True, null=True)  # Field name made lowercase.
    o_45_cut = models.CharField(max_length=750)
    o_17_sam = models.CharField(max_length=750)
    o_19_erun = models.CharField(db_column='o_19_Erun', max_length=750)  # Field name made lowercase.
    o_21_prun = models.CharField(db_column='o_21_Prun', max_length=750)  # Field name made lowercase.
    o_08_frun = models.CharField(db_column='o_08_Frun', max_length=750)  # Field name made lowercase.
    o_50_run = models.CharField(db_column='o_50_Run', max_length=750)  # Field name made lowercase.
    o_149 = models.CharField(max_length=750)
    o_07 = models.CharField(max_length=750)
    o_37 = models.CharField(max_length=750)
    o_36 = models.CharField(max_length=750)
    o_46 = models.CharField(max_length=750)
    o_10 = models.CharField(max_length=750)
    o_qname = models.CharField(max_length=35, blank=True, null=True)
    o_ordvalue = models.DecimalField(db_column='o_ordValue', max_digits=38, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    stylename = models.CharField(db_column='StyleName', max_length=50)  # Field name made lowercase.
    o_cur = models.CharField(max_length=35, blank=True, null=True)
    o_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    inchargename = models.CharField(db_column='Inchargename', max_length=83)  # Field name made lowercase.
    price_ind = models.DecimalField(db_column='Price_Ind', max_digits=38, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    exrate = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    o_customerid = models.IntegerField(db_column='o_Customerid', blank=True, null=True)  # Field name made lowercase.
    filnam = models.CharField(max_length=82, blank=True, null=True)
    actdate = models.CharField(db_column='ActDate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    orderno = models.CharField(db_column='OrderNo', max_length=50 , primary_key=True)  # Field name made lowercase.
    o_45141 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'vue_Ordersinhand'



class mistake_image(models.Model):
    lot_no = models.CharField(max_length=50)
    job_no = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=50)
    machine_id = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'images')



class master_roll_update(models.Model):
    roll_no = models.CharField(max_length=50)
    dc_no = models.CharField(max_length=50)
    lot_no = models.CharField(max_length=50)
    field_id = models.CharField(max_length=10)
    types = models.CharField(max_length=50 , null=True , blank=True)
    timer =models.TimeField(null=True , blank=True)
    m1 = models.CharField(max_length=50 , null=True , blank=True)
    m2 = models.CharField(max_length=50 , null=True , blank=True)
    m3 = models.CharField(max_length=50 , null=True , blank=True)
    m4 = models.CharField(max_length=50 , null=True , blank=True)
    m5 = models.CharField(max_length=50 , null=True , blank=True)
    m6 = models.CharField(max_length=50 , null=True , blank=True)
    m7 = models.CharField(max_length=50 , null=True , blank=True)
    m8 = models.CharField(max_length=50 , null=True , blank=True)
    m9 = models.CharField(max_length=50 , null=True , blank=True)
    m10 = models.CharField(max_length=50 , null=True , blank=True)
    m11 = models.CharField(max_length=50 , null=True , blank=True)
    m12 = models.CharField(max_length=50 , null=True , blank=True)
    remarks = models.CharField(max_length=200 , null=True , blank=True)

    class Meta:
        db_table = 'master_roll_update'


class master_final_mistake(models.Model):

    roll_no = models.CharField(max_length=50)
    machine_id = models.CharField(max_length=50)
    job_no = models.CharField(max_length=50)
    dc_no = models.CharField(max_length=50)
    lot_no = models.CharField(max_length=50)
    field_id = models.CharField(max_length=10)
    types = models.CharField(max_length=50 , null=True , blank=True)
    timer =models.TimeField(null=True , blank=True)
    m1 = models.CharField(max_length=50 , null=True , blank=True)
    m2 = models.CharField(max_length=50 , null=True , blank=True)
    m3 = models.CharField(max_length=50 , null=True , blank=True)
    m4 = models.CharField(max_length=50 , null=True , blank=True)
    m5 = models.CharField(max_length=50 , null=True , blank=True)
    m6 = models.CharField(max_length=50 , null=True , blank=True)
    m7 = models.CharField(max_length=50 , null=True , blank=True)
    m8 = models.CharField(max_length=50 , null=True , blank=True)
    m9 = models.CharField(max_length=50 , null=True , blank=True)
    m10 = models.CharField(max_length=50 , null=True , blank=True)
    m11 = models.CharField(max_length=50 , null=True , blank=True)
    m12 = models.CharField(max_length=50 , null=True , blank=True)
    finish_dia = models.CharField(max_length=50 , null=True , blank=True)
    total_meters = models.CharField(max_length=50 , null=True , blank=True)
    act_gsm = models.CharField(max_length=50 , null=True , blank=True)
    remarks = models.CharField(max_length=200 , null=True , blank=True)
    date = models.DateField(auto_now_add=True)
    # date = models.DateField(auto_now=True,null=True)

    class Meta:
        db_table = 'master_final_mistake'


class Lotsticker(models.Model):
    sl = models.AutoField(db_column='Sl', primary_key=True)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lotno = models.CharField(db_column='LotNo', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    fabric = models.CharField(db_column='Fabric', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    rollno = models.CharField(db_column='RollNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dcno = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    wgt = models.DecimalField(db_column='Wgt', max_digits=18, decimal_places=2)  # Field name made lowercase.
    m1 = models.CharField(db_column='M1', max_length=550, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    m2 = models.CharField(db_column='M2', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    m3 = models.CharField(db_column='M3', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    m4 = models.CharField(db_column='M4', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    m5 = models.CharField(db_column='M5', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    m6 = models.CharField(db_column='M6', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    m7 = models.CharField(db_column='M7', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    m8 = models.CharField(db_column='M8', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    m9 = models.CharField(db_column='M9', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    m10 = models.CharField(db_column='M10', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    m12 = models.CharField(db_column='M12', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    fdia = models.CharField(db_column='Fdia', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    mtr = models.DecimalField(db_column='Mtr', max_digits=18, decimal_places=2)  # Field name made lowercase.
    m11 = models.CharField(max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jobno = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dia = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    gsm = models.IntegerField(blank=True, null=True)
    re = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    em = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    u = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LotSticker'


class VueFindia(models.Model):
    rownum = models.BigIntegerField(db_column='RowNum', primary_key=True)  # Field name made lowercase.
    orderno = models.CharField(db_column='OrderNo', max_length=50)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fabric = models.CharField(db_column='Fabric', max_length=35)  # Field name made lowercase.
    dia = models.CharField(db_column='Dia', max_length=35)  # Field name made lowercase.
    finaldia = models.CharField(db_column='FinalDia', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vue_findia'


class back_permissions(models.Model):
    Emp_id = models.IntegerField()
    Password = models.CharField(max_length=6)
    id = models.AutoField(primary_key=True)


class BreakTime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(default=True)  # so you can toggle it

    def __str__(self):
        return f"Break from {self.start_time} to {self.end_time}"