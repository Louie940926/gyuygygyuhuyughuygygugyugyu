function M1 (pow2: number) {
    if (pow2 >= 0) {
        UDriver_PCA9685.digital_write(UDriver_PCA9685.Pin.P9, 1)
        UDriver_PCA9685.analog_write(UDriver_PCA9685.Pin.P8, Math.map(Math.abs(pow2), 0, 100, 0, 1023))
    } else {
        UDriver_PCA9685.digital_write(UDriver_PCA9685.Pin.P9, 0)
        UDriver_PCA9685.analog_write(UDriver_PCA9685.Pin.P8, Math.map(Math.abs(pow2), 0, 100, 0, 1023))
    }
}
function 移動方式 () {
    if (LightValue == 0 || LightValue == 10) {
        前後移動(50, 0)
    } else if (LightValue == 1 || LightValue == 3 || LightValue == 7) {
        右轉(30, 90, 0)
    } else if (LightValue == 6) {
        右轉(30, 20, 0)
    } else if (LightValue == 28 || LightValue == 16 || LightValue == 24) {
        左轉(30, 90, 0)
    } else if (LightValue == 30) {
        左轉(30, 20, 0)
    } else {
        前後移動(30, 0)
    }
}
function 光排偵測 () {
    P0Value = pins.analogReadPin(AnalogPin.P0)
    P1Value = pins.analogReadPin(AnalogPin.P1)
    P2Value = pins.analogReadPin(AnalogPin.P2)
    P3Value = pins.analogReadPin(AnalogPin.P3)
    P4Value = pins.analogReadPin(AnalogPin.P4)
    P10Value = pins.analogReadPin(AnalogPin.P10)
    if (P0Value <= 60) {
        LightP0 = 1
    } else {
        LightP0 = 0
    }
    if (P1Value <= 55) {
        LightP1 = 1
    } else {
        LightP1 = 0
    }
    if (P2Value <= 140) {
        LightP2 = 1
    } else {
        LightP2 = 0
    }
    if (P3Value <= 600) {
        LightP3 = 1
    } else {
        LightP3 = 0
    }
    if (P4Value <= 530) {
        LightP4 = 1
    } else {
        LightP4 = 0
    }
}
function 前後移動 (pow3: number, sec: number) {
    if (sec == 0) {
        M1(pow3)
        M2(pow3 * 94.9 / 100)
    } else {
        M1(pow3)
        M2(pow3 * 94.9 / 100)
        basic.pause(sec * 1000)
        馬達停止()
    }
}
function 左轉 (pow4: number, steering: number, sec2: number) {
    if (sec2 == 0) {
        M1(pow4 + 5)
        M2(steering * (-2 * pow4 / 100) + pow4)
    } else {
        M1(pow4 + 5)
        M2(steering * (-2 * pow4 / 100) + pow4)
        basic.pause(sec2 * 1000)
        馬達停止()
    }
}
function 右轉 (pow5: number, steering2: number, sec3: number) {
    if (sec3 == 0) {
        M1(steering2 * (-2 * pow5 / 100) + pow5)
        M2(pow5 + 5)
    } else {
        M1(steering2 * (-2 * pow5 / 100) + pow5)
        M2(pow5 + 5)
        basic.pause(sec3 * 1000)
        馬達停止()
    }
}
function M2 (pow6: number) {
    if (pow6 >= 0) {
        UDriver_PCA9685.digital_write(UDriver_PCA9685.Pin.P10, 1)
        UDriver_PCA9685.analog_write(UDriver_PCA9685.Pin.P11, Math.map(Math.abs(pow6), 0, 100, 0, 1023))
    } else {
        UDriver_PCA9685.digital_write(UDriver_PCA9685.Pin.P10, 0)
        UDriver_PCA9685.analog_write(UDriver_PCA9685.Pin.P11, Math.map(Math.abs(pow6), 0, 100, 0, 1023))
    }
}
function 馬達停止 () {
    M1(0)
    M2(0)
}
let P10Value = 0
let P4Value = 0
let P3Value = 0
let P2Value = 0
let P1Value = 0
let P0Value = 0
let LightP4 = 0
let LightP3 = 0
let LightP2 = 0
let LightP1 = 0
let LightP0 = 0
let LightValue = 0
LightValue = 0
LightP0 = 0
LightP1 = 0
LightP2 = 0
LightP3 = 0
LightP4 = 0
let LightP10 = 0
P0Value = 0
P1Value = 0
P2Value = 0
P3Value = 0
P4Value = 0
P10Value = 0
basic.forever(function () {
    光排偵測()
    LightValue = LightP0 * 16 + LightP1 * 8 + (LightP2 * 4 + LightP3 * 2) + LightP4 * 1
    移動方式()
})
