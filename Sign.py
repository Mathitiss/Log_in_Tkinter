from tkinter import *
from tkinter import messagebox
import ast

# Window
root=Tk()
root.title("Sign In")
root.geometry('1280x720')
root.resizable(False, False)
root.configure(bg='white')

# Image
image=PhotoImage(file='C:/Users/egorm/PycharmProjects/Log_in/Images/Sign_In.png')
Label(root, image=image, bg='white').place(x=13, y=24)

# Sign in Text
text=Label(root, text='Sign in', fg='#34b2e4', bg='white', font=('Microsoft YaHei UI Light',30,'bold'))
text.place(x=890, y=80)

# Login Bar
def on_enter(e):
    log_bar.delete(0, 'end')

def on_leave(e):
    name=log_bar.get()
    if name=='':
        log_bar.insert(0, 'Login')

log_bar=Entry(root, width=25, fg='black', bg='white', border=0, font=('Microsoft YaHei UI Light',20))
log_bar.place(x=785, y=160)
log_bar.insert(0, 'Login')
log_bar.bind('<FocusIn>', on_enter)
log_bar.bind('<FocusOut>', on_leave)

Frame(root, width=330, height=2, bg='black').place(x=785, y=200)

# Password Bar
def on_enter(e):
    pas_bar.delete(0, 'end')

def on_leave(e):
    name=pas_bar.get()
    if name=='':
        pas_bar.insert(0, 'Password')

pas_bar=Entry(root, width=25, fg='black', bg='white', border=0, font=('Microsoft YaHei UI Light',20))
pas_bar.place(x=785, y=230)
pas_bar.insert(0, 'Password')
pas_bar.bind('<FocusIn>', on_enter)
pas_bar.bind('<FocusOut>', on_leave)

Frame(root, width=330, height=2, bg='black').place(x=785, y=270)

# Button
def signin():
    username=log_bar.get()
    password=pas_bar.get()

    file=open('C:/Users/egorm/PycharmProjects/Log_in/Data.txt', 'r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    print(r.keys())
    print(r.values())

    if username in r.keys() and password==r[username]:
        screen=Toplevel(root)
        screen.title('App')
        screen.geometry('480x280')
        screen.config(bg='#34b2e4')
        screen.resizable(False, False)

        Label(screen, text='Welcome', bg='#34b2e4', fg='white', font=('Microsoft YaHei UI Light',30,'bold')).pack(expand=True)
        screen.mainloop()

    else:
        messagebox.showerror('Invalid', 'Invalid username or password')
###########################################################
def sign_com():
    window=Toplevel(root)
    window.title("Sign Up")
    window.geometry('1280x720')
    window.resizable(False, False)
    window.configure(bg='white')

    def signup():
        username = log_bar.get()
        password = pas_bar.get()
        confirm = pas_rep_bar.get()

        if password == confirm:
            try:
                file = open('C:/Users/egorm/PycharmProjects/Log_in/Data.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {username: password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open('C:/Users/egorm/PycharmProjects/Log_in/Data.txt', 'w')
                w = file.write(str(r))

                messagebox.showinfo('Sign up', 'Successful')

            except:
                file = open('C:/Users/egorm/PycharmProjects/Log_in/Data.txt', 'w')
                pp = str({'Username': 'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('Invalid', 'Both Passwords should match')

    def sign():
        window.destroy()

    # Image
    image = PhotoImage(file='C:/Users/egorm/PycharmProjects/Log_in/Images/Sign_Up2.png')
    Label(window, image=image, bg='white').place(x=90, y=40)

    # Sign in Text
    text = Label(window, text='Sign up', fg='#b7aeee', bg='white', font=('Microsoft YaHei UI Light', 30, 'bold'))
    text.place(x=920, y=80)

    # Login Bar
    def on_enter(e):
        log_bar.delete(0, 'end')

    def on_leave(e):
        name = log_bar.get()
        if name == '':
            log_bar.insert(0, 'Login')

    log_bar = Entry(window, width=25, fg='black', bg='white', border=0, font=('Microsoft YaHei UI Light', 20))
    log_bar.place(x=835, y=160)
    log_bar.insert(0, 'Login')
    log_bar.bind('<FocusIn>', on_enter)
    log_bar.bind('<FocusOut>', on_leave)

    Frame(window, width=330, height=2, bg='black').place(x=835, y=200)

    # Password Bar
    def on_enter(e):
        pas_bar.delete(0, 'end')

    def on_leave(e):
        name = pas_bar.get()
        if name == '':
            pas_bar.insert(0, 'Password')

    pas_bar = Entry(window, width=25, fg='black', bg='white', border=0, font=('Microsoft YaHei UI Light', 20))
    pas_bar.place(x=835, y=235)
    pas_bar.insert(0, 'Password')
    pas_bar.bind('<FocusIn>', on_enter)
    pas_bar.bind('<FocusOut>', on_leave)

    Frame(window, width=330, height=2, bg='black').place(x=835, y=275)

    # Password Repeat Bar
    def on_enter(e):
        pas_rep_bar.delete(0, 'end')

    def on_leave(e):
        name = pas_rep_bar.get()
        if name == '':
            pas_rep_bar.insert(0, 'Password Repeat')

    pas_rep_bar = Entry(window, width=25, fg='black', bg='white', border=0, font=('Microsoft YaHei UI Light', 20))
    pas_rep_bar.place(x=835, y=310)
    pas_rep_bar.insert(0, 'Password Repeat')
    pas_rep_bar.bind('<FocusIn>', on_enter)
    pas_rep_bar.bind('<FocusOut>', on_leave)

    Frame(window, width=330, height=2, bg='black').place(x=835, y=350)

    # Button
    Button(window, width=50, height=2, pady=7, text='Sign up', bg='#b7aeee', fg='white', border=0, cursor='hand2',
           command=signup).place(x=825, y=390)

    # Sign In
    ask = Label(window, text="I have an account.", fg='black', bg='white',
                font=('Microsoft YaHei UI Light', 10, 'bold'))
    ask.place(x=905, y=480)
    sign_in = Button(window, width=6, text='Sign In', font=('Microsoft YaHei UI Light', 10, 'bold'), bg='white',
                     fg='#b7aeee', border=0, cursor='hand2', command=sign)
    sign_in.place(x=1035, y=478)

    # On/Off
    window.mainloop()
###########################################################
Button(root, width=50, height=2, pady=7, text='Sign in', bg='#34b2e4', fg='white', border=0, cursor='hand2', command=signin).place(x=780, y=295)

# Sign Up
ask=Label(root, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light',10,'bold'))
ask.place(x=815, y=420)
sign_up=Button(root, width=14, text='Creat an account',  font=('Microsoft YaHei UI Light',10,'bold',), bg='white', fg='#34b2e4', border=0, cursor='hand2', command=sign_com)
sign_up.place(x=981, y=418)


# On/Off
root.mainloop()