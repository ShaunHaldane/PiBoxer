import serial
from time import sleep
from Tkinter import *
import sqlite3
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import style

style.use("dark_background")

def OpenSpeedWindow():
    
    def CloseWindow():
        speed_window.destroy()

    speed_window = Toplevel(root)
    speed_window.geometry('%dx%d+%d+%d' % (900, 600, 50, 50))
    speed_window.configure(bg="black")
    
    SpeedLabel = Label(speed_window, font=Game_Font,  bg="black", fg="red", text="Get Ready to Hit the Bag as Fast as you can for 60 Seconds")
    SpeedLabel.pack(pady=20)
    
    #Label to display countdown on GUI
    countdown_lbl = Label(speed_window)
    countdown_lbl.pack()
    
    #Countdown time to put gloves on
    countdown = 15

    #Loop to countdown
    while(countdown > 0):
        sleep(1)
        countdown -= 1
        print(countdown)
        #update GUI countdown timer, use configure and update to do this
        countdown_lbl.configure(font=Game_Font, bg="black", fg="red",text = " " + str(countdown))
        countdown_lbl.update()

    #display 'GO' when countdown is finished, update countdown label    
    countdown_lbl.configure(font=Game_Font, bg="black", fg="red", text = "Punch!!!")
    countdown_lbl.update()

    ResetButton = Button(speed_window, font=Game_Font, bg="black", fg="red", text="Reset Button", command=CloseWindow)
    ResetButton.pack(pady=5)

    # set arrays to store time and forces
    
    F1_array = []
    F2_array = []
    F3_array = []


    #variable to take data from arduino
    data = serial.Serial('/dev/ttyACM0', 9600)

    #timer variable 'i'
    i=240

    #initialise punch count variable to count punches
    punch_count = 0

    #labels to display results on GUI
    count_lbl = Label(speed_window)
    count_lbl.pack()
    punch_count_lbl = Label(speed_window)
    punch_count_lbl.pack()
    speed_lbl = Label(speed_window)
    speed_lbl.pack()
    hardest_straight_punch_lbl = Label(speed_window)
    hardest_straight_punch_lbl.pack()
    hardest_lefthook_lbl = Label(speed_window)
    hardest_lefthook_lbl.pack()
    hardest_righthook_lbl = Label(speed_window)
    hardest_righthook_lbl.pack()
    avg_force_lbl = Label(speed_window)
    avg_force_lbl.pack()

    #loop for timer
    while(i>0):
        
        #getting data from arduino
        if(data.inWaiting()>0):
            arduino_string = data.readline()
            
            #data from arduino is a string, this array splits the string at comma
            #and stores striongs in an array    
            data_array = arduino_string.split(',')
            
            #convert string data from arduino to float and store each element in variable
            F1=float(data_array[0])
            F2=float(data_array[1])
            F3=float(data_array[2])
            
            #if a force is detected add to punch count and add force to array,
            #at the end of this if statement there sould be an array with the amount
            #of times that the FSR was triggered along with force values to take avg of force
            if (F1 > 20 or F2 > 20 or F3 > 20):
                punch_count += 1
                #print("No of Punches: " + str(punch_count))
                hardest_straight_punch_lbl.configure(font=Game_Font,  bg="black", fg="red",text= "Straight Punch: " + str(F1))
                hardest_lefthook_lbl.configure(font=Game_Font,  bg="black", fg="red",text = "Left Hook: " + str(F2)) 
                hardest_righthook_lbl.configure(font=Game_Font,  bg="black", fg="red", text = "Right Hook: " + str(F3))
                F1_array.append(F1)
                F2_array.append(F2)
                F3_array.append(F3)

            #update GUI to display no of punches
            punch_count_lbl.configure(font=Game_Font, bg="black", fg="red", text = "No of Punches: " + str(punch_count))

            #update GUI to display timer, readings are produced by arduino every 0.25'
            #seconds so i is converted to real time
            time = i/4
            str_time = str(time)
            count_lbl.configure(font=Game_Font, bg="black", fg="red", text = "Time: " + str_time)
            count_lbl.update()

            #continue the countdown loop
            i=i-1

    #calculate the average force
    avg_F_1 = sum(F1_array)/ len(F1_array)
    avg_F_2 = sum(F2_array)/ len(F2_array)
    avg_F_3 = sum(F3_array)/ len(F3_array)
    total_avg_force = (avg_F_1 + avg_F_2 + avg_F_3) #put mutiplyer here after callibration
         

    #print("Average of F1 is: " + str(avg_F_1))
    #print("Average of F2 is: " + str(avg_F_2))
    #print("Average of F3 is: " + str(avg_F_3))
    print("Average Force: " + str(total_avg_force))

    #work out max force
    F1_max = max(F1_array)
    F2_max = max(F2_array)
    F3_max = max(F3_array)

    #display results on GUI
    hardest_straight_punch_lbl.configure(font=Game_Font, bg="black", fg="red", text = "Your Hardest Straight Punch is: " + str(F1_max))
    hardest_lefthook_lbl.configure(font=Game_Font, bg="black", fg="red", text = "Your Hardest Left Hook is: " + str(F2_max))
    hardest_righthook_lbl.configure(font=Game_Font, bg="black", fg="red", text = "Your Hardest Right Hook is: " + str(F3_max))
    avg_force_lbl.configure(font=Game_Font, bg="black", fg="red", text = "Your Average Force is: " +  str(total_avg_force))

    #connect to database software
    conn = sqlite3.connect('punchingdata.db')
    c = conn.cursor()

    #set up parameters for database
    name = "shaun"
    punches = punch_count
    #speed history for y axis of database graph
    speed_performance = []
    #x axis of times attempted graph from database
    performance_count = []
    ##avg force history for y axis of database graph
    avg_force_array = []
    row_no = 0

    #This should only be executed once to create a new database
    #c.execute("CREATE TABLE PunchDataSpeed2 (Name text, Punches integer, Force integer)")

    #insert new data into database
    c.execute("INSERT INTO PunchDataSpeed2 (Name, Punches, Force) VALUES(?, ?, ?)", (name, punches, total_avg_force))

    #update changes to database
    conn.commit()

    #get data from database to put on history graph
    c.execute("SELECT * FROM PunchDataSpeed2")
    rows = (c.fetchall())

    #loop through the database to take points for graph
    for row in rows:
        #append floats the graph to display results on GUI
        speed_performance.append(row[1])
        avg_force_array.append(row[2])
        row_no = row_no+1
        performance_count.append(row_no)
        
    #plot graph for speed vs attempts on GUI
    f= plt.Figure(figsize=(5,3), dpi=100)
    a = f.add_subplot(111)
    a.plot(performance_count, speed_performance)
    a.set_title('Speed History')
    #a.set_xlabel('Attempt')
    a.set_ylabel('No of Punches')
    canvas = FigureCanvasTkAgg(f, master=speed_window)
    canvas.draw()
    canvas.get_tk_widget().pack(side="left")

    #plot graph for avg force vs attempts on GUI
    fig = plt.Figure(figsize=(5,3), dpi=100)
    b = fig.add_subplot(111)
    b.plot(performance_count, avg_force_array)
    b.set_title('Avg Force History')
    #b.set_xlabel('Attempt')
    b.set_ylabel('Force')
    canvas = FigureCanvasTkAgg(fig, master=speed_window)
    canvas.draw()
    canvas.get_tk_widget().pack(side="right")

    #display graphs on GUI
    canvas.show()

    #close the database graph function
    conn.close()

root = Tk()

Game_Font = ("Helvetica", 12, "bold")

root.geometry('%dx%d+%d+%d' % (900, 600, 50, 50))
root.configure(bg="black")

WelcomeLabel = Label(root, font=Game_Font, bg="black", fg="red", text="Welcome to PyBoxer")
WelcomeLabel.pack(pady=20)

StartButton = Button(root, font=Game_Font, bg="black", fg="red", text="Start Button", command=OpenSpeedWindow)
StartButton.pack(pady=5 )


root.mainloop()

