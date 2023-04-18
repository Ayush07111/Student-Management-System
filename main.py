from tkinter import *
from tkinter import ttk
import pymysql

def main():
    a = Tk()
    app=login_page(a)
    a.mainloop()

class login_page:
    def __init__(self,a):
        self.a = a
        self.a.geometry("1400x750")
        self.a.title("STUDENT MANAGEMENT SYSTEM")
        self.title_label = Label(self.a,text = "Student Management System",font=('Helvetica 12 bold italic',36),bg="lightblue",bd=8,relief=SUNKEN
)
        self.title_label.pack(side=TOP,fill=X)
        self.main_frame = Frame(self.a,bg="lightblue",bd=6,relief=RAISED)
        self.main_frame.place(x=300,y=150,width=800,height=450)
        self.login_label = Label(self.main_frame,text="Login",bd=6,relief=GROOVE,anchor=CENTER,font=('Helvetica 12 bold italic',24))
        self.login_label.pack(side=TOP,fill=X)
        
        self.entry_frame = LabelFrame(self.main_frame,text="Enter Details",bd=6,relief=GROOVE,font=('Helvetica 12 italic',20))
        self.entry_frame.pack(fill=BOTH,expand=1)
        
        self.username_label = Label(self.entry_frame,text="Enter Username : ",bg="lightblue",font=('Helvetica 12 italic',16))
        self.username_label.grid(row=0,column=0)

#|||||||||||||||variables::
        username = StringVar()
        password = StringVar()
        self.username_ent = Entry(self.entry_frame,font=('Helvetica 12 italic',16),bd=4,textvariable=username,show="*")
        self.username_ent.grid(row=0,column=1,padx=2,pady=2)

        self.password_label = Label(self.entry_frame,text="Enter Password : ",bg="lightblue",font=('Helvetica 12 italic',16))
        self.password_label.grid(row=1,column=0)
        self.password_ent = Entry(self.entry_frame,font=('Helvetica 12 italic',16),bd=4,textvariable=password,show="*")
        self.password_ent.grid(row=1,column=1,padx=2,pady=2)

#|||||||||||||||functions::
        def check_login():
            if username.get() == "Ayush" and password.get() == "Ayush0111":
                self.enter_button.config(state="normal")
            #else:

        def reset():
            username.set("")
            password.set("")

        def enter_sec():
            self.new_window = Toplevel(self.a)
            self.app = Window2(self.new_window)

        self.button_frame = LabelFrame(self.entry_frame)
        self.button_frame.place(x=20,y=100,width=730,height=55)
        self.login_button = Button(self.button_frame,text="LOGIN",font=('Helvetica 12 italic',14),bd=5,width=15,command=check_login)
        self.login_button.grid(row=0,column=0,padx=31,pady=2)
        self.reset_button = Button(self.button_frame,text="RESET",font=('Helvetica 12 italic',14),bd=5,width=15,command=reset)
        self.reset_button.grid(row=0,column=1,padx=31,pady=2)
        self.enter_button = Button(self.button_frame,text="ENTER",font=('Helvetica 12 italic',14),bd=5,width=15,command=enter_sec)
        self.enter_button.grid(row=0,column=2,padx=31,pady=2)
        self.enter_button.config(state="disabled")

        # self.register_frame = LabelFrame(self.entry_frame)
        # self.register_frame.place(x=20,y=180,width=730,height=110)
        # self.login_label = Label(self.register_frame,text="TO REGISTER",bd=6,relief=GROOVE,anchor=CENTER,font=('Helvetica 12 bold italic',16))
        # self.login_label.pack(side=TOP,fill=X)
        # self.register_button = Button(self.register_frame,text="REGISTER",font=('Helvetica 12 italic',14),bd=5,width=15)
        # self.register_button.grid(row=0,column=0,padx=2,pady=2)

