# PyBoxer

## Purpose
This project measures the speed and strength of punches over a 1 minute interval.

## Description
The apparatus consiting of 3 force sensors, an Arduino, a Raspberry pi and a small screen 
is to be strapped to a punching bag.

![alt text](PiBoxeronBag.png?raw=true)


The user then runs the program which opens a GUI with
a start button. 

![alt text](PiBoxerStartScreen.png?raw=true)

Once the user presses the start button a 15 second countdown will begin 
so the user can put boxing gloves on. After the countdown a 60 second timer will begin and 
the user must punch the sensors as hard and fast as possible. Punch strength is displayed as 
each punch is landed and the number of punches is recorded. 

![alt text](PiBoxerPunchScreen.png?raw=true)

![alt text](PunchingPiBoxer.png?raw=true)


After 60 seconds the users' performance is stored in a database with SQLite. 2 graphs appear to compare the users performance over time from the first performance to the 
current performance. 

![alt text](PiBoxerResultsScreen.png?raw=true)

![alt text](PiBoxerResultsonBag.png?raw=true)

## Final Note
The apparatus needs more work because the wires become loose after a few sessions. It is very frustrating when the wires come loose during the 60 second punch interval and messes up the score. The software workes brilliantly.

