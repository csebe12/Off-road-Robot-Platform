EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L stripboard:TB6612 U2
U 1 1 5E620EC5
P 3300 3350
F 0 "U2" H 3375 3825 50  0000 C CNN
F 1 "TB6612" H 3375 3734 50  0000 C CNN
F 2 "stripboard:TB6612" H 3350 3150 50  0001 C CNN
F 3 "" H 3350 3150 50  0001 C CNN
	1    3300 3350
	1    0    0    -1  
$EndComp
$Comp
L stripboard:MPU-9250 U3
U 1 1 5E623759
P 9150 1300
F 0 "U3" V 9400 1500 50  0000 C CNN
F 1 "MPU-9250" V 9850 1500 50  0000 C CNN
F 2 "stripboard:MPU-9250" H 9150 1300 50  0001 C CNN
F 3 "" H 9150 1300 50  0001 C CNN
	1    9150 1300
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R5
U 1 1 5E62B209
P 10100 4000
F 0 "R5" V 10100 3950 50  0000 L CNN
F 1 "1k" H 10170 3955 50  0001 L CNN
F 2 "stripboard:R" V 10030 4000 50  0001 C CNN
F 3 "~" H 10100 4000 50  0001 C CNN
	1    10100 4000
	0    1    1    0   
$EndComp
$Comp
L Device:R R7
U 1 1 5E62B20F
P 10100 4100
F 0 "R7" V 10100 4050 50  0000 L CNN
F 1 "1k" H 10170 4055 50  0001 L CNN
F 2 "stripboard:R" V 10030 4100 50  0001 C CNN
F 3 "~" H 10100 4100 50  0001 C CNN
	1    10100 4100
	0    1    1    0   
$EndComp
$Comp
L Device:R R4
U 1 1 5E62B459
P 9600 3500
F 0 "R4" V 9600 3450 50  0000 L CNN
F 1 "1.8k" H 9350 3500 50  0000 L CNN
F 2 "stripboard:R" V 9530 3500 50  0001 C CNN
F 3 "~" H 9600 3500 50  0001 C CNN
	1    9600 3500
	1    0    0    -1  
$EndComp
$Comp
L Device:R R6
U 1 1 5E62C193
P 9700 3500
F 0 "R6" V 9700 3450 50  0000 L CNN
F 1 "1.8k" H 9770 3455 50  0001 L CNN
F 2 "stripboard:R" V 9630 3500 50  0001 C CNN
F 3 "~" H 9700 3500 50  0001 C CNN
	1    9700 3500
	1    0    0    -1  
$EndComp
$Comp
L Device:R R8
U 1 1 5E62C199
P 9800 3500
F 0 "R8" V 9800 3450 50  0000 L CNN
F 1 "1.8k" H 9870 3455 50  0001 L CNN
F 2 "stripboard:R" V 9730 3500 50  0001 C CNN
F 3 "~" H 9800 3500 50  0001 C CNN
	1    9800 3500
	1    0    0    -1  
$EndComp
$Comp
L stripboard:JST-XH-4 U6
U 1 1 5E625CDA
P 10950 3300
F 0 "U6" H 10800 3300 50  0000 L CNN
F 1 "JST-XH-4" H 10700 3500 50  0000 L CNN
F 2 "stripboard:JST_XH_B4B-XH-A_1x04_P2.50mm_Vertical" H 10950 3300 50  0001 C CNN
F 3 "" H 10950 3300 50  0001 C CNN
	1    10950 3300
	-1   0    0    -1  
$EndComp
$Comp
L stripboard:JST-XH-5 U7
U 1 1 5E626360
P 10950 3800
F 0 "U7" H 10800 3750 50  0000 L CNN
F 1 "JST-XH-5" H 10750 4000 50  0000 L CNN
F 2 "stripboard:JST_XH_B5B-XH-A_1x05_P2.50mm_Vertical" H 10950 3800 50  0001 C CNN
F 3 "" H 10950 3800 50  0001 C CNN
	1    10950 3800
	-1   0    0    -1  
$EndComp
$Comp
L stripboard:i2c-v1 U8
U 1 1 5E6745F6
P 7500 5850
F 0 "U8" H 7650 6150 50  0000 C CNN
F 1 "i2c-v1" H 7600 6450 50  0000 C CNN
F 2 "stripboard:i2c-v1" H 7500 5850 50  0001 C CNN
F 3 "" H 7500 5850 50  0001 C CNN
	1    7500 5850
	0    -1   1    0   
$EndComp
$Comp
L stripboard:spi U10
U 1 1 5E677F14
P 10950 5200
F 0 "U10" H 11050 5850 50  0000 C CNN
F 1 "spi" H 11000 6100 50  0000 C CNN
F 2 "stripboard:spi" H 10950 5200 50  0001 C CNN
F 3 "" H 10950 5200 50  0001 C CNN
	1    10950 5200
	1    0    0    -1  
$EndComp
$Comp
L stripboard-rescue:RaspberryPi3-Z-stripboard U4
U 1 1 5E679522
P 1900 6650
F 0 "U4" H 2375 8875 50  0000 C CNN
F 1 "RaspberryPi3-Z" H 2375 8784 50  0000 C CNN
F 2 "stripboard:Raspberry Pi 3 Model B" H 1900 6650 50  0001 C CNN
F 3 "" H 1900 6650 50  0001 C CNN
	1    1900 6650
	1    0    0    -1  
