import tkinter as tk
from tkinter import *
import pymysql
import db_config
import os

Image_path = os.environ['TEMP'] + r"\33.gif"
root = Tk()
root.title("DOCUMENTATION PORTAL")

image11 = tk.PhotoImage(file=Image_path)
w = image11.width()
h = image11.height()
root.geometry("%dx%d+0+0" % (w, h))

panel1 = tk.Label(root, image=image11)
panel1.grid(row=0, column=0, columnspan=4, rowspan=6)

panel1.image = image11

Label(root).grid(row=0, column=0, columnspan=8)
Label(root, text="Welcome to Immigration Air-travels Portal", font=("Bauhaus 93", 27), fg="royalblue1", width=46,
      bg="White").grid(row=0,
                       column=0,
                       columnspan=4)


def passenger():
    master = Tk()
    master.geometry("520x400")
    master.title("Air Reservation System")

    master.configure(background='deep sky blue')

    textName = StringVar()
    textDob = StringVar()
    textPassNum = StringVar()
    textPassId = StringVar()

    Label(master, text="Name: ").grid(row=0)
    Label(master, text="Date Of Birth: ").grid(row=1)
    Label(master, text="Phone Number: ").grid(row=2)
    Label(master, text="Passenger I.D.: ").grid(row=3)

    Label(master, text="(Format of Name:Lebron James )").grid(row=15)
    Label(master, text="(Format of Date Of Birth: 1996-05-05) ").grid(row=16)
    Label(master, text="(Format of Phone Number: 3012239229) ").grid(row=17)
    Label(master, text="(Format of Passenger I.D.: 1222)").grid(row=18)
    Message(master,
            text="*** Change info? You must delete your information using your "
                 "passenger I.D. and input new information ***",
            width=200).grid(row=19)

    name = Entry(master, text=textName)
    dob = Entry(master, text=textDob)
    passNum = Entry(master, text=textPassNum)
    passId = Entry(master, text=textPassId)

    def done():
        texta = "{}".format(name.get())
        textb = "{}".format(dob.get())
        textc = "{}".format(passNum.get())
        textd = "{}".format(passId.get())
        print(texta)

        dataa = (texta, textb, textc, textd)
        print(dataa)
        db = pymysql.connect(host=db_config.DB_SERVER,
                             user=db_config.DB_USER,
                             password=db_config.DB_PASS,
                             database=db_config.DB)

        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO Passenger VALUES""" + str(dataa))
        db.commit()

        cursor.execute("""SELECT * FROM Passenger;""")

        print(cursor.fetchall())

        db.close()

        # print('"{}"'.format(name.get()))

    # print(texta)

    def delete_passenger():
        deletePass = Tk()
        deletePass.geometry("700x220")
        deletePass.title("Air Reservation System")

        deletePassInput = StringVar()

        Label(deletePass, text="Passenger Number: ").grid(row=0)
        Label(deletePass, text="Enter Passenger Number to delete your passenger data").grid(row=1)
        Label(deletePass, text="(Example of Passenger Number: 1122212232) ").grid(row=2)

        passDelete = Entry(deletePass, text=deletePassInput)

        passDelete.grid(row=0, column=1)

        def delete():
            texta = "{}".format(passDelete.get())
            print(texta)
            dataa = texta
            print(dataa)

            db = pymysql.connect(host=db_config.DB_SERVER,
                                 user=db_config.DB_USER,
                                 password=db_config.DB_PASS,
                                 database=db_config.DB)

            cursor = db.cursor()

            '''Mysql for user input'''

            cursor.execute("""DELETE FROM Passenger WHERE passNum=""" + str(dataa))

            cursor.execute("""SELECT * FROM Passenger;""")

            print(cursor.fetchall())

            db.close()

        Buttonh = Button(deletePass, text="Done", command=delete).place(x=20, y=150)

    Buttonf = Button(master, text="Done", command=done).place(x=20, y=300)
    Buttong = Button(master, text="Delete Passenger", command=delete_passenger).place(x=20, y=330)

    name.grid(row=0, column=1)
    dob.grid(row=1, column=1)
    passNum.grid(row=2, column=1)
    passId.grid(row=3, column=1)


def ticket():
    master = Tk()
    master.geometry("500x250")
    master.title("Air Reservation System")
    master.configure(background='deep sky blue')

    textTicketNum = StringVar()
    textSeatNum = StringVar()

    Label(master, text="Ticket Number: ").grid(row=0)
    Label(master, text="Seat Number: ").grid(row=1)

    Label(master, text="(Example of Ticket Number input: 12255)").grid(row=15)
    Label(master, text="(Example of Seat Number input: 128) ").grid(row=16)

    # Change seat number

    ticketNum = Entry(master, text=textTicketNum)
    seatNum = Entry(master, text=textSeatNum)

    def done():
        texta = "{}".format(ticketNum.get())
        textb = "{}".format(seatNum.get())

        print(texta)

        dataa = (texta, textb)
        print(dataa)

        db = pymysql.connect(host='localhost', user='me', passwd='', db='Air Reservation',
                             autocommit=True)

        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO Ticket VALUES""" + str(dataa))
        db.commit()

        cursor.execute("""SELECT * FROM Ticket;""")

        print(cursor.fetchall())

        db.close()

        # print('"{}"'.format(name.get()))

    # print(texta)

    def delete_ticket():
        deleteTick = Tk()
        deleteTick.geometry("450x220")
        deleteTick.title("Air Reservation System")

        deleteTickInput = StringVar()

        Label(deleteTick, text="Ticket Number: ").grid(row=0)

        Label(deleteTick, text="Example of Ticket Number: 12211 ").grid(row=1)

        ticketDelete = Entry(deleteTick, text=deleteTickInput)

        ticketDelete.grid(row=0, column=1)

        def delete():
            texta = "{}".format(ticketDelete.get())
            print(texta)
            dataa = texta
            print(dataa)

            db = pymysql.connect(host='localhost', user='me', passwd='', db='Air Reservation',
                                 autocommit=True)

            cursor = db.cursor()

            '''Mysql for user input'''

            cursor.execute("""DELETE FROM Ticket WHERE ticketNum=""" + str(dataa))

            cursor.execute("""SELECT * FROM Ticket;""")

            print(cursor.fetchall())

            db.close()

        Buttonf = Button(deleteTick, text="Done", command=delete).place(x=20, y=150)

    Buttonf = Button(master, text="Done", command=done).place(x=20, y=150)
    Buttong = Button(master, text="Delete Ticket", command=delete_ticket).place(x=20, y=180)

    ticketNum.grid(row=0, column=1)
    seatNum.grid(row=1, column=1)


