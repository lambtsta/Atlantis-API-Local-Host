from rest_framework import serializers
from AtlantisAPI.models import *

#Serializers are used in REST APIs to control the format of the data being sent and received between the client and the server. 


# serializing the the TblActuators in models.py
class ActuatorsSerializers(serializers.ModelSerializer):
    class Meta:
        model=TblActuators
        fields=('__all__')
# serializing the the TblGreenhouseMonitoring in models.py
class GreenhouseMSerializers(serializers.ModelSerializer):
    class Meta:
        model=TblGreenhouseMonitoring
        fields=('__all__')

# serializing the the TblWatersensingtank in models.py
class WaterSensingtankSerializers (serializers.ModelSerializer):
    class Meta:
        model=TblWaterSensingtank
        fields=('__all__')

# serializing the the TblWaterTestbed in models.py
class WaterTestBedSerializers(serializers.ModelSerializer):
    class Meta:
        model=TblWaterTestbed
        fields=('__all__')

# serializing the the TblWaterBiofilter in models.py
class WaterBiofilterSerializers(serializers.ModelSerializer):
    class Meta:
        model=TblWaterBiofilter
        fields=('__all__')