import mysql.connector
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from datetime import date,datetime
import random
import tkinter.font as font
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 

#now = datetime.now()
#current_time = now.strftime("%H:%M:%S")

# today=date.today()
# print(today)

mydb=mysql.connector.connect(host="localhost",user='root',passwd='Appaamma@01',database='project')                            #connect with database
my_cursor=mydb.cursor()                                                                                               #create a cursor

root=Tk()
root.title("Book Store Management")                                                                                   #naming the window
root.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
root.geometry("1400x700")                                          #icon to window
#root.state("zoomed")
my_img=ImageTk.PhotoImage(Image.open(r"C:\Users\vinay\OneDrive\Desktop\new project\login.png").resize((1400,700)))                       #image to add in log in and hello name window
# my_img1=ImageTk.PhotoImage(Image.open(r"C:\Users\vinay\OneDrive\Desktop\new project\orderitems.png"))                       #image to add in genre selection window
#my_img2=ImageTk.PhotoImage(Image.open(r"C:\Users\vinay\OneDrive\Desktop\new project\books.jpeg"))                       #image to add in books display window
my_img3=ImageTk.PhotoImage(Image.open(r"C:\Users\vinay\OneDrive\Desktop\new project\orders.png"))
my_img4 = ImageTk.PhotoImage(Image.open(r"C:\Users\vinay\OneDrive\Desktop\new project\hello.png").resize((1600,900)))
my_img9=ImageTk.PhotoImage(Image.open(r"C:\Users\vinay\OneDrive\Desktop\new project\Stacks2.png").resize((1600,900)))
my_img10=ImageTk.PhotoImage(Image.open(r"C:\Users\vinay\OneDrive\Desktop\new project\book2.png").resize((1600,900)))
my_img11=ImageTk.PhotoImage(Image.open(r"C:\Users\vinay\OneDrive\Desktop\new project\orders.png").resize((1600,900)))
my_img12=ImageTk.PhotoImage(Image.open(r"C:\Users\vinay\OneDrive\Desktop\new project\adminlogin.png"))
my_img13=ImageTk.PhotoImage(Image.open(r"C:\Users\vinay\OneDrive\Desktop\new project\contact.png"))
my_img999=ImageTk.PhotoImage(Image.open(r"C:\Users\vinay\OneDrive\Desktop\new project\dashboard.jpg"))
my_img888=ImageTk.PhotoImage(Image.open(r"C:\Users\vinay\OneDrive\Desktop\new project\dashboard2.jpg"))
bg1=ImageTk.PhotoImage(Image.open(r"C:\Users\vinay\OneDrive\Desktop\new project\genre22.png").resize((1600,900)))
myfont = font.Font(family='Helvetica', size=15, weight='bold')
myfont2 = font.Font(family='Helvetica', size=12, weight='bold')
myfont3 = font.Font(family='Helvetica', size=25, weight='bold')

mylabel3=Label(image=my_img)                                                                                          #adding image1 to root
mylabel3.place(x=0,y=0)

#mylabel1=Label(root,text="Log in to your existing account")
#mylabel1.pack(pady=10)
# bg=PhotoImage(file="python/dbms/login.png")
# my_canvas=Canvas(root,width=1400,height=700)
# my_canvas.pack(fill="both",expand=True)
# my_canvas.create_image(0,0,image=bg,anchor='nw')
# my_canvas.create_text(140,295,text="Email-ID",font=('Helvetica',20),fill='white')
# my_canvas.create_text(133,358,text="Password",font=('Helvetica',20),fill='white')

bg=PhotoImage(file=r"C:\Users\vinay\OneDrive\Desktop\new project\hello.png")
#bg1=PhotoImage(file="genre22.png")
bg2=PhotoImage(file=r"C:\Users\vinay\OneDrive\Desktop\new project\book2.png")
bg3=PhotoImage(file=r"C:\Users\vinay\OneDrive\Desktop\new project\orders.png")

l1=Label(root,text="Email-ID",font=myfont,bg='#818181',fg='white')
l1.place(x=120,y=256)
e1=Entry(root,font="Helvetica 14" ,width=30,borderwidth=5)                                                                                #to enter email id to log in
e1.place(x=210,y=250,height=40)
#e1_window=my_canvas.create_window(210,287,anchor="nw",window=e1)
#e1.insert(0,"Email-ID: ")
l2=Label(root,text="Password",font=myfont,bg='#818181',fg='white')
l2.place(x=105,y=323)
e2=Entry(root,font="Helvetica 14",width=30,borderwidth=5, show='*')                                                                                #to enter password to log in
e2.place(x=210,y=317,height=40)
#e2_window=my_canvas.create_window(210,287,anchor="nw",window=e2)

#e2.insert(0,"Password: ",)

