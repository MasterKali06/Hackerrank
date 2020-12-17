'''
    Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
'''


def timeConversion(s):

    time = s.split(":")
    print(time)
    if s[-2:] == 'PM':
        if time[0] != '12':
            time[0] = str(int(time[0]) + 12)
    else:
        if time[0] == '12':
            time[0] = '00'
    ntime = ':'.join(time)
    print(str(ntime[:-2]))

timeConversion("07:05:45PM")

