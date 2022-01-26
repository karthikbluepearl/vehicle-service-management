from tkinter import*
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
import mysql.connector
from tkinter import messagebox
from tkinter import scrolledtext as tkst
top=Tk()
top.geometry("1368x768")
top.title("vehicle service")
def FIND():#SEARCH BY VEHICLE NO AND INSERT THE DATA ON FIELD
        number = Entry_s.get()
        con = mysql.connector.connect(host='localhost', user='root', password='', database='vehicle')
        cur = con.cursor()
        find_mrp = "SELECT vehiclemodelno,vehicletype,servicedate,vehicleservice,customername,customerphoneno,customeraddress,amount FROM service_manage WHERE vehicleno = %s"
        cur.execute(find_mrp, [number])
        results = cur.fetchall()
        if results:
                messagebox.showinfo("Exists","Customer {} Is Exists".format(number))
                Entry1.insert(END,number)
                print2=results[0][0]
                Entry2.insert(END,print2)
                print3=results[0][1]
                Combo1.insert(END,print3)
                print4=results[0][3]
                Combo2.insert(END,print4)
                print5=results[0][2]
                date1.insert(END,print5)
                print6=results[0][4]
                Entry3.insert(END,print6)
                print7=results[0][5]
                Entry4.insert(END,print7)
                print8=results[0][7]
                Entry6.insert(END,print8)
                print8=results[0][6]
                Entry5.insert(END,print8)
        else:
                messagebox.showinfo("Exists","Customer {} Not Already Exists".format(number))
def Cumtom_details():
        def DELETE():#delete the customer details
                for selected_item in tree.selection():
                        item = tree.item(selected_item)
                        records = item['values']
                        id1=records[0]
                con=mysql.connector.connect(host="localhost",user="root",password="",database="vehicle")
                cur=con.cursor()
                delete1 = """DELETE FROM service_manage WHERE ID = %s"""
                check=messagebox.askokcancel("","Are Delete")
                if id1=="":
                        messagebox.showinfo("","please any select one")
                
                else:
                        cur.execute(delete1,(id1,))
                        tree.delete(selected_item)
                
                con.commit()
                con.close()
        
       
        def item_selected(event):
                for selected_item in tree.selection():
                        item = tree.item(selected_item)
                        records = item['values']
        def Exit():#exit button custom details to main page
                frame1.destroy()
        #----------------------- custom details Frame--------------------------              
        frame1=Frame(canvas,bg="white",height="700",width="1200")
        frame1.place(x=80,y=80)
        Button1= Button(frame1, text="Delete", font="times 20 bold", fg="darkblue",activebackground="blue", bg="white", bd=0,command=DELETE)
        Button1.place(x=450, y=365)
        Button2= Button(frame1, text="Exit", font="times 20 bold", fg="darkblue",activebackground="blue",bg="white", bd=0,command=Exit)
        Button2.place(x=650, y=365)
        Label_s=Label(frame1,text="CUSTOMER DETAILS",fg="darkblue",font="times 20 bold")
        Label_s.place(x=437,y=10)
        #treeview
        s=ttk.Style()
        s.theme_use('default')
        s.map('Treeview',background=[('selected',"darkblue")])
        tree = ttk.Treeview(frame1,columns=(1,2,3,4,5,6,7,8,9,10), show='headings',selectmode='browse')
        #define headings
        tree.heading('1',text='ID')
        tree.column('1',width=50)
        tree.heading('2',text='vehicleno')
        tree.column('2',width=100)
        tree.heading('3',text='vehiclemodelno')
        tree.column('3',width=100)
        tree.heading('4',text='vehicletype')
        tree.column('4',width=120)
        tree.heading('5',text='servicedate')
        tree.column('5',width=100)
        tree.heading('6',text='vehicleservice')
        tree.column('6',width=100)
        tree.heading('7',text='customername')
        tree.column('7',width=100)
        tree.heading('8',text='customerphoneno')
        tree.column('8',width=200)
        tree.heading('9',text='ADDRESS')
        tree.column('9',width=150)
        tree.heading('10',text='amount')
        tree.column('10',width=100)
        tree.bind('<<TreeviewSelect>>', item_selected)
        con=mysql.connector.connect(host="localhost",user="root",password="",database="vehicle")
        cur=con.cursor()
        c=cur.execute("SELECT* from service_manage")
        rows = cur.fetchall()
        for contact in rows:#database value insert in treeview
                tree.insert('', END, values=contact)
        tree.place(x=10,y=100)
def REMOVE():#connect remove button
        vehicleno=Entry1.delete(0,END)
        vehiclemodelno=Entry2.delete(0,END)
        vehicletype=Combo1.delete(0,END)
        servicedate=date1.delete(0,END)
        vehicleservice=Combo2.delete(0,END)
        amount=Entry6.delete(0,END)
        customername=Entry3.delete(0,END)
        customerphoneno=Entry4.delete(0,END)
        customeraddress=Entry5.delete(0,END)
   
    
        
