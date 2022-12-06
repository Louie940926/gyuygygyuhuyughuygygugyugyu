def M1(pow2: number):
    if pow2 >= 0:
        UDriver_PCA9685.digital_write(UDriver_PCA9685.Pin.P9, 1)
        UDriver_PCA9685.analog_write(UDriver_PCA9685.Pin.P8, Math.map(abs(pow2), 0, 100, 0, 1023))
    else:
        UDriver_PCA9685.digital_write(UDriver_PCA9685.Pin.P9, 0)
        UDriver_PCA9685.analog_write(UDriver_PCA9685.Pin.P8, Math.map(abs(pow2), 0, 100, 0, 1023))
def 移動方式():
    if LightValue == 0 or LightValue == 10:
        前後移動(50, 0)
    elif LightValue == 1 or LightValue == 3 or LightValue == 7:
        右轉(30, 90, 0)
    elif LightValue == 15:
        右轉(30, 20, 0)
    elif LightValue == 28 or LightValue == 16 or LightValue == 24:
        左轉(30, 90, 0)
    elif LightValue == 30:
        左轉(30, 20, 0)
    else:
        前後移動(30, 0)
def 光排偵測():
    global sT, P0Value, P1Value, P2Value, P3Value, P4Value, P10Value, LightP0, LightP1, LightP2, LightP3, LightP4, LightP10
    sT = 0
    P0Value = pins.analog_read_pin(AnalogPin.P0)
    P1Value = pins.analog_read_pin(AnalogPin.P1)
    P2Value = pins.analog_read_pin(AnalogPin.P2)
    P3Value = pins.analog_read_pin(AnalogPin.P3)
    P4Value = pins.analog_read_pin(AnalogPin.P4)
    P10Value = pins.analog_read_pin(AnalogPin.P10)
    if P0Value <= 300:
        LightP0 = 1
    else:
        LightP0 = 0
    if P1Value <= 300:
        LightP1 = 1
    else:
        LightP1 = 0
    if P2Value <= 300:
        LightP2 = 1
    else:
        LightP2 = 0
    if P3Value <= 525:
        LightP3 = 1
    else:
        LightP3 = 0
    if P4Value <= 600:
        LightP4 = 1
    else:
        LightP4 = 0
    if P10Value <= 800:
        LightP10 = 1
    else:
        LightP10 = 0
def 前後移動(pow3: number, sec: number):
    if sec == 0:
        M1(pow3)
        M2(pow3 * 94.9 / 100)
    else:
        M1(pow3)
        M2(pow3 * 94.9 / 100)
        basic.pause(sec * 1000)
        馬達停止()
def 左轉(pow4: number, steering: number, sec2: number):
    if sec2 == 0:
        M1(pow4 + 5)
        M2(steering * (-2 * pow4 / 100) + pow4)
    else:
        M1(pow4 + 5)
        M2(steering * (-2 * pow4 / 100) + pow4)
        basic.pause(sec2 * 1000)
        馬達停止()
def 右轉(pow5: number, steering2: number, sec3: number):
    if sec3 == 0:
        M1(steering2 * (-2 * pow5 / 100) + pow5)
        M2(pow5 + 5)
    else:
        M1(steering2 * (-2 * pow5 / 100) + pow5)
        M2(pow5 + 5)
        basic.pause(sec3 * 1000)
        馬達停止()
def M2(pow6: number):
    if pow6 >= 0:
        UDriver_PCA9685.digital_write(UDriver_PCA9685.Pin.P10, 1)
        UDriver_PCA9685.analog_write(UDriver_PCA9685.Pin.P11,
            Math.map(abs(pow6), 0, 100, 0, 1023))
    else:
        UDriver_PCA9685.digital_write(UDriver_PCA9685.Pin.P10, 0)
        UDriver_PCA9685.analog_write(UDriver_PCA9685.Pin.P11,
            Math.map(abs(pow6), 0, 100, 0, 1023))
def 馬達停止():
    M1(0)
    M2(0)
P10Value = 0
P4Value = 0
P3Value = 0
P2Value = 0
P1Value = 0
P0Value = 0
LightP10 = 0
LightP4 = 0
LightP3 = 0
LightP2 = 0
LightP1 = 0
LightP0 = 0
LightValue = 0
sT = 0
for index in range(5):
    sT = sonar.ping(DigitalPin.P13, DigitalPin.P14, PingUnit.CENTIMETERS)
LightValue = 0
LightP0 = 0
LightP1 = 0
LightP2 = 0
LightP3 = 0
LightP4 = 0
LightP10 = 0
P0Value = 0
P1Value = 0
P2Value = 0
P3Value = 0
P4Value = 0
P10Value = 0

def on_forever():
    global sT, LightValue
    sT = sonar.ping(DigitalPin.P13, DigitalPin.P14, PingUnit.CENTIMETERS)
    if sT <= 10 and sT > 0:
        馬達停止()
        basic.pause(1000)
        左轉(40, 100, 0.3)
        右轉(40, 15, 0)
        while not (pins.analog_read_pin(AnalogPin.P1) >= 300):
            pass
    else:
        光排偵測()
        LightValue = LightP0 * 16 + LightP1 * 8 + (LightP2 * 4 + LightP3 * 2) + LightP4 * 1
        移動方式()
basic.forever(on_forever)