def proceed():                                                                                                       #funtion executed after logging in
    current_e=e1.get()  #getting enetered email id
    current_p=e2.get()  #getting entered password
    email=current_e[:]
    password=current_p[:]
    my_q1="select email from customer"
    my_cursor.execute(my_q1)
    x=[]
    for i in my_cursor:
        x.append(i[0])       #creating an array of all customers email
    if(email in x):   #checking if entered email exists in database
        my_q="""select password from customer where email=%s"""
        my_v=email
        my_cursor.execute(my_q,(my_v,))  #query to retreive password where email id matches the one that is entered
        password_true=''
        name=""
        for i in my_cursor:
            password_true=i[0]         #retreiving password from database
        my_q="""select first_name from customer where email=%s"""
        my_v=email
        my_cursor.execute(my_q,(my_v,))   #getting first name to greet after logging in
        for i in my_cursor:
            name=i[0]
        password_e=''
        my_q999="""select SHA(%s)"""
        my_cursor.execute(my_q999,(str(password),))
        for i in my_cursor:
            password_e=i[0]
        if(password_e==password_true):
            def new_order(email,name):
                top=Toplevel()
                top.title("Place Your Order")
                top.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
                top.geometry("1400x700")
                my_canvas=Canvas(top,width=1400,height=700)
                my_canvas.pack(fill="both",expand=True)
                my_canvas.create_image(0,0,image=bg1,anchor='nw')
                #mylabel3=Label(top,image=my_img1).pack(pady=10)
                my_q="""select distinct genre from books"""
                my_cursor.execute(my_q)
                genre=[]
                r=StringVar()
                for i in my_cursor:
                    genre.append((i[0],i[0]))
                r.set(genre[0][0])
                space=0
                for i,j in genre:
                    a=Radiobutton(top,text=i,variable=r,value=j,font=('Helvetica',14),bg='#D3D3D3',fg='black')
                    a_window=my_canvas.create_window(650,200+space,anchor="nw",window=a)
                    space+=50

                def show_books(chosen_genre,customer_email,name):
                    top1=Toplevel()
                    top1.title("Choose Your Books")
                    top1.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
                    top1.geometry("1400x800")
                    my_canvas=Canvas(top1,width=1400,height=800)
                    my_canvas.pack(fill="both",expand=True)
                    my_canvas.create_image(0,0,image=bg2,anchor='nw')
                    #mylabel3=Label(top,image=my_img2).pack(pady=10)

                    x=customer_email
                    my_q="""select b.title,a.name,b.publisher_name,b.ISBN,b.price from books b,author a where b.ISBN=a.book_isbn and b.genre=%s"""
                    my_v=chosen_genre
                    my_cursor.execute(my_q,(my_v,))
                    books=[]
                    r=StringVar()
                    ISBN=[]
                    for i,j,k,isbn,pri in my_cursor:
                        a=i+" By "+j+" from "+k+" publication for ₹"+str(pri)
                        books.append((a,i))
                        ISBN.append((i,isbn))
                    r.set(books[0][1])
                    options=[1,2,3,4,5,6,7,8,9,10]
                    clicked=IntVar()
                    clicked.set(options[0])
                    space1=0
                    for i,j in books:
                        b=Radiobutton(top1,text=i,variable=r,value=j,font=('Helvetica',14),bg='#83837B',fg='black')#.pack(pady=5)
                        b_window=my_canvas.create_window(200,space1+200,anchor="nw",window=b)
                        drop=OptionMenu(top1,clicked,*options)#.config(font=('Helvetica',12),bg='#83837B',fg='white')#.pack()
                        drop.config(bg='#83837B',fg='black')
                        #drop_window=my_canvas.create_window(600,space1+200+30,anchor="nw",window=drop)
                        drop_window=my_canvas.create_window(1200,space1+200,anchor="nw",window=drop)

                        space1+=70

                    def add_cart(book_name,quantity,isbn,email):
                        x="Do you want to add "+book_name+" X"+str(quantity)+" to your cart?"
                        response=messagebox.askyesno("Confirm?",x,parent=top1)
                        if(response==1):
                            a=''
                            for i,j in isbn:
                                if(i==book_name):
                                    a=str(j)
                            my_q="""select count from books_in_cart where book_ISBN=%s and customer_email=%s"""
                            my_cursor.execute(my_q,(a,email))
                            yesno=0
                            for i in my_cursor:
                                yesno=1
                            if(yesno==0):
                                my_q1="""insert into books_in_cart(book_ISBN, count, customer_email) values (%s,%s,%s)"""
                                my_cursor.execute(my_q1,(a,str(quantity),email))
                                mydb.commit()
                            else:
                                my_q2="""select count from books_in_cart where book_ISBN=%s and customer_email=%s"""
                                my_cursor.execute(my_q2,(a,email))
                                flag=0
                                for i in my_cursor:
                                    #print(i[0])
                                    if(int(i[0])+int(quantity)>10):
                                        flag=1
                                if(flag==0):
                                    my_q1="""update books_in_cart set count=count+%s where book_ISBN=%s and customer_email=%s"""
                                    my_cursor.execute(my_q1,(str(quantity),a,email))
                                    mydb.commit()
                                else:
                                    messagebox.showinfo("Error!","You cannot add more than 10 of this to your cart",parent=top1)
                    def cart(email,name):
                        top2=Toplevel()
                        top2.title("Book Store Management")
                        top2.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
                        top2.geometry("800x700")
                        main_frame=Frame(top2)
                        main_frame.pack(fill=BOTH,expand=1)
                        my_canvas=Canvas(main_frame)
                        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
                        my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
                        my_scrollbar.pack(side=RIGHT,fill=Y)
                        my_canvas.configure(yscrollcommand=my_scrollbar.set)
                        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                        second_frame=Frame(my_canvas)
                        my_canvas.create_window((0,0),window=second_frame,anchor="nw")
                        Label(second_frame,text="Your Cart "+name+": ",font=myfont3).pack(pady=10)
                        my_q="""select b.title, c.count, a.name, b.publisher_name, b.price from books b,books_in_cart c, author a where c.customer_email=%s and c.book_ISBN=b.ISBN and b.ISBN=a.book_isbn"""
                        my_cursor.execute(my_q,(email,))
                        disp=[]
                        for i in my_cursor:
                            disp.append(i)

                        def remove_cart(cart_data,email):
                            top3=Toplevel()
                            top3.title("Edit Your Cart")
                            top3.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
                            Label(top3,text="Your Cart "+name+": ",font=myfont3).pack(pady=10)
                            r=StringVar()
                            index=1
                            r.set(cart_data[0][0])
                            options=[0,1,2,3,4,5,6,7,8,9,10]
                            clicked=IntVar()
                            clicked.set(options[0])
                            index=1
                            for t,c,n,p,pr in disp:
                                Radiobutton(top3,text=str(index)+") "+t+" by "+n+" from "+p+" publications X"+str(c),variable=r,value=t,font=('Helvetica',12)).pack(pady=10)
                                drop=OptionMenu(top3,clicked,*options).pack()
                                index+=1
                            def update_cart(title,count,email):
                                x="Do you want to update your cart?"
                                response=messagebox.askyesno("Confirm?",x,parent=top3)
                                if(response==1):
                                    my_q1="""select ISBN from books where title=%s"""
                                    my_cursor.execute(my_q1,(title,))
                                    isbn=0
                                    for i in my_cursor:
                                        isbn=i[0]
                                    if(count>0):
                                        my_q="""update books_in_cart set count=%s where book_ISBN=%s and customer_email=%s"""
                                        my_cursor.execute(my_q,(str(count),str(isbn),str(email)))
                                        mydb.commit()
                                    else:
                                        my_q="""delete from books_in_cart where book_ISBN=%s and customer_email=%s"""
                                        my_cursor.execute(my_q,(str(isbn),str(email)))
                                        mydb.commit()


                            mybutton=Button(top3,text="Update",command=lambda: update_cart(r.get(),clicked.get(),email),font=myfont2).pack(pady=10)

                        amount=0
                        index=1
                        for t,c,n,p,pr in disp:
                            if(c==0):
                                continue
                            Label(second_frame,text=str(index)+") "+t+" by "+n+" from "+p+" publications",font=myfont2).pack(pady=10,anchor='w')
                            Label(second_frame,text="Quantity: "+str(c),font=myfont2).pack(pady=10,anchor='w')
                            amount+=int(c)*int(pr)
                            index+=1
                        Label(second_frame,text="Total amount: "+str(amount),font=myfont2).pack(pady=10,anchor='w')
                        def refresh(top2,email,name):
                            top.destroy()
                            cart(email,name)

                        def buy_cart(disp,email):   #title,count,author name,publisher name,price = disp
                            a=messagebox.askyesno("Proceed?","Do you want to buy all items in your cart?",parent=top2)
                            if(len(disp)==0):
                                return
                            if(a==1):
                                my_q="""select id from orders"""
                                my_cursor.execute(my_q)
                                existing_ids=[]
                                for i in my_cursor:
                                    existing_ids.append(i[0])
                                id=random.randint(1000,9999)
                                while(id in existing_ids):
                                    id=random.randint(1000,9999)
                                my_q="""insert into orders(date,customer_email,id) values (%s,%s,%s)"""
                                today=date.today()
                                d1=today.strftime("%Y-%m-%d")
                                my_cursor.execute(my_q,(str(d1),str(email),str(id)))
                                mydb.commit()
                                isbn=[]
                                counter=0
                                amount=0
                                for i in disp:
                                    my_q7="""select ISBN from books where title=%s"""
                                    my_cursor.execute(my_q7,(i[0],))
                                    for j in my_cursor:
                                        isbn.append(j[0])
                                    my_q5="""insert into order_items(book_isbn,count,order_id) values (%s,%s,%s)"""
                                    my_cursor.execute(my_q5,(str(isbn[counter]),str(i[1]),str(id)))
                                    mydb.commit()
                                    counter+=1
                                    amount+=int(i[4])*int(i[1])

                                my_q1="""select * from customer where email=%s"""
                                my_cursor.execute(my_q1,(str(email),))
                                f_name=''
                                l_name=''
                                address=''
                                p_no=''
                                for i in my_cursor:
                                    f_name=i[1]
                                    l_name=i[2]
                                    address=i[3]
                                my_q102="""select phone_number from phone_number where customer_email=%s"""
                                my_cursor.execute(my_q102,(str(email),))
                                for i in my_cursor:
                                    p_no=i[0]
                                top4=Toplevel()
                                top4.title("Your Order")
                                top4.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
                                top4.geometry("1000x500")
                                main_frame=Frame(top4)
                                main_frame.pack(fill=BOTH,expand=1)
                                my_canvas=Canvas(main_frame)
                                my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
                                my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
                                my_scrollbar.pack(side=RIGHT,fill=Y)
                                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                                second_frame=Frame(my_canvas)
                                my_canvas.create_window((0,0),window=second_frame,anchor="nw")
                                Label(second_frame,text="==============================================================================================================================").pack(pady=10,anchor='w')
                                Label(second_frame,text="Order ID: "+str(id),font=myfont).pack(pady=5,anchor='w')
                                Label(second_frame,text="Order Date: "+str(d1),font=myfont).pack(pady=5,anchor='w')
                                Label(second_frame,text="==============================================================================================================================").pack(pady=10,anchor='w')


                                #Label(top,text="Order Details",font=myfont3).pack(pady=10)
                                #Label(top,text="Order date: "+str(d1),font=myfont2).pack(pady=10,anchor='w')
                                #Label(top,text="Order #: "+str(id),font=myfont2).pack(pady=10,anchor='w')
                                counter1=1
                                for i in disp:
                                    Label(second_frame,text=str(counter1)+") "+str(i[0]),font=myfont2).pack(pady=10,anchor='w')
                                    Label(second_frame,text="Quantity: "+str(i[1]),font=myfont2).pack(pady=10,anchor='w')
                                    counter1+=1
                                Label(second_frame,text="Order Total: "+str(amount),font=myfont2).pack(pady=10,anchor='w')
                                Label(second_frame,text="Name: "+f_name+" "+l_name,font=myfont2).pack(pady=10,anchor='w')
                                Label(second_frame,text="Address: "+str(address),font=myfont2).pack(pady=10,anchor='w')
                                Label(second_frame,text="Email Address: "+str(email),font=myfont2).pack(pady=10,anchor='w')
                                Label(second_frame,text="Contact Information: "+str(p_no),font=myfont2).pack(pady=10,anchor='w')
                                my_q103="""delete from books_in_cart where customer_email=%s"""
                                my_cursor.execute(my_q103,(str(email),))
                                mydb.commit()


                        mybutton3=Button(second_frame,text="Buy all items in cart",command=lambda: buy_cart(disp,email),font=myfont2).pack(pady=10)
                        mybutton=Button(second_frame,text="Update Items from cart",command=lambda: remove_cart(disp,email),font=myfont2).pack(pady=10)
                        mybutton2=Button(second_frame,text="Refresh Cart",command=lambda:refresh(top2,email,name),font=myfont2).pack(pady=10)

                    def buy(book_name,quantity,isbn,email):
                        a=messagebox.askyesno("Proceed?","Do you want to buy "+str(book_name)+"	X "+str(quantity),parent=top1)
                        if(a==1):
                            my_q="""select id from orders"""
                            my_cursor.execute(my_q)
                            existing_ids=[]
                            for i in my_cursor:
                                existing_ids.append(i[0])
                            id=random.randint(1000,9999)
                            while(id in existing_ids):
                                id=random.randint(1000,9999)
                            my_q="""insert into orders(date,customer_email,id) values (%s,%s,%s)"""
                            today=date.today()
                            d1=today.strftime("%Y-%m-%d")
                            my_cursor.execute(my_q,(str(d1),str(email),str(id)))
                            mydb.commit()
                            isbn1=''
                            for i in isbn:
                                if(i[0]==book_name):
                                    isbn1=str(i[1])
                            my_q4="""insert into order_items(book_isbn,count,order_id) values (%s,%s,%s)"""
                            my_cursor.execute(my_q4,(str(isbn1),str(quantity),str(id)))
                            mydb.commit()
                            my_q1="""select * from customer where email=%s"""
                            my_cursor.execute(my_q1,(str(email),))
                            f_name=''
                            l_name=''
                            address=''
                            p_no=''
                            for i in my_cursor:
                                f_name=i[1]
                                l_name=i[2]
                                address=i[3]
                            my_q10="""select phone_number from phone_number where customer_email=%s"""
                            my_cursor.execute(my_q10,(str(email),))
                            for i in my_cursor:
                                p_no=i[0]
                            top5=Toplevel()
                            top5.title("Your Order")
                            top5.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
                            top5.geometry("1000x500")
                            Label(top5,text="==============================================================================================================================").pack(pady=10,anchor='w')
                            Label(top5,text="Order ID: "+str(id),font=myfont).pack(pady=5,anchor='w')
                            Label(top5,text="Order Date: "+str(d1),font=myfont).pack(pady=5,anchor='w')
                            Label(top5,text="==============================================================================================================================").pack(pady=10,anchor='w')
                            #Label(top,text="Order Details",font=myfont3).pack(pady=10)
                            my_q2="""select price from books where title=%s"""
                            my_v=str(book_name)
                            my_cursor.execute(my_q2,(my_v,))
                            price=0
                            for i in my_cursor:
                                price=i[0]
                            #Label(top,text="Order date: "+str(d1),font=myfont).pack(pady=10,anchor='w')
                            #Label(top,text="Order #: "+str(id),font=myfont).pack(pady=10,anchor='w')
                            Label(top5,text="Book Title: "+str(book_name),font=myfont).pack(pady=10,anchor='w')
                            Label(top5,text="Quantity: "+str(quantity),font=myfont).pack(pady=10,anchor='w')
                            Label(top5,text="Order Total: "+str(int(quantity)*int(price)),font=myfont).pack(pady=10,anchor='w')
                            Label(top5,text="Name: "+f_name+" "+l_name,font=myfont).pack(pady=10,anchor='w')
                            Label(top5,text="Address: "+str(address),font=myfont).pack(pady=10,anchor='w')
                            Label(top5,text="Email Address: "+str(email),font=myfont).pack(pady=10,anchor='w')
                            Label(top5,text="Contact Information: "+str(p_no),font=myfont).pack(pady=10,anchor='w')




                    mybutton3=Button(top1,text="    Buy    ",command=lambda: buy(r.get(),clicked.get(),ISBN,x),font=('Helvetica',14),height=1,width=20,bg='#83837B',fg='black')#.pack(pady=10)
                    mybutton=Button(top1,text="Add to Cart",command=lambda: add_cart(r.get(),clicked.get(),ISBN,x),font=('Helvetica',14),height=1,width=20,bg='#83837B',fg='black')#.pack(pady=10)
                    mybutton1=Button(top1,text="View your cart",command=lambda: cart(x,name),font=('Helvetica',14),height=1,width=20,bg='#83837B',fg='black')#.pack(pady=10)
                    mybutton3_window=my_canvas.create_window(560,620,anchor="nw",window=mybutton3)
                    mybutton_window=my_canvas.create_window(560,670,anchor="nw",window=mybutton)
                    mybutton1_window=my_canvas.create_window(560,720,anchor="nw",window=mybutton1)

                mybutton=Button(top,text="Show books",command=lambda: show_books(r.get(),email,name),font=('Helvetica',15),height=2,width=20,bg='#FFFFFF',fg='black')
                mybutton_window=my_canvas.create_window(600,550,anchor="nw",window=mybutton)

            def old_orders(email,name):
                top=Toplevel()
                top.title("Your Orders")
                top.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
                top.geometry("600x700")
                main_frame=Frame(top)
                main_frame.pack(fill=BOTH,expand=1)
                my_canvas=Canvas(main_frame)
                my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
                my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
                my_scrollbar.pack(side=RIGHT,fill=Y)
                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                second_frame=Frame(my_canvas)
                my_canvas.create_window((0,0),window=second_frame,anchor="nw")
                Label(second_frame,image=my_img3).pack(pady=10)
                Label(second_frame,text="Your history with us "+name,font=myfont).pack(pady=10)
                # my_canvas=Canvas(top,width=1400,height=700)
                # my_canvas.pack(fill="both",expand=True)
                # my_canvas.create_image(0,0,image=bg3,anchor='nw')
                # Label(top,image=my_img3).pack(pady=10)
                # Label(top,text="Your history with us "+name).pack(pady=10)
                my_q="""select id,date from orders where customer_email=%s"""
                my_v=email
                my_cursor.execute(my_q,(my_v,))
                r=IntVar()
                orders=[]
                format="%d/%m/%Y"
                for i in my_cursor:
                    orders.append((i[0],i[1].strftime(format)))
                r.set(orders[0][0])
                #space2=0
                date={}
                for i,j in orders:
                    Radiobutton(second_frame,text="Order with Order ID: "+str(i)+" dated: "+j,variable=r,value=i,font=('Helvetica',12),bg="#A9BCA6",fg="black").pack(pady=10)
                    date[str(i)]=str(j)
                    #a_window=my_canvas.create_window(500,200+space,anchor="nw",window=a)
                    #space2+=10

                def show_items(id,name,date):
                    top1=Toplevel()
                    top1.title("Your Orders")
                    top1.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
                    top1.geometry("1000x500")
                    main_frame=Frame(top1)
                    main_frame.pack(fill=BOTH,expand=1)
                    my_canvas=Canvas(main_frame)
                    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
                    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
                    my_scrollbar.pack(side=RIGHT,fill=Y)
                    my_canvas.configure(yscrollcommand=my_scrollbar.set)
                    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                    second_frame=Frame(my_canvas)
                    my_canvas.create_window((0,0),window=second_frame,anchor="nw")
                    #Label(top,image=my_img1).pack(pady=10)
                    #Label(top,text="Your order with order ID: "+str(id)+" had the following items",font=myfont3).pack(pady=10)
                    Label(second_frame,text="==============================================================================================================================").pack(pady=10,anchor='w')
                    Label(second_frame,text="Order ID: "+str(id),font=myfont).pack(pady=5,anchor='w')
                    Label(second_frame,text="Order Date: "+date[str(id)],font=myfont).pack(pady=5,anchor='w')
                    Label(second_frame,text="==============================================================================================================================").pack(pady=10,anchor='w')
                    my_q="""select o.count,b.title,b.price,a.name,b.publisher_name from order_items o,books b,author a where o.order_id=%s and o.book_isbn=b.ISBN and b.ISBN=a.book_isbn"""
                    my_v=str(id)
                    my_cursor.execute(my_q,(my_v,))
                    items=[]
                    for i in my_cursor:
                        items.append(i)
                    amount=0
                    i=1
                    #Label(second_frame,text="BOOK NAME",font=myfont).place(x=0,y=150)
                    #Label(second_frame,text="QUANTITY",font=myfont).place(x=700,y=150)
                    for a,b,c,d,e in items:
                        Label(second_frame,text=str(i)+") "+b+" by "+d+" from "+e+" publication",font=myfont).pack(pady=4,anchor='w')
                        Label(second_frame,text="Quantity: "+str(a),font=myfont).pack(pady=10,anchor='w')
                        amount+=c
                        i+=1
                    Label(second_frame,text="Total Amount paid= "+str(amount),font=myfont).pack(pady=10,anchor=W)

                mybutton=Button(second_frame,text="View items in this order",command=lambda: show_items(r.get(),name,date),font=myfont2,height=2,width=25,bg="#A9BCA6",fg="black").pack(pady=10)

            def cart(email,name):
                top=Toplevel()
                top.title("Book Store Management")
                top.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
                top.geometry("800x700")
                main_frame=Frame(top)
                main_frame.pack(fill=BOTH,expand=1)
                my_canvas=Canvas(main_frame)
                my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
                my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
                my_scrollbar.pack(side=RIGHT,fill=Y)
                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                second_frame=Frame(my_canvas)
                my_canvas.create_window((0,0),window=second_frame,anchor="nw")
                Label(second_frame,text="Your Cart "+name+": ", font = myfont3).pack(pady=10)
                my_q="""select b.title, c.count, a.name, b.publisher_name, b.price from books b,books_in_cart c, author a where c.customer_email=%s and c.book_ISBN=b.ISBN and b.ISBN=a.book_isbn"""
                my_cursor.execute(my_q,(email,))
                disp=[]
                for i in my_cursor:
                    disp.append(i)

                def remove_cart(cart_data,email):
                    top1=Toplevel()
                    top1.title("Edit Your Cart")
                    top1.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
                    Label(top1,text="Your Cart "+name+": ",font=myfont2).pack(pady=10)
                    r=StringVar()
                    index=1
                    r.set(cart_data[0][0])
                    options=[0,1,2,3,4,5,6,7,8,9,10]
                    clicked=IntVar()
                    clicked.set(options[0])
                    index=1
                    for t,c,n,p,pr in disp:
                        Radiobutton(top1,text=str(index)+") "+t+" by "+n+" from "+p+" publications X"+str(c),variable=r,value=t,font=('Helvetica',12)).pack(pady=10)
                        drop=OptionMenu(top1,clicked,*options).pack()
                        index+=1
                    def update_cart(title,count,email):
                        x="Do you want to update your cart?"
                        response=messagebox.askyesno("Confirm?",x,parent=top1)
                        if(response==1):
                            my_q1="""select ISBN from books where title=%s"""
                            my_cursor.execute(my_q1,(title,))
                            isbn=0
                            for i in my_cursor:
                                isbn=i[0]
                            if(count>0):
                                my_q="""update books_in_cart set count=%s where book_ISBN=%s and customer_email=%s"""
                                my_cursor.execute(my_q,(str(count),str(isbn),str(email)))
                                mydb.commit()
                            else:
                                my_q="""delete from books_in_cart where book_ISBN=%s and customer_email=%s"""
                                my_cursor.execute(my_q,(str(isbn),str(email)))
                                mydb.commit()


                    mybutton=Button(top1,text="Update",command=lambda: update_cart(r.get(),clicked.get(),email),font=myfont2).pack(pady=10)

                amount=0
                index=1
                for t,c,n,p,pr in disp:
                    if(c==0):
                        continue
                    Label(second_frame,text=str(index)+") "+t+" by "+n+" from "+p+" publications",font=myfont2).pack(pady=10,anchor='w')
                    Label(second_frame,text="Quantity: "+str(c),font=myfont2).pack(pady=10,anchor='w')
                    amount+=int(c)*int(pr)
                    index+=1
                Label(second_frame,text="Total amount: "+str(amount),font=myfont2).pack(pady=10,anchor='w')
                def refresh(top,email,name):
                    top.destroy()
                    cart(email,name)

                def buy_cart(disp,email):   #title,count,author name,publisher name,price = disp
                    a=messagebox.askyesno("Proceed?","Do you want to buy all items in your cart?",parent=top)
                    if(len(disp)==0):
                        return
                    if(a==1):
                        my_q="""select id from orders"""
                        my_cursor.execute(my_q)
                        existing_ids=[]
                        for i in my_cursor:
                            existing_ids.append(i[0])
                        id=random.randint(1000,9999)
                        while(id in existing_ids):
                            id=random.randint(1000,9999)
                        my_q="""insert into orders(date,customer_email,id) values (%s,%s,%s)"""
                        today=date.today()
                        d1=today.strftime("%Y-%m-%d")
                        my_cursor.execute(my_q,(str(d1),str(email),str(id)))
                        mydb.commit()
                        isbn=[]
                        counter=0
                        amount=0
                        for i in disp:
                            my_q7="""select ISBN from books where title=%s"""
                            my_cursor.execute(my_q7,(i[0],))
                            for j in my_cursor:
                                isbn.append(j[0])
                            my_q5="""insert into order_items(book_isbn,count,order_id) values (%s,%s,%s)"""
                            my_cursor.execute(my_q5,(str(isbn[counter]),str(i[1]),str(id)))
                            mydb.commit()
                            counter+=1
                            amount+=int(i[4])*int(i[1])

                        my_q1="""select * from customer where email=%s"""
                        my_cursor.execute(my_q1,(str(email),))
                        f_name=''
                        l_name=''
                        address=''
                        p_no=''
                        for i in my_cursor:
                            f_name=i[1]
                            l_name=i[2]
                            address=i[3]
                        my_q101="""select phone_number from phone_number where customer_email=%s"""
                        my_cursor.execute(my_q101,(str(email),))
                        for i in my_cursor:
                            p_no=i[0]
                        top3=Toplevel()
                        top3.title("Your Order")
                        top3.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
                        top3.geometry("1000x500")
                        main_frame=Frame(top3)
                        main_frame.pack(fill=BOTH,expand=1)
                        my_canvas=Canvas(main_frame)
                        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
                        my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
                        my_scrollbar.pack(side=RIGHT,fill=Y)
                        my_canvas.configure(yscrollcommand=my_scrollbar.set)
                        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                        second_frame=Frame(my_canvas)
                        my_canvas.create_window((0,0),window=second_frame,anchor="nw")
                        Label(second_frame,text="==============================================================================================================================").pack(pady=10,anchor='w')
                        Label(second_frame,text="Order ID: "+str(id),font=myfont).pack(pady=5,anchor='w')
                        Label(second_frame,text="Order Date: "+str(d1),font=myfont).pack(pady=5,anchor='w')
                        Label(second_frame,text="==============================================================================================================================").pack(pady=10,anchor='w')

                        #Label(top,text="==============================================").pack(pady=10)
                        #Label(top,text="Order Details",font=myfont3).pack(pady=10)
                        # Label(top,text="Order date: "+str(d1),font=myfont).pack(pady=10,anchor='w')
                        # Label(top,text="Order #: "+str(id),font=myfont).pack(pady=10,anchor='w')
                        # Label(top,text="==============================================").pack(pady=10)
                        # Label(top,text="\tBook Title\t\t\t\t\t\tQuantity").pack(pady=10)
                        counter1=1
                        for i in disp:
                            Label(second_frame,text=str(counter1)+") "+str(i[0]),font=myfont).pack(pady=10,anchor='w')
                            Label(second_frame,text="Quantity: "+str(i[1]),font=myfont).pack(pady=10,anchor='w')
                            counter1+=1
                        Label(second_frame,text="Order Total: "+str(amount),font=myfont).pack(pady=10,anchor='w')
                        Label(second_frame,text="Name: "+f_name+" "+l_name,font=myfont).pack(pady=10,anchor='w')
                        Label(second_frame,text="Address: "+str(address),font=myfont).pack(pady=10,anchor='w')
                        Label(second_frame,text="Email Address: "+str(email),font=myfont).pack(pady=10,anchor='w')
                        Label(second_frame,text="Contact Information: "+str(p_no),font=myfont).pack(pady=10,anchor='w')
                        my_q103="""delete from books_in_cart where customer_email=%s"""
                        my_cursor.execute(my_q103,(str(email),))
                        mydb.commit()


                mybutton3=Button(second_frame,text="Buy all items in cart",command=lambda: buy_cart(disp,email), font = myfont2).pack(pady=10)
                mybutton=Button(second_frame,text="Update Items from cart",command=lambda: remove_cart(disp,email), font = myfont2).pack(pady=10)
                mybutton2=Button(second_frame,text="Refresh Cart",command=lambda:refresh(top,email,name), font = myfont2).pack(pady=10)

            top9=Toplevel()
            top9.title("Book Store Management")
            top9.geometry("1400x700")
            #top.state("zoomed")
            top9.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
            # Label(top,image=my_img4).place(x=0,y=0)
            # Label(top,text="Hello "+name).place(x=780,y=200)

            my_canvas=Canvas(top9,width=1400,height=700)
            my_canvas.pack(fill="both",expand=True)
            my_canvas.create_image(0,0,image=bg,anchor='nw')
            button1=Button(top9,text="Place New Order",command=lambda: new_order(email,name),font=('Helvetica',12),height=2,width = 20,fg='#804000',bg='#EFE4B0')
            button2=Button(top9,text="Review Old Orders",command=lambda: old_orders(email,name),font=('Helvetica',12),height=2,width = 20,fg='#804000',bg='#EFE4B0')
            button3=Button(top9,text="View your cart",command=lambda: cart(email,name),font=('Helvetica',12),height=2,width = 20,fg='#804000',bg='#EFE4B0')
            my_canvas.create_text(700,150,text="Hello "+name+"!",font=('Helvetica',50),fill='#EFE4B0')
            button1_window=my_canvas.create_window(600,287,anchor="nw",window=button1)
            button2_window=my_canvas.create_window(600,387,anchor="nw",window=button2)
            button3_window=my_canvas.create_window(600,487,anchor="nw",window=button3)


        else:
            messagebox.showinfo("Error","Entered combination doesnt exist! Please try again or Sign Up")
    else:
        messagebox.showinfo("Error","Entered combination doesnt exist! Please try again or Sign Up")


