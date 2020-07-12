import tkinter as tk
from tkinter import *
import pymysql
import db_config
import os
from PIL import ImageTk, Image
from tkinter import messagebox

Image_path = os.environ['TEMP'] + r"\333.gif"
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
Label(root, text="Welcome To The ImmigrationS Air-travels Portal", font=("Bauhaus 93", 27), fg="brown", width=46,
      bg="peach puff").grid(row=0,
                       column=0,
                       columnspan=4)


def passenger():
    master = Tk()
    master.geometry("600x620")
    master.title("PASSENGERS DOCUMENTATION PORTAL")
    master.configure(background='peach puff')

    textName = StringVar()
    textDob = StringVar()
    textPassNum = StringVar()
    textPassId = StringVar()

    myLabel = tk.Label(master, text="Kindly Fill Your Passenger Info Below", bg='brown', fg="white",
                       font=("san serif""bold", 14))
    myLabel.place(x=120, y=15)
    Label(master, text="Name: ", font=("fixedsys", 14), fg="black").place(x=80, y=60)
    Label(master, text="Date Of Birth: ", font=("fixedsys", 14), fg="black").place(x=80, y=120)
    Label(master, text="Passenger Number: ", font=("fixedsys", 14), fg="black").place(x=80, y=180)
    Label(master, text="Passenger I.D.: ", font=("fixedsys", 14,), fg="black").place(x=80, y=240)

    Label(master, text="(Name Format: Lebron James )", font=("fixedsys", 15), bg="peach puff", fg="black").place(
        x=80, y=300)
    Label(master, text="(Date Of Birth Format: YYYY-MM-DD) ", font=("fixedsys", 15), bg="peach puff",
          fg="black").place(x=80, y=330)
    Label(master, text="(Passenger Number Format: 3012xxxxxx) ", font=("fixedsys", 15), bg="peach puff",
          fg="black").place(x=80, y=360)
    Label(master, text="(Passenger I.D. Format: 12xx)", font=("fixedsys", 15), bg="peach puff", fg="black").place(
        x=80, y=390)
    Message(master,
            text="*** Change info? You must delete your information using your "
                 "passenger I.D. and input new information ***", bg="peach puff", fg="black", font=("fixedsys", 14),
            width=500).place(x=80, y=420)

    name = Entry(master, text=textName, relief="raised")
    dob = Entry(master, text=textDob, relief="raised")
    passNum = Entry(master, text=textPassNum, relief="raised")
    passId = Entry(master, text=textPassId, relief="raised")

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
                             database=db_config.DB, autocommit=True)

        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO Passenger VALUES""" + str(dataa))
        db.commit()

        cursor.execute("""SELECT * FROM Passenger;""")

        print(cursor.fetchall())

        db.close()
        messagebox.showinfo("SUCCESS", "Database Updated")
        # print('"{}"'.format(name.get()))

    # print(texta)

    def delete_passenger():
        deletePass = Tk()
        deletePass.geometry("700x220")
        deletePass.title("Delete Passenger")
        deletePass.configure(background='peach puff')

        deletePassInput = StringVar()

        Label(deletePass, text="Passenger Number: ", font=("fixedsys", 15), bg="peach puff", fg="black").grid(row=0)
        Label(deletePass, text="Enter Passenger Number to delete your passenger data", font=("fixedsys", 15),
              bg="peach puff", fg="black").grid(row=1)
        Label(deletePass, text="(Passenger Number Format: 112xxxxxxx) ", font=("fixedsys", 15), bg="peach puff",
              fg="black").grid(row=2)

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
                                 database=db_config.DB, autocommit=True)

            cursor = db.cursor()

            '''Mysql for user input'''

            cursor.execute("""DELETE FROM Passenger WHERE passNum=""" + str(dataa))

            cursor.execute("""SELECT * FROM Passenger;""")

            print(cursor.fetchall())

            db.close()
            deletePass.destroy()

        Buttonh = Button(deletePass, text="Done", command=delete, width=20, bg='brown', fg='white').place(x=20, y=150)

    Buttonf = Button(master, text="Done", command=done, width=20, bg='brown', fg='white').place(x=80, y=500)
    Buttong = Button(master, text="Delete Passenger", command=delete_passenger, width=20, bg='brown', fg='white').place(
        x=300, y=500)
    buttonz = Button(master, text='Quit', command=master.quit, width=20, bg='brown', fg='white').place(x=190, y=560)

    name.place(x=240, y=60)
    dob.place(x=240, y=120)
    passNum.place(x=240, y=180)
    passId.place(x=240, y=240)


def ticket():
    master = Tk()
    master.geometry("500x350")
    master.title("TICKET DOCUMENTATION PORTAL")
    master.configure(background='peach puff')

    textTicketNum = StringVar()
    textSeatNum = StringVar()

    myLabel = tk.Label(master, text="Kindly Fill Your Ticket Info Below", bg='brown', fg="white",
                       font=("san serif""bold", 14))
    myLabel.place(x=120, y=15)

    Label(master, text="Ticket Number: ", font=("fixedsys", 14), fg="black").place(x=80, y=60)
    Label(master, text="Seat Number: ", font=("fixedsys", 14), fg="black").place(x=80, y=120)

    Label(master, text="(Ticket Number Format: 12XXX)", font=("fixedsys", 15), bg="peach puff",
          fg="black").place(
        x=80, y=180)
    Label(master, text="(Seat Number Format: 1XX) ", font=("fixedsys", 15), bg="peach puff",
          fg="black").place(
        x=80, y=210)

    # Change seat number

    ticketNum = Entry(master, text=textTicketNum)
    seatNum = Entry(master, text=textSeatNum)

    def done():
        texta = "{}".format(ticketNum.get())
        textb = "{}".format(seatNum.get())

        print(texta)

        dataa = (texta, textb)
        print(dataa)

        db = pymysql.connect(host=db_config.DB_SERVER,
                             user=db_config.DB_USER,
                             password=db_config.DB_PASS,
                             database=db_config.DB, autocommit=True)

        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO Ticket VALUES""" + str(dataa))
        db.commit()

        cursor.execute("""SELECT * FROM Ticket;""")

        print(cursor.fetchall())

        db.close()
        messagebox.showinfo("SUCCESS", "Database Updated")

        # print('"{}"'.format(name.get()))

    # print(texta)

    def delete_ticket():
        deleteTick = Tk()
        deleteTick.geometry("450x220")
        deleteTick.title("Delete Ticket")
        deleteTick.configure(background='peach puff')

        deleteTickInput = StringVar()

        Label(deleteTick, text="Ticket Number: ", font=("fixedsys", 14), fg="black").place(x=80, y=60)

        Label(deleteTick, text="Ticket Number Format: 12xxx ", font=("fixedsys", 14), fg="black").place(x=80, y=120)

        ticketDelete = Entry(deleteTick, text=deleteTickInput)
        ticketDelete.place(x=240, y=60)

        def delete():
            texta = "{}".format(ticketDelete.get())
            print(texta)
            dataa = texta
            print(dataa)

            db = pymysql.connect(host=db_config.DB_SERVER,
                                 user=db_config.DB_USER,
                                 password=db_config.DB_PASS,
                                 database=db_config.DB, autocommit=True)

            cursor = db.cursor()

            '''Mysql for user input'''

            cursor.execute("""DELETE FROM Ticket WHERE  ticketNum=""" + str(dataa))

            cursor.execute("""SELECT * FROM Ticket;""")

            print(cursor.fetchall())

            db.close()
            deleteTick.destroy()

        Buttonf = Button(deleteTick, text="Done", command=delete, width=20, bg='brown', fg='white').place(x=20, y=150)

    Buttonf = Button(master, text="Done", command=done, width=20, bg='brown', fg='white').place(x=80, y=275)
    Buttong = Button(master, text="Delete Ticket", command=delete_ticket, width=20, bg='brown', fg='white').place(x=270,
                                                                                                                  y=275)
    Buttonz = Button(master, text='Quit', command=master.quit, width=20, bg='brown', fg='white').place(x=175, y=317)

    ticketNum.place(x=240, y=60)
    seatNum.place(x=240, y=120)