$EndComp
$Comp
L LED:NeoPixel_THT D1
U 1 1 5E677A56
P 3900 6650
F 0 "D1" H 3550 6400 50  0000 L CNN
F 1 "NeoPixel_THT" H 3350 6300 50  0000 L CNN
F 2 "stripboard:Neopixel" H 3950 6350 50  0001 L TNN
F 3 "https://www.adafruit.com/product/1938" H 4000 6275 50  0001 L TNN
	1    3900 6650
	1    0    0    1   
$EndComp
Wire Wire Line
	7450 4400 7450 5150
Wire Wire Line
	7450 5150 9250 5150
Wire Wire Line
	7550 4500 7550 5050
Wire Wire Line
	7550 5050 9150 5050
$Comp
L stripboard:servo-uart U17
U 1 1 5E6B8DFF
P 9300 6200
F 0 "U17" V 9100 6450 50  0000 L CNN
F 1 "servo-uart" V 9450 5900 50  0000 L CNN
F 2 "stripboard:servo-uart" H 9300 6200 50  0001 C CNN
F 3 "" H 9300 6200 50  0001 C CNN
	1    9300 6200
	0    1    1    0   
$EndComp
$Comp
L stripboard:uart U20
U 1 1 5E67D800
P 3750 5550
F 0 "U20" H 3650 5700 50  0000 C CNN
F 1 "uart" H 3550 5850 50  0000 C CNN
F 2 "stripboard:uart" H 3750 5550 50  0001 C CNN
F 3 "" H 3750 5550 50  0001 C CNN
	1    3750 5550
	-1   0    0    -1  
$EndComp
Wire Wire Line
	2700 5350 3750 5350
Wire Wire Line
	2700 5450 3750 5450
Wire Wire Line
	2700 5650 3400 5650
Wire Wire Line
	2700 5750 3200 5750
Wire Wire Line
	3200 5750 3200 7200
Wire Wire Line
	2700 5850 3050 5850
Wire Wire Line
	3050 5850 3050 7050
Wire Wire Line
	1900 5550 1450 5550
Wire Wire Line
	1450 5550 1450 7200
Wire Wire Line
	1900 5650 1550 5650
Wire Wire Line
	1550 5650 1550 7100
Wire Wire Line
	1900 5750 1650 5750
Wire Wire Line
	2700 5050 3300 5050
Text GLabel 1550 4650 0    50   Input ~ 0
3V3
Wire Wire Line
	1900 4650 1550 4650
Text GLabel 3300 5050 2    50   Input ~ 0
RPi(TX)-Pyb(RX)
Wire Wire Line
	2700 4950 3300 4950
Text GLabel 3300 4950 2    50   Input ~ 0
RPi(RX)-Pyb(TX)
Text GLabel 7200 3400 0    50   Input ~ 0
RPi(TX)-Pyb(RX)
Text GLabel 7200 3500 0    50   Input ~ 0
RPi(RX)-Pyb(TX)
Text GLabel 4050 3500 2    50   Input ~ 0
GND
Text GLabel 4050 3600 2    50   Input ~ 0
5V
$Comp
L Motor:Motor_DC M1
U 1 1 5E832AE6
P 1450 2650
F 0 "M1" V 1650 2350 50  0000 L CNN
F 1 "Motor_DC" V 1650 2500 50  0000 L CNN
F 2 "stripboard:screw-terminal" H 1450 2560 50  0001 C CNN
F 3 "~" H 1450 2560 50  0001 C CNN
	1    1450 2650
	0    -1   -1   0   
$EndComp
Wire Wire Line
	1250 2500 1250 2650
Wire Wire Line
	1250 3000 1250 3250
Text GLabel 7000 5550 1    50   Input ~ 0
GND
Text GLabel 7400 5550 1    50   Input ~ 0
5V
Text GLabel 7500 5550 1    50   Input ~ 0
3V3
Wire Wire Line
	7000 5850 7000 5550
Wire Wire Line
	7500 5850 7500 5550
Text GLabel 8100 5550 1    50   Input ~ 0
5V
Text GLabel 8000 5550 1    50   Input ~ 0
GND
Text GLabel 7900 5550 1    50   Input ~ 0
3V3
Wire Wire Line
	3050 3500 2950 3500
Wire Wire Line
	2950 3500 2950 3700
Wire Wire Line
	7800 6350 7900 6350
Wire Wire Line
	7750 6400 8000 6400
Wire Wire Line
	7700 6450 8100 6450
Wire Wire Line
	7900 6350 7900 6300
Wire Wire Line
	8000 6400 8000 6300
Wire Wire Line
	8100 6450 8100 6300
Wire Wire Line
	9750 5800 9850 5800
Wire Wire Line
	9850 5800 9850 6250
Wire Wire Line
	9850 6250 9750 6250
Wire Wire Line
	9650 5750 9900 5750
Wire Wire Line
	9900 5750 9900 6300
Wire Wire Line
	9900 6300 9650 6300
Wire Wire Line
	9550 5700 9950 5700
Wire Wire Line
	9950 5700 9950 6350
Wire Wire Line
	9950 6350 9550 6350
Text GLabel 9750 5550 1    50   Input ~ 0
3V3
Text GLabel 9650 5550 1    50   Input ~ 0
GND
Text GLabel 9550 5550 1    50   Input ~ 0
5V
Wire Wire Line
	9550 6200 9550 6350