def sign_up():
    top=Toplevel()
    top.title("Book Store Management")
    top.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
    Label(top,image=my_img9).pack(pady=5)
    #Label(top,text="Welcome! Please fill in your details").place(x=650,y=50)

    l11=Label(top,text="Enter your First Name",font=myfont)
    l11.place(x=780,y=206)
    e1=Entry(top,width=50,borderwidth=5)
    e1.place(x=1000,y=200,height=40)
    #e1.insert(0,"Enter your First Name: ")
    l12=Label(top,text="Enter your Last Name",font=myfont)
    l12.place(x=780,y=256)
    e2=Entry(top,width=50,borderwidth=5)
    e2.place(x=1000,y=250,height=40)
    #e2.insert(0,"Enter your Last Name: ")
    l13=Label(top,text="Enter your Email-ID",font=myfont)
    l13.place(x=800,y=306)
    e3=Entry(top,width=50,borderwidth=5)
    e3.place(x=1000,y=300,height=40)
    #e3.insert(0,"Enter your Email-ID: ")
    l14=Label(top,text="Enter your Phone Number",font=myfont)
    l14.place(x=735,y=356)
    e4=Entry(top,width=50,borderwidth=5)
    e4.place(x=1000,y=350,height=40)
    #e4.insert(0,"Enter your Phone Number: ")
    l14=Label(top,text="Enter your Address",font=myfont)
    l14.place(x=800,y=406)
    e5=Entry(top,width=50,borderwidth=5)
    e5.place(x=1000,y=400,height=40)
    #e5.insert(0,"Enter the locality where you stay: ")
    l14=Label(top,text="Set a password",font=myfont)
    l14.place(x=835,y=456)
    e6=Entry(top,width=50,borderwidth=5,show="*")
    e6.place(x=1000,y=450,height=40)
    #e6.insert(0,"Set a password: ")

    def sign_up():
        f_name=e1.get()[:].strip()
        l_name=e2.get()[:].strip()
        e_id=e3.get()[:].strip()
        p_no=e4.get()[:].strip()
        area=e5.get()[:].strip()
        pwd=e6.get()[:].strip()

        if(len(p_no)!=10 or (not p_no.isdigit())):
            messagebox.showinfo("Error","Enter a valid phone number!",parent=top)
        else:
            my_q="""insert into customer(email,first_name,last_name,address,password) values (%s,%s,%s,%s,%s)"""
            my_q111111="""select SHA(%s)"""
            my_cursor.execute(my_q111111,(str(pwd),))
            new_pwd=''
            for i in my_cursor:
                new_pwd=i[0]
            my_cursor.execute(my_q,(e_id,f_name,l_name,area,new_pwd))
            mydb.commit()
            my_q1="""insert into phone_number(phone_number,customer_email) values(%s,%s)"""
            my_cursor.execute(my_q1,(p_no,e_id))
            mydb.commit()
            messagebox.showinfo("","Sign Up complete! Log in to continue",parent=top)
            top.destroy()

    button1=Button(top,text="Submit",command=sign_up,font=myfont2,height=2,width=20).place(x=1050,y=530)


