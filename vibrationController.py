from gpiozero import InputDevice, OutputDevice, PWMOutputDevice
from time import sleep, time

# the patterns are stored localy and the app sends string.
array_pattern = ['M3','M2','M4']

M1 = PWMOutputDevice(5)
M2 = PWMOutputDevice(6)
M3 = PWMOutputDevice(13)
M4 = PWMOutputDevice(22)
M5 = PWMOutputDevice(27)

for e in array_pattern:
    if e == 'M1':
        M1.value = 0.5
        sleep(2)
        M1.value = 0
    elif e == 'M2':
        M2.value = 0.5
        sleep(2)
        M2.value = 0
    elif e == 'M3':
        M3.value = 0.5
        sleep(2)
        M3.value = 0
    elif e == 'M4':
        M3.value = 0.5
        sleep(2)
        M3.value = 0
    elif e == 'M5':
        M3.value = 0.5
        sleep(2)
        M3.value = 0

print("done")