def flight():
    master = Tk()
    master.geometry("600x650")
    master.title("FLIGHT DOCUMENTATION PORTAL")
    master.configure(background='peach puff')

    textFlightId = StringVar()
    textFlightTerm = StringVar()
    textFlighTicket = StringVar()
    textNumFlights = StringVar()

    myLabel = tk.Label(master, text="Kindly Fill Your Flight Info Below", bg='brown', fg="white",
                       font=("san serif""bold", 14))
    myLabel.place(x=120, y=15)
    Label(master, text="Flight I.D.: ", font=("fixedsys", 14), fg="black").place(x=80, y=60)
    Label(master, text="Flight Terminal: ", font=("fixedsys", 14), fg="black").place(x=80, y=120)
    Label(master, text="Flight Ticket: ", font=("fixedsys", 14), fg="black").place(x=80, y=180)
    Label(master, text="Number of Flights: ", font=("fixedsys", 14), fg="black").place(x=80, y=240)

    Label(master, text="(Flight I.D. Format: 12xx) ", font=("fixedsys", 15), bg="peach puff", fg="black").place(
        x=80, y=300)
    Label(master, text="(Flight Terminal Format: A-5) ", font=("fixedsys", 15), bg="peach puff", fg="black").place(
        x=80, y=330)
    Label(master, text="(Flight Ticket Format: 1xx)  ", font=("fixedsys", 15), bg="peach puff", fg="black").place(
        x=80, y=360)
    Label(master, text="(Number of Flights Format: 1) ", font=("fixedsys", 15), bg="peach puff", fg="black").place(
        x=80, y=390)
    Message(master,
            text="*** In order to change flight information, you must delete it using your flight I.D. number and "
                 "then insert another one***", bg="peach puff", fg="black", font=("fixedsys", 14),
            width=500).place(x=80, y=420)

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
                             database=db_config.DB, autocommit=True)

        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO Flight VALUES""" + str(dataa))
        db.commit()

        cursor.execute("""SELECT * FROM Flight;""")

        print(cursor.fetchall())

        db.close()
        messagebox.showinfo("SUCCESS", "Database Updated")

        # print('"{}"'.format(name.get()))

    # print(texta)

    def delete_flight():
        deleteFli = Tk()
        deleteFli.geometry("700x220")
        deleteFli.title("Delete Flight")
        deleteFli.configure(background='peach puff')

        deleteFliInput = StringVar()

        Label(deleteFli, text="Passenger Number: ", font=("fixedsys", 15), bg="peach puff", fg="black").grid(row=0)
        Label(deleteFli, text="You have to know your Flight I.D. to delete your flight data", font=("fixedsys", 15),
              bg="peach puff", fg="black").grid(row=1)
        Label(deleteFli, text="Passenger Number Format: 112xxxxxxx ", font=("fixedsys", 15), bg="peach puff",
              fg="black").grid(row=3)

        fliDelete = Entry(deleteFli, text=deleteFliInput)

        fliDelete.grid(row=0, column=1)

        def delete():
            texta = "{}".format(fliDelete.get())
            print(texta)
            dataa = texta
            print(dataa)

            db = pymysql.connect(host=db_config.DB_SERVER,
                                 user=db_config.DB_USER,
                                 password=db_config.DB_PASS,
                                 database=db_config.DB, autocommit=True)

            cursor = db.cursor()

            '''Mysql for user input'''

            cursor.execute("""DELETE FROM Flight WHERE flightId=""" + str(dataa))

            cursor.execute("""SELECT * FROM Flight;""")

            print(cursor.fetchall())

            db.close()
            deleteFli.destroy()

        Buttonh = Button(deleteFli, text="Done", command=delete, width=20, bg='brown', fg='white').place(x=20, y=150)

    Buttonf = Button(master, text="Done", command=done, width=20, bg='brown', fg='white').place(x=80, y=500)
    Buttong = Button(master, text="Delete Flight", command=delete_flight, width=20, bg='brown', fg='white').place(
        x=300, y=500)
    buttonz = Button(master, text='Quit', command=master.quit, width=20, bg='brown', fg='white').place(x=190, y=560)

    flightId.place(x=240, y=60)
    flightTerm.place(x=240, y=120)
    flightTicket.place(x=240, y=180)
    numFlights.place(x=240, y=240)


def plane():
    master = Tk()
    master.geometry("650x620")
    master.title("PLANE DOCUMENTATION PORTAL")
    master.configure(background='peach puff')

    textArrival = StringVar()
    textDeparture = StringVar()
    textPlaneNum = StringVar()
    textSeatNum = StringVar()
    textPlaneSize = StringVar()

    myLabel = tk.Label(master, text="Kindly Fill Your Flight Info Below", bg='brown', fg="white",
                       font=("san serif""bold", 14))
    myLabel.place(x=120, y=15)

    Label(master, text="Arrival: ", font=("fixedsys", 14), fg="black").place(x=80, y=60)
    Label(master, text="Departure: ", font=("fixedsys", 14), fg="black").place(x=80, y=120)
    Label(master, text="Plane Number: ", font=("fixedsys", 14), fg="black").place(x=80, y=180)
    Label(master, text="Number of Seats: ", font=("fixedsys", 14), fg="black").place(x=80, y=240)
    Label(master, text="Plane Size: ", font=("fixedsys", 14), fg="black").place(x=80, y=300)

    Label(master, text="(Time Format: 11:00:00 (Insert time based on 24-hour clock)) ",
          font=("fixedsys", 15), bg="peach puff", fg="black").place(
        x=80, y=360)
    Label(master, text="(Plane Number Format: 125XXX) ", font=("fixedsys", 15), bg="peach puff", fg="black").place(
        x=80, y=390)
    Label(master, text="(Number of Seats Format: 2XX ", font=("fixedsys", 15), bg="peach puff", fg="black").place(
        x=80, y=420)
    Label(master, text="(Plane Size: Small, Medium or Large) ", font=("fixedsys", 15), bg="peach puff",
          fg="black").place(
        x=80, y=450)
    Label(master,
          text="Plane Size = Small(150 ft), Medium(200 ft), Large(250 ft)",
          font=("fixedsys", 15), bg="peach puff", fg="black").place(
        x=80, y=480)

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
        db = pymysql.connect(host=db_config.DB_SERVER,
                             user=db_config.DB_USER,
                             password=db_config.DB_PASS,
                             database=db_config.DB, autocommit=True)

        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO Plane VALUES""" + str(dataa))
        db.commit()

        cursor.execute("""SELECT * FROM Plane;""")

        print(cursor.fetchall())

        db.close()
        messagebox.showinfo("SUCCESS", "Database Updated")

        # print('"{}"'.format(name.get()))

    # print(texta)

    Buttonf = Button(master, text="Done", command=done, width=20, bg='brown', fg='white').place(x=120, y=550)
    buttonz = Button(master, text='Quit', command=master.quit, width=20, bg='brown', fg='white').place(x=350, y=550)

    arrival.place(x=240, y=60)
    departure.place(x=240, y=120)
    planeNum.place(x=240, y=180)
    seatNum.place(x=240, y=240)
    planeSize.place(x=240, y=300)