Wire Wire Line
	9650 6200 9650 6300
Wire Wire Line
	9750 6200 9750 6250
$Comp
L stripboard:servo-uart U5
U 1 1 5E66BDA7
P 8350 5850
F 0 "U5" V 8200 6100 50  0000 L CNN
F 1 "servo-uart" V 7850 5550 50  0000 L CNN
F 2 "stripboard:servo-uart" H 8350 5850 50  0001 C CNN
F 3 "" H 8350 5850 50  0001 C CNN
	1    8350 5850
	0    -1   -1   0   
$EndComp
Wire Wire Line
	9550 5550 9550 5700
Connection ~ 9550 5700
Wire Wire Line
	9550 5700 9550 5850
Wire Wire Line
	9650 5550 9650 5750
Connection ~ 9650 5750
Wire Wire Line
	9650 5750 9650 5850
Wire Wire Line
	9750 5550 9750 5800
Connection ~ 9750 5800
Wire Wire Line
	9750 5800 9750 5850
Wire Wire Line
	8000 5850 8000 5750
Wire Wire Line
	7900 5850 7900 5800
Wire Wire Line
	8100 5550 8100 5700
Wire Wire Line
	7800 6350 7800 5800
Wire Wire Line
	7800 5800 7900 5800
Connection ~ 7900 5800
Wire Wire Line
	7900 5800 7900 5550
Wire Wire Line
	7750 5750 8000 5750
Wire Wire Line
	7750 5750 7750 6400
Connection ~ 8000 5750
Wire Wire Line
	8000 5750 8000 5550
Wire Wire Line
	7700 5700 8100 5700
Wire Wire Line
	7700 5700 7700 6450
Connection ~ 8100 5700
Wire Wire Line
	8100 5700 8100 5850
Wire Wire Line
	8600 4900 8700 4900
Wire Wire Line
	8700 4900 8700 5950
Wire Wire Line
	8700 5950 8250 5950
Wire Wire Line
	8600 4800 8750 4800
Wire Wire Line
	8750 4800 8750 6100
Wire Wire Line
	8750 6100 8250 6100
Wire Wire Line
	8600 4700 8800 4700
Wire Wire Line
	8800 4700 8800 6100
Wire Wire Line
	8800 6100 9400 6100
Wire Wire Line
	8600 4600 8850 4600
Wire Wire Line
	8850 5950 9400 5950
$Comp
L stripboard:i2c-v1 U19
U 1 1 5E683517
P 7650 1400
F 0 "U19" V 7750 1650 50  0000 C CNN
F 1 "i2c-v1" V 7950 1650 50  0000 C CNN
F 2 "stripboard:i2c-v1" H 7650 1400 50  0001 C CNN
F 3 "" H 7650 1400 50  0001 C CNN
	1    7650 1400
	0    -1   -1   0   
$EndComp
$Comp
L stripboard:i2c-v1 U18
U 1 1 5E6A84E0
P 8500 1400
F 0 "U18" V 8600 1650 50  0000 C CNN
F 1 "i2c-v1" V 8800 1650 50  0000 C CNN
F 2 "stripboard:i2c-v1" H 8500 1400 50  0001 C CNN
F 3 "" H 8500 1400 50  0001 C CNN
	1    8500 1400
	0    -1   -1   0   
$EndComp
Wire Wire Line
	8600 4100 9100 4100
Wire Wire Line
	9000 2000 8300 2000
Connection ~ 9000 2000
Connection ~ 8300 2000
Wire Wire Line
	8300 2000 7450 2000
Wire Wire Line
	9100 2100 8100 2100
Connection ~ 9100 2100
Connection ~ 8100 2100
Wire Wire Line
	8100 2100 7250 2100
Text GLabel 8500 1750 3    50   Input ~ 0
3V3
Text GLabel 8000 1750 3    50   Input ~ 0
GND
Text GLabel 7150 1750 3    50   Input ~ 0
GND
Text GLabel 7650 1750 3    50   Input ~ 0
3V3
Text GLabel 7550 1750 3    50   Input ~ 0
5V
Text GLabel 8400 1750 3    50   Input ~ 0
5V
Wire Wire Line
	9100 1400 9100 2100
Wire Wire Line
	9000 1400 9000 2000
Wire Wire Line
	8300 1400 8300 2000
Wire Wire Line
	8100 1400 8100 2100
Wire Wire Line
	8000 1400 8000 1750
Wire Wire Line
	8500 1400 8500 1750
Wire Wire Line
	8400 1400 8400 1500
Wire Wire Line
	7650 1400 7650 1750
Wire Wire Line
	7550 1400 7550 1500
Wire Wire Line
	7250 1400 7250 2100
Wire Wire Line
	7150 1400 7150 1750
Wire Wire Line
	7450 1400 7450 2000
Wire Wire Line
	7350 1400 7350 1500
Wire Wire Line
	7350 1500 7550 1500
Connection ~ 7550 1500
Wire Wire Line
	7550 1500 7550 1750
Wire Wire Line
	8200 1400 8200 1500
Wire Wire Line
	8200 1500 8400 1500
Connection ~ 8400 1500
Wire Wire Line
	8400 1500 8400 1750
Text GLabel 8900 1750 3    50   Input ~ 0
3V3
Text GLabel 8800 1750 3    50   Input ~ 0
GND
Wire Wire Line
	8800 1400 8800 1750
