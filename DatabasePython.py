import sqlite3
import matplotlib.pyplot as plt

performance = []
performance_count = []
i = 0

conn = sqlite3.connect('boxingdata.db')


c = conn.cursor()

#c.execute("CREATE TABLE boxingreadings (name text, punches integer)")

c.execute("INSERT INTO boxingreadings (punches) VALUES(10)")

conn.commit()

c.execute("SELECT * FROM boxingreadings")

rows = (c.fetchall())

for row in rows:
    performance.append(row[1])
    i = i+1
    performance_count.append(i)
    
performance_count 

plt.plot(performance_count, performance)
plt.show()


    