'''mainloop( ): This is the main menu'''

myButtond = Button(root, text="Flights", relief='flat', highlightthickness=3, bd=1, command=flight)
myButtond.grid(row=1, column=0, columnspan=4)
img2 = PhotoImage(file="C:/Users/user/Downloads/button(17).png")
myButtond.configure(image=img2)

myButtonb = Button(root, text="Plane", relief="flat", command=plane)
myButtonb.grid(row=3, column=0, columnspan=4)
img = PhotoImage(file="C:/Users/user/Downloads/button(15).png")
myButtonb.configure(image=img)

myButtonc = Button(root, text="Tickets", relief="flat", command=ticket)
myButtonc.grid(row=2, column=0, columnspan=4)
img1 = PhotoImage(file="C:/Users/user/Downloads/button(16).png")
myButtonc.configure(image=img1)

myButtone = Button(root, text="Passenger", relief='flat', command=passenger)
myButtone.grid(row=4, column=0, columnspan=4)
img3 = PhotoImage(file="C:/Users/user/Downloads/button(21).png")
myButtone.configure(image=img3)

Label(root, text="Copyright  ©   Immigrations   2020", font=("comic sans 23", 11, "bold"), fg="brown", width=148,
      bg="Peach puff").grid(row=5,
                       column=0,
                       columnspan=4)

root.mainloop()
