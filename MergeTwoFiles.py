from Npp import *


def mergeTwoFiles(firstFileName, secondFileName):
    print(firstFileName)
    print(secondFileName)

    console.write(firstFileName)
    console.write(secondFileName)


if __name__ == '__main__':
    file_name = 'config/config.ini'
    section_name = 'merge_section'
    first_file_name = 'first_file_name'
    second_file_name = 'second_file_name'
    start_flag = 'start_flag'

    editor.flash(100)

    flag = config_read(file_name, section_name, start_flag)
    if flag == '0':
        config_write(file_name, section_name, start_flag, '1')
        config_write(file_name, section_name, first_file_name, notepad.getCurrentFilename())
    else:
        config_write(file_name, section_name, start_flag, '0')
        mergeTwoFiles(config_read(file_name, section_name, first_file_name), notepad.getCurrentFilename())