def admin():
    top=Toplevel()
    top.title("Book Store Management")
    top.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
    top.geometry("1280x720")
    mylabel=Label(top,image=my_img12)
    mylabel.place(x=0,y=0)
    l1=Label(top,text="USERNAME",bg="#578199",fg="#FFFFFF",font="Helvetica 18 bold")
    l1.place(x=230,y=310)
    e1=Entry(top,bg="#0e1c21",fg="#FFFFFF",width=70,font=myfont,borderwidth=2,bd=2)
    e1.config(insertbackground="#00bbe0")
    e1.place(x=231,y=350)  
    l2=Label(top,text="PASSWORD",bg="#578199",fg="#FFFFFF",font="Helvetica 18 bold")
    l2.place(x=230,y=440)
    e2=Entry(top,bg="#0e1c21",fg="#FFFFFF",width=70,font=myfont,borderwidth=2,bd=2,show="*")
    e2.config(insertbackground="#00bbe0")
    e2.place(x=231,y=480)

    def admin_afterlogin(email):
        top1=Toplevel()
        top1.title("Book Store Management")
        top1.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
        top1.geometry("1000x700")
        frame1=LabelFrame(top1,bg="grey",height=700,width=200,bd=1)
        in_frame1=Label(frame1,image=my_img999)
        in_frame1.pack()
        frame2=LabelFrame(top1,height=700,width=800,bd=1,bg="grey")
        frame1.place(x=0,y=0)
        frame2.place(x=200,y=0)
        in_frame2=Label(frame2,image=my_img888)
        in_frame2.pack()
        l1=Label(frame1,image=my_img13,bg="#1687a9")
        l1.place(x=50,y=30)
        my_q="""select first_name from customer where email=%s"""
        my_cursor.execute(my_q,(email,))
        name=""
        for i in my_cursor:
            name=i[0]
            l2=Label(frame1,text="Welcome "+name+"!",bg="#1687a9",fg="white",font="Helvetica 12 bold")
            l2.place(x=28,y=160)


        fig = Figure(figsize = (5, 5), dpi = 100)
        x=[]
        y=[]
        my_q2=""" select b.genre, sum(o.count) from order_items o, books b where o.book_isbn=b.ISBN group by b.genre"""
        my_cursor.execute(my_q2)
        for i,j in my_cursor:
            x.append(i)
            y.append(j)
        plot1 = fig.add_subplot(111)
        plot1.bar(x,y,color='#e1aec9')
        canvas = FigureCanvasTkAgg(fig, master = frame2)
        canvas.draw() 
        canvas.get_tk_widget().place(x=150,y=170)
        frame3=LabelFrame(frame2,bg="#1687a9",height=80,width=150,bd=5)
        frame3.place(x=50,y=50)
        frame4=LabelFrame(frame2,bg="#1687a9",height=80,width=150,bd=5)
        frame4.place(x=300,y=50)
        frame5=LabelFrame(frame2,bg="#1687a9",height=80,width=150,bd=5)
        frame5.place(x=550,y=50)
        l3=Label(frame3,text="Sales",bg="#1687a9",fg="white",font="Helvetica 12")
        l3.place(x=40,y=40)
        l4=Label(frame4,text="Products sold",bg="#1687a9",fg="white",font="Helvetica 12")
        l4.place(x=12,y=40)
        l5=Label(frame5,text="Books in stock",bg="#1687a9",fg="white",font="Helvetica 12")
        l5.place(x=12,y=40)
        my_q3="""select count(*) from orders"""
        my_cursor.execute(my_q3)
        c_orders=''
        for i in my_cursor:
            c_orders=i
        my_q4="""select sum(count) from order_items"""
        my_cursor.execute(my_q4)
        c_sold=''
        for i in my_cursor:
            c_sold=i
        my_q5="""select count(*) from books"""
        my_cursor.execute(my_q5)
        c_books=''
        for i in my_cursor:
            c_books=i
        l31=Label(frame3,text=c_orders,bg="#1687a9",fg="white",font="Helvetica 18 bold")
        l31.place(x=50,y=0)
        l41=Label(frame4,text=c_sold,bg="#1687a9",fg="white",font="Helvetica 18 bold")
        l41.place(x=45,y=0)
        l51=Label(frame5,text=c_books,bg="#1687a9",fg="white",font="Helvetica 18 bold")
        l51.place(x=50,y=0)


        def add_books():
            top2=Toplevel()
            top2.title("Book Store Management")
            top2.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
            top2.geometry("1100x500")
            main_frame=Frame(top2)
            main_frame.pack(fill=BOTH,expand=1)
            my_canvas=Canvas(main_frame)
            my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
            my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT,fill=Y)
            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
            second_frame=Frame(my_canvas)
            my_canvas.create_window((0,0),window=second_frame,anchor="nw")
            my_q="""select * from books"""
            my_cursor.execute(my_q)
            r=0
            c=0
            for i in my_cursor:
                for j in range(len(i)):
                    if(j==1 or j==4 or j==0):
                        e=Entry(second_frame,width=30,fg="blue",font="Helvetica 13")
                    else:
                        e=Entry(second_frame,width=15,fg="blue",font="Helvetica 13")
                    e.grid(row=r,column=c)
                    if(c==0):
                        e.insert(END, str(r+1)+")   "+str(i[j]))
                    else:
                        e.insert(END,i[j])
                    c+=1
                r+=1
                c=0
            l1=Label(second_frame,text="Enter Book Title ",font="Helvetica 13")
            l1.grid(row=r+1,column=0,pady=10)
            e1=Entry(second_frame,width=30,fg="blue",font="Helvetica 13")
            e1.grid(row=r+1,column=1,pady=10)
            l2=Label(second_frame,text="Enter Book ISBN ",font="Helvetica 13")
            l2.grid(row=r+2,column=0,pady=10)
            e2=Entry(second_frame,width=30,fg="blue",font="Helvetica 13")
            e2.grid(row=r+2,column=1,pady=10)
            l3=Label(second_frame,text="Enter Book Price ",font="Helvetica 13")
            l3.grid(row=r+3,column=0,pady=10)
            e3=Entry(second_frame,width=30,fg="blue",font="Helvetica 13")
            e3.grid(row=r+3,column=1,pady=10)
            l4=Label(second_frame,text="Choose Genre ",font="Helvetica 13")
            l4.grid(row=r+4,column=0,pady=10)
            l5=Label(second_frame,text="Choose Author ",font="Helvetica 13")
            l5.grid(row=r+5,column=0,pady=10)
            l6=Label(second_frame,text="Choose Publisher ",font="Helvetica 13")
            l6.grid(row=r+6,column=0,pady=10)
            my_q1="""select distinct genre from books"""
            my_q2="""select distinct publisher_name from books"""
            my_q3="""select distinct name from author"""
            my_cursor.execute(my_q1)
            genre=[]
            for i in my_cursor:
                genre.append(i[0])
            my_cursor.execute(my_q2)
            pub=[]
            for i in my_cursor:
                pub.append(i[0])
            my_cursor.execute(my_q3)
            aut=[]
            for i in my_cursor:
                aut.append(i[0])
            clicked1=StringVar()
            clicked1.set(genre[0])
            clicked2=StringVar()
            clicked2.set(pub[0])
            clicked3=StringVar()
            clicked3.set(aut[0])
            drop1=OptionMenu(second_frame,clicked1,*genre)
            drop1.config(font="Helvetica 12")
            drop2=OptionMenu(second_frame,clicked2,*pub)
            drop2.config(font="Helvetica 12")
            drop3=OptionMenu(second_frame,clicked3,*aut)
            drop3.config(font="Helvetica 12")
            drop1.grid(row=r+4,column=1,pady=10)
            drop3.grid(row=r+5,column=1,pady=10)
            drop2.grid(row=r+6,column=1,pady=10)

            def add(title,isbn,price,genre,publisher,author):
                a=messagebox.askyesno("Continue?","Do you want to add this book to the database?",parent=top2)
                if(a==True):
                    if(int(isbn)<99 or int(isbn)>999):
                        messagebox.showinfo("Error!","Invalid ISBN!",parent=top2)
                    else:    
                        my_q4="""insert into books(ISBN,title,price,genre,publisher_name) values(%s,%s,%s,%s,%s)"""
                        my_cursor.execute(my_q4,(str(isbn),str(title),str(price),str(genre),str(publisher),))
                        mydb.commit()
                        my_q5="""select ID from author where name=%s"""
                        my_cursor.execute(my_q5,(str(author),))
                        id=""
                        for i in my_cursor:
                            id=str(i[0])
                        my_q6="""insert into author(ID,name,book_isbn) values(%s,%s,%s)"""
                        my_cursor.execute(my_q6,(str(id),str(name),str(isbn),))
                        mydb.commit()
                        top2.destroy()
                        add_books()

            button1=Button(second_frame,text="Add Book",fg="black",font="Helvetica 12 bold",bd=7,command=lambda: add(e1.get(),e2.get(),e3.get(),clicked1.get(),clicked2.get(),clicked3.get()))
            button1.grid(row=r+7,column=1,pady=10)

        def update_data():
            top3=Toplevel()
            top3.title("Book Store Management")
            top3.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
            top3.geometry("1100x500")
            main_frame=Frame(top3)
            main_frame.pack(fill=BOTH,expand=1)
            my_canvas=Canvas(main_frame)
            my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
            my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT,fill=Y)
            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
            second_frame=Frame(my_canvas)
            my_canvas.create_window((0,0),window=second_frame,anchor="nw")
            my_q="""select title,price,genre from books"""
            my_cursor.execute(my_q)
            l=[]
            r=0
            c=0
            for i in my_cursor: 
                l.append(i[0])
                for j in range(len(i)):
                    e = Entry(second_frame, width=50, fg='blue',font="Helvetica 13") 
                    e.grid(row=r,column=c)
                    if(c==0):
                        e.insert(END, str(r+1)+") "+i[j])
                    else: 
                        e.insert(END, i[j])
                    c+=1
                r+=1
                c=0
            l1=Label(second_frame,text="Enter row number ",font="Helvetica 13")
            l1.grid(row=r,column=0,pady=10)
            e1=Entry(second_frame,width=30,fg="blue",font="Helvetica 13")
            e1.grid(row=r,column=1,pady=10)

            l2=Label(second_frame,text="Enter updated price",font="Helvetica 13")
            l2.grid(row=r+1,column=0,pady=10)
            e2=Entry(second_frame,width=30,fg="blue",font="Helvetica 13")
            e2.grid(row=r+1,column=1,pady=10)

            def update(l,row,price):
                my_q="""select price from books where title=%s"""
                my_cursor.execute(my_q,(str(l[int(row)-1]),))
                price_og=""
                for i in my_cursor:
                    price_og=str(i[0])

                a=messagebox.askyesno("Continue?", "Do you want to update price of "+str(l[int(row)-1])+" from ₹"+str(price_og)+" to ₹"+str(price)+"?",parent=top3) 
                if(a==True):
                    my_q2="""update books set price=%s where title=%s"""
                    my_cursor.execute(my_q2,(str(price),str(l[int(row)-1]),))
                    mydb.commit()
                    top3.destroy()
                    update_data()
            button=Button(second_frame,text="Update Price",fg="black",font="Helvetica 12 bold",command=lambda: update(l,e1.get(),e2.get()),bd=7)
            button.grid(row=r+2,column=1,pady=10)

        def view_orders():
            top4=Toplevel()
            top4.title("Your Orders")
            top4.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
            top4.geometry("700x700")
            main_frame=Frame(top4)
            main_frame.pack(fill=BOTH,expand=1)
            my_canvas=Canvas(main_frame)
            my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
            my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT,fill=Y)
            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
            second_frame=Frame(my_canvas)
            my_canvas.create_window((0,0),window=second_frame,anchor="nw")
            my_q="""select id,date,customer_email from orders"""
            my_cursor.execute(my_q)
            oid=[]
            date=[]
            email=[]
            full=[]
            r=IntVar()
            for i,j,k in my_cursor:
                oid.append(i)
                date.append(str(j))
                email.append(k)
                full.append((i,str(j),k))


            r.set(full[0][0])
            for i,j,k in full:
                Radiobutton(second_frame,text="Order with Order ID: "+str(i)+" dated: "+str(j)+" with customer email: "+str(k),variable=r,value=i,font=('Helvetica',12),bg="white",fg="black").pack(pady=10)
            

            def show(id):
                top1=Toplevel()
                top1.title("Your Orders")
                top1.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
                top1.geometry("1000x500")
                main_frame=Frame(top1)
                main_frame.pack(fill=BOTH,expand=1)
                my_canvas=Canvas(main_frame)
                my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
                my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
                my_scrollbar.pack(side=RIGHT,fill=Y)
                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                second_frame=Frame(my_canvas)
                my_canvas.create_window((0,0),window=second_frame,anchor="nw")
                my_q101="""select date, customer_email from orders where id=%s"""
                my_cursor.execute(my_q101,(str(id),))
                email=''
                date=''
                for i,j in my_cursor:
                    email=j
                    date=str(i)
                #Label(top,image=my_img1).pack(pady=10)
                #Label(top,text="Your order with order ID: "+str(id)+" had the following items",font=myfont3).pack(pady=10)
                Label(second_frame,text="==============================================================================================================================").pack(pady=10,anchor='w')
                Label(second_frame,text="Order ID: "+str(id),font=myfont).pack(pady=5,anchor='w')
                Label(second_frame,text="Order Date: "+str(date),font=myfont).pack(pady=5,anchor='w')
                Label(second_frame,text="==============================================================================================================================").pack(pady=10,anchor='w')
                my_q="""select o.count,b.title,b.price,a.name,b.publisher_name from order_items o,books b,author a where o.order_id=%s and o.book_isbn=b.ISBN and b.ISBN=a.book_isbn"""
                my_v=str(id)
                my_cursor.execute(my_q,(my_v,))
                items=[]
                for i in my_cursor:
                    items.append(i)
                amount=0
                i=1
                    #Label(second_frame,text="BOOK NAME",font=myfont).place(x=0,y=150)
                    #Label(second_frame,text="QUANTITY",font=myfont).place(x=700,y=150)
                for a,b,c,d,e in items:
                    Label(second_frame,text=str(i)+") "+b+" by "+d+" from "+e+" publication",font=myfont).pack(pady=4,anchor='w')
                    Label(second_frame,text="Quantity: "+str(a),font=myfont).pack(pady=10,anchor='w')
                    amount+=c
                    i+=1
                my_q999="""select * from customer where email=%s"""
                my_cursor.execute(my_q999,(str(email),))
                name=""
                address=""
                for a,b,c,d,e in my_cursor:
                    #print(a,b,c,d)
                    name=str(b)+" "+str(c)
                    address=str(d)
                my_q888="""select phone_number from phone_number where customer_email=%s"""
                my_cursor.execute(my_q888,(str(email),))
                p_no=''
                for i in my_cursor:
                    p_no=str(i[0])
                Label(second_frame,text="Customer Name: "+str(name),font=myfont).pack(pady=10,anchor=W)
                Label(second_frame,text="Customer Phone number: "+str(p_no),font=myfont).pack(pady=10,anchor=W)
                Label(second_frame,text="Customer Email: "+str(email),font=myfont).pack(pady=10,anchor=W)
                Label(second_frame,text="Customer Address:  "+str(address),font=myfont).pack(pady=10,anchor=W)
                Label(second_frame,text="Total Amount paid= "+str(amount),font=myfont).pack(pady=10,anchor=W)


            button2=Button(second_frame,text="Show Items",font="Helvetica 14 bold",command=lambda: show(r.get()),width=20,bd=6).pack(pady=10)


        def remove_books():
            top3=Toplevel()
            top3.title("Book Store Management")
            top3.iconbitmap(r"C:\Users\vinay\OneDrive\Desktop\new project\image.ico")
            top3.geometry("1100x500")
            main_frame=Frame(top3)
            main_frame.pack(fill=BOTH,expand=1)
            my_canvas=Canvas(main_frame)
            my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
            my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT,fill=Y)
            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
            second_frame=Frame(my_canvas)
            my_canvas.create_window((0,0),window=second_frame,anchor="nw")
            my_q="""select * from books"""
            my_cursor.execute(my_q)
            r=0
            c=0
            l={}
            for i in my_cursor:
                l[r+1]=i[1]
                for j in range(len(i)):
                    if(j==1 or j==4 or j==0):
                        e=Entry(second_frame,width=30,fg="blue",font="Helvetica 13")
                    else:
                        e=Entry(second_frame,width=15,fg="blue",font="Helvetica 13")
                    e.grid(row=r,column=c)
                    if(c==0):
                        e.insert(END, str(r+1)+")   "+str(i[j]))
                    else:
                        e.insert(END,i[j])
                    c+=1
                r+=1
                c=0      
            l1=Label(second_frame,text="Enter row number",font="Helvetica 13")
            l1.grid(row=r+1,column=0,pady=10)
            e1=Entry(second_frame,width=20,fg="blue",font="Helvetica 13")
            e1.grid(row=r+1,column=1,pady=10)

            def remove(l,pos):
                a=messagebox.askyesno("Continue?","Do you want to remove "+str(l[pos])+" from the database?",parent=top3)
                if(a==True):
                    my_q="""delete from books where title=%s"""
                    my_cursor.execute(my_q,(str(l[pos]),))
                    mydb.commit()
                    top3.destroy()
                    remove_books()

            button1=Button(second_frame,text="Remove Book",fg="black",font="Helvetica 12 bold",bd=7,command=lambda: remove(l,int(e1.get())))
            button1.grid(row=r+2,column=1,pady=10)
            


        b2=Button(frame1,text="Add Books",bg="#1687a9",fg="white",font="Helvetics 12 bold",command=add_books,width=16)
        b2.place(x=18,y=250)
        b5=Button(frame1,text="Remove Books",bg="#1687a9",fg="white",font="Helvetica 12 bold",command=remove_books,width=16)
        b5.place(x=18,y=300)
        b3=Button(frame1,text="Update Price",bg="#1687a9",fg="white",font="Helvetics 12 bold",command=update_data,width=16)
        b3.place(x=18,y=350)
        b4=Button(frame1,text="View Orders",bg="#1687a9",fg="white",font="Helvetics 12 bold",command=view_orders,width=16)
        b4.place(x=18,y=400)


    def admin_login(email,pwd):
        my_q1="""select SHA(%s)"""
        my_cursor.execute(my_q1,(pwd,))
        for i in my_cursor:
            pwd=i[0]
        my_q="""select email,password from customer"""
        my_cursor.execute(my_q)
        e=[]
        p={}
        for i,j in my_cursor:
            e.append(i)
            p[i]=j

        if((email in e) and (p[email]==pwd)):
            admin_afterlogin(email)
        else:
            messagebox.showinfo("Error","Email ID and Password doesn't match!",parent=top)




            

    button=Button(top,text="Log in",command=lambda: admin_login(str(e1.get()),str(e2.get())),bg="#0e1c21",fg="white",height=2,width=10,font=myfont2)
    button.place(x=551,y=572)

button1=Button(root,text="Log in",height=2,width = 20,command=proceed,bg='#818181',fg='white')
button1['font']=myfont2
button1.place(x=250, y=380)

button3=Button(root,text="Admin?",height=2,width=20,command=admin,font=myfont2,bg='#818181',fg='white')
button3.place(x=250,y=460)

button2=Button(root,text="Sign up",height=2,width = 20,command=sign_up,bg='#818181',fg='white',font=myfont2)
button2.place(x=250, y=570)


root.mainloop()

