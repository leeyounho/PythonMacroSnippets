import configparser


def config_write(file_name, section_name, key, value):
    # read config file
    config = configparser.ConfigParser()
    config.read(file_name, encoding='utf-8')

    # create section
    if not config.has_section(section_name):
        config.add_section(section_name)

    # create key value
    if value == "":
        if config.has_option(section_name, key):
            config.remove_option(section_name, key)
    else:
        config[section_name][key] = value

    # write config file
    with open(file_name, 'w', encoding='utf-8') as configfile:
        config.write(configfile)


def config_read(file_name, section_name, key):
    # read config file
    config = configparser.ConfigParser()
    config.read(file_name, encoding='utf-8')

    if config.has_option(section_name, key):
        return config[section_name][key]
    else:
        return ""


def print_config(config):
    for section in config.sections():
        print(section, dict(config[section]))
