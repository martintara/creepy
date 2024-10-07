import serial
import time

thresholdDistance = 20

ser = serial.Serial( 'COM3', 9600)                          #serial connection to arduino
time.sleep(2)                                               #wait for connection

while True:
    if ser.in_waiting > 0:                                  #check if data is available from the arduino 
        raw_data = ser.readline().decode('utf-8').strip()   #read and decode distance 
        #print(f"Raw data received: {raw_data}")
        
        try:
            distance = float(raw_data)                      #attempt to convert to float
            print(f"Distance: {distance} cm")
               
            if distance < thresholdDistance:                #check if distance is less than the threshold
                print("Obstacle detected!")                 #take action (stop, turn)
            else:
                print("Path is clear")                      #continue walking     
    
        except ValueError:
            print("Error")                                  #handle conversion error
    
    

        
