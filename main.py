from tkinter import*
from PIL import Image,ImageTk
import time
from MySQLdb import*
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
from tkcalendar import  DateEntry

def time1():
    string = time.strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time1)


def stufrmfun():

    homeframe.pack_forget()
    admnframe.forget()
    messagebox.showinfo('सफलता ', 'सफलतापूर्वक लोग इन हुआ  ')


    def adff1():
        adf1.forget()
        adf2.forget()
        adf3.forget()
        adf4.forget()
        l2.destroy()
        r1 = Label(adf1, text='   नयी छात्रा रजिस्टर करे    ', font=('Comic Sans MS', 20), bg='DarkSeaGreen2')
        r1.place(rely=0,relwidth=1,bordermode=OUTSIDE)
        #  ----------------------------clear button --------------------------
        def clearr():
            first_name.delete(0, END)
            father_name.delete(0, END)
            dob.delete(0,END)
            scholar.delete(0, END)
            class1.set('9')
            samgra.delete(0, END)
            acc.delete(0, END)
            mobileno.delete(0, END)




        # ----------------data to mysql -----------------
        def register():
            if first_name.get() == "" or father_name.get() == "" or dob.get() == 0 or scholar.get() == "" or class1.get() == "" or samgra.get() == "" or acc.get() == "" or mobileno.get() == "":
                messagebox.showinfo("Error", 'Please Fill All Details')
            else:
                try:
                    dbhost = "remotemysql.com"
                    dbuser = "xsJRQzLgdj"
                    dbpass = "QWX2fUpO5J"
                    dbname = "xsJRQzLgdj"
                    db = connect(dbhost, dbuser, dbpass, dbname)
                    cur = db.cursor()

                    sql3 = "SELECT * FROM `student` WHERE scholar='" + scholar.get() + "'AND Class='"+class1.get()+"'"
                    cur.execute(sql3)
                    row = cur.fetchall()
                    if cur.rowcount != 0:
                        for d in row:
                            messagebox.showinfo('Error', f'scholar No "{scholar.get()}  {d[0]} {d[1]}" Already Registered')
                        adff1()

                    else:
                        try:

                            sql = '''INSERT INTO student ( scholar,first_name ,father_name ,DOB,samgra ,Account_no,mobile_no,Class ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'''
                            values = (scholar.get(),first_name.get().upper(), father_name.get().upper(), dob.get(),
                                samgra.get(),
                                acc.get(), mobileno.get(),  class1.get())
                            print(dob.get())
                            try:
                                cur1 = db.cursor()
                                cur1.execute(sql, values)
                                db.commit()
                                messagebox.showinfo("Success", "Successfully Registered")
                                clearr()
                            except:
                                messagebox.showinfo('Error', text="Not Registered")
                        except:
                            messagebox.showinfo("error", "database not connected")
                except:
                    messagebox.showinfo("error", "internet required !!!!!!!!!!")



        # 0------------------------------------code for ---------------------
        first_name = Label(adf1, text="Name :", font='Verdana 14 bold', bg='turquoise1')
        first_name.place(relx=.34, rely=.09)

        father_name = Label(adf1, text="Father Name:", font='Verdana 14 bold', bg='turquoise1')
        father_name.place(relx=.34, rely=.18)

        dob = Label(adf1, text="Date Of Birth", font='Verdana 14 bold', bg='turquoise1')
        dob.place(relx=.34, rely=.27)

        scholar = Label(adf1, text="Scholar no. :", font='Verdana 14 bold',bg='turquoise1')
        scholar.place(relx=.34, rely=.36)

        class1 = Label(adf1, text="Class", font='Verdana 14 bold', bg='turquoise1')
        class1.place(relx=.34, rely=.45)

        samgra = Label(adf1, text="Samgra Id", font='Verdana 14 bold', bg='turquoise1')
        samgra.place(relx=.34, rely=.54)

        acc = Label(adf1, text="Account No.", font='Verdana 14 bold', bg='turquoise1')
        acc.place(relx=.34, rely=.63)

        mobileno = Label(adf1, text="Mobile No.", font='Verdana 14 bold', bg='turquoise1')
        mobileno.place(relx=.34, rely=.72)



        #  entry
        first_name = StringVar()
        father_name = StringVar()
        dob = StringVar()
        scholar = IntVar()
        scholar.set('')
        class1 = StringVar()
        class1.set('9')
        samgra = IntVar()
        samgra.set('')
        acc = IntVar()
        acc.set('')
        mobileno = IntVar()
        mobileno.set('')



        first_name = Entry(adf1, width=25, textvariable=first_name, font='Verdana 12 bold')
        first_name.place(relx=.52, rely=.09)

        father_name = Entry(adf1, width=25, textvariable=father_name,font='Verdana 12 bold')
        father_name.place(relx=.52, rely=.18)

        dob = DateEntry(adf1,  textvariable=dob,font=('Comic Sans MS', 10),state='readonly',date_pattern='dd/mm/yyyy',cursor="hand1", year=2003, month=1, day=1)
        dob.place(relx=.52, rely=.27)

        scholar = Entry(adf1, width=25, textvariable=scholar,font='Verdana 12 bold')
        scholar.place(relx=.52, rely=.36)


        data = (9,10,11,12)
        cb = Combobox(adf1, values=data, textvariable=class1, state='readonly')
        cb.place(relx=.52, rely=.45)

        samgra = Entry(adf1, width=25, textvariable=samgra, font='Verdana 12 bold')
        samgra.place(relx=.52, rely=.54)

        acc = Entry(adf1, width=25, textvariable=acc,font='Verdana 12 bold')
        acc.place(relx=.52, rely=.63)

        mobileno = Entry(adf1, width=25, textvariable=mobileno, font='Verdana 12 bold')
        mobileno.place(relx=.52, rely=.72)

        # button login and clear

        btn_login = Button(adf1, text="रजिस्टर ", font='Verdana 16 bold' ,command=register ,bg='DarkSeaGreen2')
        btn_login.place(relx=.42, rely=.85,relwidth=.2,bordermode=OUTSIDE)

        btn_login = Button(adf1, text="मिटाए  ", font='Verdana 16 bold', command=clearr,bg='DarkSeaGreen2')
        btn_login.place(relx=.64, rely=.85,relwidth=.12,bordermode=OUTSIDE)

        # -----------------------------------------------------------------------








        adf1.pack(fill='both',expand=1)
    def adff2():
        adf1.forget()
        adf2.forget()
        adf3.forget()
        adf4.forget()
        l2.destroy()




        l21.place(relx=.0,rely=.2)
        b2.place(relx=.2, rely=.4)
        adf2.pack(fill='both',expand=1)
    def adff3():
        adf1.forget()
        adf2.forget()
        adf3.forget()
        adf4.forget()
        l2.destroy()
        global tv
        tv.pack_forget()
        global  tv1
        tv1.pack_forget()
        tv = Frame(adf3, )

        tv1 = Frame(adf3, bg='cyan3')

        tree = Treeview(tv, column=("c1", "c2", "c3", "c4"), show='headings')
        tree.forget()


           


        def view9():
            tv1.forget()
            try:
                dbhost = "remotemysql.com"
                dbuser = "xsJRQzLgdj"
                dbpass = "QWX2fUpO5J"
                dbname = "xsJRQzLgdj"
                db = connect(dbhost, dbuser, dbpass, dbname)
                cur = db.cursor()
                sql = "SELECT * FROM `student` WHERE Class='9' ORDER BY scholar "
                cur.execute(sql)
                row = cur.fetchall()
                for d in row:

                    tree.insert("",END, values=d)
                tree.place(relx=0,rely=0,relheight=1,relwidth=1)

                tv.pack(fill="both", expand=1)

            except:
                messagebox.showinfo('Error', 'internet connection required ')
        def view10():
            tv1.forget()
            try:
                dbhost = "remotemysql.com"
                dbuser = "xsJRQzLgdj"
                dbpass = "QWX2fUpO5J"
                dbname = "xsJRQzLgdj"
                db = connect(dbhost, dbuser, dbpass, dbname)
                cur = db.cursor()
                sql = "SELECT * FROM `student` WHERE Class='10' ORDER BY scholar"
                cur.execute(sql)
                row = cur.fetchall()
                for d in row:

                    tree.insert("",END, values=d)
                tree.place(relx=0,rely=0,relheight=1,relwidth=1)

                tv.pack(fill="both", expand=1)

            except:
                messagebox.showinfo('Error', 'internet connection required ')
        def view11():
            tv1.forget()
            try:
                dbhost = "remotemysql.com"
                dbuser = "xsJRQzLgdj"
                dbpass = "QWX2fUpO5J"
                dbname = "xsJRQzLgdj"
                db = connect(dbhost, dbuser, dbpass, dbname)
                cur = db.cursor()
                sql = "SELECT * FROM `student` WHERE Class='11' ORDER BY scholar"
                cur.execute(sql)
                row = cur.fetchall()
                for d in row:

                    tree.insert("",END, values=d)
                tree.place(relx=0,rely=0,relheight=1,relwidth=1)

                tv.pack(fill="both", expand=1)

            except:
                messagebox.showinfo('Error', 'internet connection required ')
        def view12():
            tv1.forget()
            try:
                dbhost = "remotemysql.com"
                dbuser = "xsJRQzLgdj"
                dbpass = "QWX2fUpO5J"
                dbname = "xsJRQzLgdj"
                db = connect(dbhost, dbuser, dbpass, dbname)
                cur = db.cursor()
                sql = "SELECT * FROM `student` WHERE Class='12' ORDER BY scholar"
                cur.execute(sql)
                row = cur.fetchall()
                for d in row:

                    tree.insert("",END, values=d)
                tree.place(relx=0,rely=0,relheight=1,relwidth=1)

                tv.pack(fill="both", expand=1)

            except:
                messagebox.showinfo('Error', 'internet connection required ')
        tree.column("#1", anchor=CENTER)

        tree.heading("#1", text="Scholar")

        tree.column("#2", anchor=CENTER)

        tree.heading("#2", text=" NAME")

        tree.column("#3", anchor=CENTER)

        tree.heading("#3", text="Father Name")

        tree.column("#4", anchor=CENTER)

        tree.heading("#4", text="Date Of Birth")


        bttn =Button(tv1, text='CLASS 9',bg='thistle',command=view9)
        bttn.place(relx=.10,rely=.4,relheight=.08,relwidth=.1)

        bttn1 = Button(tv1, text='CLASS 10',bg='thistle',command=view10)
        bttn1.place(relx=.32, rely=.4, relheight=.08, relwidth=.1)

        bttn2 = Button(tv1, text='CLASS 11',bg='thistle',command=view11)
        bttn2.place(relx=.54, rely=.4, relheight=.08, relwidth=.1)

        bttn3 = Button(tv1, text='CLASS 12', bg='thistle',command=view12)
        bttn3.place(relx=.76, rely=.4, relheight=.08, relwidth=.1)







        tv1.pack(fill='both',expand=1)




        adf3.pack(fill='both',expand=1)
    def adff4():     #search
        global showframe
        adf1.forget()
        adf2.forget()
        adf3.forget()
        adf4.forget()
        global src
        src.pack_forget()
        src=Frame(master=adf4,bg='deep sky blue')



        # -----------search func--------
        def search():
            global showframe
            # ----------------------------------------
            showframe.pack_forget()

            showframe = Frame(master=src,bg='deep sky blue' )

            showframe.place(relx=0, rely=.4, relheight=.6, relwidth=1)
            # -----------------FUNCTION FOR FETCHING MY SQL--
            dbhost = "remotemysql.com"
            dbuser = "xsJRQzLgdj"
            dbpass = "QWX2fUpO5J"
            dbname = "xsJRQzLgdj"

            db = connect(dbhost, dbuser, dbpass, dbname)
            cur = db.cursor()
            global s
            s = srh.get()

            if s == ''or cls.get()=='':
                messagebox.showinfo('त्रुटि ', 'कृपया रोल नंबर और कक्षा दर्ज करे  ')
            else:

                sql = "SELECT * FROM `student` WHERE scholar='" + s + "' AND Class='"+cls.get()+"'"
                cur.execute(sql)
                row = cur.fetchall()
                if cur.rowcount == 0:
                    messagebox.showinfo('त्रुटि', 'इस रोल नंबर से कोई विद्यार्थी आपके डेटाबेस में रेजिस्ट्रेड नहीं है ')
                else:

                    for d in row:
                        # ----------------label for description -------------
                        l1 = Label(showframe, text='NAME',bg='deep sky blue', font='Verdana 15 bold')
                        l1.place(relx=.28, rely=.18)
                        l2 = Label(showframe, text='FATHER_NAME',bg='deep sky blue', font='Verdana 13 bold')
                        l2.place(relx=.06, rely=.38)
                        l3 = Label(showframe, text='Date Of Birth',bg='deep sky blue', font='Verdana 13 bold')
                        l3.place(relx=.06, rely=.58)

                        l5 = Label(showframe, text='SCHOLAR No.',bg='deep sky blue', font='Verdana 13 bold')
                        l5.place(relx=.06, rely=.78)
                        l6 = Label(showframe, text='SAMGRA',bg='deep sky blue', font='Verdana 13 bold')
                        l6.place(relx=.52, rely=.38)
                        l7 = Label(showframe, text='MOBILE No.',bg='deep sky blue', font='Verdana 13 bold')
                        l7.place(relx=.52, rely=.58)
                        l8 = Label(showframe, text='Account No.',bg='deep sky blue', font='Verdana 13 bold')
                        l8.place(relx=.52, rely=.78)
                        # ----------------------label for show data ---------------------
                        l1 = Label(showframe, text=d[1],bg='deep sky blue', font='Verdana 15 bold')
                        l1.place(relx=.46, rely=.18)
                        l2 = Label(showframe, text=d[2],bg='deep sky blue', font='Verdana 13 bold')
                        l2.place(relx=.23, rely=.38)
                        l3 = Label(showframe, text=d[3],bg='deep sky blue', font='Verdana 13 bold')
                        l3.place(relx=.23, rely=.58)

                        l5 = Label(showframe, text=d[0],bg='deep sky blue', font='Verdana 13 bold')
                        l5.place(relx=.23, rely=.78)
                        l6 = Label(showframe, text=d[4],bg='deep sky blue', font='Verdana 13 bold')
                        l6.place(relx=.65, rely=.38)
                        l7 = Label(showframe, text=d[6],bg='deep sky blue', font='Verdana 13 bold')
                        l7.place(relx=.65, rely=.58)
                        l8 = Label(showframe, text=d[5],bg='deep sky blue', font='Verdana 13 bold')
                        l8.place(relx=.65, rely=.78)
                        b4 = Button(showframe, text='UPDATE',width=24)
                        b4.place(relx=.45, rely=.9)

                db.close()

        # ------------searching coding


        w = Label(src, text='रोल नंबर से जानकारी देखें ', font='Verdana 20 bold',bg='deep sky blue')
        w.place(relx=.4, rely=.0)
        srh = Label(src , text="  रोल नंबर :", font='Verdana 18 bold',bg='deep sky blue')
        srh.place(relx=.30, rely=.2)
        srh = Entry(src, width=20, textvariable=srh,font='Verdana 16 bold')
        srh.place(relx=.45, rely=.2)
        cls = Label(src, text=" कक्षा  :", font='Verdana 18 bold', bg='deep sky blue')
        cls.place(relx=.30, rely=.1)
        cls = StringVar()
        data = (9, 10, 11, 12)
        cb = Combobox(src, values=data, textvariable=cls, state='readonly')
        cb.place(relx=.45, rely=.1)
        btn_srh = Button(src , text="देखें", font='Verdana 15 bold', command=search, width=20,bg='salmon4')
        btn_srh.place(relx=.40, rely=.32)

        src.pack(fill='both',expand=1)

        adf4.pack(fill='both', expand=1)


    def time1():
        string = time.strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000, time1)
    def logout():
        adf1.forget()
        adf2.forget()
        adf3.forget()
        adf4.forget()
        l2.destroy()

        showframe.forget()

        homefrrr()



    phtbtn = Button(l1, image=admnimg2)
    phtbtn.place(relx=.0,rely=.0)
    l1.pack(side='top',fill='x')
    dashb.pack(side='left',fill='y')
    l2 = Label(master=admnframe, text=f'स्कूल प्रबंधन में आपका स्वागत है सर !!!!', font=('Comic Sans MS', 25, 'bold'),
               bg='#33A1C9')
    l2.place(relx=.4,rely=.4)
    admnframe.pack(fill='both', expand='yes')

    adf1 = Frame(master=admnframe, bg='turquoise1')
    adf2 = Frame(master=admnframe, bg='crimson')
    adf3 = Frame(master=admnframe, bg='cyan2')
    adf4 = Frame(master=admnframe, bg='deep sky blue')


    #upper lable
    lbl = Label(master=l1, font=('Comic Sans MS', 10, 'bold'), background='powderblue', foreground='red',padx=30)
    lbl.place(relx=.9, rely=.7)
    time1()
    nnn=f'जुवानसिंह सोलंकी '
    nme.config(text=nnn)
    nme.place(relx=.21, rely=.85,anchor='e')
    # ------------------
    btn1 = Button(dashb, text='नया एडमिशन ',command=adff1,font=('Comic Sans MS', 20, 'bold'),padx=0,pady=13,bg='maroon4')
    btn1.place(relx=.01, rely=.0)
    btn2 = Button(dashb, text='रिजल्ट   ',font=('Comic Sans MS', 20, 'bold'),command=adff2,padx=50,pady=13,bg='burlywood4')
    btn2.place(relx=.01, rely=.14)
    btn3 = Button(dashb, text='पूरी जानकारी ',font=('Comic Sans MS', 20, 'bold'),command=adff3,padx=10,pady=13,bg='sienna3')
    btn3.place(relx=.01, rely=.28)
    btn4 = Button(dashb, text='सर्च छात्रा',font=('Comic Sans MS', 20, 'bold'),command=adff4,padx=35,pady=13,bg='seashell3')
    btn4.place(relx=.01, rely=.42)
    btne = Button(dashb, text='Log-Out',font=('Comic Sans MS', 20, 'bold'),command=logout,padx=40,pady=13,bg='magenta3')
    btne.place(relx=.01, rely=.56)
   # adf1 profile frame defination


    # adf2 result
    l21=LabelFrame(adf2,height=500,width=1500,bg='#33A1C9')
    b2=Label(l21, text='रिजल्ट अभी तैयार नहीं हुआ है ',font=('Comic Sans MS', 28, 'bold'),bg='#33A1C9' )


