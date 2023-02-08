from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1280x800+0+0")


        #  =============ist img================
        img1=Image.open(r"C:\Users\Pruthviraj Gavali\Desktop\hotel_management_system\hotel_images\hotel1.png")
        img1=img1.resize((1280,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1280,height=140)

        #  ==============logo==================
        img2=Image.open(r"C:\Users\Pruthviraj Gavali\Desktop\hotel_management_system\hotel_images\logohotel.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        #  =================title=================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1280,height=50)

        #  ===============main Frame==============
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1280,height=500)

        #  ===============Menu===============
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=190) 

        #  ==============btn Frame===========
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=187,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=16,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=16,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=16,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="REPORT",width=16,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",width=16,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        logout_btn.grid(row=4,column=0,pady=1)


        #  ================right side image===============

        img3=Image.open(r"C:\Users\Pruthviraj Gavali\Desktop\hotel_management_system\hotel_images\slide3.jpg")
        img3=img3.resize((1081,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=190,y=0,width=1081,height=490)

        #  =================down image====================

        img4=Image.open(r"C:\Users\Pruthviraj Gavali\Desktop\hotel_management_system\hotel_images\khana.jpg")
        img4=img4.resize((190,265),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=225,width=190,height=265)

        #img5=Image.open(r"C:\Users\Pruthviraj Gavali\Desktop\hotel_management_system\hotel_images\logohotel.jpg")
        #img5=img5.resize((230,190),Image.ANTIALIAS)
        #self.photoimg5=ImageTk.PhotoImage(img5)

        #lblimg=Label(self.root,image=self.photoimg5,bd=4,relief=RIDGE)
        #lblimg.place(x=0,y=420,width=230,height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)    
        
    

        




if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
