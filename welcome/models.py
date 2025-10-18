# welcome/models.py
from django.contrib.auth.models import User
from django.db import models

class UserPermission(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    can_access_admin = models.BooleanField(default=False)
    can_access_roll = models.BooleanField(default=False)
    can_access_attendance = models.BooleanField(default=False)
    powerbi_data = models.BooleanField(default=False)
    production_data = models.BooleanField(default=False)
    lay_spreading = models.BooleanField(default=False)
    lay_admin = models.BooleanField(default=False)
    unit1 = models.BooleanField(default=False)
    unit2 = models.BooleanField(default=False)
    unit3 = models.BooleanField(default=False)
    unit4 = models.BooleanField(default=False)
    unit5 = models.BooleanField(default=False)
    merch1 = models.BooleanField(default=False)
    merch2 = models.BooleanField(default=False)
    server13 = models.BooleanField(default=False)
    server10 = models.BooleanField(default=False)
    server15 = models.BooleanField(default=False)
    bill = models.BooleanField(default=False)

    def __str__(self):
        return f"Permissions for {self.user.username}"
    

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


class OrdOrderOms(models.Model):
    insdatenew = models.CharField(db_column='insdateNew', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    jobno_oms = models.CharField(db_column='Jobno Oms', max_length=50,primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    printing = models.CharField(db_column='Printing', max_length=750, blank=True, null=True)  # Field name made lowercase.
    jobnoomsnew = models.CharField(db_column='JobnoOmsnew', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mainimagepath = models.CharField(max_length=511, blank=True, null=True)
    ordimg1_pen = models.CharField(db_column='OrdImg1_Pen', max_length=9)  # Field name made lowercase.
    styleid = models.IntegerField()
    final_delivery_date = models.CharField(db_column='Final delivery date', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    finaldelvdate1 = models.DateTimeField(blank=True, null=True)
    year = models.CharField(db_column='Year', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    final_year_delivery = models.CharField(db_column='Final Year delivery', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    final_year_delivery1 = models.CharField(db_column='Final Year delivery1', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ddays = models.IntegerField(blank=True, null=True)
    fdays = models.IntegerField(db_column='Fdays', blank=True, null=True)  # Field name made lowercase.
    insdays = models.IntegerField(blank=True, null=True)
    finaldelvdate = models.CharField(db_column='FinalDelvDate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ourdeldate = models.CharField(db_column='Ourdeldate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ourdelvdate = models.CharField(db_column='OurDelvDate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    podate = models.CharField(db_column='PODate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    vessel_dt = models.CharField(max_length=4000, blank=True, null=True)
    vessel_yr = models.CharField(max_length=4000, blank=True, null=True)
    pono = models.CharField(db_column='PONo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shipmentcompleted = models.SmallIntegerField(db_column='ShipmentCompleted')  # Field name made lowercase.
    reference = models.CharField(max_length=2100, blank=True, null=True)
    no = models.CharField(db_column='No', max_length=50)  # Field name made lowercase.
    company_name = models.CharField(max_length=50, blank=True, null=True)
    mer_un = models.CharField(max_length=71, blank=True, null=True)
    image_order = models.CharField(db_column='Image Order', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    abc = models.CharField(db_column='ABC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    order_follow_up = models.CharField(db_column='Order_Follow_up', max_length=35)  # Field name made lowercase.
    quality_controller = models.CharField(db_column='Quality Controller', max_length=35)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    buyer_sh = models.CharField(db_column='Buyer_sh', max_length=10, blank=True, null=True)  # Field name made lowercase.
    punit_sh = models.CharField(db_column='PUnit_sh', max_length=6, blank=True, null=True)  # Field name made lowercase.
    insdateyear = models.CharField(db_column='insdateYear', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    insdate = models.CharField(db_column='Insdate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    buyer = models.CharField(db_column='Buyer', max_length=15, blank=True, null=True)  # Field name made lowercase.
    merch = models.CharField(max_length=35, blank=True, null=True)
    u46 = models.CharField(max_length=750, blank=True, null=True)
    actdaten = models.DateTimeField(db_column='actdateN', blank=True, null=True)  # Field name made lowercase.
    actdate = models.CharField(db_column='Actdate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    actyeardate = models.CharField(db_column='Actyeardate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    con_actdate = models.CharField(db_column='Con_Actdate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    production_unit = models.CharField(db_column='Production_unit', max_length=35, blank=True, null=True)  # Field name made lowercase.
    director_sample_order = models.CharField(db_column='Director_Sample_Order', max_length=6)  # Field name made lowercase.
    z_o_ordfol_qualitycon = models.CharField(db_column='Z_O_Ordfol_Qualitycon', max_length=72, blank=True, null=True)  # Field name made lowercase.
    con_ordno_mer_buy = models.CharField(db_column='Con_ordno_mer_buy', max_length=95, blank=True, null=True)  # Field name made lowercase.
    con_ord_un_buy_mer_sty_qty = models.CharField(db_column='Con_ord_un_buy_mer_sty_Qty', max_length=173, blank=True, null=True)  # Field name made lowercase.
    z_o_dd_ord_findt_buy_mer_qty = models.CharField(db_column='Z_O_DD_Ord_Findt_Buy_mer_Qty', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    z_o_yy_findt_dir_sty_uom_pty = models.CharField(db_column='Z_O_yy_Findt_dir_sty_uom_pty', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    con_str_sty_uom_prodty = models.CharField(db_column='Con_Str_Sty_UOM_Prodty', max_length=22, blank=True, null=True)  # Field name made lowercase.
    con_findt_ordno_dir_un_buy_uom_qty_mer = models.CharField(db_column='Con_Findt_ordno_dir_un_Buy_Uom_Qty_mer', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    production_type_inside_outside = models.CharField(db_column='Production_type_Inside_Outside', max_length=7, blank=True, null=True)  # Field name made lowercase.
    shipment_complete = models.CharField(db_column='Shipment_complete', max_length=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ord_Order_Oms'

class EmpAttendanceFact(models.Model):
    code_emb_attendance_fact = models.IntegerField(db_column='Code Emb Attendance Fact', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    intime = models.DateTimeField(blank=True, null=True)
    outtime = models.DateTimeField(blank=True, null=True)
    emppic = models.CharField(db_column='Emppic', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    img = models.CharField(max_length=53, blank=True, null=True)
    con_code_name_in_out = models.CharField(db_column='Con_Code_name_in_out', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    rel_code_name = models.CharField(db_column='Rel_code_name', max_length=112, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Emp_Attendance_Fact'

class OrdMaterialplanPen(models.Model):
    orderno = models.CharField(db_column='OrderNo', max_length=50,primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=7)  # Field name made lowercase.
    days = models.CharField(db_column='Days', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ord_MaterialPlan_pen'


# class FabKnitprgvsrecd(models.Model):
#     no = models.IntegerField(db_column='No', primary_key=True)  # Set as primary key
#     hex = models.CharField(max_length=15, blank=True, null=True)
#     img_fpath = models.CharField(db_column='Img_Fpath', max_length=8000, blank=True, null=True)
#     date = models.DateTimeField(db_column='Date')
#     re_date = models.DateTimeField(db_column='[Re.date]', blank=True, null=True)  # ✅ Fixed
#     orderno = models.CharField(db_column='OrderNo', max_length=50, blank=True, null=True)
#     knitter = models.CharField(db_column='Knitter', max_length=35, blank=True, null=True)
#     process = models.CharField(db_column='Process', max_length=35, blank=True, null=True)
#     yarninfo = models.CharField(db_column='YarnInfo', max_length=971)
#     completed = models.SmallIntegerField(db_column='Completed')
#     colour = models.CharField(db_column='Colour', max_length=50)
#     dia = models.CharField(db_column='Dia', max_length=35, blank=True, null=True)
#     gsm = models.SmallIntegerField(db_column='GSM')
#     fabrictype = models.CharField(db_column='FabricType', max_length=35, blank=True, null=True)
#     fabric = models.CharField(db_column='Fabric', max_length=35, blank=True, null=True)
#     prg_weight = models.DecimalField(db_column='[Prg.Weight]', max_digits=38, decimal_places=4, blank=True, null=True)  # ✅ Fixed
#     rec_weight = models.DecimalField(db_column='[Rec.weight]', max_digits=38, decimal_places=4, blank=True, null=True)  # ✅ Fixed

#     class Meta:
#         managed = False
#         db_table = 'Fab_KnitPrgVsRecd'


class OrdStk(models.Model):
    trstype = models.CharField(db_column='Trstype', max_length=6)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=50)  # Field name made lowercase.
    jobno = models.CharField(db_column='Jobno', max_length=50,primary_key=True)  # Field name made lowercase.
    tb = models.CharField(db_column='Tb', max_length=50)  # Field name made lowercase.
    clr = models.CharField(max_length=50)
    bc = models.IntegerField()
    sew = models.IntegerField()
    che = models.IntegerField()
    irn = models.IntegerField()
    pack = models.IntegerField()
    oth = models.IntegerField()
    mist = models.IntegerField()
    trstype_all = models.CharField(max_length=80, blank=True, null=True)
    deldt = models.DateTimeField(db_column='DelDt')  # Field name made lowercase.
    merch = models.CharField(db_column='MERCH', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(max_length=50)
    orderimage = models.CharField(db_column='OrderImage', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    tbimage = models.CharField(db_column='TBImage', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    director_sample_order = models.CharField(db_column='Director_Sample_Order', max_length=6, blank=True, null=True)  # Field name made lowercase.
    finaldelvdate = models.CharField(db_column='FinalDelvDate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    final_year_delivery = models.CharField(db_column='Final Year delivery', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insdatenew = models.CharField(db_column='insdateNew', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    c = models.IntegerField(db_column='C')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ord_stk'


class GeneralDeliveryReport(models.Model):
    lz_no = models.IntegerField(db_column='LZ_No',primary_key=True)  # Field name made lowercase.
    le_date = models.DateTimeField(db_column='LE_Date')  # Field name made lowercase.
    uom = models.CharField(db_column='Uom', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lz_reference = models.CharField(db_column='LZ_Reference', max_length=20, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=13, blank=True, null=True)
    lz_delivery_to = models.CharField(db_column='LZ_Delivery To', max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lz_name = models.CharField(db_column='LZ_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lz_party_ref_no = models.CharField(db_column='LZ_Party Ref No', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lz_vehicle_no = models.CharField(db_column='LZ_Vehicle No', max_length=16, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lz_incharge = models.CharField(db_column='LZ_Incharge', max_length=35, blank=True, null=True)  # Field name made lowercase.
    rf_tot_qty = models.DecimalField(db_column='RF_Tot Qty', max_digits=18, decimal_places=4)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lz_department = models.CharField(db_column='LZ_Department', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lz_completed = models.SmallIntegerField(db_column='LZ_Completed', blank=True, null=True)  # Field name made lowercase.
    sl = models.IntegerField(db_column='Sl', blank=True, null=True)  # Field name made lowercase.
    inwdate = models.DateField(db_column='InwDate', blank=True, null=True)  # Field name made lowercase.
    inwdcno = models.CharField(db_column='InwDcNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qtyreceived = models.IntegerField(db_column='QtyReceived', blank=True, null=True)  # Field name made lowercase.
    ourdcno = models.CharField(db_column='OurDcNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    party = models.CharField(db_column='Party', max_length=50, blank=True, null=True)  # Field name made lowercase.
    verified = models.CharField(db_column='Verified', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inw_date = models.CharField(db_column='Inw_Date', max_length=4000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'General_Delivery_Report'

class FabFabricStatus(models.Model):
    jobno_fabric_status = models.CharField(db_column='Jobno Fabric Status', max_length=50, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sl = models.IntegerField()
    process = models.CharField(db_column='Process', max_length=35)  # Field name made lowercase.
    counts = models.CharField(db_column='Counts', max_length=35)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mill = models.CharField(db_column='Mill', max_length=35)  # Field name made lowercase.
    supplier = models.CharField(db_column='Supplier', max_length=35, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pono = models.IntegerField(db_column='PONO')  # Field name made lowercase.
    req = models.DecimalField(db_column='Req', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pokgs = models.DecimalField(max_digits=38, decimal_places=4)
    reckgs = models.DecimalField(db_column='Reckgs', max_digits=38, decimal_places=4)  # Field name made lowercase.
    trs = models.DecimalField(max_digits=38, decimal_places=4)
    balkgs = models.DecimalField(db_column='BalKgs', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=500)  # Field name made lowercase.
    status_flag = models.CharField(db_column='Status_Flag', max_length=500)  # Field name made lowercase.
    cou_fab = models.CharField(db_column='Cou_Fab', max_length=80, blank=True, null=True)  # Field name made lowercase.
    con_ord_clr_fab = models.CharField(db_column='Con_Ord_Clr_Fab', max_length=139, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fab_Fabric_Status1'
        
        
class FabYarn(models.Model):
    rate_weight = models.DecimalField(db_column='Rate_Weight', max_digits=19, decimal_places=4)  # Field name made lowercase.
    img_fpath = models.CharField(db_column='Img_Fpath', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    fabimg_pen = models.CharField(db_column='Fabimg_pen', max_length=67, blank=True, null=True)  # Field name made lowercase.
    fabty = models.CharField(db_column='Fabty', max_length=35)  # Field name made lowercase.
    supplier = models.CharField(max_length=35)
    orderno = models.CharField(max_length=50,primary_key=True)
    clr = models.CharField(max_length=50)
    fabric = models.CharField(max_length=35)
    prs = models.CharField(max_length=35)
    kg = models.IntegerField(blank=True, null=True)
    id = models.IntegerField()
    ty = models.IntegerField()
    hex = models.CharField(max_length=15)
    kw = models.CharField(max_length=1)
    dia = models.CharField(max_length=35, blank=True, null=True)
    mainimagepath = models.CharField(max_length=4000, blank=True, null=True)
    finaldia = models.CharField(db_column='FinalDia', max_length=70, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fab_Yarn'

class FabKnitprgvsrecd(models.Model):
    no = models.IntegerField(db_column='No', primary_key=True)  # Set as primary key
    hex = models.CharField(max_length=15, blank=True, null=True)
    img_fpath = models.CharField(db_column='Img_Fpath', max_length=8000, blank=True, null=True)
    date = models.DateTimeField(db_column='Date')
    re_date = models.DateTimeField(db_column='[Re.date]', blank=True, null=True)  # ✅ Fixed
    orderno = models.CharField(db_column='OrderNo', max_length=50, blank=True, null=True)
    knitter = models.CharField(db_column='Knitter', max_length=35, blank=True, null=True)
    process = models.CharField(db_column='Process', max_length=35, blank=True, null=True)
    yarninfo = models.CharField(db_column='YarnInfo', max_length=971)
    completed = models.SmallIntegerField(db_column='Completed')
    colour = models.CharField(db_column='Colour', max_length=50)
    dia = models.CharField(db_column='Dia', max_length=35, blank=True, null=True)
    gsm = models.SmallIntegerField(db_column='GSM')
    fabrictype = models.CharField(db_column='FabricType', max_length=35, blank=True, null=True)
    fabric = models.CharField(db_column='Fabric', max_length=35, blank=True, null=True)
    prg_weight = models.DecimalField(db_column='[Prg.Weight]', max_digits=38, decimal_places=4, blank=True, null=True)  # ✅ Fixed
    rec_weight = models.DecimalField(db_column='[Rec.weight]', max_digits=38, decimal_places=4, blank=True, null=True)  # ✅ Fixed

    class Meta:
        managed = False
        db_table = 'Fab_KnitPrgVsRecd'



class YarnPovspi(models.Model):
    orderno = models.CharField(db_column='OrderNo', max_length=50, primary_key=True)  # Field name made lowercase.
    hex = models.CharField(max_length=15, blank=True, null=True)
    img_fpath = models.CharField(db_column='Img_Fpath', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    supplier = models.CharField(db_column='Supplier', max_length=35, blank=True, null=True)  # Field name made lowercase.
    yarntype = models.CharField(db_column='YarnType', max_length=35, blank=True, null=True)  # Field name made lowercase.
    yarn = models.CharField(db_column='Yarn', max_length=35, blank=True, null=True)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=50)  # Field name made lowercase.
    no = models.IntegerField(db_column='No')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    pi_date = models.DateTimeField(db_column='[Pi.Date]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    completed = models.SmallIntegerField(db_column='Completed')  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pen_days = models.IntegerField(db_column='Pen Days', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    po_qty = models.DecimalField(db_column='[Po.Qty]', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pi_qty = models.DecimalField(db_column='[Pi.Qty]', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bal = models.DecimalField(db_column='Bal', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    per = models.DecimalField(db_column='Per', max_digits=38, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Yarn_PovsPi'


class PrintRgbAlt(models.Model):
    jobno_joint = models.CharField(db_column='[Jobno Joint]', max_length=50,primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prnclr = models.CharField(max_length=50, blank=True, null=True)
    prnfile1 = models.CharField(max_length=250, blank=True, null=True)
    prnfile2 = models.CharField(max_length=250, blank=True, null=True)
    jobno_print_emb = models.CharField(db_column='[Jobno Print Emb]', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    img_fpath = models.CharField(db_column='Img_Fpath', max_length=1550, blank=True, null=True)  # Field name made lowercase.
    hex = models.CharField(max_length=15, blank=True, null=True)
    imgtb1 = models.CharField(max_length=1550, blank=True, null=True)
    print_img_pen = models.CharField(db_column='Print_img_pen', max_length=13)  # Field name made lowercase.
    image_tb = models.CharField(db_column='Image_tb', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    con_fimg_grclr = models.CharField(db_column='Con_Fimg_grclr', max_length=20, blank=True, null=True)  # Field name made lowercase.
    con_jobno_print = models.CharField(db_column='Con_jobno_Print', max_length=802, blank=True, null=True)  # Field name made lowercase.
    jobno_print_new_rgb = models.CharField(db_column='Jobno_Print_New_RGB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    con_jobno_prndes = models.CharField(db_column='Con_Jobno_PrnDes', max_length=102, blank=True, null=True)  # Field name made lowercase.
    con_jobno_top_clr_line = models.CharField(db_column='Con_jobno_top_clr_line', max_length=200, blank=True, null=True)  # Field name made lowercase.
    con_jobno_top_clr_siz_line = models.CharField(max_length=250, blank=True, null=True)
    con_inout_outsup = models.CharField(db_column='Con_InOut_Outsup', max_length=67, blank=True, null=True)  # Field name made lowercase.
    print_screen_1 = models.CharField(db_column='[Print Screen 1]', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_screen_2 = models.CharField(db_column='[Print Screen 2]', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_screen_3 = models.CharField(db_column='[Print Screen 3]', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    top_bottom = models.CharField(db_column='[Top Bottom]', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    clrcomb = models.CharField(max_length=100, blank=True, null=True)
    screen_number = models.IntegerField(db_column='[Screen Number]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_type = models.CharField(db_column='[Print Type]', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_description = models.CharField(db_column='[Print Description]', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    individual_part_print_emb = models.CharField(db_column='[Individual Part Print Emb]', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colours = models.IntegerField(db_column='[Print Colours]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_emb_ground_colour = models.CharField(db_column='[Print & Emb Ground Colour]', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inside_outside_print_emb = models.CharField(db_column='[Inside,Outside Print Emb]', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_emb_outside_supplier = models.CharField(db_column='[Print Emb Outside Supplier]', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_1 = models.CharField(db_column='[Print Colour 1]', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_2 = models.CharField(db_column='[Print Colour 2]', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_3 = models.CharField(db_column='[Print Colour 3]', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_4 = models.CharField(db_column='[Print Colour 4]', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_5 = models.CharField(db_column='[Print Colour 5]', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_6 = models.CharField(db_column='[Print Colour 6]', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_7 = models.CharField(db_column='[Print Colour 7]', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_8 = models.CharField(db_column='[Print Colour 8]', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_size_details = models.CharField(db_column='[Print Size Details]', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_emb_ground_colour_rgb = models.CharField(db_column='[Print & Emb Ground Colour RGB]', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    img_print = models.CharField(db_column='Img_Print', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    img_print_mmt = models.CharField(db_column='Img_Print_MMT', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    con_jobno_top_clr_siz = models.CharField(db_column='Con_jobno_top_clr_siz', max_length=256, blank=True, null=True)  # Field name made lowercase.
    con_jobno_top_clr = models.CharField(db_column='Con_jobno_top_clr', max_length=204, blank=True, null=True)  # Field name made lowercase.
    rgb = models.CharField(db_column='RGB', max_length=15, blank=True, null=True)  # Field name made lowercase.
    print_colour_rgb_1 = models.CharField(db_column='[Print Colour RGB 1]', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_2 = models.CharField(db_column='[Print Colour RGB 2]', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_3 = models.CharField(db_column='[Print Colour RGB 3]', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_4 = models.CharField(db_column='[Print Colour RGB 4]', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_5 = models.CharField(db_column='[Print Colour RGB 5]', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_6 = models.CharField(db_column='[Print Colour RGB 6]', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_7 = models.CharField(db_column='[Print Colour RGB 7]', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_8 = models.CharField(db_column='[Print  Colour RGB 8]', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Print_RGB_Alt'


class AllotPen(models.Model):
    insdatenew = models.CharField(db_column='insdateNew', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    jobno_oms = models.CharField(db_column='Jobno Oms', max_length=50,primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    printing = models.CharField(db_column='Printing', max_length=750, blank=True, null=True)  # Field name made lowercase.
    jobnoomsnew = models.CharField(db_column='JobnoOmsnew', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mainimagepath = models.CharField(max_length=511, blank=True, null=True)
    ordimg1_pen = models.CharField(db_column='OrdImg1_Pen', max_length=9)  # Field name made lowercase.
    styleid = models.IntegerField()
    final_delivery_date = models.CharField(db_column='Final delivery date', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    finaldelvdate1 = models.DateTimeField(blank=True, null=True)
    year = models.CharField(db_column='Year', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    final_year_delivery = models.CharField(db_column='Final Year delivery', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    final_year_delivery1 = models.CharField(db_column='Final Year delivery1', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ddays = models.IntegerField(blank=True, null=True)
    fdays = models.IntegerField(db_column='Fdays', blank=True, null=True)  # Field name made lowercase.
    insdays = models.IntegerField(blank=True, null=True)
    finaldelvdate = models.CharField(db_column='FinalDelvDate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ourdeldate = models.CharField(db_column='Ourdeldate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ourdelvdate = models.CharField(db_column='OurDelvDate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    podate = models.CharField(db_column='PODate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    vessel_dt = models.CharField(max_length=4000, blank=True, null=True)
    vessel_yr = models.CharField(max_length=4000, blank=True, null=True)
    pono = models.CharField(db_column='PONo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shipmentcompleted = models.SmallIntegerField(db_column='ShipmentCompleted')  # Field name made lowercase.
    reference = models.CharField(max_length=2100, blank=True, null=True)
    no = models.CharField(db_column='No', max_length=50)  # Field name made lowercase.
    company_name = models.CharField(max_length=50, blank=True, null=True)
    mer_un = models.CharField(max_length=71, blank=True, null=True)
    image_order = models.CharField(db_column='Image Order', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    abc = models.CharField(db_column='ABC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    order_follow_up = models.CharField(db_column='Order_Follow_up', max_length=35)  # Field name made lowercase.
    quality_controller = models.CharField(db_column='Quality Controller', max_length=35)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    buyer_sh = models.CharField(db_column='Buyer_sh', max_length=10, blank=True, null=True)  # Field name made lowercase.
    punit_sh = models.CharField(db_column='PUnit_sh', max_length=6, blank=True, null=True)  # Field name made lowercase.
    insdateyear = models.CharField(db_column='insdateYear', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    insdate = models.CharField(db_column='Insdate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    buyer = models.CharField(db_column='Buyer', max_length=15, blank=True, null=True)  # Field name made lowercase.
    merch = models.CharField(max_length=35, blank=True, null=True)
    u46 = models.CharField(max_length=750, blank=True, null=True)
    actdaten = models.DateTimeField(db_column='actdateN', blank=True, null=True)  # Field name made lowercase.
    actdate = models.CharField(db_column='Actdate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    actyeardate = models.CharField(db_column='Actyeardate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    con_actdate = models.CharField(db_column='Con_Actdate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    production_unit = models.CharField(db_column='Production_unit', max_length=35, blank=True, null=True)  # Field name made lowercase.
    director_sample_order = models.CharField(db_column='Director_Sample_Order', max_length=6)  # Field name made lowercase.
    z_o_ordfol_qualitycon = models.CharField(db_column='Z_O_Ordfol_Qualitycon', max_length=72, blank=True, null=True)  # Field name made lowercase.
    con_ordno_mer_buy = models.CharField(db_column='Con_ordno_mer_buy', max_length=95, blank=True, null=True)  # Field name made lowercase.
    con_ord_un_buy_mer_sty_qty = models.CharField(db_column='Con_ord_un_buy_mer_sty_Qty', max_length=173, blank=True, null=True)  # Field name made lowercase.
    z_o_dd_ord_findt_buy_mer_qty = models.CharField(db_column='Z_O_DD_Ord_Findt_Buy_mer_Qty', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    z_o_yy_findt_dir_sty_uom_pty = models.CharField(db_column='Z_O_yy_Findt_dir_sty_uom_pty', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    con_str_sty_uom_prodty = models.CharField(db_column='Con_Str_Sty_UOM_Prodty', max_length=22, blank=True, null=True)  # Field name made lowercase.
    con_findt_ordno_dir_un_buy_uom_qty_mer = models.CharField(db_column='Con_Findt_ordno_dir_un_Buy_Uom_Qty_mer', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    production_type_inside_outside = models.CharField(db_column='Production_type_Inside_Outside', max_length=7, blank=True, null=True)  # Field name made lowercase.
    shipment_complete = models.CharField(db_column='Shipment_complete', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ordno = models.CharField(db_column='OrdNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbimage = models.CharField(max_length=8000, blank=True, null=True)
    part = models.CharField(db_column='Part', max_length=50, blank=True, null=True)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mainimg = models.CharField(max_length=511, blank=True, null=True)
    ppic1 = models.CharField(max_length=1550, blank=True, null=True)
    imagepen = models.CharField(db_column='ImagePen', max_length=11, blank=True, null=True)  # Field name made lowercase.
    allot_pen = models.CharField(db_column='Allot_pen', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Allot_pen'




class PrintNew(models.Model):
    jobno_joint = models.CharField(db_column='Jobno Joint', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prnclr = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    prnfile1 = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    prnfile2 = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jobno_print_emb = models.CharField(db_column='Jobno Print Emb', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    img_fpath = models.CharField(db_column='Img_Fpath', max_length=1550, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hex = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    imgtb1 = models.CharField(max_length=1550, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    print_img_pen = models.CharField(db_column='Print_img_pen', max_length=13, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    image_tb = models.CharField(db_column='Image_tb', max_length=8000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    con_fimg_grclr = models.CharField(db_column='Con_Fimg_grclr', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    con_jobno_print = models.CharField(db_column='Con_jobno_Print', max_length=802, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    jobno_print_new_rgb = models.CharField(db_column='Jobno_Print_New_RGB', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    con_jobno_prndes = models.CharField(db_column='Con_Jobno_PrnDes', max_length=102, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    con_jobno_top_clr_line = models.CharField(db_column='Con_jobno_top_clr_line', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    con_jobno_top_clr_siz_line = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    con_inout_outsup = models.CharField(db_column='Con_InOut_Outsup', max_length=67, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    print_screen_1 = models.CharField(db_column='Print Screen 1', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_screen_2 = models.CharField(db_column='Print Screen 2', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_screen_3 = models.CharField(db_column='Print Screen 3', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    top_bottom = models.CharField(db_column='Top Bottom', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    clrcomb = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    screen_number = models.IntegerField(db_column='Screen Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_type = models.CharField(db_column='Print Type', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_description = models.CharField(db_column='Print Description', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    individual_part_print_emb = models.CharField(db_column='Individual Part Print Emb', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colours = models.IntegerField(db_column='Print Colours', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_emb_ground_colour = models.CharField(db_column='Print & Emb Ground Colour', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inside_outside_print_emb = models.CharField(db_column='Inside,Outside Print Emb', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_emb_outside_supplier = models.CharField(db_column='Print Emb Outside Supplier', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_1 = models.CharField(db_column='Print Colour 1', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_2 = models.CharField(db_column='Print Colour 2', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_3 = models.CharField(db_column='Print Colour 3', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_4 = models.CharField(db_column='Print Colour 4', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_5 = models.CharField(db_column='Print Colour 5', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_6 = models.CharField(db_column='Print Colour 6', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_7 = models.CharField(db_column='Print Colour 7', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_8 = models.CharField(db_column='Print Colour 8', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_size_details = models.CharField(db_column='Print Size Details', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_emb_ground_colour_rgb = models.CharField(db_column='Print & Emb Ground Colour RGB', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    img_print = models.CharField(db_column='Img_Print', max_length=8000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    img_print_mmt = models.CharField(db_column='Img_Print_MMT', max_length=8000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    con_jobno_top_clr_siz = models.CharField(db_column='Con_jobno_top_clr_siz', max_length=256, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    con_jobno_top_clr = models.CharField(db_column='Con_jobno_top_clr', max_length=204, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rgb = models.CharField(db_column='RGB', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    print_colour_rgb_1 = models.CharField(db_column='Print Colour RGB 1', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_2 = models.CharField(db_column='Print Colour RGB 2', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_3 = models.CharField(db_column='Print Colour RGB 3', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_4 = models.CharField(db_column='Print Colour RGB 4', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_5 = models.CharField(db_column='Print Colour RGB 5', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_6 = models.CharField(db_column='Print Colour RGB 6', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_7 = models.CharField(db_column='Print Colour RGB 7', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    print_colour_rgb_8 = models.CharField(db_column='Print  Colour RGB 8', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Print_New'

class OrdSampleStatus(models.Model):
    print = models.CharField(db_column='Print', max_length=750)  # Field name made lowercase.
    emb = models.CharField(db_column='Emb', max_length=750)  # Field name made lowercase.
    img = models.CharField(max_length=82, blank=True, null=True)
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    img1 = models.CharField(max_length=1550, blank=True, null=True)
    topbottomimg = models.CharField(db_column='TopBottomImg', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=150)  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock')  # Field name made lowercase.
    cutqty = models.IntegerField(db_column='CutQty')  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=10, blank=True, null=True)  # Field name made lowercase.
    o_finaldelvdate = models.DateField(db_column='o_FinalDelvdate', blank=True, null=True)  # Field name made lowercase.
    jobno = models.CharField(db_column='Jobno', max_length=50,primary_key=True)  # Field name made lowercase.
    merch = models.CharField(db_column='Merch', max_length=35, blank=True, null=True)  # Field name made lowercase.
    buy = models.CharField(db_column='Buy', max_length=5, blank=True, null=True)  # Field name made lowercase.
    buyer = models.CharField(db_column='Buyer', max_length=40, blank=True, null=True)  # Field name made lowercase.
    sample_status = models.CharField(db_column='Sample Status', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unitname = models.CharField(db_column='Unitname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    topbottom_des = models.CharField(db_column='TopBottom_des', max_length=50, blank=True, null=True)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sampletype = models.CharField(db_column='Sampletype', max_length=50, blank=True, null=True)  # Field name made lowercase.
    send_dt = models.DateTimeField(db_column='SEND_DT', blank=True, null=True)  # Field name made lowercase.
    apr_dt = models.DateTimeField(db_column='APR_DT', blank=True, null=True)  # Field name made lowercase.
    rej_dt = models.DateTimeField(db_column='REJ_DT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ord_Sample_status'



class AllotPen1(models.Model):
    insdatenew = models.CharField(db_column='insdateNew', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    jobno_oms = models.CharField(db_column='Jobno Oms', max_length=50,primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    printing = models.CharField(db_column='Printing', max_length=750, blank=True, null=True)  # Field name made lowercase.
    jobnoomsnew = models.CharField(db_column='JobnoOmsnew', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mainimagepath = models.CharField(max_length=511, blank=True, null=True)
    ordimg1_pen = models.CharField(db_column='OrdImg1_Pen', max_length=9)  # Field name made lowercase.
    styleid = models.IntegerField()
    final_delivery_date = models.CharField(db_column='Final delivery date', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    finaldelvdate1 = models.DateTimeField(blank=True, null=True)
    year = models.CharField(db_column='Year', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    final_year_delivery = models.CharField(db_column='Final Year delivery', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    final_year_delivery1 = models.CharField(db_column='Final Year delivery1', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ddays = models.IntegerField(blank=True, null=True)
    fdays = models.IntegerField(db_column='Fdays', blank=True, null=True)  # Field name made lowercase.
    insdays = models.IntegerField(blank=True, null=True)
    finaldelvdate = models.CharField(db_column='FinalDelvDate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ourdeldate = models.CharField(db_column='Ourdeldate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ourdelvdate = models.CharField(db_column='OurDelvDate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    podate = models.CharField(db_column='PODate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    vessel_dt = models.CharField(max_length=4000, blank=True, null=True)
    vessel_yr = models.CharField(max_length=4000, blank=True, null=True)
    pono = models.CharField(db_column='PONo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shipmentcompleted = models.SmallIntegerField(db_column='ShipmentCompleted')  # Field name made lowercase.
    reference = models.CharField(max_length=2100, blank=True, null=True)
    no = models.CharField(db_column='No', max_length=50)  # Field name made lowercase.
    company_name = models.CharField(max_length=50, blank=True, null=True)
    mer_un = models.CharField(max_length=71, blank=True, null=True)
    image_order = models.CharField(db_column='Image Order', max_length=4000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    abc = models.CharField(db_column='ABC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    order_follow_up = models.CharField(db_column='Order_Follow_up', max_length=35)  # Field name made lowercase.
    quality_controller = models.CharField(db_column='Quality Controller', max_length=35)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    buyer_sh = models.CharField(db_column='Buyer_sh', max_length=10, blank=True, null=True)  # Field name made lowercase.
    punit_sh = models.CharField(db_column='PUnit_sh', max_length=6, blank=True, null=True)  # Field name made lowercase.
    insdateyear = models.CharField(db_column='insdateYear', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    insdate = models.CharField(db_column='Insdate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    buyer = models.CharField(db_column='Buyer', max_length=15, blank=True, null=True)  # Field name made lowercase.
    merch = models.CharField(max_length=35, blank=True, null=True)
    u46 = models.CharField(max_length=750, blank=True, null=True)
    actdaten = models.DateTimeField(db_column='actdateN', blank=True, null=True)  # Field name made lowercase.
    actdate = models.CharField(db_column='Actdate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    actyeardate = models.CharField(db_column='Actyeardate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    con_actdate = models.CharField(db_column='Con_Actdate', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    production_unit = models.CharField(db_column='Production_unit', max_length=35, blank=True, null=True)  # Field name made lowercase.
    director_sample_order = models.CharField(db_column='Director_Sample_Order', max_length=6)  # Field name made lowercase.
    z_o_ordfol_qualitycon = models.CharField(db_column='Z_O_Ordfol_Qualitycon', max_length=72, blank=True, null=True)  # Field name made lowercase.
    con_ordno_mer_buy = models.CharField(db_column='Con_ordno_mer_buy', max_length=95, blank=True, null=True)  # Field name made lowercase.
    con_ord_un_buy_mer_sty_qty = models.CharField(db_column='Con_ord_un_buy_mer_sty_Qty', max_length=173, blank=True, null=True)  # Field name made lowercase.
    z_o_dd_ord_findt_buy_mer_qty = models.CharField(db_column='Z_O_DD_Ord_Findt_Buy_mer_Qty', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    z_o_yy_findt_dir_sty_uom_pty = models.CharField(db_column='Z_O_yy_Findt_dir_sty_uom_pty', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    con_str_sty_uom_prodty = models.CharField(db_column='Con_Str_Sty_UOM_Prodty', max_length=22, blank=True, null=True)  # Field name made lowercase.
    con_findt_ordno_dir_un_buy_uom_qty_mer = models.CharField(db_column='Con_Findt_ordno_dir_un_Buy_Uom_Qty_mer', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    production_type_inside_outside = models.CharField(db_column='Production_type_Inside_Outside', max_length=7, blank=True, null=True)  # Field name made lowercase.
    shipment_complete = models.CharField(db_column='Shipment_complete', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ordno = models.CharField(db_column='OrdNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbimage = models.CharField(max_length=8000, blank=True, null=True)
    part = models.CharField(db_column='Part', max_length=50, blank=True, null=True)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mainimg = models.CharField(max_length=511, blank=True, null=True)
    ppic1 = models.CharField(max_length=1550, blank=True, null=True)
    imagepen = models.CharField(db_column='ImagePen', max_length=11, blank=True, null=True)  # Field name made lowercase.
    allot_pen = models.CharField(db_column='Allot_pen', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Allot_pen1'

class OrdSampleStatus1(models.Model):
    print = models.CharField(db_column='Print', max_length=750)  # Field name made lowercase.
    emb = models.CharField(db_column='Emb', max_length=750)  # Field name made lowercase.
    img = models.CharField(max_length=82, blank=True, null=True)
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    img1 = models.CharField(max_length=1550, blank=True, null=True)
    topbottomimg = models.CharField(db_column='TopBottomImg', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=150)  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock')  # Field name made lowercase.
    cutqty = models.IntegerField(db_column='CutQty')  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=10, blank=True, null=True)  # Field name made lowercase.
    o_finaldelvdate = models.DateField(db_column='o_FinalDelvdate', blank=True, null=True)  # Field name made lowercase.
    jobno = models.CharField(db_column='Jobno', max_length=50,primary_key=True)  # Field name made lowercase.
    merch = models.CharField(db_column='Merch', max_length=35, blank=True, null=True)  # Field name made lowercase.
    buy = models.CharField(db_column='Buy', max_length=5, blank=True, null=True)  # Field name made lowercase.
    buyer = models.CharField(db_column='Buyer', max_length=40, blank=True, null=True)  # Field name made lowercase.
    sample_status = models.CharField(db_column='Sample Status', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unitname = models.CharField(db_column='Unitname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    topbottom_des = models.CharField(db_column='TopBottom_des', max_length=50, blank=True, null=True)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sampletype = models.CharField(db_column='Sampletype', max_length=50, blank=True, null=True)  # Field name made lowercase.
    send_dt = models.DateTimeField(db_column='SEND_DT', blank=True, null=True)  # Field name made lowercase.
    apr_dt = models.DateTimeField(db_column='APR_DT', blank=True, null=True)  # Field name made lowercase.
    rej_dt = models.DateTimeField(db_column='REJ_DT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ord_Sample_status1'



class TBuyer(models.Model):
    buyerid = models.IntegerField(db_column='BuyerID', primary_key=True)  # Field name made lowercase.
    buyername = models.CharField(db_column='BuyerName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    orderno = models.CharField(db_column='OrderNo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    refresh = models.CharField(db_column='Refresh', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_buyer'
