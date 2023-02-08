from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1081x590+195+220")


        # =============variables==================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proff=StringVar()
        self.var_id_number=StringVar()

        #  =================title=================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",16,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1081,height=35)


        #  ==============logo==================
        img2=Image.open(r"C:\Users\Pruthviraj Gavali\Desktop\hotel_management_system\hotel_images\logohotel.jpg")
        img2=img2.resize((90,35),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=3,y=2,width=90,height=31)

        #  ==============label frame==================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=35,width=300,height=395)

        #  ================labels and entrys=============
        #  custRef
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref :",font=("arial",10,"bold"),padx=2,pady=5)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=23,textvariable=self.var_ref,state="readonly",font=("arial",10,"bold"))
        enty_ref.grid(row=0,column=1)

        #  cust name
        cname=Label(labelframeleft,font=("arial",10,"bold"),text="Customer Name :",padx=2,pady=5)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=23,font=("arial",10,"bold"))
        txtcname.grid(row=1,column=1)

        #  Mother name
        lblmname=Label(labelframeleft,font=("arial",10,"bold"),text="Mother Name :",padx=2,pady=5)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,width=23,font=("arial",10,"bold"))
        txtmname.grid(row=2,column=1)

        #  gender combobox
        label_gender=Label(labelframeleft,font=("arial",10,"bold"),text="Gender :",padx=2,pady=5)
        label_gender.grid(row=3,column=0,sticky=W)
        
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",10,"bold"),width=20,state="readonly")
        combo_gender["value"]=("Select","Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #  postcode
        lblPostCode=Label(labelframeleft,font=("arial",10,"bold"),text="Postcode :",padx=2,pady=5)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,width=23,font=("arial",10,"bold"))
        txtPostCode.grid(row=4,column=1)

        #  Mobile number
        lblMobile=Label(labelframeleft,font=("arial",10,"bold"),text="Mobile No :",padx=2,pady=5)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=23,font=("arial",10,"bold"))
        txtMobile.grid(row=5,column=1)

        #  email
        lblEmail=Label(labelframeleft,font=("arial",10,"bold"),text="Email :",padx=2,pady=5)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=23,font=("arial",10,"bold"))
        txtEmail.grid(row=6,column=1)

        #  nationality
        lblNationality=Label(labelframeleft,font=("arial",10,"bold"),text="Nationality :",padx=2,pady=5)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",10,"bold"),width=20,state="readonly")
        combo_Nationality["value"]=("India","America","Other")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)

        #  idproof type combobox
        label_gender=Label(labelframeleft,font=("arial",10,"bold"),text="ID Proof Type :",padx=2,pady=5)
        label_gender.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proff,font=("arial",10,"bold"),width=20,state="readonly")
        combo_id["value"]=("AdharCard","Driving Licence","Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        #  ID Number
        lblIdNumber=Label(labelframeleft,font=("arial",10,"bold"),text="ID Number :",padx=2,pady=5)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=23,font=("arial",10,"bold"))
        txtIdNumber.grid(row=9,column=1)

        #  address
        lblAddress=Label(labelframeleft,font=("arial",10,"bold"),text="Address :",padx=2,pady=5)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=23,font=("arial",10,"bold"))
        txtAddress.grid(row=10,column=1)

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

        #  =========================table frame search system============
        
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=310,y=35,width=770,height=395)

        lblSearchBy=Label(Table_Frame,font=("arial",10,"bold"),text="Search By :",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.serch_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.serch_var,font=("arial",10,"bold"),width=15,state="readonly")
        combo_Search["value"]=("Select","Mobile","Ref")
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
        details_table.place(x=0,y=35,width=760,height=335)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="ID Proff")
        self.Cust_Details_Table.heading("idnumber",text="ID Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100) 
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("ERROR!","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_ref.get(),
                                                                            self.var_cust_name.get(),
                                                                            self.var_mother.get(),
                                                                            self.var_gender.get(),
                                                                            self.var_post.get(),
                                                                            self.var_mobile.get(),
                                                                            self.var_email.get(),
                                                                            self.var_nationality.get(),
                                                                            self.var_id_proff.get(),
                                                                            self.var_id_number.get(),
                                                                            self.var_address.get(),
                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()                                                        
                messagebox.showinfo("SUCCESS","Customer has been Added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("WARNING",f"Something went wrong:{str(es)}",parent=self.root)  

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close() 

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proff.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10]),



    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("ERROR!","Please enter mobile Number",parent=self.root)
        else:

            conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                                                                                                                                                            
                                                                                                                                                            self.var_cust_name.get(),
                                                                                                                                                            self.var_mother.get(),
                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                            self.var_post.get(),
                                                                                                                                                            self.var_mobile.get(),
                                                                                                                                                            self.var_email.get(),
                                                                                                                                                            self.var_nationality.get(),
                                                                                                                                                            self.var_id_proff.get(),
                                                                                                                                                            self.var_id_number.get(),
                                                                                                                                                            self.var_address.get(),
                                                                                                                                                            self.var_ref.get()
                                                                                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("UPDATE","Customer Details has been Updated Successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do You Want Delete This Customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proff.set(""),
        self.var_id_number.set(""),
        self.var_address.set(""),
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()        
        


                                                                                                                                                 

                  


               





        


        





        




        













if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()