def flight():
    master = Tk()
    master.geometry("500x350")
    master.title("Air Reservation System")
    master.configure(background='deep sky blue')

    textFlightId = StringVar()
    textFlightTerm = StringVar()
    textFlighTicket = StringVar()
    textNumFlights = StringVar()

    Label(master, text="Flight I.D.: ").grid(row=0)
    Label(master, text="Flight Terminal: ").grid(row=1)
    Label(master, text="Flight Ticket: ").grid(row=2)
    Label(master, text="Number of Flights: ").grid(row=3)

    Label(master, text="(Example of Flight I.D.: 1221) ").grid(row=15)
    Label(master, text="(Example of Flight Terminal: A-5) ").grid(row=16)
    Label(master, text="(Example of Flight Ticket: 128)  ").grid(row=17)
    Label(master, text="(Example of Number of Flights: 1) ").grid(row=18)
    Message(master,
            text="*** In order to change flight information, you must delete it using your flight I.D. number and "
                 "then insert another one***",
            width=200).grid(row=19)

    flightId = Entry(master, text=textFlightId)
    flightTerm = Entry(master, text=textFlightTerm)
    flightTicket = Entry(master, text=textFlighTicket)
    numFlights = Entry(master, text=textNumFlights)

    def done():
        texta = "{}".format(flightId.get())
        textb = "{}".format(flightTerm.get())
        textc = "{}".format(flightTicket.get())
        textd = "{}".format(numFlights.get())
        print(texta)

        dataa = (texta, textb, textc, textd)
        print(dataa)
        db = pymysql.connect(host=db_config.DB_SERVER,
                             user=db_config.DB_USER,
                             password=db_config.DB_PASS,
                             database=db_config.DB)

        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO Flight VALUES""" + str(dataa))
        db.commit()

        cursor.execute("""SELECT * FROM Flight;""")

        print(cursor.fetchall())

        db.close()

        # print('"{}"'.format(name.get()))

    # print(texta)

    def delete_flight():
        deleteFli = Tk()
        deleteFli.geometry("700x220")
        deleteFli.title("Air Reservation System")

        deleteFliInput = StringVar()

        Label(deleteFli, text="Passenger Number: ").grid(row=0)
        Label(deleteFli, text="You have to know your Flight I.D. to delete your flight data").grid(row=1)
        Label(deleteFli, text="Example of Passenger Number: 1122212232 ").grid(row=2)

        fliDelete = Entry(deleteFli, text=deleteFliInput)

        fliDelete.grid(row=0, column=1)

        def delete():
            texta = "{}".format(fliDelete.get())
            print(texta)
            dataa = (texta)
            print(dataa)

            db = pymysql.connect(host=db_config.DB_SERVER,
                                 user=db_config.DB_USER,
                                 password=db_config.DB_PASS,
                                 database=db_config.DB)

            cursor = db.cursor()

            '''Mysql for user input'''

            cursor.execute("""DELETE FROM Flight WHERE flightId=""" + str(dataa))

            cursor.execute("""SELECT * FROM Flight;""")

            print(cursor.fetchall())

            db.close()

        Buttonh = Button(deleteFli, text="Done", command=delete).place(x=20, y=150)

    Buttonf = Button(master, text="Done", command=done).place(x=20, y=280)
    Buttong = Button(master, text="Delete Passenger", command=delete_flight).place(x=20, y=310)

    flightId.grid(row=0, column=1)
    flightTerm.grid(row=1, column=1)
    flightTicket.grid(row=2, column=1)
    numFlights.grid(row=3, column=1)


def plane():
    master = Tk()
    master.geometry("850x300")
    master.title("Air Reservation System")
    master.configure(background='deep sky blue')

    textArrival = StringVar()
    textDeparture = StringVar()
    textPlaneNum = StringVar()
    textSeatNum = StringVar()
    textPlaneSize = StringVar()

    Label(master, text="Arrival: ").grid(row=0)
    Label(master, text="Departure: ").grid(row=1)
    Label(master, text="Plane Number: ").grid(row=2)
    Label(master, text="Number of Seats: ").grid(row=3)
    Label(master, text="Plane Size: ").grid(row=4)

    Label(master, text="(Example of Arrival Time: 11:00:00 (Insert time based on 24 hour clock)) ").grid(row=15)
    Label(master, text="(Example of Departure Time: 12:00:00 (Insert time based on 24 hour clock)) ").grid(row=16)
    Label(master, text="(Example of Plane Number: 125588) ").grid(row=17)
    Label(master, text="(Example of Number of Seats: 200) ").grid(row=18)
    Label(master, text="(Example of Plane Size: Small,Medium, or Large) ").grid(row=19)
    Label(master,
          text="For reference on Plane Size, Small(150 feet long), Medium(200 feet long), Large(250 feet long)").grid(
        row=20)

    arrival = Entry(master, text=textArrival)
    departure = Entry(master, text=textDeparture)
    planeNum = Entry(master, text=textPlaneNum)
    seatNum = Entry(master, text=textSeatNum)
    planeSize = Entry(master, text=textPlaneSize)

    def done():
        texta = "{}".format(arrival.get())
        textb = "{}".format(departure.get())
        textc = "{}".format(planeNum.get())
        textd = "{}".format(seatNum.get())
        texte = "{}".format(planeSize.get())
        print(texta)

        dataa = (texta, textb, textc, textd, texte)
        print(dataa)
        db = pymysql.connect(host='localhost', user='me', passwd='', db='Air Reservation',
                             autocommit=True)

        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO Plane VALUES""" + str(dataa))
        db.commit()

        cursor.execute("""SELECT * FROM Plane;""")

        print(cursor.fetchall())

        db.close()

        # print('"{}"'.format(name.get()))

    # print(texta)

    Buttonf = Button(master, text="Done", command=done).place(x=20, y=270)

    arrival.grid(row=0, column=1)
    departure.grid(row=1, column=1)
    planeNum.grid(row=2, column=1)
    seatNum.grid(row=3, column=1)
    planeSize.grid(row=4, column=1)


