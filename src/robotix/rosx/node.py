class Node:
    '''Each node in ROS should be responsible for a single,
    modular purpose, e.g. controlling the wheel motors or
    publishing the sensor data from a laser range-finder.
    Each node can send and receive data from other nodes via topics,
    services, actions, or parameters.'''
    def __init__(self, id, parent=None):
        pass