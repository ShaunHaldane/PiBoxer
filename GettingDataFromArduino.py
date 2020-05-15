import serial
from time import sleep
import matplotlib.pyplot as plt

t = []
Force_1 = []
Force_2 = []
Force_3 = []
data = serial.Serial('/dev/ttyACM0', 9600)

i=0
punch_count = 0
j = 0
timing_array = []
F1_array = []
F2_array = []
F3_array = []

while(i<120):
    
    
    if(data.inWaiting()>0):
        arduino_string = data.readline()
        
        data_array = arduino_string.split(',')
        F_1=float(data_array[0])
        F_2=float(data_array[1])
        F_3=float(data_array[2])
        if (F_1 or F_2 or F_3 > 20):
            punch_count += 1
            print("No of Punches: " + str(punch_count))
            
            j=i
            F1 = F_1
            F2 = F_2
            F3 = F_3
            F1_array.append(F1)
            F2_array.append(F2)
            F3_array.append(F3)
            
        timing_array.append(j)
        Force_1.append(F_1)
        Force_2.append(F_2)
        Force_3.append(F_3)

        t.append(i)

        i=i+1
        

        #print F1_array, F2_array, F3_array

print(timing_array)
print("No of Punches: " + str(punch_count))

if (punch_count < 15):
    print("You slow bastard")
elif (punch_count >= 15 and punch_count < 20):
    print("Good work")
else:
    print("You are fast as fuck")

avg_F_1 = sum(F1_array)/ len(F1_array)
avg_F_2 = sum(F2_array)/ len(F2_array)
avg_F_3 = sum(F3_array)/ len(F3_array)
 

print("Average of F1 is: " + str(avg_F_1))
print("Average of F2 is: " + str(avg_F_2))
print("Average of F3 is: " + str(avg_F_3))

print("Your hardest hits are: ")
print("Straight =  " + str(max(F1_array)))
print("Left Hook =  " + str(max(F2_array)))
print("Right Hook =  " + str(max(F3_array)))

#plt.plot(t, Force_1, 'r-', label='Force 1')
#plt.legend()
#plt.plot(t, Force_2, 'b-', label='Force 2')
#plt.legend()
#plt.plot(t, Force_3, 'g-', label='Force 3')
#plt.legend()
#plt.plot(t, timing_array, 'y-', label='Speed')
#plt.legend()
#plt.xlabel("time")
#plt.ylabel("Force")
#plt.show()