def adminlogin():
    stunf = Frame(bg='#008080', master=homeframe)
    stunf.pack(fill='both', expand=1)
    f1 = LabelFrame(stunf, text='ADMIN LOG-IN', font=('Comic Sans MS', 18), height=340, width=450, bg='#5967FF')
    f1.place(relx=.35, rely=.30)

    def time1():
        string = time.strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000, time1)

    lbl = Label(stunf, font=('calibri', 10, 'bold'), background='powderblue', foreground='red', padx=90)
    lbl.place(relx=.85, rely=.96)
    time1()


    def log():
        try:


            dbhost = "remotemysql.com"
            dbuser = "xsJRQzLgdj"
            dbpass = "QWX2fUpO5J"
            dbname = "xsJRQzLgdj"

            db = connect(dbhost, dbuser, dbpass, dbname)
            cur = db.cursor()
            global s
            a1 = username.get()
            a2 = password.get()

            if a1 =='' or a2 =='':
                messagebox.showinfo('Error', 'Please enter given field ')
            else:

                sql = "SELECT * FROM `staffpass` WHERE userid='"+a1+"' AND password='"+a2+"'"
                cur.execute(sql)
                row = cur.fetchall()
                if cur.rowcount == 0:
                    messagebox.showinfo('Error', 'Mr जुवानसिंह आपका यूजर नाम और पासवर्ड गलत है ')
                else:



                    stufrmfun()

                    stunf.pack_forget()  # remove this if you want to go at login screen after logout
            db.close()
        except:
            messagebox.showinfo('Error', 'internet connection requied ')
    #   mysql dtatabase

    usernameLabel = Label(f1, text="User Name", bg='#8470FF', font=('Calibri', 15)).place(relx=.2, rely=.2)
    username = StringVar()
    usernameEntry = Entry(f1, textvariable=username, font=('Calibri', 15)).place(relx=.5, rely=.2)

    # password label and password entry box
    passwordLabel = Label(f1, text="Password", bg='#8470FF', font=('Calibri', 15)).place(relx=.2, rely=.4)
    password = StringVar()
    passwordEntry = Entry(f1, textvariable=password, show='*', font=('Calibri', 15)).place(relx=.5, rely=.4)
    # button
    loginButton = Button(f1, text="Login", bg='#68228B', padx=60, font=('Calibri', 15), command=log).place(relx=.15,
                                                                                                           rely=.75)
    back = Button(f1, text="Home", bg='#68228B', padx=40, font=('Calibri', 15), command=stunf.forget).place(relx=.60,
                                                                                                               rely=.75)