def vehicle(Event):#bind with Combo2(vehicle service)
    vehicle=Combo2.get()
    WW=1000
    D=500
    T=1200
    
    if vehicle in "Water Wash":
        Entry6.insert(END,WW)
    if vehicle in "dent removel":
        Entry6.delete(0,END)
        Entry6.insert(END,D)
    if vehicle in "tyre Change":
        Entry6.delete(0,END)
        Entry6.insert(END,T)

    
def DB():#all details insert into database
    vehicleno=Entry1.get()
    vehiclemodelno=Entry2.get()
    vehicletype=Combo1.get()
    servicedate=date1.get()
    vehicleservice=Combo2.get()
    customername=Entry3.get()
    customerphoneno=Entry4.get()
    customeraddress=Entry5.get()
    amount=Entry6.get()
    if vehicleno=="" or vehiclemodelno=="" or vehicletype=="" or servicedate==""or vehicleservice==""or customername==""or customerphoneno=="" or customeraddress=="" or amount=="":
            messagebox.showinfo('Error', "All fields are required")
    
    else:
            #--------------------------INSERT DATA
            con=mysql.connector.connect(host="localhost",user="root",password="",database="vehicle")
            cur=con.cursor()
            sql=("INSERT INTO service_manage (id,vehicleno,vehiclemodelno,vehicletype,servicedate,vehicleservice,customername,customerphoneno,customeraddress,amount)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            var=("",vehicleno,vehiclemodelno,vehicletype,servicedate,vehicleservice,customername,customerphoneno,customeraddress,amount)
            sub1=cur.execute(sql,var)
            print("print:",sub1)
            con.commit()
            con.close()
            w1=messagebox.showinfo('Success', "Inserted Successfully ")
            label2=Label(frame1,text="Customer Name  :"+customername,fg="black")
            label2.place(x=640,y=240)
            label2=Label(frame1,text="Customer Phoneno : "+customerphoneno,fg="black")
            label2.place(x=900,y=240)
            label3="  {}\t\t  {}\t \t{}\t\t{}   \t\t\t {}".format(vehicleno,vehicletype,vehicleservice,servicedate,amount)
            Scrolledtext1.insert('6.0', label3)
            vehicleservice=Combo2.delete(0,END)
            amount=Entry6.delete(0,END)
    
    
canvas=Canvas(top,bg="darkblue",height="768",width="1368")
canvas.place(x=-5,y=0)
#heading label
label_head=Label(canvas,text="Vehicle repair And maintenance service Management",fg="white",bg="darkblue",font="times 30 bold")
label_head.place(x=250,y=5)
#frame details frame
frame1=Frame(canvas,bg="white",height="600",width="1200")
frame1.place(x=80,y=140)
#bill heading
label_head1=Label(frame1,text="Bill Window",fg="white",bg="darkblue",font="times 15 bold")
label_head1.place(x=790,y=200)
#bill detail headings labels
label1=Label(frame1,text="\nvehicleno \t\t  vehicleype \tvehicleservice \tdate \t   \tamount      ",fg="black",bd=0,font="times 10 bold")
label1.place(x=630,y=268)
#scrolledtext for blling (print details )   
Scrolledtext1 = tkst.ScrolledText(frame1)
Scrolledtext1.place(x=600,y=300, width=564, height=275)
Scrolledtext1.configure(borderwidth=0)
Scrolledtext1.configure(font="futura 10 bold")
Scrolledtext1.configure(state="normal")
Scrolledtext1.configure(bg="white")
#searching frame
frame_search=Frame(canvas,bg="white",height="60",width="1200")
frame_search.place(x=80,y=70)
#search part____________________________________
Label_s=Label(frame_search,text="Search by Vehicle No:",fg="darkblue",font="times 20 bold")
Label_s.place(x=127,y=10)
Entry_s=Entry(frame_search,width="25",fg="black",font="times 15 bold",bd=0,selectforeground="darkblue",selectbackground="white",relief="flat")
Entry_s.place(x=400,y=15)
frame_s= Frame(frame_search, height=2, width=276, bg="darkblue")
frame_s.place(x=400, y=40)
Button2= Button(frame_search, text="Search", font="times 20 bold", fg="darkblue",activebackground="blue", bg="white", bd=0,command=FIND)
Button2.place(x=650, y=5)
#customer details button
Button3 = Button(frame_search, text="Customber Details", font="times 20 bold", fg="darkblue",activebackground="blue",bg="white", bd=0,command=Cumtom_details)
Button3.place(x=870, y=5)
#vehicle details heading
label_head1=Label(frame1,text="Vehicle Details",fg="white",bg="darkblue",font="times 20 bold")
label_head1.place(x=50,y=5)
#Customer detail heading
label_head2=Label(frame1,text="Customer Details",fg="white",bg="darkblue",font="times 20 bold")
label_head2.place(x=650,y=5)

#vehicle No 
Label1=Label(frame1,text="Vehicle No:",fg="darkblue",font="times 20 bold")
Label1.place(x=50,y=60)
Entry1=Entry(frame1,width="25",fg="black",font="times 15 bold",bd=0,selectforeground="darkblue",selectbackground="white",relief="flat")
Entry1.place(x=200,y=65)
frame2= Frame(frame1, height=2, width=276, bg="darkblue")
frame2.place(x=200, y=90)
#Vehicle Type
Label2=Label(frame1,text="Vehicle Type         :",fg="darkblue",font="times 20 bold",activeforeground="darkblue")
Label2.place(x=50,y=210)
Combo1=ttk.Combobox(frame1,width="20",font="futura 15 italic")
Combo1['values']=("2Wheeler","3Wheeler","3Wheeler")
Combo1.current()
Combo1.place(x=290,y=213)
#Vehicle Model No
Label3=Label(frame1,text="Vehicle Model No :",fg="darkblue",font="times 20 bold")
Label3.place(x=50,y=130)
Entry2=Entry(frame1,width="25",fg="black",font="times 15 bold",bd=0,selectforeground="darkblue",selectbackground="white",relief="flat")
Entry2.place(x=285,y=135)
frame3= Frame(frame1, height=2, width=256, bg="darkblue")
frame3.place(x=285, y=160)
#Customer Name
Label4=Label(frame1,text="Customer Name :",fg="darkblue",font="times 20 bold")
Label4.place(x=645,y=60)
Entry3=Entry(frame1,width="25",fg="black",font="times 15 bold",bd=0,selectforeground="darkblue",selectbackground="white",relief="flat")
Entry3.place(x=865,y=65)
frame4= Frame(frame1, height=2, width=256, bg="darkblue")
frame4.place(x=865, y=90)
#Customer Phone No
Label5=Label(frame1,text="Customer Phone No :",fg="darkblue",font="times 20 bold")
Label5.place(x=600,y=110)
Entry4=Entry(frame1,width="25",fg="black",font="times 15 bold",bd=0,selectforeground="darkblue",selectbackground="white",relief="flat")
Entry4.place(x=865,y=115)
frame5= Frame(frame1, height=2, width=256, bg="darkblue")
frame5.place(x=865, y=140)
#Customer Address
Label7=Label(frame1,text="Customer Address :",fg="darkblue",font="times 20 bold")
Label7.place(x=620,y=160)
Entry5=Entry(frame1,width="25",fg="black",font="times 15 bold",bd=0,selectforeground="darkblue",selectbackground="white",relief="flat")
Entry5.place(x=865,y=165)
frame6= Frame(frame1, height=2, width=256, bg="darkblue")
frame6.place(x=865, y=190)
#Date of Service
Label6=Label(frame1,text="Date of Service     :",fg="darkblue",font="times 20 bold")
Label6.place(x=50,y=290)
date1=DateEntry(frame1,selectmode="day",fg="darkblue",width=37,relief="flat")
date1.place(x=290,y=300)
Dt=date(2022,12,1)
date1.set_date(Dt)
date1.delete(0,END)
#Vehicle Service
Label7=Label(frame1,text="Vehicle Service     :",fg="darkblue",font="times 20 bold",activeforeground="darkblue")
Label7.place(x=50,y=360)
Combo2=ttk.Combobox(frame1,width="20",font="futura 15 italic")
Combo2['values']=("Water Wash","dent removel","tyre Change","other(Custom Price)")
Combo2.current()
Combo2.place(x=290,y=363)
#bind the Combo2(vehicle service)with vehicle function
Combo2.bind("<<ComboboxSelected>>",vehicle)
#Amount
Label8=Label(frame1,text="Amount                 :",fg="darkblue",font="times 20 bold")
Label8.place(x=50,y=420)
Entry6=Entry(frame1,width="25",fg="black",font="times 15 bold",bd=0,selectforeground="darkblue",selectbackground="white",relief="flat")
Entry6.place(x=285,y=425)
frame7= Frame(frame1, height=2, width=256, bg="darkblue")
frame7.place(x=285, y=450)
#Add button connect to DB function
Button1 = Button(frame1, text="ADD", font="times 18 bold", fg="darkblue",activebackground="blue", bg="white", bd=0,command=DB)
Button1.place(x=200, y=520)
#Remove button connect to REMOVE function
Button2= Button(frame1, text="REMOVE", font="times 18 bold", fg="darkblue",activebackground="blue",bg="white", bd=0,command=REMOVE)
Button2.place(x=350, y=520)
top.mainloop()
