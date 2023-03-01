from django.conf.urls import url
from AtlantisAPI import views 


urlpatterns =[
    url(r'^Actuators', views.actuatorsAPI),
    url(r'^GreenhouseMonitoring', views.greenhousemAPI),
    url(r'^WaterSensingTank', views.watersensingAPI),
    url(r'^WaterTestBed', views.watertestbedAPI),
    url(r'^WaterBiofilter', views.waterbiofilterAPI)
]
# localhost:8000/api/v1.0/Actuators
# localhost:8000/api/v1.0/GreenhouseMonitoring
# localhost:8000/api/v1.0/WaterSensingTank
# localhost:8000/api/v1.0/WaterTestBed
# localhost:8000/api/v1.0/WaterBiofilter