Wire Wire Line
	8900 1400 8900 1750
Text GLabel 10450 3200 0    50   Input ~ 0
GND
Wire Wire Line
	10950 3200 10450 3200
Wire Wire Line
	8600 4400 10050 4400
Wire Wire Line
	10050 4400 10050 4700
Wire Wire Line
	10050 4700 10950 4700
Wire Wire Line
	8600 4300 9950 4300
Wire Wire Line
	9950 4300 9950 4900
Wire Wire Line
	9950 4900 10950 4900
Wire Wire Line
	8600 4200 9850 4200
Wire Wire Line
	9850 5100 10950 5100
Text GLabel 10550 4800 0    50   Input ~ 0
3V3
Text GLabel 10550 5000 0    50   Input ~ 0
GND
Text GLabel 10550 4600 0    50   Input ~ 0
5V
Wire Wire Line
	10950 4600 10550 4600
Wire Wire Line
	10950 4800 10550 4800
Wire Wire Line
	10950 5000 10550 5000
Text GLabel 10450 3700 0    50   Input ~ 0
GND
Wire Wire Line
	9250 4100 9900 4100
Wire Wire Line
	10700 4000 10700 3500
Wire Wire Line
	10700 3500 10950 3500
Connection ~ 10700 4000
Wire Wire Line
	10700 4000 10950 4000
Wire Wire Line
	10600 3900 10600 3400
Wire Wire Line
	10600 3400 10950 3400
Connection ~ 10600 3900
Wire Wire Line
	10600 3900 10950 3900
Wire Wire Line
	10500 3300 10950 3300
Wire Wire Line
	10950 3700 10450 3700
Wire Wire Line
	10950 3800 10500 3800
Wire Wire Line
	10500 3800 10500 3300
Connection ~ 10500 3800
Wire Wire Line
	8600 3900 9700 3900
$Comp
L Device:R R3
U 1 1 5E62ABD7
P 10100 3900
F 0 "R3" V 10100 3850 50  0000 L CNN
F 1 "1k" H 10170 3855 50  0001 L CNN
F 2 "stripboard:R" V 10030 3900 50  0001 C CNN
F 3 "~" H 10100 3900 50  0001 C CNN
	1    10100 3900
	0    1    1    0   
$EndComp
Wire Wire Line
	8600 3800 9600 3800
Wire Wire Line
	10500 3800 10250 3800
$Comp
L Device:R R2
U 1 1 5E62A6E5
P 9900 3500
F 0 "R2" V 9900 3450 50  0000 L CNN
F 1 "1.8k" H 9970 3455 50  0001 L CNN
F 2 "stripboard:R" V 9830 3500 50  0001 C CNN
F 3 "~" H 9900 3500 50  0001 C CNN
	1    9900 3500
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 5E6292EE
P 10100 3800
F 0 "R1" V 10100 3750 50  0000 L CNN
F 1 "1k" V 10000 3750 50  0000 L CNN
F 2 "stripboard:R" V 10030 3800 50  0001 C CNN
F 3 "~" H 10100 3800 50  0001 C CNN
	1    10100 3800
	0    1    1    0   
$EndComp
Wire Wire Line
	10250 3900 10600 3900
Wire Wire Line
	10250 4000 10700 4000
Wire Wire Line
	10250 4100 10950 4100
Text GLabel 9750 3250 1    50   Input ~ 0
GND
Wire Wire Line
	9900 3350 9800 3350
Connection ~ 9700 3350
Wire Wire Line
	9700 3350 9600 3350
Connection ~ 9800 3350
Wire Wire Line
	9800 3350 9750 3350
Wire Wire Line
	9750 3350 9750 3250
Connection ~ 9750 3350
Wire Wire Line
	9750 3350 9700 3350
Wire Wire Line
	9600 3650 9600 3800
Connection ~ 9600 3800
Wire Wire Line
	9600 3800 9950 3800
Wire Wire Line
	9700 3650 9700 3900
Connection ~ 9700 3900
Wire Wire Line
	9700 3900 9950 3900
Wire Wire Line
	9800 3650 9800 4000
Connection ~ 9800 4000
Wire Wire Line
	9900 3650 9900 4100
Connection ~ 9900 4100
Wire Wire Line
	9900 4100 9950 4100
$Comp
L Device:R R11
U 1 1 5F050C6D
P 3450 6650
F 0 "R11" V 3450 6600 50  0000 L CNN
F 1 "470" V 3350 6600 50  0000 L CNN
F 2 "stripboard:R" V 3380 6650 50  0001 C CNN
F 3 "~" H 3450 6650 50  0001 C CNN
	1    3450 6650
	0    -1   1    0   
$EndComp
Wire Wire Line
	7100 4200 7100 5250
Wire Wire Line
	7400 5550 7400 5750
Wire Wire Line
	7200 5850 7200 5750
Wire Wire Line
	7200 5750 7400 5750
Connection ~ 7400 5750
Wire Wire Line
	7400 5750 7400 5850
$Comp
L Device:R R9
U 1 1 5F0C12BF
P 4050 7200
F 0 "R9" V 4050 7150 50  0000 L CNN
F 1 "1.6k" V 3950 7100 50  0000 L CNN
F 2 "stripboard:R" V 3980 7200 50  0001 C CNN
F 3 "~" H 4050 7200 50  0001 C CNN
	1    4050 7200
	0    -1   1    0   
