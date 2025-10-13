from django.db import models

# Create your models here.


class layemployee(models.Model):
    emp1 = models.CharField(max_length=100)
    emp2 = models.CharField(max_length=100)
    emp3 = models.CharField(max_length=100)
    emp4 = models.CharField(max_length=100)
    emp5 = models.CharField(max_length=100)
    emp6 = models.CharField(max_length=100)
    table =models.IntegerField()
    date = models.DateField( auto_now_add=True )


class Punchdtls1(models.Model):
    unitname = models.CharField(db_column='Unitname', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dt = models.DateTimeField(blank=True, null=True)
    shift = models.IntegerField(blank=True, null=True)
    intime = models.DateTimeField(blank=True, null=True)
    outtime = models.DateTimeField(blank=True, null=True)
    sl = models.IntegerField(blank=True, null=True)
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




class VuePlandtlsTablewise(models.Model):
    rownum = models.BigIntegerField(db_column='RowNum', primary_key=True)  # Field name made lowercase.
    planno = models.IntegerField()
    tableno = models.IntegerField()
    jobno = models.CharField(db_column='Jobno', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lotno = models.CharField(max_length=10)
    ply = models.IntegerField(blank=True, null=True)
    wgt = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    lay_lenmtr = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    clrcomb = models.CharField(max_length=50)
    sample_descr = models.CharField(db_column='Sample_Descr', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vue_plandtls_tablewise'

class VuePlandetails(models.Model):
    rownum = models.BigIntegerField(db_column='RowNum', primary_key=True)  # Field name made lowercase.
    planno = models.IntegerField(db_column='Planno')  # Field name made lowercase.
    jobno = models.CharField(db_column='Jobno', max_length=50)  # Field name made lowercase.
    markerno = models.CharField(db_column='MARKERNO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fabclr = models.CharField(db_column='FABCLR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lotno = models.CharField(max_length=10)
    clrcomb = models.CharField(max_length=50)
    lay_lenmtr = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tabledia = models.DecimalField(db_column='tABLEDIA', max_digits=18, decimal_places=2)  # Field name made lowercase.
    cuttabledia = models.DecimalField(db_column='CUTTABLEDIA', max_digits=18, decimal_places=2)  # Field name made lowercase.
    prgdia = models.CharField(db_column='PRGDIA', max_length=50)  # Field name made lowercase.
    progwgt = models.DecimalField(db_column='PROGWGT', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    avgwgt = models.CharField(db_column='AVGWGT', max_length=4000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vue_plandetails'


class overwrite_permissions(models.Model):
    Emp_id = models.IntegerField()
    Password = models.CharField(max_length=6)
    id = models.AutoField(primary_key=True)


class table_lock(models.Model):
    table_no_1 = models.BooleanField()
    table_no_2 = models.BooleanField()
    id = models.AutoField(primary_key=True)


class lay_data_update(models.Model):
    id = models.AutoField(primary_key=True)
    plan_no = models.CharField(max_length=50,blank=True, null=True)
    date = models.DateField( auto_now_add=True )
    timer = models.CharField(max_length=50)
    brown_sheet_timer = models.CharField(max_length=50,blank=True, null=True)
    join_marker_timer = models.CharField(max_length=50,blank=True, null=True)
    plan_no = models.CharField(max_length=50,blank=True, null=True)
    job_no = models.CharField(max_length=50,blank=True, null=True)
    marker_no = models.CharField(max_length=50,blank=True, null=True)
    


class TrsCplan4(models.Model):
    planno = models.IntegerField(db_column='Planno')  # Field name made lowercase.
    markerno = models.IntegerField()
    rlno = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    planwgt = models.DecimalField(max_digits=18, decimal_places=3)
    ply = models.IntegerField(blank=True, null=True)
    planmtr = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    estply = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    usdanthr = models.CharField(max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    rlwgt = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    fdia = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    rejwgt = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    sl = models.AutoField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'Trs_cplan4'


class roll_data_update(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField( auto_now_add=True )
    timer = models.CharField(max_length=50)
    plan_no = models.CharField(max_length=50,blank=True, null=True)
    job_no = models.CharField(max_length=50,blank=True, null=True)
    roll_no = models.CharField(max_length=50,blank=True, null=True)
    f_dia = models.CharField(max_length=50,blank=True, null=True)
    plan_ply = models.CharField(max_length=50,blank=True, null=True)
    scl_wgt = models.CharField(max_length=50,blank=True, null=True)
    plan_obwgt = models.CharField(max_length=50,blank=True, null=True)
    req_wgt = models.CharField(max_length=50,blank=True, null=True)
    actual_dia = models.CharField(max_length=50,blank=True, null=True)
    actual_ply = models.CharField(max_length=50,blank=True, null=True)
    actual_obwgt = models.CharField(max_length=50,blank=True, null=True)
    end_bit = models.CharField(max_length=50,blank=True, null=True)
    bal_wgt = models.CharField(max_length=50,blank=True, null=True)
    remarks = models.CharField(max_length=150,blank=True, null=True)


class final_plans(models.Model):
    id = models.AutoField(primary_key=True)
    plan_no = models.CharField(max_length=50,blank=True, null=True)
    job_no = models.CharField(max_length=50,blank=True, null=True)
    marker_no = models.CharField(max_length=50,blank=True, null=True)
    lot_no = models.CharField(max_length=50,blank=True, null=True)
    fabric_color = models.CharField(max_length=50,blank=True, null=True)
    date = models.DateField( auto_now_add=True )
    timer = models.CharField(max_length=50)

    class Meta:
        db_table = 'final_plans'
    
    
    

