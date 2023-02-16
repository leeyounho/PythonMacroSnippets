import yaml

class YamlWrapper:
    def __init__(self, config_file_name):
        self.config_file_name = config_file_name

    def read(self):
        with open(self.config_file_name) as f:
            return yaml.safe_load(f)

    def write_dict(self, d):
        with open(self.config_file_name, 'w') as f:
            yaml.safe_dump(d, f)


if __name__ == '__main__':
    yamlWrapper = YamlWrapper('../config/config.yaml')
    print(yamlWrapper.read()['S3']['IP'])
    print(yamlWrapper.read()['S3']['PORT'])

    for key, value in yamlWrapper.read()['S3'].items():
        print(key, value)

