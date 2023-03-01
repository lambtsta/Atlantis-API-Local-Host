from django.db import models

# Models in Django are used to represent the structure of data that is being stored in your application. 

# Create your models here.

class TblActuators(models.Model):
    actuators_id = models.AutoField(primary_key=True)
    greenhouse = models.ForeignKey('TblGreenhouse', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(blank=False, null=False)
    exhaust_fan = models.IntegerField(blank=False, null=False)
    evaporator_cooler = models.IntegerField(blank=False, null=False)
    greenhouse_light = models.IntegerField(blank=False, null=False)
    warmer_lamps = models.IntegerField(blank=False, null=False)
    ac_motors = models.IntegerField(blank=False, null=False)
    water_pump = models.IntegerField(blank=False, null=False)
    aeration_pump = models.IntegerField(blank=False, null=False)
    automatic_baiting_system = models.IntegerField(blank=False, null=False)
    water_heater = models.IntegerField(blank=False, null=False)
    water_aerator = models.IntegerField(blank=False, null=False)
    water_blender = models.IntegerField(blank=False, null=False)
    solenoid_valve_1 = models.IntegerField(blank=False, null=False)
    solenoid_valve_2 = models.IntegerField(blank=False, null=False)
    solenoid_valve_3 = models.IntegerField(blank=False, null=False)
    solenoid_valve_4 = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'tbl_actuators'


class TblFishData(models.Model):
    fd_id = models.AutoField(primary_key=True)
    greenhouse = models.ForeignKey('TblGreenhouse', on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    fish_width = models.FloatField()
    fish_height = models.FloatField()
    fish_weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tbl_fish_data'


class TblGreenhouse(models.Model):
    greenhouse_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey('TblUserData', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'tbl_greenhouse'


class TblGreenhouseMonitoring(models.Model):
    gm_id = models.AutoField(primary_key=True)
    greenhouse = models.ForeignKey(TblGreenhouse, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    air_temperature = models.FloatField()
    relative_humidity = models.FloatField()
    co2_level = models.FloatField()
    intensity_illumination = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tbl_greenhouse_monitoring'


class TblPlantData(models.Model):
    pd_id = models.AutoField(primary_key=True)
    greenhouse = models.ForeignKey(TblGreenhouse, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    plant_health = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'tbl_plant_data'


class TblUserData(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, blank=True, null=True)
    password = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_user_data'


class TblWaterBiofilter(models.Model):
    wbf_id = models.AutoField(primary_key=True)
    greenhouse = models.ForeignKey(TblGreenhouse, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    nitrite = models.FloatField()
    nitrate = models.FloatField()
    ammonia = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tbl_water_biofilter'


class TblWaterSensingtank(models.Model):
    wst_id = models.AutoField(primary_key=True)
    greenhouse = models.ForeignKey(TblGreenhouse, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    ph_level = models.FloatField()
    water_temperature = models.FloatField()
    elec_conductivity = models.FloatField()
    total_dissolved_solids = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tbl_water_sensingtank'


class TblWaterTestbed(models.Model):
    wtb_id = models.AutoField(primary_key=True)
    greenhouse = models.ForeignKey(TblGreenhouse, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    ph_level = models.FloatField()
    water_temperature = models.FloatField()
    dissolved_o2_level = models.FloatField()
    elec_conductivity = models.FloatField()
    total_dissolved_solids = models.FloatField()
    nitrite = models.FloatField()
    nitrate = models.FloatField()
    ammonia = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tbl_water_testbed'