$EndComp
$Comp
L Device:R R10
U 1 1 5F0C13FE
P 3900 7350
F 0 "R10" V 3900 7300 50  0000 L CNN
F 1 "560" V 3800 7300 50  0000 L CNN
F 2 "stripboard:R" V 3830 7350 50  0001 C CNN
F 3 "~" H 3900 7350 50  0001 C CNN
	1    3900 7350
	1    0    0    1   
$EndComp
Text GLabel 3900 6300 1    50   Input ~ 0
GND
Text GLabel 3900 7500 3    50   Input ~ 0
5V
Text GLabel 4200 7200 2    50   Input ~ 0
GND
Connection ~ 3900 7200
$Comp
L Device:C_Small C1
U 1 1 5F135D51
P 4350 6650
F 0 "C1" H 4100 6700 50  0000 L CNN
F 1 "0.1 uF" H 4000 6600 50  0000 L CNN
F 2 "stripboard:capacitor" H 4350 6650 50  0001 C CNN
F 3 "~" H 4350 6650 50  0001 C CNN
	1    4350 6650
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3900 6950 3900 7200
Wire Wire Line
	4350 6750 4350 6950
Wire Wire Line
	4350 6950 3900 6950
Connection ~ 3900 6950
Wire Wire Line
	4350 6550 4350 6350
Wire Wire Line
	4350 6350 3900 6350
Wire Wire Line
	3900 6300 3900 6350
Connection ~ 3900 6350
Text GLabel 8100 3000 1    50   Input ~ 0
5V
$Comp
L stripboard:INA219 U9
U 1 1 5E7189B6
P 400 3200
F 0 "U9" V 600 3650 50  0000 R CNN
F 1 "INA219" V 500 3750 50  0000 R CNN
F 2 "stripboard:INA219" H 400 3200 50  0001 C CNN
F 3 "" H 400 3200 50  0001 C CNN
	1    400  3200
	0    1    1    0   
$EndComp
Wire Wire Line
	700  3850 700  3500
Text GLabel 700  3850 3    50   Input ~ 0
Vlipo
Wire Wire Line
	900  3500 900  3600
Text GLabel 800  3850 3    50   Input ~ 0
GND
Wire Wire Line
	800  3500 800  3850
Text GLabel 850  2850 1    50   Input ~ 0
GND
Text GLabel 950  2850 1    50   Input ~ 0
3V3
Wire Wire Line
	850  3200 850  2850
Wire Wire Line
	950  3200 950  2850
$Comp
L Device:C_Small C5
U 1 1 5E7AE554
P 8200 3150
F 0 "C5" V 8200 2550 50  0000 L CNN
F 1 "100 nF" V 8200 2700 50  0000 L CNN
F 2 "stripboard:capacitor" H 8200 3150 50  0001 C CNN
F 3 "~" H 8200 3150 50  0001 C CNN
	1    8200 3150
	0    -1   -1   0   
$EndComp
Wire Wire Line
	8100 3000 8100 3150
Connection ~ 8100 3150
Wire Wire Line
	8100 3150 8100 3350
Wire Wire Line
	8350 3350 8350 3150
Wire Wire Line
	8350 3150 8300 3150
$Comp
L Device:C_Small C2
U 1 1 5E82DCBF
P 3350 4650
F 0 "C2" H 3150 4700 50  0000 L CNN
F 1 "100 nF" H 3000 4600 50  0000 L CNN
F 2 "stripboard:capacitor" H 3350 4650 50  0001 C CNN
F 3 "~" H 3350 4650 50  0001 C CNN
	1    3350 4650
	1    0    0    -1  
$EndComp
Text GLabel 3350 4450 1    50   Input ~ 0
5V
Text GLabel 3500 4850 2    50   Input ~ 0
GND
Wire Wire Line
	2700 4750 3100 4750
Wire Wire Line
	3100 4750 3100 4550
Wire Wire Line
	3100 4550 3350 4550
Connection ~ 3350 4550
Wire Wire Line
	2700 4850 3350 4850
Wire Wire Line
	3350 4750 3350 4850
Connection ~ 3350 4850
Wire Wire Line
	3350 4850 3500 4850
Wire Wire Line
	3350 4450 3350 4550
$Comp
L Switch:SW_SPDT SW11
U 1 1 5E903C42
P 3950 5800
F 0 "SW11" V 3950 5500 50  0000 C CNN
F 1 "SW_SPDT" V 3850 5500 50  0000 C CNN
F 2 "" H 3950 5800 50  0001 C CNN
F 3 "~" H 3950 5800 50  0001 C CNN
	1    3950 5800
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R17
U 1 1 5E93C002
P 6700 2250
F 0 "R17" V 6800 2200 50  0000 L CNN
F 1 "10k" V 6700 2200 50  0000 L CNN
F 2 "stripboard:R" V 6630 2250 50  0001 C CNN
F 3 "~" H 6700 2250 50  0001 C CNN
	1    6700 2250
	0    1    1    0   
$EndComp
Text GLabel 3550 2200 0    50   Input ~ 0
3V3
Connection ~ 7100 5250
Wire Wire Line
	7100 5250 7100 5850
