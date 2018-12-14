# Recieving Mobile sensor data coming on PORT mentioned, from 'Sensor Node Free.apk'
import socket
import bs4 as bs
from tkinter import *
import time



UDP_IP = "192.168.43.173"
UDP_PORT = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

root = Tk()
a_1 = ''
acc1 = Label(root, font=('times', 20, 'bold'), bg='green')
acc1.pack(fill=BOTH, expand=1)
a_2 = ''
acc2 = Label(root, font=('times', 20, 'bold'), bg='green')
acc2.pack(fill=BOTH, expand=1)
a_3 = ''
acc3 = Label(root, font=('times', 20, 'bold'), bg='green')
acc3.pack(fill=BOTH, expand=1)


g_1 = ''
gra1 = Label(root, font=('times', 20, 'bold'), bg='green')
gra1.pack(fill=BOTH, expand=1)
g_2 = ''
gra2 = Label(root, font=('times', 20, 'bold'), bg='green')
gra2.pack(fill=BOTH, expand=1)
g_3 = ''
gra3 = Label(root, font=('times', 20, 'bold'), bg='green')
gra3.pack(fill=BOTH, expand=1)


m_1 = ''
mag1 = Label(root, font=('times', 20, 'bold'), bg='green')
mag1.pack(fill=BOTH, expand=1)
m_2 = ''
mag2 = Label(root, font=('times', 20, 'bold'), bg='green')
mag2.pack(fill=BOTH, expand=1)
m_3 = ''
mag3 = Label(root, font=('times', 20, 'bold'), bg='green')
mag3.pack(fill=BOTH, expand=1)


G_1 = ''
gyro1 = Label(root, font=('times', 20, 'bold'), bg='green')
gyro1.pack(fill=BOTH, expand=1)
G_2 = ''
gyro2 = Label(root, font=('times', 20, 'bold'), bg='green')
gyro2.pack(fill=BOTH, expand=1)
G_3 = ''
gyro3 = Label(root, font=('times', 20, 'bold'), bg='green')
gyro3.pack(fill=BOTH, expand=1)


la_1 = ''
lin_acc1 = Label(root, font=('times', 20, 'bold'), bg='green')
lin_acc1.pack(fill=BOTH, expand=1)
la_2 = ''
lin_acc2 = Label(root, font=('times', 20, 'bold'), bg='green')
lin_acc2.pack(fill=BOTH, expand=1)
la_3 = ''
lin_acc3 = Label(root, font=('times', 20, 'bold'), bg='green')
lin_acc3.pack(fill=BOTH, expand=1)


rv_1 = ''
rot_vec1 = Label(root, font=('times', 20, 'bold'), bg='green')
rot_vec1.pack(fill=BOTH, expand=1)
rv_2 = ''
rot_vec2 = Label(root, font=('times', 20, 'bold'), bg='green')
rot_vec2.pack(fill=BOTH, expand=1)
rv_3 = ''
rot_vec3 = Label(root, font=('times', 20, 'bold'), bg='green')
rot_vec3.pack(fill=BOTH, expand=1)


gps_1 = ''
gps_read1 = Label(root, font=('times', 20, 'bold'), bg='green')
gps_read1.pack(fill=BOTH, expand=1)
gps_read2 = ''
gps_read2 = Label(root, font=('times', 20, 'bold'), bg='green')
gps_read2.pack(fill=BOTH, expand=1)
gps_3 = ''
gps_read3 = Label(root, font=('times', 20, 'bold'), bg='green')
gps_read3.pack(fill=BOTH, expand=1)



