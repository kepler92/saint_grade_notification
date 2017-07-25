refresh_time = int(60)  # seconds

import platform
import struct
import datetime


def driver():
    os_ver = platform.system()
    driver_root = 'driver/'

    if os_ver in 'Windows':
        driver_root = driver_root + 'windows/'

    elif os_ver in 'Darwin':
        driver_root = driver_root + 'mac/'

    elif os_ver in {'Linux', 'Linux2'}:
        os_bit = struct.calcsize("P") * 8
        if os_bit == 32:  # bit
            driver_root = driver_root + 'linux32/'
        elif os_bit == 64:  # bit
            driver_root = driver_root + 'linux64/'

    else:
        print ('지원되지 않는 운영체제입니다.')
        exit()

    return driver_root


def semester():
    d = datetime.date.today()

    year = int(d.year)
    month = int(d.month)
    type = 0

    if month <= 2 :
        type = 21
        year -= 1

    elif 3 <= month and month <= 6:
        type = 10

    elif 7 <= month and month <= 8:
        type = 11

    else:
        type = 20

    value = year * 1000 + type
    return str(value)


def message_format(input):
    '''
    message = '<html> <head> <style>' \
              'table.tbl_view th {border-bottom:solid 1px #b9b9bd;background:#dedee1;text-align:left;border-top:solid 1px #ffffff;font-weight:normal;padding:0.7em 0em 0.7em 1em;line-height:1.4em;font-size:0.9em;border-left:solid 1px #b9b9bd;border-right:solid 1px #b9b9bd;vertical-align:top;}' \
              'table.tbl_view td {border-bottom:solid 1px #b9b9bd;padding:0.7em 0em 0.7em 1em;background:#ffffff;line-height:1.4em;font-size:0.9em;border-right:solid 1px #b9b9bd;vertical-align:top;}' \
              'table.tbl_view tr.first th, table.tbl_view tr.first td {border-top:solid 2px #d10e0e;}' \
              'table.tbl_view th.ac, table.tbl_view td.ac {padding-left:0;text-align:center;}' \
              'table.tbl_view th.small, table.tbl_view td.small {font-size:0.8em;}' \
              '</style> </head> <body>'
              '''

    message = '<table>'
    for i in input:
        message += str(i)
    message += '</table>'

    message = message.replace('td ', 'td style="text-align:center"')

    return message