$Comp
L stripboard:i2c-Rpi U15
U 1 1 5EB381C8
P 800 5000
F 0 "U15" H 600 5200 50  0000 L CNN
F 1 "i2c-Rpi" H 550 5450 50  0000 L CNN
F 2 "stripboard:i2c Rpi" H 800 5000 50  0001 C CNN
F 3 "" H 800 5000 50  0001 C CNN
	1    800  5000
	1    0    0    -1  
$EndComp
$Comp
L stripboard:spi-RPi U12
U 1 1 5EBD6E64
P 2500 7500
F 0 "U12" V 2350 7250 50  0000 R CNN
F 1 "spi-RPi" V 2450 7400 50  0000 R CNN
F 2 "stripboard:spi-RPi" H 2500 7500 50  0001 C CNN
F 3 "" H 2500 7500 50  0001 C CNN
	1    2500 7500
	0    -1   -1   0   
$EndComp
Wire Wire Line
	1650 5750 1650 7000
Wire Wire Line
	1450 7200 2100 7200
Wire Wire Line
	2100 7200 2100 7500
Wire Wire Line
	1550 7100 2200 7100
Wire Wire Line
	2200 7100 2200 7500
Wire Wire Line
	1650 7000 2300 7000
Wire Wire Line
	2300 7000 2300 7500
Wire Wire Line
	3200 7200 2500 7200
Wire Wire Line
	2500 7200 2500 7500
Wire Wire Line
	3050 7050 2400 7050
Wire Wire Line
	2400 7050 2400 7500
Wire Wire Line
	9000 2000 9000 4000
Wire Wire Line
	9100 2100 9100 4100
Wire Wire Line
	7850 4500 7550 4500
Wire Wire Line
	7850 4400 7450 4400
Wire Wire Line
	7300 4300 7850 4300
Wire Wire Line
	7100 4200 7850 4200
Wire Wire Line
	7850 3900 7200 3900
Wire Wire Line
	7200 3800 7850 3800
Wire Wire Line
	7200 3700 7850 3700
Wire Wire Line
	7200 3600 7850 3600
Wire Wire Line
	7850 3500 7200 3500
Wire Wire Line
	7200 3400 7850 3400
Text GLabel 6150 1950 0    50   Input ~ 0
3V3
$Comp
L Device:R R16
U 1 1 5E93BFFC
P 6700 1850
F 0 "R16" V 6800 1800 50  0000 L CNN
F 1 "10k" V 6700 1800 50  0000 L CNN
F 2 "stripboard:R" V 6630 1850 50  0001 C CNN
F 3 "~" H 6700 1850 50  0001 C CNN
	1    6700 1850
	0    1    1    0   
$EndComp
$Comp
L Device:R R15
U 1 1 5E84497C
P 6500 5800
F 0 "R15" V 6600 5750 50  0000 L CNN
F 1 "10k" V 6500 5750 50  0000 L CNN
F 2 "stripboard:R" V 6430 5800 50  0001 C CNN
F 3 "~" H 6500 5800 50  0001 C CNN
	1    6500 5800
	1    0    0    -1  
$EndComp
Text GLabel 6600 6350 3    50   Input ~ 0
3V3
$Comp
L Switch:SW_Push_DPDT SW3
U 1 1 5E844983
P 6400 6150
F 0 "SW3" H 6150 6050 50  0000 C CNN
F 1 "SW_Push_DPDT" H 6100 6200 50  0000 C CNN
F 2 "stripboard:dpdt" H 6400 6350 50  0001 C CNN
F 3 "~" H 6400 6350 50  0001 C CNN
	1    6400 6150
	0    -1   -1   0   
$EndComp
Text GLabel 6200 6350 3    50   Input ~ 0
3V3
$Comp
L Device:R R14
U 1 1 5E84498A
P 6100 5800
F 0 "R14" V 6200 5750 50  0000 L CNN
F 1 "10k" V 6100 5750 50  0000 L CNN
F 2 "stripboard:R" V 6030 5800 50  0001 C CNN
F 3 "~" H 6100 5800 50  0001 C CNN
	1    6100 5800
	1    0    0    -1  
$EndComp
Wire Wire Line
	6500 5250 6500 5650
Wire Wire Line
	6500 5250 7100 5250
Wire Wire Line
	6100 5150 6100 5650
$Comp
L Device:R R13
U 1 1 5E8A3859
P 1250 5500
F 0 "R13" V 1350 5450 50  0000 L CNN
F 1 "10k" V 1250 5450 50  0000 L CNN
F 2 "stripboard:R" V 1180 5500 50  0001 C CNN
F 3 "~" H 1250 5500 50  0001 C CNN
	1    1250 5500
	0    1    1    0   
$EndComp
Text GLabel 700  5600 0    50   Input ~ 0
3V3
$Comp
L Switch:SW_Push_DPDT SW1
U 1 1 5E8A3860
P 900 5400
F 0 "SW1" H 800 4900 50  0000 C CNN
F 1 "SW_Push_DPDT" H 800 5000 50  0000 C CNN
F 2 "stripboard:dpdt" H 900 5600 50  0001 C CNN
F 3 "~" H 900 5600 50  0001 C CNN
	1    900  5400
	1    0    0    -1  
$EndComp
Text GLabel 700  5200 0    50   Input ~ 0
3V3
$Comp
L Device:R R12
U 1 1 5E8A3867
P 1250 5100
F 0 "R12" V 1350 5050 50  0000 L CNN
F 1 "10k" V 1250 5050 50  0000 L CNN
F 2 "stripboard:R" V 1180 5100 50  0001 C CNN
F 3 "~" H 1250 5100 50  0001 C CNN
	1    1250 5100
	0    1    1    0   