'''mainloop( ): This is the main menu'''

myButtonb = Button(root, text="Plane", relief="flat", command=plane)
myButtonb.grid(row=1, column=0, columnspan=4)
img = PhotoImage(file="C:/Users/user/Downloads/button(13).png")
myButtonb.configure(image=img)

myButtonc = Button(root, text="Tickets", relief="flat", command=ticket)
myButtonc.grid(row=2, column=0, columnspan=4)
img1 = PhotoImage(file="C:/Users/user/Downloads/button(4).png")
myButtonc.configure(image=img1)

myButtond = Button(root, text="Flights", relief='flat', highlightthickness=3, bd=1, command=flight)
myButtond.grid(row=3, column=0, columnspan=4)
img2 = PhotoImage(file="C:/Users/user/Downloads/button(5).png")
myButtond.configure(image=img2)

myButtone = Button(root, text="Passenger", relief='flat', command=passenger)
myButtone.grid(row=4, column=0, columnspan=4)
img3 = PhotoImage(file="C:/Users/user/Downloads/button(12).png")
myButtone.configure(image=img3)
Label(root, text="Copyright © Air Orion 2020", font=("comic sans 23", 11, "bold"), fg="royalblue1", width=97,
      bg="white").grid(row=5,
                       column=0,
                       columnspan=4)

root.mainloop()
