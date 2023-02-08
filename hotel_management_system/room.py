from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1081x590+195+220")

        #  ==========variables=============
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        #  =================title=================
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",16,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1081,height=35)

        #  ==============label frame==================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roombooking Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=35,width=300,height=395)


        #  ==============logo==================
        img2=Image.open(r"C:\Users\Pruthviraj Gavali\Desktop\hotel_management_system\hotel_images\logohotel.jpg")
        img2=img2.resize((90,35),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=3,y=2,width=90,height=31)  

        #  ================labels and entrys=============
        #  Customer Contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact :",font=("arial",10,"bold"),padx=2,pady=5)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=13,font=("arial",10,"bold"))
        enty_contact.grid(row=0,column=1,sticky=W) 

        #  Fetech data buttton
        btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=7)
        btnFetchData.place(x=230,y=0)

        #  Check in Date
        check_in_date=Label(labelframeleft,text="Check_in Date :",font=("arial",10,"bold"),padx=2,pady=5)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=20,font=("arial",10,"bold"))
        txtcheck_in_date.grid(row=1,column=1)

        #  Check out Date
        lbl_check_out=Label(labelframeleft,text="Check_Out Date :",font=("arial",10,"bold"),padx=2,pady=5)
        lbl_check_out.grid(row=2,column=0,sticky=W)
        txt_check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=20,font=("arial",10,"bold"))
        txt_check_out.grid(row=2,column=1) 

        #  Room Type
        label_RoomType=Label(labelframeleft,font=("arial",10,"bold"),text="Room Type :",padx=2,pady=5)
        label_RoomType.grid(row=3,column=0,sticky=W)
        
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",10,"bold"),width=20,state="readonly")
        combo_RoomType["value"]=("Select","Single","Double","Luxary")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        #  Available Room
        lblRoomAvailable=Label(labelframeleft,text="Available Room :",font=("arial",10,"bold"),padx=2,pady=5)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=20,font=("arial",10,"bold"))
        txtRoomAvailable.grid(row=4,column=1) 

        #  Meal
        lblMeal=Label(labelframeleft,text="Meal :",font=("arial",10,"bold"),padx=2,pady=5)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=20,font=("arial",10,"bold"))
        txtMeal.grid(row=5,column=1) 

        #  No Of Days 
        lblNoOfDays=Label(labelframeleft,text="No Of Days :",font=("arial",10,"bold"),padx=2,pady=5)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=20,font=("arial",10,"bold"))
        txtNoOfDays.grid(row=6,column=1) 

        #  Paid Tax
        lblNoOfDays=Label(labelframeleft,text="Paid Tax :",font=("arial",10,"bold"),padx=2,pady=5)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=20,font=("arial",10,"bold"))
        txtNoOfDays.grid(row=7,column=1) 

        #  Sub Total 
        lblNoOfDays=Label(labelframeleft,text="Sub Total :",font=("arial",10,"bold"),padx=2,pady=5)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=20,font=("arial",10,"bold"))
        txtNoOfDays.grid(row=8,column=1)

        #  Total Cost 
        lblIdNumber=Label(labelframeleft,text="Total Cost :",font=("arial",10,"bold"),padx=2,pady=5)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_total,width=20,font=("arial",10,"bold"))
        txtIdNumber.grid(row=9,column=1) 

        # ===========Bill Button===============
        btnBill=Button(labelframeleft,text="BILL",command=self.total,font=("arial",10,"bold"),bg="black",fg="gold",width=7)
        btnBill.grid(row=10,column=0,padx=2,sticky=W)

        #  =================btns================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=339,width=285,height=30)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",10,"bold"),bg="black",fg="gold",width=7)
        btnAdd.grid(row=0,column=0,padx=2)

        btnUpdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",10,"bold"),bg="black",fg="gold",width=7)
        btnUpdate.grid(row=0,column=1,padx=2)

        btnDelete=Button(btn_frame,text="DELETE",command=self.mDelete,font=("arial",10,"bold"),bg="black",fg="gold",width=7)
        btnDelete.grid(row=0,column=2,padx=2)

        btnReset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",10,"bold"),bg="black",fg="gold",width=7)
        btnReset.grid(row=0,column=3,padx=2)

        #  ===========Rightside image=================
        img3=Image.open(r"C:\Users\Pruthviraj Gavali\Desktop\hotel_management_system\hotel_images\bed.jpg")
        img3=img3.resize((530,180),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=540,y=40,width=530,height=180) 

        #  =========================table frame search system============
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=310,y=220,width=770,height=210)

        lblSearchBy=Label(Table_Frame,font=("arial",10,"bold"),text="Search By :",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.serch_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.serch_var,font=("arial",10,"bold"),width=15,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=20,font=("arial",10,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="SEARCH",command=self.search,font=("arial",10,"bold"),bg="black",fg="gold",width=7)
        btnSearch.grid(row=0,column=3,padx=2)

        btnShowAll=Button(Table_Frame,text="SHOW ALL",command=self.fetch_data,font=("arial",10,"bold"),bg="black",fg="gold",width=9)
        btnShowAll.grid(row=0,column=4,padx=2)

        # ================Show Data Table=========================

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=35,width=760,height=160)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="NoOfDays")

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100) 
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)

        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        # ================ add data ==============
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("ERROR!","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_contact.get(),
                                                                            self.var_checkin.get(),
                                                                            self.var_checkout.get(),
                                                                            self.var_roomtype.get(),
                                                                            self.var_roomavailable.get(),
                                                                            self.var_meal.get(),
                                                                            self.var_noofdays.get(),
                                                                            
                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()                                                        
                messagebox.showinfo("SUCCESS","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("WARNING",f"Something went wrong:{str(es)}",parent=self.root)   

        #  =====Fetch Data===========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        #getcursor
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

        #  update function
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("ERROR!","Please enter mobile Number",parent=self.root)
        else:

            conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
                                                                                                                                                            
                                                                                                                                                            self.var_checkin.get(),
                                                                                                                                                            self.var_checkout.get(),
                                                                                                                                                            self.var_roomtype.get(),
                                                                                                                                                            self.var_roomavailable.get(),
                                                                                                                                                            self.var_meal.get(),
                                                                                                                                                            self.var_noofdays.get(),
                                                                                                                                                            self.var_contact.get(),
                                                                                                                                                            
                                                                                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("UPDATE","Room Details has been Updated Successfully",parent=self.root)

            # delete function
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do You Want Delete This Customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):  
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("") 
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("") 

                 
    
        #  ==============All Data Fetch=======================

    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("ERROR!","Please Enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("ERROR!","This Number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=310,y=37,width=225,height=180)

                lblName=Label(showDataframe,text="Name :",font=("arial",10,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",10,"bold"))
                lbl.place(x=60,y=0)

                #  =============Gender=============
                conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender :",font=("arial",10,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",10,"bold"))
                lbl2.place(x=60,y=30)

                #  =============Email=============
                conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showDataframe,text="Email :",font=("arial",10,"bold"))
                lblemail.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row,font=("arial",10,"bold"))
                lbl3.place(x=60,y=60)

                #  =============Nationality=============
                conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataframe,text="Nationality :",font=("arial",10,"bold"))
                lblNationality.place(x=0,y=90)

                lbl4=Label(showDataframe,text=row,font=("arial",10,"bold"))
                lbl4.place(x=90,y=90)

                #  =============Address=============
                conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblAddress=Label(showDataframe,text="Address :",font=("arial",10,"bold"))
                lblAddress.place(x=0,y=120)

                lbl5=Label(showDataframe,text=row,font=("arial",10,"bold"))
                lbl5.place(x=90,y=120)

                #  =============Contact=============
                conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
                my_cursor=conn.cursor()
                query=("select Mobile from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblContact=Label(showDataframe,text="Contact :",font=("arial",10,"bold"))
                lblContact.place(x=0,y=150)

                lbl5=Label(showDataframe,text=row,font=("arial",10,"bold"))
                lbl5.place(x=90,y=150)

    # ====================search system=================   
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from room where "+str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()         

    def total(self):
        inDate=self.var_checkin.get() 
        outDate=self.var_checkout.get() 
        inDate=datetime.strptime(inDate,"%d/%m/%Y") 
        outDate=datetime.strptime(outDate,"%d/%m/%Y")  
        self.var_noofdays.set(abs(outDate-inDate).days) 

        if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Luxary"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1)) 
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))  
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 


        if (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1)) 
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))  
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)      

                

                
        


        






if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()