def homefrrr():

    homeframe.pack(fill='both', expand=1)
    admnframe.forget()



root=Tk()
root.title('SCHOOL MANAGEMENT')
root.minsize(1300,700)

# image define for use
img1=Image.open('adminimg.jpg')

admnimg= img1.resize((200,200),Image.ANTIALIAS)

admnimg1=ImageTk.PhotoImage(admnimg)
img2 = Image.open('teacheravtar.jpg')
admnimgg = img2.resize((80, 80), Image.ANTIALIAS)
admnimg2 = ImageTk.PhotoImage(admnimgg)




homeframe=Frame(root,bg='#33A1C9')
hm1=LabelFrame(homeframe,bg='#27408B',width=444,height=300)
# homebtn
admnbtn=Button(homeframe,image=admnimg1,command=adminlogin)

admnbtn.place(relx=.5,rely=.6,anchor='center')

hm1.place(relx=.5,rely=.6,anchor='center')
# Add Text






#   all frame defination

admnframe=Frame(root,bg='#33A1C9')
#  adminframe
adf1 = Frame(master=admnframe, bg='turquoise1')
adf2 = Frame(master=admnframe, bg='crimson')
adf3 = Frame(master=admnframe, bg='green')
adf4 = Frame(master=admnframe, bg='pink')
tv= Frame(adf3 ,)
tv1= Frame(adf3 ,bg='cyan3')
r1 = Label(adf1, text='   नयी छात्रा रजिस्टर करे    ', font=('Comic Sans MS', 20), bg='DarkSeaGreen2')
src=Frame(master=adf4 , bg='deep sky blue')
showframe = Frame(master=src ,bg='deep sky blue')
l1=LabelFrame(admnframe, text='GOVERNMENT GIRLS HIGH SECONDARY SCHOOL DAHI',height=100)
dashb=LabelFrame(admnframe,width=200,bg='#27408B')
nme = Label(master=l1, font=('Comic Sans MS', 16, 'bold'), foreground='black')
homefrrr()



#-----------------time




# Styling the label widget so that clock
# will look more attractive

lbl = Label(homeframe, font=('calibri', 10, 'bold'),background='powderblue',foreground='red',padx=90)
scname = Label(homeframe, font=('Comic Sans MS', 33, 'bold'),background='powderblue',foreground='red',text='GOVERNMENT GIRLS HIGH SECONDARY SCHOOL DAHI',)
scname.place(relx=.5,rely=.1,anchor='center')
# Placing clock at the centre
# of the tkinter window
lbl.place(relx=.85,rely=.96)
time1()
# -------------------------time ------ close
Label(root,text='developed by -:   RAJENDRA  CHOUNGAD',bg='powderblue',padx=180).place(relx=0,rely=.96)
root.mainloop()
