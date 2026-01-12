from mathx.linalg.tensor.vector.vector import Vector
from robotix.structure.kind.body.sensor.observation.observation import Observation as SensorObservation

class Observation(SensorObservation):
    def __init__(self, time:float, val:Vector):
        #@todo check 720 dim
        pass