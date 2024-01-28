import winsound, random, sys, os
from datetime import datetime
from waiter import Wait as wait

custom_lib_path = os.path.join(os.path.dirname(__file__), '..', '..', 'CustomLibraries')
normcus_lib_path = os.path.normpath(custom_lib_path)
sys.path.append(normcus_lib_path)

alarm_date = input('Enter the date on which you want to set the alarm: ').strip()
alarm_time = ''.join(input("Enter the time of alarm to be set in HH:MM,AM/PM format: ").split())
music_or_beep = input("Enter m for a music or b for beep sound: ")

if music_or_beep == 'b':
    dur = int(input("Duration in seconds: ")) * 1000 #winsound takes in milliseconds
    freq = int(input("Frequency of the noise: ")) #optimal- 500

alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_period = alarm_time[6:8].upper()

print('Setting alarm.', end = "", flush = True)
for _ in range(random.randint(4,6)):
    wait(.58528)
    print(".", end = "", flush = True)

print("\n")

while True:
    current_time = datetime.now()
    current_hour = current_time.strftime('%I')
    current_minute = current_time.strftime('%M')
    current_period = current_time.strftime('%p')
    current_date = current_time.strftime('%d')
    if current_date == alarm_date and current_period == alarm_period and current_hour == alarm_hour and current_minute == alarm_minute:
        print('*'*10)
        print('| '+'Wake up!'+' |')
        print('*'*10)
        if music_or_beep=='m':
            winsound.PlaySound('audio.wav', winsound.SND_FILENAME)
        else:
            winsound.Beep(freq,dur)
        break