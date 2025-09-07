import yaml
from yaml import CLoader

class SensorSetObssFromYamlFile(SensorSetObss):
    def __init__(self, path_to_yaml_file):
        self._path_to_yaml_file = path_to_yaml_file

    def cache(self):
        pass

    def __generate_sensor_set_obs_seq(self):
        with open(self._path_to_yaml_file, "r") as file:
            topic_rows = yaml.load_all(file, Loader=CLoader)