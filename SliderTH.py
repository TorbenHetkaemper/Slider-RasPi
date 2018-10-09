import PiMotor
import Adafruit_ADS1x15
import time
import RPi.GPIO as GPIO
import random
import math
m1 = PiMotor.Stepper("STEPPER1")
arrow_for = PiMotor.Arrow(1)
arrow_back = PiMotor.Arrow(3)
adc = Adafruit_ADS1x15.ADS1115()
Button_PIN = 29
GPIO.setup(Button_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

################################################################
#Variablen
GAIN = 1
rotations = 1
delay = 0.001
delay_drive = 0.01
s = 0 #Stepps
sw = 0 #Switch Counter

#################################################################
#Freie Fahrt/Startpunkt anfahren
print("Startpunkt anfahren und dann Button drücken")

while True:
    values = [0]*4
    values[1] = adc.read_adc(1, gain=GAIN)
       
    if values[1] < 18000:
        #delay_for = 0.1/18000*values[1]+0.001
        arrow_for.on()
        m1.forward(delay_drive,rotations)
        arrow_for.off()
        s = s+1
        print (s)
       
    if values[1] > 20000:
        #delay_back = (0.1/13300*0-values[1]+32800)+0.001
        arrow_back.on()
        m1.backward(delay_drive,rotations)
        arrow_back.off()
        s = s-1
        print (s)

    
    """
    analoge stuffenlose Geschwindigkeit
    
    if values[1] < 18000:
        delay_for = 0.1/18500*values[1]+0.001
        arrow_for.on()
        m1.forward(delay_for,rotations)  # Delay and rotations
        arrow_for.off()
        s = s+1
        
    if values[1] > 20000:
        delay_back = 0.1/13300*(0-values[1]+32800)+0.001
        arrow_back.on()
        m1.backward(delay_back,rotations)
        arrow_back.off()
        s = s-1
    """
    if GPIO.input(Button_PIN) == False:
        sw = sw+1
        while GPIO.input(Button_PIN) == False:
            ()
            
    if sw == 1:    
        s = 0
        break
    
##############################################################
#Endpunkt anfahren
print("Endpunkt anfahren und dann Button drücken")

while True:
    values = [0]*4
    values[1] = adc.read_adc(1, gain=GAIN)
    
    if values[1] < 18000:
        #delay_for = 0.1/18000*values[1]+0.001
        arrow_for.on()
        m1.forward(delay_drive,rotations)
        arrow_for.off()
        s = s+1
        print (s)
       
    if values[1] > 20000:
        #delay_back = (0.1/13300*0-values[1]+32800)+0.001
        arrow_back.on()
        m1.backward(delay_drive,rotations)
        arrow_back.off()
        s = s-1
        print (s)
        
    """
    Fahrt mit zwei unterschiedlichen Geschwindigkeiten
    
    if values[1] < 3000:
        #delay_for = 0.1/18000*values[1]+0.001
        arrow_for.on()
        m1.forward(0.001,rotations)
        arrow_for.off()
        s = s+1
        print (s)
     
    if 3000 < values[1] < 18000:
        #delay_for = 0.1/18000*values[1]+0.001
        arrow_for.on()
        m1.forward(0.01,rotations)
        arrow_for.off()
        s = s+1
        print (s)
       
    if 29000 > values[1] > 20000:
        #delay_back = (0.1/13300*0-values[1]+32800)+0.001
        arrow_back.on()
        m1.backward(0.01,rotations)
        arrow_back.off()
        s = s-1
        print (s)
        
    if 33000 > values[1] > 29000:
        #delay_back = (0.1/13300*0-values[1]+32800)+0.001
        arrow_back.on()
        m1.backward(0.001,rotations)
        arrow_back.off()
        s = s-1
        print (s)
    """
    
    """
    analoge stufenlose Geschwindigkeit
    
    if values[1] < 18000:
        delay_for = 0.1/18500*values[1]+0.001
        arrow_for.on()
        m1.forward(delay_for,rotations)  # Delay and rotations
        arrow_for.off()
        s = s+1
        
    if values[1] > 20000:
        delay_back = 0.1/13300*(0-values[1]+32800)+0.001
        arrow_back.on()
        m1.backward(delay_back,rotations)
        arrow_back.off()
        s = s-1
    """
    if GPIO.input(Button_PIN) == False:
        sw = sw+1
        while GPIO.input(Button_PIN) == False:
            ()
            
    if sw == 2:    
        s_end = s
        print(s_end)
        break
print("rotations"," ", rotations)      
#################################################################
#Rückfahrt
print("Schlitten fährt zurück zum Startpunkt")
   
if s < 0:
    s_end = s_end*(-1)
    arrow_for.on()
    m1.forward(delay,s_end) 
    arrow_for.off()
    print (s_end)
        #s_end = s_end+1
if s > 0:
    arrow_back.on()
    m1.backward(delay,s)
    arrow_back.off()
    print (s_end)
        #s_end = s_end-1
######################################################
#Zeitwahl
print("Fahrtdauer in Sekunden wählen")

time_set = 0

while True:
    values = [0]*4
    values[0] = adc.read_adc(0, gain=GAIN)
    
    if values[0] < 18000:
        time_set = time_set-10
        time.sleep(0.2)
        print(time_set)
        
    if values[0] > 20000:
        time_set = time_set+10
        time.sleep(0.2)
        print(time_set)  
     
    if GPIO.input(Button_PIN) == False:
        sw = sw+1
        while GPIO.input(Button_PIN) == False:
            ()
        
    if sw == 3:    
        print(s)
        break
time_set = time_set/s
print("time", " ", time_set, " ", "rotations",s," ", s_end)     
#########################################################    
#Automatische Fahrt
then = time.time()

while True: 
    if s > 0:
        arrow_for.on()
        m1.forward(0.01,rotations) 
        arrow_for.off()
        s = s-1
        time.sleep(time_set)
    
    if s < 0:
        arrow_back.on()
        m1.backward(0.01,rotations)
        arrow_back.off()
        time.sleep(math.fabs(time_set))
        s = s+1
    
    if s == 0:
        break
    
now = time.time()
print("Dauer der Fahrt", now-then)   