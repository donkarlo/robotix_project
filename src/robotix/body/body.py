from robotix.body.actuator.collection.collection import Collection as ActuatorCollection
from sensorx.collection.collection import Collection as SensorCollection

class Body:
    def __init__(self, actuator_collection: ActuatorCollection, sensors_collection: SensorCollection):
        self._actuators:ActuatorCollection = actuator_collection
        self._sensor_collection = sensors_collection

    def get_actuators(self)->ActuatorCollection:
        return self._actuators

    def get_sensors(self)->SensorCollection:
        return self._sensor_collection