class Window2:
    def __init__(self,a):
        self.a = a
        self.a.geometry("1400x750")
        self.a.title("STUDENT MANAGEMENT SYSTEM")
        self.title_label = Label(self.a,text = "Student Management System",font=('Helvetica 12 bold italic',36),bg="lightblue",bd=8,relief=SUNKEN
)       
        self.title_label.pack(side=TOP,fill=X)
        self.student_frame = LabelFrame(self.a,text="Student Details",font=('Helvetica 12 italic',25),border=12,relief=GROOVE,bg="lightgrey")
        self.student_frame.place(x=40,y=90,width=480,height=620)

        self.data_frame = Frame(self.a,bd=12,bg="lightgrey",relief=GROOVE)
        self.data_frame.place(x=580,y=90,width=790,height=620)
        
        scholarno = StringVar()
        name = StringVar()
        branch = StringVar()
        contact = StringVar()
        email = StringVar()
        fathername = StringVar()
        dob = StringVar()
        gender = StringVar()
        cgpa = StringVar()
        search1 = StringVar()

        self.scholar_no = Label(self.student_frame,text="Scholar No. ",font=('Helvetica 12 italic',18),bg="lightgrey")
        self.scholar_no.grid(row=0,column=0,padx=2,pady=2)
        self.scholar_no_ent = Entry(self.student_frame,bd=7,font=('Helvetica 12 italic',18),textvariable=scholarno)
        self.scholar_no_ent.grid(row=0,column=1,padx=2,pady=2)

        self.name = Label(self.student_frame,text="Name ",font=('Helvetica 12 italic',18),bg="lightgrey")
        self.name.grid(row=1,column=0,padx=2,pady=2)
        self.name_ent = Entry(self.student_frame,bd=7,font=('Helvetica 12 italic',18),textvariable=name)
        self.name_ent.grid(row=1,column=1,padx=2,pady=2)

        self.branch = Label(self.student_frame,text="Branch ",font=('Helvetica 12 italic',18),bg="lightgrey")
        self.branch.grid(row=2,column=0,padx=2,pady=2)
        self.branch_ent = Entry(self.student_frame,bd=7,font=('Helvetica 12 italic',18),textvariable=branch)
        self.branch_ent.grid(row=2,column=1,padx=2,pady=2)

        self.contact = Label(self.student_frame,text="Contact NO. ",font=('Helvetica 12 italic',18),bg="lightgrey")
        self.contact.grid(row=3,column=0,padx=2,pady=2)
        self.contact_ent = Entry(self.student_frame,bd=7,font=('Helvetica 12 italic',18),textvariable=contact)
        self.contact_ent.grid(row=3,column=1,padx=2,pady=2)

        self.email = Label(self.student_frame,text="E-mail ",font=('Helvetica 12 italic',18),bg="lightgrey")
        self.email.grid(row=4,column=0,padx=2,pady=2)
        self.email_ent = Entry(self.student_frame,bd=7,font=('Helvetica 12 italic',18),textvariable=email)
        self.email_ent.grid(row=4,column=1,padx=2,pady=2)

        self.father = Label(self.student_frame,text="Father's name ",font=('Helvetica 12 italic',18),bg="lightgrey")
        self.father.grid(row=5,column=0,padx=2,pady=2)
        self.father_ent = Entry(self.student_frame,bd=7,font=('Helvetica 12 italic',18),textvariable=fathername)
        self.father_ent.grid(row=5,column=1,padx=2,pady=2)

        self.dob = Label(self.student_frame,text="Date of Birth ",font=('Helvetica 12 italic',18),bg="lightgrey")
        self.dob.grid(row=6,column=0,padx=2,pady=2)
        self.dob_ent = Entry(self.student_frame,bd=7,font=('Helvetica 12 italic',18),textvariable=dob)
        self.dob_ent.grid(row=6,column=1,padx=2,pady=2)
        
        self.gender = Label(self.student_frame,text="Gender ",font=('Helvetica 12 italic',18),bg="lightgrey")
        self.gender.grid(row=7,column=0,padx=2,pady=2)
        self.gender_ent = Entry(self.student_frame,bd=7,font=('Helvetica 12 italic',18),textvariable=gender)
        self.gender_ent.grid(row=7,column=1,padx=2,pady=2)

        self.result = Label(self.student_frame,text="CGPA ",font=('Helvetica 12 italic',18),bg="lightgrey")
        self.result.grid(row=8,column=0,padx=2,pady=2)
        self.result_ent = Entry(self.student_frame,bd=7,font=('Helvetica 12 italic',18),textvariable=cgpa)
        self.result_ent.grid(row=8,column=1,padx=2,pady=2)

        def fetch_data():
            conn = pymysql.connect(host="localhost",user="root",password="",database="sms")
            curr = conn.cursor()
            curr.execute("SELECT * FROM data")
            rows = curr.fetchall()
            if len(rows)!=0:
                tree.delete(*tree.get_children())
                for row in rows:
                    tree.insert('',END,values=row)
                conn.commit()
            conn.close()

        def add_func():
            if scholarno.get()=="" or name.get()=="" or branch.get()=="":
                Message.showerror("ERROR....PLEASE ENTER THE REQUIRED FIELDS!!")
            else:
                conn = pymysql.connect(host="localhost",user="root",password="",database="sms")
                curr = conn.cursor()
                curr.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name.get(),scholarno.get(),branch.get(),contact.get(),email.get(),fathername.get(),gender.get(),dob.get(),cgpa.get()))
                conn.commit()
                conn.close()
                fetch_data()

        def get_data(event):
            cursor_row = tree.focus()
            content = tree.item(cursor_row)
            row = content['values']
            name.set(row[0])
            scholarno.set(row[1])
            branch.set(row[2])
            contact.set(row[3])
            email.set(row[4])
            fathername.set(row[5])
            gender.set(row[6])
            dob.set(row[7])
            cgpa.set(row[8])

        def clear():
            name.set("")
            scholarno.set("")
            branch.set("")
            contact.set("")
            email.set("")
            fathername.set("")
            gender.set("")
            dob.set("")
            cgpa.set("")

        def update_func():
            conn = pymysql.connect(host="localhost",user="root",password="",database="sms")
            curr = conn.cursor()
            curr.execute("UPDATE `data` SET `Name`=%s,`Branch`=%s,`ContactNo.`=%s,`E-mail`=%s,`Fathername`=%s,`Gender`=%s,`DOB`=%s,`CGPA`=%s WHERE `ScholarNo.`=%s",(name.get(),branch.get(),contact.get(),email.get(),fathername.get(),gender.get(),dob.get(),cgpa.get(),scholarno.get()))
            conn.commit()
            fetch_data()
            conn.close()
            clear()


        def delete():
            conn = pymysql.connect(host="localhost",user="root",password="",database="sms")
            curr = conn.cursor()
            curr.execute("DELETE FROM `data` WHERE `ScholarNo.`=%s",scholarno.get())
            conn.commit()
            fetch_data()
            conn.close()
            clear()

        def search():
            conn = pymysql.connect(host="localhost",user="root",password="",database="sms")
            curr = conn.cursor()
            curr.execute("SELECT * FROM `data` WHERE Like '%s%" + str(search1.get())+"%'")
            rows = curr.fetchall()
            if len(rows) != 0:
                tree.delete(*tree.get_children())
                for row in rows:
                    tree.insert('',END,values=row)
                conn.commit()
            conn.close()
            clear()

        self.button2_frame= Frame(self.student_frame,bg="lightblue",bd=10,relief=GROOVE)
        self.button2_frame.place(x=20,y=430,width=410,height=135)
        self.add_buttom = Button(self.button2_frame,bg="lightgrey",text="ADD",bd=8,font=('Helvetica 12 italic',14),width=15,command=add_func)
        self.add_buttom.grid(row=0,column=0,padx=3,pady=3)
        self.update_buttom = Button(self.button2_frame,bg="lightgrey",text="UPDATE",bd=8,font=('Helvetica 12 italic',14),width=15,command=update_func)
        self.update_buttom.grid(row=0,column=1,padx=3,pady=3)
        self.delete_buttom = Button(self.button2_frame,bg="lightgrey",text="DELETE",bd=8,font=('Helvetica 12 italic',14),width=15,comm=delete)
        self.delete_buttom.grid(row=1,column=0,padx=3,pady=3)
        self.clear_buttom = Button(self.button2_frame,bg="lightgrey",text="CLEAR",bd=8,font=('Helvetica 12 italic',14),width=15,command=clear)
        self.clear_buttom.grid(row=1,column=1,padx=3,pady=3)

        self.search_frame = Frame(self.data_frame,bd=10,bg="lightgrey",relief=GROOVE)
        self.search_frame.pack(side=TOP,fill=X)
        self.search_label = Label(self.search_frame,text="Search",bg="lightgrey",font=('Helvetica 12 italic',18))
        self.search_label.grid(row=0,column=0,padx=2,pady=2)
        self.search_ent = Entry(self.search_frame,bd=7,font=('Helvetica 12 italic',18),textvariable=search1)
        self.search_ent.grid(row=0,column=1,padx=2,pady=2)
        self.search_buttom = Button(self.search_frame,bg="lightgrey",text="SEARCH",bd=8,font=('Helvetica 12 italic',14),width=14,command=search)
        self.search_buttom.grid(row=0,column=2,padx=5,pady=2)
        self.showall_buttom = Button(self.search_frame,bg="lightgrey",text="SHOW ALL",bd=8,font=('Helvetica 12 italic',14),width=14)
        self.showall_buttom.grid(row=0,column=3,padx=5,pady=2)

        self.main_frame = Frame(self.data_frame,bg="white",bd=10,relief=GROOVE)
        self.main_frame.pack(fil=BOTH,expand=1)
        x_scroll_bar = ttk.Scrollbar(self.main_frame,orient=HORIZONTAL)
        x_scroll_bar.pack(side=BOTTOM,fill=X)
        y_scroll_bar = ttk.Scrollbar(self.main_frame,orient=VERTICAL)
        y_scroll_bar.pack(side=RIGHT,fill=Y)
        tree = ttk.Treeview(self.main_frame,column=("c1", "c2", "c3","c4","c5","c6","c7","c8","c9"), show='headings',xscrollcommand=x_scroll_bar.set,yscrollcommand=y_scroll_bar)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="NAME")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="SCHOLAR NO.")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="BRANCH")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="CONTACT NO.")
        tree.column("# 5", anchor=CENTER)
        tree.heading("# 5", text="E-MAIL")
        tree.column("# 6", anchor=CENTER)
        tree.heading("# 6", text="FATHER'S NAME")
        tree.column("# 7", anchor=CENTER)
        tree.heading("# 7", text="GENDER")
        tree.column("# 8", anchor=CENTER)
        tree.heading("# 8", text="DATE OF BIRTH")
        tree.column("# 9", anchor=CENTER)
        tree.heading("# 9", text="CGPA")

        x_scroll_bar.config(command=tree.xview)
        y_scroll_bar.config(command=tree.yview)
        tree.pack(fill=BOTH,expand=TRUE)
        fetch_data()

        tree.bind("<ButtonRelease-1>",get_data)

        

if __name__ == "__main__":
    main()