$EndComp
Wire Wire Line
	1400 5100 1450 5100
Wire Wire Line
	1450 5100 1450 4750
Wire Wire Line
	1400 5500 1550 5500
Wire Wire Line
	3850 5600 3850 5550
Wire Wire Line
	2700 5550 3850 5550
Wire Wire Line
	3400 6000 3950 6000
Wire Wire Line
	3400 5650 3400 6000
Wire Wire Line
	7300 5150 7300 5850
Wire Wire Line
	7300 4300 7300 5150
Connection ~ 7300 5150
Wire Wire Line
	6100 5150 7300 5150
Wire Wire Line
	2700 6150 3300 6150
Wire Wire Line
	3300 6150 3300 6650
Wire Wire Line
	1900 1900 1550 1900
Wire Wire Line
	2250 1900 2450 1900
Connection ~ 2250 1900
Wire Wire Line
	2250 1550 2250 1900
Wire Wire Line
	2200 1900 2250 1900
$Comp
L Device:Fuse F1
U 1 1 5EEA94BA
P 2050 1900
F 0 "F1" V 1853 1900 50  0000 C CNN
F 1 "Fuse" V 1944 1900 50  0000 C CNN
F 2 "stripboard:fuse" V 1980 1900 50  0001 C CNN
F 3 "~" H 2050 1900 50  0001 C CNN
	1    2050 1900
	0    1    1    0   
$EndComp
Text Notes 2500 2100 0    50   ~ 0
5V switch
Text Notes 2450 1250 0    50   ~ 0
Motor switch
Text GLabel 3850 2000 2    50   Input ~ 0
GND
Text GLabel 3850 1900 2    50   Input ~ 0
5V
Text GLabel 3850 1550 2    50   Input ~ 0
Vlipo
Text Label 3300 1550 0    50   ~ 0
Vlipo
Wire Wire Line
	3550 2000 3850 2000
Wire Wire Line
	3550 1900 3850 1900
Wire Wire Line
	2850 1550 3850 1550
Wire Wire Line
	2250 1550 2450 1550
Wire Wire Line
	1550 2000 3200 2000
Wire Wire Line
	2850 1900 3200 1900
$Comp
L Switch:SW_SPST SW15
U 1 1 5E6A45E6
P 2650 1550
F 0 "SW15" H 2650 1785 50  0000 C CNN
F 1 "SW_SPST" H 2650 1694 50  0000 C CNN
F 2 "" H 2650 1550 50  0001 C CNN
F 3 "~" H 2650 1550 50  0001 C CNN
	1    2650 1550
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_SPST SW20
U 1 1 5E6A4179
P 2650 1900
F 0 "SW20" H 2650 2135 50  0000 C CNN
F 1 "SW_SPST" H 2650 2044 50  0000 C CNN
F 2 "" H 2650 1900 50  0001 C CNN
F 3 "~" H 2650 1900 50  0001 C CNN
	1    2650 1900
	1    0    0    -1  
$EndComp
$Comp
L stripboard:power U16
U 1 1 5E67DFFC
P 1550 2050
F 0 "U16" H 1400 2200 50  0000 L CNN
F 1 "power" H 1250 2300 50  0000 L CNN
F 2 "stripboard:screw-terminal" H 1550 2050 50  0001 C CNN
F 3 "" H 1550 2050 50  0001 C CNN
	1    1550 2050
	1    0    0    -1  
$EndComp
$Comp
L stripboard:buck-converter U11
U 1 1 5E66D723
P 3200 2300
F 0 "U11" H 3400 2925 50  0000 C CNN
F 1 "buck-converter" H 3400 2834 50  0000 C CNN
F 2 "stripboard:buck converter" H 3200 2300 50  0001 C CNN
F 3 "" H 3200 2300 50  0001 C CNN
	1    3200 2300
	1    0    0    -1  
$EndComp
Wire Wire Line
	1550 5500 1550 4850
Wire Wire Line
	800  4750 1450 4750
Wire Wire Line
	800  4850 1550 4850
Connection ~ 1450 4750
Wire Wire Line
	1450 4750 1900 4750
Connection ~ 1550 4850
Wire Wire Line
	1550 4850 1900 4850
Wire Notes Line width 16 style solid
	4850 2350 450  2350
Wire Notes Line width 16 style solid
	4850 4150 450  4150
Wire Notes Line width 16 style solid
	4850 450  4850 7800
Text Notes 550  750  0    118  ~ 0
Power management
Text Notes 600  4350 0    118  ~ 0
Raspberry Pi connections
Text Notes 9300 750  0    118  ~ 0
Pyboard connections
Text Notes 7350 7500 0    79   ~ 0
Off-road robotic platform schematic
Text Notes 8150 7650 0    79   ~ 0
12/03/2020
Text Notes 7000 6650 0    79   ~ 0
Schematic designed by: Bence Cserkuti (bc1u17@soton.ac.uk)
$Comp
L Switch:SW_Push_DPDT SW2
U 1 1 5E6D36D2
P 6350 2150
F 0 "SW2" H 6100 2050 50  0000 C CNN
F 1 "SW_Push_DPDT" H 6050 2200 50  0000 C CNN
F 2 "stripboard:dpdt" H 6350 2350 50  0001 C CNN
F 3 "~" H 6350 2350 50  0001 C CNN
	1    6350 2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	900  3600 3050 3600
