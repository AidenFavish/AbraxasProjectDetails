import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

print("{:>5}\t{:>5}".format('raw', 'v'))

mem: [float] = []
max_mem = 10
average = 0.032

while True:
    print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
    print(f"average: {average}")

    if chan.voltage - average:
        exec(open("~/Desktop/AbraxasProject/AbraxasNotificationSystem/main.py").read())

    if len(mem) < max_mem:
        mem.append(chan.voltage)
    else:
        mem.remove(0)
        mem.append(chan.voltage)

    sum = 0
    for i in mem:
        sum += i
    average = sum / len(mem)

    time.sleep(0.5)