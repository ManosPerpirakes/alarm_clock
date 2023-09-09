import playsound
import time

filedir = 'alarm.mp3'
print('Enter the time in the format shown in the examples below')
print('Thu Aug 31 15:12:26 2023')
print('Tue Aug  1 15:12:26 2023')
print('Sun Jul  2 15:12:26 2023')
print('Fri Jun  2 15:12:26 2023')
print('Wed May  3 15:12:26 2023')
print('Mon Apr  3 15:12:26 2023')
print('Sat Mar  4 14:12:26 2023')
print('Thu Feb  2 14:12:26 2023')
print('Tue Jan  3 14:12:26 2023')
print('Sun Dec  4 14:12:26 2022')
print('Fri Nov  4 14:12:26 2022')
print('Wed Oct  5 15:12:26 2022')
timeinput = input('Please type here:')
print('processing...')
close = False
timevar = time.time()
while close == False:
    if timeinput == time.ctime(timevar):
        close = True
    else:
        timevar += 1
print('done. the alarm will ring at the chosen time. please do not close the program or the computer (because if this happens the alarm will not ring)')
close = False
while close == False:
    if timeinput == time.ctime(time.time()):
        close = True
while True:
    playsound.playsound(filedir)
    print('the alarm will ring again in 5 minutes. wake up to close the program.')
    time.sleep(300)