Wire Wire Line
	7450 2000 6850 2000
Wire Wire Line
	6850 2000 6850 1850
Connection ~ 7450 2000
Wire Wire Line
	7250 2100 6850 2100
Wire Wire Line
	6850 2100 6850 2250
Connection ~ 7250 2100
Wire Wire Line
	3650 3600 4050 3600
Wire Wire Line
	3650 3500 4000 3500
Wire Wire Line
	4000 3700 4000 3500
Wire Wire Line
	2950 3700 4000 3700
Connection ~ 4000 3500
Wire Wire Line
	4000 3500 4050 3500
Text GLabel 650  2850 1    50   Input ~ 0
SDA
Text GLabel 750  2850 1    50   Input ~ 0
SCL
Text GLabel 4000 3100 2    50   Input ~ 0
PWM_L
Text GLabel 4000 3200 2    50   Input ~ 0
PWM_R
Text GLabel 4000 3300 2    50   Input ~ 0
DIR_L
Text GLabel 4000 3400 2    50   Input ~ 0
DIR_R
Wire Wire Line
	9150 5050 9150 4000
Wire Wire Line
	9150 4000 9800 4000
Wire Wire Line
	9850 4200 9850 5100
Wire Wire Line
	9250 5150 9250 4100
Wire Wire Line
	9800 4000 9950 4000
Wire Wire Line
	8850 4600 8850 5950
Wire Wire Line
	8600 4000 9000 4000
Wire Wire Line
	8600 4500 10950 4500
$Comp
L stripboard:Pyboard U1
U 1 1 5E61D9E3
P 8550 4700
F 0 "U1" H 8250 5850 50  0000 C CNN
F 1 "Pyboard" H 8250 5950 50  0000 C CNN
F 2 "stripboard:Pyboard" H 8550 4700 50  0001 C CNN
F 3 "" H 8550 4700 50  0001 C CNN
	1    8550 4700
	1    0    0    -1  
$EndComp
Text GLabel 7200 3600 0    50   Input ~ 0
PWM_L
Text GLabel 7200 3700 0    50   Input ~ 0
PWM_R
Text GLabel 7200 3800 0    50   Input ~ 0
DIR_L
Text GLabel 7200 3900 0    50   Input ~ 0
DIR_R
Wire Wire Line
	3650 3400 4000 3400
Wire Wire Line
	3650 3300 4000 3300
Wire Wire Line
	3650 3200 4000 3200
Wire Wire Line
	3650 3100 4000 3100
Wire Wire Line
	750  2850 750  3200
Wire Wire Line
	650  2850 650  3200
Text Notes 600  2550 0    118  ~ 0
Motor
$Comp
L Device:C C10
U 1 1 5EAB2CD0
P 1500 3500
F 0 "C10" V 1550 3350 50  0000 C CNN
F 1 "100nF" V 1550 3700 50  0000 C CNN
F 2 "" H 1538 3350 50  0001 C CNN
F 3 "~" H 1500 3500 50  0001 C CNN
	1    1500 3500
	0    1    1    0   
$EndComp
$Comp
L Device:C C11
U 1 1 5EAC6E1F
P 1500 2900
F 0 "C11" V 1550 2750 50  0000 C CNN
F 1 "100nF" V 1550 3100 50  0000 C CNN
F 2 "" H 1538 2750 50  0001 C CNN
F 3 "~" H 1500 2900 50  0001 C CNN
	1    1500 2900
	0    1    1    0   
$EndComp
$Comp
L Motor:Motor_DC M2
U 1 1 5E832281
P 1450 3250
F 0 "M2" V 1650 2950 50  0000 L CNN
F 1 "Motor_DC" V 1650 3100 50  0000 L CNN
F 2 "stripboard:screw-terminal" H 1450 3160 50  0001 C CNN
F 3 "~" H 1450 3160 50  0001 C CNN
	1    1450 3250
	0    -1   -1   0   
$EndComp
Wire Wire Line
	1250 3250 1250 3500
Wire Wire Line
	1250 3500 1350 3500
Connection ~ 1250 3250
Wire Wire Line
	1750 3250 1750 3400
Wire Wire Line
	1750 3500 1650 3500
Wire Wire Line
	1250 2650 1250 2900
Wire Wire Line
	1250 2900 1350 2900
Connection ~ 1250 2650
Wire Wire Line
	1650 2900 1750 2900
Wire Wire Line
	1750 2900 1750 2800
Wire Wire Line
	3050 3400 1750 3400
Connection ~ 1750 3400
Wire Wire Line
	1750 3400 1750 3500
Wire Wire Line
	3050 3300 1850 3300
Wire Wire Line
	1850 3300 1850 3000
Wire Wire Line
	1250 3000 1850 3000
Wire Wire Line
	3050 3200 1950 3200
Wire Wire Line
	1950 3200 1950 2800
Wire Wire Line
	1950 2800 1750 2800
Connection ~ 1750 2800
Wire Wire Line
	1750 2800 1750 2650
Wire Wire Line
	3050 3100 2050 3100
Wire Wire Line
	2050 3100 2050 2500
Wire Wire Line
	1250 2500 2050 2500
$EndSCHEMATC