def acc():

    global t,a1, a2, a3, g1, g2, g3,G1,G2,G3, m1 ,m2, m3, la1, la2, la3, rv1, rv2, rv3, li1, li2, li3,p, nl1, nl2, nl3, gps1, gps2, gps3,soup
    soup = bs.BeautifulSoup(data, 'lxml')
    # print(soup)

    try:
        #accelerometer
        a1 = soup.find('accelerometer1').text
        print('a1 = ', a1)
        a2 = soup.find('accelerometer2').text
        print('a2 = ', a2)


   #Gyroscope

    #gyro
        g1 = soup.find('gyroscope1').text
        print('g1 = ', g1)
        g2 = soup.find('gyroscope2').text
        print('g2 = ', g2)
        g3 = soup.find('gyroscope3').text
        print('g3 = ', g3)
    except:pass


    # Magnetometer
    try:
        m1 = soup.find('magnetometer1').text
        print('m1 = ', m1)
        m2 = soup.find('magnetometer2').text
        print('m2 = ', m2)
        m3 = soup.find('magnetometer3').text
        print('m3 = ', m3)
    except:pass

    p=soup.find('proximity').text
    print('Proximity : ',p)

    t=soup.find('timestamp').text
    print('TimeStamp : ',t)

    # Gravity
    try:
        G1 = soup.find('gravity1').text
        print('G1 = ', G1)
        G2 = soup.find('gravity2').text
        print('G2 = ', G2)
        G3 = soup.find('gravity3').text
        print('G3 = ', G3)
    except:pass


    # LinearAcceleration
    try:
        la1 = soup.find('linearacceleration1').text
        print('la1 = ', la1)
        la2 = soup.find('linearacceleration2').text
        print('la2 = ', la2)
        la3 = soup.find('linearacceleration3').text
        print('la3 = ', la3)
    except:pass


    # RotationVector
    try:
        rv1 = soup.find('rotationvector1').text
        print('rv1 = ',rv1)
        rv2 = soup.find('rotationvector2').text
        print('rv2 = ',rv2)
        rv3 = soup.find('rotationvector3').text
        print('rv3 = ',rv3)
    except:pass


    # LightIntensity
    try:
        li1 = soup.find('lightintensity1').text
        print('li1 = ', li1)
        li2 = soup.find('lightintensity2').text
        print('li2 = ', li2)
        li3 = soup.find('lightintensity3').text
        print('li3 = ', li3)
    except:pass


    # GPS
    try:
        gps1 = soup.find('latitude').text
        print('gps1 = ', gps1)
        gps2 = soup.find('longitude').text
        print('gps2 = ', gps2)
        gps3 = soup.find('accuracy').text
        print('gps3 = ', gps3)
    except:pass


# use Tkinter to show a digital clock
# tested with Python24    vegaseat    10sep2006



def tick():
    acc()
    global a_1
    # get the current local time from the PC
    acc_reading = a1
    # if time string has changed, update it
    if acc_reading != a_1:
        a_1 = acc_reading
        acc1.config(text=acc_reading)


    gyro_reading = g_1
    # if time string has changed, update it
    if gyro_reading != g_1:
        g_1 = gyro_reading
        gyro.config(text=gyro_reading)

    acc_reading = a1
    # if time string has changed, update it
    if acc_reading != a_1:
        a_1 = acc_reading
        acc1.config(text=acc_reading)

    acc_reading = a1
    # if time string has changed, update it
    if acc_reading != a_1:
        a_1 = acc_reading
        acc1.config(text=acc_reading)


    acc_reading = a1
    # if time string has changed, update it
    if acc_reading != a_1:
        a_1 = acc_reading
        acc1.config(text=acc_reading)

    acc_reading = a1
    # if time string has changed, update it
    if acc_reading != a_1:
        a_1 = acc_reading
        acc1.config(text=acc_reading)

    acc_reading = a1
    # if time string has changed, update it
    if acc_reading != a_1:
        a_1 = acc_reading
        acc1.config(text=acc_reading)


    acc_reading = a1
    # if time string has changed, update it
    if acc_reading != a_1:
        a_1 = acc_reading
        acc1.config(text=acc_reading)

    acc_reading = a1
    # if time string has changed, update it
    if acc_reading != a_1:
        a_1 = acc_reading
        acc1.config(text=acc_reading)


    acc_reading = a1
    # if time string has changed, update it
    if acc_reading != a_1:
        a_1 = acc_reading
        acc1.config(text=acc_reading)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky

    acc1.after(200, tick)






while True:
    data, addr = sock.recvfrom(4800)
    # print(data)
    # acc()
    tick()
    root.mainloop()

    # tts()
    time.sleep(0)




    # ------------------------------------- Completed to requirement --------------------------------------------
