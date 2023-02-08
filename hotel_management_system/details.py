from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1081x590+195+220")


        #  =================title=================
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",16,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1081,height=35)

        #  ==============label frame==================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=35,width=450,height=350)


        #  ==============logo==================
        img2=Image.open(r"C:\Users\Pruthviraj Gavali\Desktop\hotel_management_system\hotel_images\logohotel.jpg")
        img2=img2.resize((90,35),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=3,y=2,width=90,height=31)

        #  Floor
        lbl_floor=Label(labelframeleft,text="Floor :",font=("arial",10,"bold"),padx=2,pady=5)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=25,font=("arial",10,"bold"))
        enty_floor.grid(row=0,column=1,sticky=W)

        
        #  Room No
        lbl_RoomNo=Label(labelframeleft,text="Room No :",font=("arial",10,"bold"),padx=2,pady=5)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        self.var_roomNo=StringVar()
        enty_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomNo,width=25,font=("arial",10,"bold"))
        enty_RoomNo.grid(row=1,column=1,sticky=W)

        #  Room Type
        lbl_RoomType=Label(labelframeleft,text="Room Type :",font=("arial",10,"bold"),padx=2,pady=5)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()
        enty_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=25,font=("arial",10,"bold"))
        enty_RoomType.grid(row=2,column=1,sticky=W)

        #  =================btns================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=285,height=30)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",10,"bold"),bg="black",fg="gold",width=7)
        btnAdd.grid(row=0,column=0,padx=2)

        btnUpdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",10,"bold"),bg="black",fg="gold",width=7)
        btnUpdate.grid(row=0,column=1,padx=2)

        btnDelete=Button(btn_frame,text="DELETE",font=("arial",10,"bold"),bg="black",fg="gold",width=7)
        btnDelete.grid(row=0,column=2,padx=2)

        btnReset=Button(btn_frame,text="RESET",font=("arial",10,"bold"),bg="black",fg="gold",width=7)
        btnReset.grid(row=0,column=3,padx=2)

        #  =========================table frame search system============
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=500,y=35,width=500,height=350)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        self.room_table=ttk.Treeview(Table_Frame,column=("floor","roomno","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomType",text="Room Type")
        

        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100) 
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomType",width=100)
       
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_data(self):
            if self.var_floor.get()=="" or self.var_RoomType.get()=="":
                messagebox.showerror("ERROR!","All fields are required",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                self.var_floor.get(),
                                                                                self.var_roomNo.get(),
                                                                                self.var_RoomType.get(),
                                                                                
                                                                            ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()                                                        
                    messagebox.showinfo("SUCCESS","New Room Added Successfully",parent=self.root)
                except Exception as es:
                    messagebox.showwarning("WARNING",f"Something went wrong:{str(es)}",parent=self.root)        


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_RoomType.set(row[2]),

    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("ERROR!","Please enter mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s, where RoomNo=%s",(                                                                     
                                                                                    self.var_floor.get(),
                                                                                    self.var_RoomType.get(),
                                                                                    self.var_roomNo.get(),                                                                     
                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("UPDATE","New Room Details has been Updated Successfully",parent=self.root)    

            


if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()        