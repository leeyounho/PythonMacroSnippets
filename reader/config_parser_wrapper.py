import configparser


class ConfigParserWrapper:
    def __init__(self, config_file_name):
        self.config = configparser.ConfigParser()
        self.config_file_name = config_file_name

    def write_section(self, section_name, key, value):
        # read reader file
        self.config.read(self.config_file_name, encoding='utf-8')

        # create section
        if not self.config.has_section(section_name):
            self.config.add_section(section_name)

        # create key value
        if value == "":
            if self.config.has_option(section_name, key):
                self.config.remove_option(section_name, key)
        else:
            self.config[section_name][key] = value

        # write reader file
        with open(self.config_file_name, 'w', encoding='utf-8') as config_file:
            self.config.write(config_file)

    def read_section(self, section_name, key):
        # read reader file
        self.config.read(self.config_file_name, encoding='utf-8')

        if self.config.has_option(section_name, key):
            return self.config[section_name][key]
        else:
            return ""

    def read_all_sections(self):
        self.config.read(self.config_file_name, 'utf-8')
        for section in self.config.sections():
            print(section, dict(self.config[section]))


def config_test():
    print('test')

if __name__ == '__main__':
    configParserWrapper = ConfigParserWrapper('../config/config.ini')
    configParserWrapper.read_all_sections()

    print(configParserWrapper.read_section('test', 'test2'))
    print(configParserWrapper.read_section('test_section', 'test'))

    configParserWrapper.write_section('database2', 'test', 'testsdfsfsdf')
    print(configParserWrapper.read_section('database2', 'test'))

    configParserWrapper.read_all_sections()
