import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkcalendar import Calendar
from tkinter import messagebox
import webbrowser
import mysql.connector
import datetime
from io import BytesIO
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from chat import get_response, bot_name
import random
# rmb to change your_email and your_password in send_email()

database = mysql.connector.connect(host="localhost", user="root", password="xueer.1014", database="pik")
cursor = database.cursor()
image_cursor = database.cursor()

# Chatbot CLASS
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
chat_app_instance = None


class ChatApplication:

    def __init__(self, parent_window):
        self.window = Toplevel(parent_window)
        self._setup_main_window()
        self.window.protocol("WM_DELETE_WINDOW", self._on_close)
        self.window.iconphoto(False, tk.PhotoImage(file='C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/icon.png'))

    def run(self):
        self.window.mainloop()

    def _on_close(self):
        self.window.withdraw()

    def reset_window(self):
        # Clear the text widget
        self.text_widget.configure(state=NORMAL)
        self.text_widget.delete(1.0, END)
        self.text_widget.configure(state=DISABLED)

        # Clear the message entry
        self.msg_entry.delete(0, END)

        # Set focus on the message entry
        self.msg_entry.focus()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5, wrap='word')
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", lambda event: self._on_enter_pressed())

        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed())
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


def database_signup():
    user_name = username2_entry.get()
    user_email = email2_entry.get()
    user_password = password2_entry.get()
    user_type = "user"
    cursor.execute("INSERT INTO USER(user_name, user_email, user_password, user_type) VALUES (%s, %s, %s, %s)",
                   (user_name, user_email, user_password, user_type))
    database.commit()


def insert_username1():
    if username1_entry.cget('fg') == '#8D93AB':
        username1_entry.delete(0, tk.END)
        username1_entry.config(fg='#363636')


def leave_username1():
    username1_entry.get()
    if username1_entry.get() == '':
        username1_entry.insert(0, 'Username')
        username1_entry.config(fg='#8D93AB')


def insert_password1():
    if password1_entry.cget('fg') == '#8D93AB':
        password1_entry.delete(0, tk.END)
        password1_entry.config(fg='#363636')
        if openEye_status.cget('text') == 'Open':
            password1_entry.config(show='')
        elif openEye_status.cget('text') == 'Close':
            password1_entry.config(show='*')


def leave_password1():
    password1_entry.get()
    if password1_entry.get() == '':
        password1_entry.insert(0, 'Password')
        password1_entry.config(fg='#8D93AB', show='')


def show_password():
    if openEye_status.cget('text') == 'Close' and password1_entry.cget('fg') == '#8D93AB':
        openEye_button.configure(image=openEyeButton_image)
        password1_entry.config(show='')
        openEye_status.configure(text='Open')
    elif openEye_status.cget('text') == 'Open' and password1_entry.cget('fg') == '#8D93AB':
        openEye_button.configure(image=closeEyeButton_image)
        password1_entry.config(show='')
        openEye_status.configure(text='Close')
    elif openEye_status.cget('text') == 'Close':
        openEye_button.configure(image=openEyeButton_image)
        password1_entry.config(show='')
        openEye_status.configure(text='Open')
    elif openEye_status.cget('text') == 'Open':
        openEye_button.configure(image=closeEyeButton_image)
        password1_entry.config(show='*')
        openEye_status.configure(text='Close')


def insert_username2():
    if username2_entry.cget('fg') == '#8D93AB':
        username2_entry.delete(0, tk.END)
        username2_entry.config(fg='#363636')


def leave_username2():
    username2_entry.get()
    if username2_entry.get() == '':
        username2_entry.insert(0, 'Username')
        username2_entry.config(fg='#8D93AB')


def insert_email2():
    if email2_entry.cget('fg') == '#8D93AB':
        email2_entry.delete(0, tk.END)
        email2_entry.config(fg='#363636')


def leave_email2():
    email2_entry.get()
    if email2_entry.get() == '':
        email2_entry.insert(0, 'Email')
        email2_entry.config(fg='#8D93AB')


def insert_password2():
    if password2_entry.cget('fg') == '#8D93AB':
        password2_entry.delete(0, tk.END)
        password2_entry.config(fg='#363636')
        if openEye_status1.cget('text') == 'Open':
            password2_entry.config(show='')
        elif openEye_status1.cget('text') == 'Close':
            password2_entry.config(show='*')


def leave_password2():
    password2_entry.get()
    if password2_entry.get() == '':
        password2_entry.insert(0, 'Password')
        password2_entry.config(fg='#8D93AB', show='')


def insert_confirmed_password2():
    if confirmed_password2_entry.cget('fg') == '#8D93AB':
        confirmed_password2_entry.delete(0, tk.END)
        confirmed_password2_entry.config(fg='#363636')
        if openEye_status2.cget('text') == 'Open':
            confirmed_password2_entry.config(show='')
        elif openEye_status2.cget('text') == 'Close':
            confirmed_password2_entry.config(show='*')


def leave_confirmed_password2():
    confirmed_password2_entry.get()
    if confirmed_password2_entry.get() == '':
        confirmed_password2_entry.insert(0, 'Confirmed Password')
        confirmed_password2_entry.config(fg='#8D93AB', show='')


def show_password1():
    if openEye_status1.cget('text') == 'Close' and password2_entry.cget('fg') == '#8D93AB':
        openEye_button1.configure(image=openEyeButton_image)
        password2_entry.config(show='')
        openEye_status1.configure(text='Open')
    elif openEye_status1.cget('text') == 'Open' and password2_entry.cget('fg') == '#8D93AB':
        openEye_button1.configure(image=closeEyeButton_image)
        password2_entry.config(show='')
        openEye_status1.configure(text='Close')
    elif openEye_status1.cget('text') == 'Close':
        openEye_button1.configure(image=openEyeButton_image)
        password2_entry.config(show='')
        openEye_status1.configure(text='Open')
    elif openEye_status1.cget('text') == 'Open':
        openEye_button1.configure(image=closeEyeButton_image)
        password2_entry.config(show='*')
        openEye_status1.configure(text='Close')


def show_password2():
    if openEye_status2.cget('text') == 'Close' and confirmed_password2_entry.cget('fg') == '#8D93AB':
        openEye_button2.configure(image=openEyeButton_image)
        confirmed_password2_entry.config(show='')
        openEye_status2.configure(text='Open')
    elif openEye_status2.cget('text') == 'Open' and confirmed_password2_entry.cget('fg') == '#8D93AB':
        openEye_button2.configure(image=closeEyeButton_image)
        confirmed_password2_entry.config(show='')
        openEye_status2.configure(text='Close')
    elif openEye_status2.cget('text') == 'Close':
        openEye_button2.configure(image=openEyeButton_image)
        confirmed_password2_entry.config(show='')
        openEye_status2.configure(text='Open')
    elif openEye_status2.cget('text') == 'Open':
        openEye_button2.configure(image=closeEyeButton_image)
        confirmed_password2_entry.config(show='*')
        openEye_status2.configure(text='Close')


# Switching
def clear_login1_frame():
    username1_entry.delete(0, tk.END)
    username1_entry.insert(0, 'Username')
    username1_entry.config(fg='#8D93AB')

    password1_entry.delete(0, tk.END)
    password1_entry.insert(0, 'Password')
    password1_entry.config(fg='#8D93AB', show='')


def clear_signup2_frame():
    username2_entry.delete(0, tk.END)
    username2_entry.insert(0, 'Username')
    username2_entry.config(fg='#8D93AB')

    email2_entry.delete(0, tk.END)
    email2_entry.insert(0, 'Email')
    email2_entry.config(fg='#8D93AB')

    password2_entry.delete(0, tk.END)
    password2_entry.insert(0, 'Password')
    password2_entry.config(fg='#8D93AB', show='')

    confirmed_password2_entry.delete(0, tk.END)
    confirmed_password2_entry.insert(0, 'Confirmed Password')
    confirmed_password2_entry.config(fg='#8D93AB', show='')


def switch_login1_frame():
    clear_signup2_frame()
    signup_frame.place_forget()
    login_frame.place(relx=0.5, rely=0.5, anchor='center')
    login_frame.focus_set()

    password1_entry.config(show='')
    openEye_button.config(image=closeEyeButton_image)
    openEye_status.config(text='Close')

    signup_success_window.withdraw()


def close_forgot_password():
    forgot_password_window.withdraw()
    fg_username_entry.delete(0, tk.END)
    fg_username_entry.config(show='')

    new_password_entry.delete(0, tk.END)
    new_password_entry.config(show='')
    openEye_button3.config(image=closeEyeButton_image)
    openEye_status3.config(text='Close')

    confirm_password_entry.delete(0, tk.END)
    confirm_password_entry.config(show='')
    openEye_button4.config(image=closeEyeButton_image)
    openEye_status4.config(text='Close')


def switch_signup2_frame():
    clear_login1_frame()
    login_frame.place_forget()
    signup_frame.place(relx=0.5, rely=0.5, anchor='center')
    signup_frame.focus_set()

    password2_entry.config(show='')
    openEye_button1.config(image=closeEyeButton_image)
    openEye_status1.config(text='Close')

    confirmed_password2_entry.config(show='')
    openEye_button2.config(image=closeEyeButton_image)
    openEye_status2.config(text='Close')

    close_forgot_password()


def display_error_message(message):
    messagebox.showerror("Error", message)


def successful_submit():
    cursor.execute('SELECT user_name FROM USER WHERE user_name = %s', (username2_entry.get(),))
    existing_username = cursor.fetchone()
    c1 = password2_entry.get() == confirmed_password2_entry.get()
    c2 = password2_entry.cget('fg') == '#363636' and confirmed_password2_entry.cget('fg') == '#363636'
    c3 = username2_entry.cget('fg') == '#363636' and username2_entry.get() != ''
    c4 = email2_entry.cget('fg') == '#363636' and email2_entry.get() != ''
    c5 = existing_username
    c6 = len(password2_entry.get()) >= 8
    c7 = '@' and '.com' in email2_entry.get()
    if c1 and c2 and c3 and c4 and c6 and c7 and not c5:
        # Show SignUp Successfully Window
        signup_success_window.deiconify()
        database_signup()
    elif c4 and c3 and c2 and not c6:
        display_error_message("Minimum 8 characters of password")
    elif c4 and c3 and c2 and not c1:
        display_error_message("Password does not match")
    elif c4 and c3 and c2 and c1 and not c7:
        display_error_message("Invalid email format")
    elif c4 and c3 and c2 and c1 and c6 and c7 and c5:
        display_error_message('Username exists, please try another one')
    else:
        display_error_message("Please fill in all the details")


def switch_main_window():
    close_forgot_password()
    user_name = username1_entry.get()
    user_password = password1_entry.get()
    cursor.execute('SELECT user_type FROM USER WHERE user_name=%s AND user_password=%s', (user_name, user_password,))
    user_type = cursor.fetchone()

    if user_type:
        switch_to_main()
        login_window.withdraw()
        main_window.deiconify()

        cursor.execute('''SELECT * FROM destination WHERE destination_type=%s AND destination_status=%s''', ('attraction', 1))
        attractions = cursor.fetchall()
        various_attraction(attractions)
        search_filter_attraction()
        navigate_to_spots()
        select_content_spots()

        various_transport()

        cursor.execute('''SELECT * FROM destination WHERE destination_type=%s AND destination_status=%s''', ('restaurant', 1))
        restaurants = cursor.fetchall()
        various_restaurant(restaurants)
        search_filter_restaurant()

        change_password_button.config(command=change_password_profile)
        forgot_password_window.bind('<Return>', lambda event: change_password_profile())
        if user_type[0] == 'user':
            pass
        elif user_type[0] == 'admin':
            print('admin')
    else:
        display_error_message("Incorrect Username or Password")


def sign_out():
    global chat_app_instance
    if chat_app_instance is not None:
        chat_app_instance.reset_window()
        chat_app_instance._on_close()

    clear_login1_frame()
    signup_frame.place_forget()
    login_frame.place(relx=0.5, rely=0.5, anchor='center')
    login_window.deiconify()
    main_window.withdraw()
    change_password_button.config(command=change_password)
    forgot_password_window.bind('<Return>', lambda event: change_password())


def switch_forgot_password():
    forgot_password_window.deiconify()
    forgot_password_window.focus_set()

    new_password_entry.config(show='*')
    openEye_button3.config(image=closeEyeButton_image)
    openEye_status3.config(text='Close')

    confirm_password_entry.config(show='*')
    openEye_button4.config(image=closeEyeButton_image)
    openEye_status4.config(text='Close')


def show_password3():
    if openEye_status3.cget('text') == 'Close' and new_password_entry.get() == '':
        openEye_button3.configure(image=openEyeButton_image)
        new_password_entry.config(show='')
        openEye_status3.configure(text='Open')
    elif openEye_status3.cget('text') == 'Open' and new_password_entry.get() == '':
        openEye_button3.configure(image=closeEyeButton_image)
        new_password_entry.config(show='')
        openEye_status3.configure(text='Close')
    elif openEye_status3.cget('text') == 'Close':
        openEye_button3.configure(image=openEyeButton_image)
        new_password_entry.config(show='')
        openEye_status3.configure(text='Open')
    elif openEye_status3.cget('text') == 'Open':
        openEye_button3.configure(image=closeEyeButton_image)
        new_password_entry.config(show='*')
        openEye_status3.configure(text='Close')


def show_password4():
    if openEye_status4.cget('text') == 'Close' and confirm_password_entry.get() == '':
        openEye_button4.configure(image=openEyeButton_image)
        confirm_password_entry.config(show='')
        openEye_status4.configure(text='Open')
    elif openEye_status4.cget('text') == 'Open' and confirm_password_entry.get() == '':
        openEye_button4.configure(image=closeEyeButton_image)
        confirm_password_entry.config(show='')
        openEye_status4.configure(text='Close')
    elif openEye_status4.cget('text') == 'Close':
        openEye_button4.configure(image=openEyeButton_image)
        confirm_password_entry.config(show='')
        openEye_status4.configure(text='Open')
    elif openEye_status4.cget('text') == 'Open':
        openEye_button4.configure(image=closeEyeButton_image)
        confirm_password_entry.config(show='*')
        openEye_status4.configure(text='Close')


def change_password():
    cursor.execute('''SELECT user_name from user''')
    usernames = cursor.fetchall()
    exist_name = []
    for username in usernames:
        exist_name.append(username[0])

    enter_username = fg_username_entry.get()
    new_password = new_password_entry.get()
    confirm_password = confirm_password_entry.get()

    if enter_username == '':
        display_error_message('Please fill in your username')
        return
    elif enter_username not in exist_name:
        display_error_message('User does not exist')
        return
    elif new_password == '' and confirm_password == '':
        display_error_message('Please enter your new password')
        return
    elif new_password != confirm_password:
        display_error_message('Password does not match')
        return
    elif len(new_password) < 8:
        display_error_message('Minimum 8 characters of Password is required')
        return
    else:
        cursor.execute("UPDATE USER SET user_password = %s WHERE user_name = %s", (new_password, enter_username,))
        database.commit()
        messagebox.showinfo("Success", "Password updated successfully.")
        close_forgot_password()


# Login, SignUp
login_window = tk.Tk()
login_window.title('Penang Information Kiosk')
login_window.geometry('950x600')
login_window.iconphoto(False, tk.PhotoImage(file='C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/icon.png'))

login_frame = tk.Frame(login_window, height=550, width=700, bg='#F5F5F5')
login_frame.place(relx=0.5, rely=0.5, anchor='center')

bg_image = Image.open('C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/Sign Up.jpg')
bg_resize_image = bg_image.resize((950, 600), Image.LANCZOS)
bg_tk_image = ImageTk.PhotoImage(bg_resize_image)

bg_label = tk.Label(login_frame, image=bg_tk_image)
bg_label.pack()

# Username (LogIn Frame)
username1_frame = tk.Frame(login_frame, height=40, width=230, bg='#F5F5F5',
                           highlightbackground='#363636', highlightthickness=0.5)
username1_frame.place(x=650, y=250)

username1_entry = tk.Entry(login_frame, font=('Arial', 12), width=24, border=0,
                           fg='#8D93AB', bg='#F5F5F5')
username1_entry.place(x=653, y=260)
username1_entry.insert(0, 'Username')

username1_entry.bind('<FocusIn>', lambda event: insert_username1())
username1_entry.bind('<FocusOut>', lambda event: leave_username1())
username1_entry.bind('<Return>', lambda event: switch_main_window())

# Password (LogIn Frame)
password1_frame = tk.Frame(login_frame, height=40, width=230,
                           highlightbackground='#363636', highlightthickness=0.5)
password1_frame.place(x=650, y=305)

password1_entry = tk.Entry(login_frame, font=('Arial', 12), width=24, border=0, show='*', fg='#8D93AB', bg='#F5F5F5')
password1_entry.place(x=653, y=315)
password1_entry.insert(0, 'Password')

password1_entry.bind('<FocusIn>', lambda event: insert_password1())
password1_entry.bind('<FocusOut>', lambda event: leave_password1())
password1_entry.bind('<Return>', lambda event: switch_main_window())

# Show Password Button
openEye_image = Image.open('C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/openeyes.png')
openEye_resize_image = openEye_image.resize((15, 15), Image.LANCZOS)
openEyeButton_image = ImageTk.PhotoImage(openEye_resize_image)
closeEye_image = Image.open('C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/closeeyes.jpeg')
closeEye_resize_image = closeEye_image.resize((15, 15), Image.LANCZOS)
closeEyeButton_image = ImageTk.PhotoImage(closeEye_resize_image)

openEye_button = tk.Button(login_frame, image=closeEyeButton_image, bd=0, bg='white',
                           activebackground='white', cursor='hand2', command=show_password)
openEye_button.place(x=850, y=315)
openEye_status = tk.Label(login_frame, text='Close')

# Login Button
login1_button = tk.Button(login_frame, text='LOG IN', font=('Arial', 10), width=10, height=2,
                          fg='#FFFFFF', bg='#344955', cursor='hand2', command=switch_main_window)
login1_button.place(x=720, y=375)

# Forgot Password Button
forgot_password_image = Image.open('C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/ForgotPassword.jpg')
forgotPassword_resize = forgot_password_image.resize((100, 15), Image.LANCZOS)
forgotPassword_button_image = ImageTk.PhotoImage(forgotPassword_resize)
forgotPassword_button = tk.Button(login_frame, image=forgotPassword_button_image, bd=0, bg='white', cursor='hand2',
                                  command=switch_forgot_password)
forgotPassword_button.place(x=775, y=350)

# Forgot Password Window
forgot_password_window = tk.Toplevel(login_window)
forgot_password_window.title('Forgot Password')
forgot_password_window.geometry('400x200')
forgot_password_window.iconphoto(False, tk.PhotoImage(file='C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/icon.png'))
forgot_password_window.attributes('-topmost', 1)
forgot_password_window.configure(bg='#F5F5F5')
forgot_password_window.withdraw()
forgot_password_window.bind('<Return>', lambda event: change_password())
forgot_password_window.protocol('WM_DELETE_WINDOW', close_forgot_password)

# Forgot Password (Forgot Password Window)
forgot_password_label = tk.Label(forgot_password_window, text='Reset Password',
                                 font=('Arial', 10, 'bold'), fg='#363636', bg='#F5F5F5')
forgot_password_label.place(x=150, y=20)

fg_username_label = tk.Label(forgot_password_window, text='Username:')
fg_username_label.place(x=105, y=50)
fg_username_entry = tk.Entry(forgot_password_window, show='')
fg_username_entry.place(x=170, y=50)

new_password_label = tk.Label(forgot_password_window, text="New Password:")
new_password_label.place(x=80, y=80)
new_password_entry = tk.Entry(forgot_password_window, show='*')
new_password_entry.place(x=170, y=80)

confirm_password_label = tk.Label(forgot_password_window, text="Confirm Password:")
confirm_password_label.place(x=60, y=110)
confirm_password_entry = tk.Entry(forgot_password_window, show='*')
confirm_password_entry.place(x=170, y=110)

change_password_button = tk.Button(forgot_password_window, text="Change Password", fg='#FFFFFF', bg='#344955',
                                   command=change_password)
change_password_button.place(x=180, y=140)

# New Password
openEye_button3 = tk.Button(forgot_password_window, image=closeEyeButton_image, bd=0, bg='white',
                            activebackground='white', cursor='hand2', command=show_password3)
openEye_button3.place(x=300, y=80)
openEye_status3 = tk.Label(forgot_password_window, text='Close')

# Confirm New Password
openEye_button4 = tk.Button(forgot_password_window, image=closeEyeButton_image, bd=0, bg='white',
                            activebackground='white', cursor='hand2', command=show_password4)
openEye_button4.place(x=300, y=110)
openEye_status4 = tk.Label(forgot_password_window, text='Close')

# Not registered? Text (LogIn Frame)
signUpNow_image = Image.open('C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/SignUpNow.jpg')
signUpNow_resize = signUpNow_image.resize((100, 15), Image.LANCZOS)
signUpNowButton_image = ImageTk.PhotoImage(signUpNow_resize)
signup1_button = tk.Button(login_frame, image=signUpNowButton_image, bd=0, bg='white',
                           cursor='hand2', command=switch_signup2_frame)
signup1_button.place(x=772, y=430)

# Sign Up
signup_frame = tk.Frame(login_window, height=550, width=700, bg='#F5F5F5')
signup_frame.place(relx=0.5, rely=0.5, anchor='center')
signup_frame.bind('<Return>', lambda event: successful_submit())

signUpBg_image = Image.open('C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/Login.jpg')
signUpBg_resize_image = signUpBg_image.resize((950, 600), Image.LANCZOS)
signUpBg_tk_image = ImageTk.PhotoImage(signUpBg_resize_image)

bg_label = tk.Label(signup_frame, image=signUpBg_tk_image)
bg_label.pack()

# Username (SignUp Frame)
username2_frame = tk.Frame(signup_frame, height=40, width=230, bg='#F5F5F5',
                           highlightbackground='#363636', highlightthickness=0.5)
username2_frame.place(x=650, y=240)

username2_entry = tk.Entry(signup_frame, font=('Arial', 12), width=24, border=0,
                           fg='#8D93AB', bg='#F5F5F5')
username2_entry.place(x=653, y=250)
username2_entry.insert(0, 'Username')
username2_entry.bind('<FocusIn>', lambda event: insert_username2())
username2_entry.bind('<FocusOut>', lambda event: leave_username2())
username2_entry.bind('<Return>', lambda event: successful_submit())

# Email (SignUp Frame)
email2_frame = tk.Frame(signup_frame, height=40, width=230, bg='#F5F5F5',
                        highlightbackground='#363636', highlightthickness=0.5)
email2_frame.place(x=650, y=290)

email2_entry = tk.Entry(signup_frame, font=('Arial', 12), width=24, border=0, fg='#8D93AB', bg='#F5F5F5')
email2_entry.place(x=653, y=300)
email2_entry.insert(0, 'Email')
email2_entry.bind('<FocusIn>', lambda event: insert_email2())
email2_entry.bind('<FocusOut>', lambda event: leave_email2())
email2_entry.bind('<Return>', lambda event: successful_submit())

# Password (SignUp Frame)
password2_frame = tk.Frame(signup_frame, height=40, width=230,
                           highlightbackground='#363636', highlightthickness=0.5)
password2_frame.place(x=650, y=340)

password2_entry = tk.Entry(signup_frame, font=('Arial', 12), width=24, border=0, show='*', fg='#8D93AB', bg='#F5F5F5')
password2_entry.place(x=653, y=350)
password2_entry.insert(0, 'Password')
password2_entry.bind('<FocusIn>', lambda event: insert_password2())
password2_entry.bind('<FocusOut>', lambda event: leave_password2())
password2_entry.bind('<Return>', lambda event: successful_submit())

confirmed_password2_frame = tk.Frame(signup_frame, height=40, width=230, bg='#F5F5F5',
                                     highlightbackground='#363636', highlightthickness=0.5)
confirmed_password2_frame.place(x=650, y=390)

confirmed_password2_entry = tk.Entry(signup_frame, font=('Arial', 12), width=24, border=0, show='*', fg='#8D93AB',
                                     bg='#F5F5F5')
confirmed_password2_entry.place(x=653, y=400)
confirmed_password2_entry.insert(0, 'Confirmed Password')
confirmed_password2_entry.bind('<FocusIn>', lambda event: insert_confirmed_password2())
confirmed_password2_entry.bind('<FocusOut>', lambda event: leave_confirmed_password2())
confirmed_password2_entry.bind('<Return>', lambda event: successful_submit())

# Show Password Button (Sign Up Password)
openEye_button1 = tk.Button(signup_frame, image=closeEyeButton_image, bd=0, bg='white',
                            activebackground='white', cursor='hand2', command=show_password1)
openEye_button1.place(x=850, y=350)
openEye_status1 = tk.Label(signup_frame, text='Close')

# Hide Password Button (confirmed password)
openEye_button2 = tk.Button(signup_frame, image=closeEyeButton_image, bd=0, bg='white',
                            activebackground='white', cursor='hand2', command=show_password2)
openEye_button2.place(x=850, y=400)
openEye_status2 = tk.Label(signup_frame, text='Close')

# SignUp Button (SignUp Frame)
signup2_button = tk.Button(signup_frame, text='SIGN UP', font=('Arial', 10), width=10, height=2,
                           fg='#FFFFFF', bg='#344955', cursor='hand2', command=successful_submit)
signup2_button.place(x=720, y=455)

# LogIn Button (SignUp Frame)
login_image = Image.open('C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/Login(Button).jpg')
login_resize = login_image.resize((45, 15), Image.LANCZOS)
loginButton_image = ImageTk.PhotoImage(login_resize)
login2_button = tk.Button(signup_frame, image=loginButton_image, bd=0, bg='white', cursor='hand2',
                          command=switch_login1_frame)
login2_button.place(x=828, y=505)

# SignUp Successfully Window
signup_success_window = tk.Toplevel(login_window)
signup_success_window.title('Penang Information Kiosk')
signup_success_window.geometry('200x80')
signup_success_window.iconphoto(False, tk.PhotoImage(file='C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/icon.png'))
signup_success_window.configure(bg='#F5F5F5')
signup_success_window.withdraw()
signup_success_window.bind('<Return>', lambda event: switch_login1_frame())
signup_success_window.protocol('WM_DELETE_WINDOW', switch_login1_frame)
# (add icon photo here)

# SignUp Successfully Text (SignUp Successfully Window)
signup_success3_label = tk.Label(signup_success_window, text='Sign Up Successful',
                                 font=('Arial', 10, 'bold'), fg='#363636', bg='#F5F5F5')
signup_success3_label.pack(pady=10)

# Done Button (SignUp Successfully Window)
done3_button = tk.Button(signup_success_window, text='Done', font=('Arial', 8), width=10, fg='#FFFFFF', bg='#344955',
                         command=switch_login1_frame)
done3_button.pack()


def switch_to_view_feedback():
    content_frame.forget()
    map_frame.place_forget()
    feedback_frame.place_forget()
    purchase_history_frame.place_forget()
    booking_history_frame.place_forget()
    profile_frame.place_forget()
    view_feedback_frame.place(x=0, y=80)
    all_feedback()


def switch_to_map():
    close_forgot_password()
    feedback_frame.place_forget()
    profile_frame.place_forget()
    purchase_history_frame.place_forget()
    booking_history_frame.place_forget()
    content_frame.place_forget()
    view_feedback_frame.place_forget()
    view_feedback_list.unbind("<<ListboxSelect>>")
    map_frame.place(x=0, y=80)


def switch_to_feedback():
    close_forgot_password()
    map_frame.place_forget()
    profile_frame.place_forget()
    purchase_history_frame.place_forget()
    booking_history_frame.place_forget()
    content_frame.place_forget()
    view_feedback_frame.place_forget()
    view_feedback_list.unbind("<<ListboxSelect>>")
    feedback_frame.place(x=0, y=80)
    create_feedback_form()
    feedback_canvas.create_window((0, 0), window=feedback_content_frame, anchor="nw")
    feedback_content_frame.update_idletasks()
    feedback_canvas.configure(scrollregion=feedback_canvas.bbox("all"))


def switch_to_main():
    close_forgot_password()
    map_frame.place_forget()
    feedback_frame.place_forget()
    profile_frame.place_forget()
    purchase_history_frame.place_forget()
    booking_history_frame.place_forget()
    view_feedback_frame.place_forget()
    view_feedback_list.unbind("<<ListboxSelect>>")
    content_frame.place(x=0, y=80)


def switch_to_profile():
    content_frame.forget()
    map_frame.place_forget()
    feedback_frame.place_forget()
    purchase_history_frame.place_forget()
    booking_history_frame.place_forget()
    view_feedback_frame.place_forget()
    view_feedback_list.unbind("<<ListboxSelect>>")
    profile_frame.place(x=0, y=80)
    profile()


def switch_to_purchase_history():
    content_frame.forget()
    map_frame.place_forget()
    feedback_frame.place_forget()
    booking_history_frame.place_forget()
    profile_frame.place_forget()
    view_feedback_frame.place_forget()
    view_feedback_list.unbind("<<ListboxSelect>>")
    purchase_history_frame.place(x=0, y=80)
    update_ph_bh()
    purchase_history()
    purchase_history_canvas.create_window((0, 0), window=purchase_history_content_frame, anchor="nw")
    purchase_history_content_frame.update_idletasks()
    purchase_history_canvas.configure(scrollregion=purchase_history_canvas.bbox("all"))


def switch_to_booking_history():
    content_frame.forget()
    map_frame.place_forget()
    feedback_frame.place_forget()
    purchase_history_frame.place_forget()
    profile_frame.place_forget()
    view_feedback_frame.place_forget()
    view_feedback_list.unbind("<<ListboxSelect>>")
    booking_history_frame.place(x=0, y=80)
    update_ph_bh()
    booking_history()
    booking_history_canvas.create_window((0, 0), window=booking_history_content_frame, anchor="nw")
    booking_history_content_frame.update_idletasks()
    booking_history_canvas.configure(scrollregion=booking_history_canvas.bbox("all"))


def navigate_to_transport():
    transport_frame.place(x=0, y=65)
    spots_frame.place_forget()
    food_beverage_frame.place_forget()
    games_content_frame.place_forget()
    selection_frame.place(x=245, y=60)
    transport_canvas.create_window((0, 0), window=transport_content_frame, anchor="nw")
    transport_content_frame.update_idletasks()
    transport_canvas.configure(scrollregion=transport_canvas.bbox("all"))


def navigate_to_food_beverage():
    transport_frame.place_forget()
    spots_frame.place_forget()
    food_beverage_frame.place(x=0, y=65)
    games_content_frame.place_forget()
    selection_frame.place(x=490, y=60)
    food_beverage_canvas.create_window((0, 0), window=food_beverage_main_frame, anchor="nw")
    food_beverage_main_frame.update_idletasks()
    food_beverage_canvas.configure(scrollregion=food_beverage_canvas.bbox("all"))


def navigate_to_games():
    transport_frame.place_forget()
    spots_frame.place_forget()
    food_beverage_frame.place_forget()
    games_content_frame.place(x=0, y=65)
    selection_frame.place(x=735, y=60)


def navigate_to_spots():
    transport_frame.place_forget()
    spots_frame.place(x=0, y=65)
    food_beverage_frame.place_forget()
    games_content_frame.place_forget()
    selection_frame.place(x=0, y=60)
    spots_canvas.create_window((0, 0), window=spots_main_frame, anchor="nw")
    spots_main_frame.update_idletasks()
    spots_canvas.configure(scrollregion=spots_canvas.bbox("all"))


def show_profile_menu():
    close_forgot_password()
    menu_x = profile_button.winfo_rootx()
    menu_y = profile_button.winfo_rooty() + profile_button.winfo_height()
    profile_menu.post(menu_x, menu_y)


# Main Page
main_window = tk.Toplevel(login_window)
main_window.title('Penang Information Kiosk')
main_window.geometry('950x600')
main_window.iconphoto(False,
                      tk.PhotoImage(file='C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/icon.png'))
main_window.withdraw()

# Main Page - Center Frame
center_frame = tk.Frame(main_window, height=600, width=950)
center_frame.place(relx=0.5, rely=0.5, anchor='center')

# Main Page - Title Frame
title_frame = tk.Frame(center_frame, width=950, height=80, bg='#344955')
title_frame.place(x=0, y=0)

title_text = tk.Label(title_frame, text='Penang Information Kiosk', font=('Times New Roman', 32, 'bold'),
                      bg='#344955', fg='#FDFEFF')
title_text.place(relx=0.5, rely=0.5, anchor='center')

profile_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/profile.png")
profile_resize_image = profile_image.resize((55, 55), Image.LANCZOS)
profile_tk_image = ImageTk.PhotoImage(profile_resize_image)
profile_button = tk.Button(title_frame, bg='#344955', image=profile_tk_image, border=0, command=show_profile_menu)
profile_button.place(x=15, y=12)

profile_menu = tk.Menu(title_frame, tearoff=0)
profile_menu.configure(bg='#E5F2F8')
profile_menu.add_command(label='Profile', font=('Arial', 10), command=switch_to_profile)
profile_menu.add_command(label='Purchase History', font=('Arial', 10), command=switch_to_purchase_history)
profile_menu.add_command(label='Booking History', font=('Arial', 10), command=switch_to_booking_history)
profile_menu.add_command(label='Sign Out', font=('Arial', 10), command=sign_out)
profile_menu.add_command(label='View Feedback', font=('Arial', 10), command=switch_to_view_feedback)

map_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/map.png")
map_resize_image = map_image.resize((50, 40), Image.LANCZOS)
map_tk_image = ImageTk.PhotoImage(map_resize_image)
map_button = tk.Button(title_frame, bg='#344955', image=map_tk_image, border=0, command=switch_to_map)
map_button.place(x=790, y=20)

chatbot_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/chatbot.png")
chatbot_resize_image = chatbot_image.resize((42, 40), Image.LANCZOS)
chatbot_tk_image = ImageTk.PhotoImage(chatbot_resize_image)


def open_chatbot_window():
    global chat_app_instance

    if chat_app_instance is not None:
        chat_app_instance.window.deiconify()
        chat_app_instance.window.lift()
    else:
        chat_app_instance = ChatApplication(main_window)
        chat_app_instance.run()


chatbot_button = tk.Button(title_frame, bg='#344955', image=chatbot_tk_image, border=0, command=open_chatbot_window)
chatbot_button.place(x=845, y=20)

feedback_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/feedback.png")
feedback_resize_image = feedback_image.resize((42, 40), Image.LANCZOS)
feedback_tk_image = ImageTk.PhotoImage(feedback_resize_image)
feedback_button = tk.Button(title_frame, bg='#344955', image=feedback_tk_image, border=0,
                            command=switch_to_feedback)
feedback_button.place(x=895, y=18)

# Main Page - Content Frame
content_frame = tk.Frame(center_frame, width=950, height=520)
content_frame.place(x=0, y=80)

# Navigation Bar
navigation_frame = tk.Frame(content_frame, width=950, height=65, bg='#E5F2F8')
navigation_frame.place(x=0, y=0)

spots_button = tk.Button(navigation_frame, width=20, height=2, border=0, text='Local Attraction Spots',
                         bg='#E5F2F8', fg='#000000', font=('Times New Roman', 16), command=navigate_to_spots)
spots_button.place(x=0, y=2)

transport_button = tk.Button(navigation_frame, width=20, height=2, border=0, text='Public Transportation',
                             bg='#E5F2F8', fg='#000000', font=('Times New Roman', 16),
                             command=navigate_to_transport)
transport_button.place(x=245, y=2)

food_beverage_button = tk.Button(navigation_frame, width=20, height=2, border=0, text='Food & Beverages',
                                 bg='#E5F2F8', fg='#000000', font=('Times New Roman', 16),
                                 command=navigate_to_food_beverage)
food_beverage_button.place(x=490, y=2)

games_button = tk.Button(navigation_frame, width=18, height=2, border=0, text='Games',
                         bg='#E5F2F8', fg='#000000', font=('Times New Roman', 16), command=navigate_to_games)
games_button.place(x=735, y=2)

selection_frame = tk.Frame(navigation_frame, width=245, height=5, bg='#F9AA33')
selection_frame.place(x=0, y=60)

# Attraction & Restaurant Images Dict
image_cursor.execute('''SELECT * FROM image''')
image_data = image_cursor.fetchall()
image_dict = {}
r_image_dict = {}
h_image_dict = {}
x = 0
for data in image_data:
    image_stream = BytesIO(data[2])
    img = Image.open(image_stream)
    resized_img = img.resize((210, 125), Image.LANCZOS)
    tk_image = ImageTk.PhotoImage(resized_img)
    destination_id = data[1]
    image_dict[x] = [destination_id, tk_image]
    x += 1

    r_resized_img = img.resize((550, 290), Image.LANCZOS)
    r_tk_image = ImageTk.PhotoImage(r_resized_img)
    r_image_dict[x] = [destination_id, r_tk_image]

    h_resized_img = img.resize((200, 150), Image.LANCZOS)
    h_tk_image = ImageTk.PhotoImage(h_resized_img)
    h_image_dict[x] = [destination_id, h_tk_image]

# Local Attraction Spots (Complete)
spots_frame = tk.Frame(content_frame, width=950, height=455)
spots_frame.place(x=0, y=65)


def select_content_spots():
    spots_content_frame.place(x=0, y=0)
    spots_second_frame.place_forget()
    spots_third_frame.place_forget()
    spots_canvas.create_window((0, 0), window=spots_main_frame, anchor="nw")
    spots_main_frame.update_idletasks()
    spots_canvas.configure(scrollregion=spots_canvas.bbox("all"))


def select_attraction():
    spots_content_frame.place_forget()
    spots_second_frame.place(x=0, y=0)
    spots_third_frame.place_forget()
    spots_second_canvas.create_window((0, 0), window=spots_detail_frame, anchor="nw")
    spots_detail_frame.update_idletasks()
    spots_second_canvas.configure(scrollregion=spots_second_canvas.bbox("all"))


def select_purchase():
    spots_content_frame.place_forget()
    spots_second_frame.place_forget()
    spots_third_frame.place(x=0, y=0)
    spots_third_canvas.create_window((0, 0), window=spots_purchase_frame, anchor="nw")
    spots_purchase_frame.update_idletasks()
    spots_third_canvas.configure(scrollregion=spots_third_canvas.bbox("all"))


# Attraction Spots - Content/Main
spots_content_frame = tk.Frame(spots_frame, width=950, height=455, bg='#FFFFFF')
spots_content_frame.place(x=0, y=0)
spots_canvas = tk.Canvas(spots_content_frame, height=435, width=950, bg='#FFFFFF',
                         highlightthickness=0)
spots_canvas.place(x=0, y=0)
spots_scrollbar = tk.Scrollbar(spots_content_frame, orient='vertical')
spots_scrollbar.place(x=933, y=0, height=455)
spots_canvas.configure(yscrollcommand=spots_scrollbar.set)
spots_scrollbar.configure(command=spots_canvas.yview)

spots_main_frame = tk.Frame(spots_canvas, bg='#FFFFFF')

# Attraction Spots - Detail
spots_second_frame = tk.Frame(spots_frame, width=950, height=455, bg='#FFFFFF')
spots_second_canvas = tk.Canvas(spots_second_frame, height=435, width=950, bg='#FFFFFF',
                                highlightthickness=0)
spots_second_canvas.place(x=0, y=0)
spots_second_scrollbar = tk.Scrollbar(spots_second_frame, orient='vertical')
spots_second_scrollbar.place(x=933, y=0, height=455)
spots_second_canvas.configure(yscrollcommand=spots_second_scrollbar.set)
spots_second_scrollbar.configure(command=spots_second_canvas.yview)

spots_detail_frame = tk.Frame(spots_second_canvas, bg='#FFFFFF')

# Attraction Spots - Purchase
spots_third_frame = tk.Frame(spots_frame, width=950, height=455, bg='#FFFFFF')
spots_third_canvas = tk.Canvas(spots_third_frame, height=435, width=950, bg='#FFFFFF',
                               highlightthickness=0)
spots_third_canvas.place(x=0, y=0)
spots_third_scrollbar = tk.Scrollbar(spots_third_frame, orient='vertical')
spots_third_scrollbar.place(x=933, y=0, height=455)
spots_third_canvas.configure(yscrollcommand=spots_third_scrollbar.set)
spots_third_scrollbar.configure(command=spots_third_canvas.yview)

spots_purchase_frame = tk.Frame(spots_third_canvas, bg='#FFFFFF')

search_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/search.png")
search_resize_image = search_image.resize((20, 20), Image.LANCZOS)
search_tk_image = ImageTk.PhotoImage(search_resize_image)
refresh_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/refresh.png")
refresh_resize_image = refresh_image.resize((20, 20), Image.LANCZOS)
refresh_tk_image = ImageTk.PhotoImage(refresh_resize_image)
clear_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/clear.png")
clear_resize_image = clear_image.resize((20, 20), Image.LANCZOS)
clear_tk_image = ImageTk.PhotoImage(clear_resize_image)
star_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/star.png")
star_resize_image = star_image.resize((15, 15), Image.LANCZOS)
star_tk_image = ImageTk.PhotoImage(star_resize_image)
previous_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/previous.png")
previous_resize_image = previous_image.resize((30, 50), Image.LANCZOS)
previous_tk_image = ImageTk.PhotoImage(previous_resize_image)
next_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/next.png")
next_resize_image = next_image.resize((30, 50), Image.LANCZOS)
next_tk_image = ImageTk.PhotoImage(next_resize_image)
calendar_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/calendar.png")
calendar_resize_image = calendar_image.resize((20, 20), Image.LANCZOS)
calendar_tk_image = ImageTk.PhotoImage(calendar_resize_image)
minus_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/minus.png")
minus_resize_image = minus_image.resize((15, 15), Image.LANCZOS)
minus_tk_image = ImageTk.PhotoImage(minus_resize_image)
add_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/add.png")
add_resize_image = add_image.resize((15, 15), Image.LANCZOS)
add_tk_image = ImageTk.PhotoImage(add_resize_image)
payment_method_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/payment_method.png")
payment_method_resize_image = payment_method_image.resize((20, 20), Image.LANCZOS)
payment_method_tk_image = ImageTk.PhotoImage(payment_method_resize_image)
payment_method_button_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/payment_method_button.png")
payment_method_button_resize_image = payment_method_button_image.resize((12, 10), Image.LANCZOS)
payment_method_button_tk_image = ImageTk.PhotoImage(payment_method_button_resize_image)


def various_attraction(attraction_list):
    num_results = len(attraction_list)
    row_value = 0
    column_value = 0

    if num_results == 0:
        attraction_space0_frame = tk.Frame(spots_main_frame, bg='#FFFFFF', width=220, height=200)
        attraction_space0_frame.grid(row=0, column=0, padx=10)
        attraction_space1_frame = tk.Frame(spots_main_frame, bg='#FFFFFF', width=220, height=200)
        attraction_space1_frame.grid(row=0, column=1)
        attraction_space2_frame = tk.Frame(spots_main_frame, bg='#FFFFFF', width=220, height=200)
        attraction_space2_frame.grid(row=0, column=2, padx=10)
        attraction_space3_frame = tk.Frame(spots_main_frame, bg='#FFFFFF', width=220, height=200)
        attraction_space3_frame.grid(row=1, column=0)
    else:
        for attraction in attraction_list:
            name = attraction[1]
            rate = attraction[2]
            formatted_rate = "{:.1f}".format(rate)
            price = attraction[4]
            formatted_price = "{:.2f}".format(price)

            describe = attraction[3]
            address = attraction[5]
            contact = attraction[6]
            operation = attraction[7]
            tag = attraction[9]

            if column_value == 0 or column_value == 2:
                x_value = 10
            else:
                x_value = 0

            if row_value % 2 == 0:
                y_value = 20
            else:
                y_value = 0

            attraction_frame = tk.Frame(spots_main_frame, bg='#EAEAEA', width=220, height=200)
            attraction_frame.grid(row=row_value, column=column_value, padx=x_value, pady=y_value)

            a_id = attraction[0]
            filtered_dict = {key: value for key, value in image_dict.items() if a_id in value}
            dict_list = list(filtered_dict.items())
            k = dict_list[0][0]
            attraction_image_label = tk.Label(attraction_frame, bg='#EAEAEA', image=image_dict[k][1])
            attraction_image_label.place(x=3, y=3)

            attraction_title_label = tk.Label(attraction_frame, text=name, font=('Arial', 12, 'bold'), bg='#EAEAEA')
            attraction_title_label.place(x=3, y=130)

            attraction_rate_label = tk.Label(attraction_frame, bg='#EAEAEA', image=star_tk_image, text=' ' + str(formatted_rate),
                                             compound=tk.LEFT, font=('Arial', 10, 'bold'))
            attraction_rate_label.place(x=3, y=153)
            attraction_price_label = tk.Label(attraction_frame, bg='#EAEAEA', font=('Arial', 10, 'bold'))
            attraction_price_label.place(x=4, y=176)

            if formatted_price == '0.00':
                attraction_price_label.config(text='Free')
            else:
                attraction_price_label.config(text='RM ' + str(formatted_price))

            if num_results == 1:
                attraction_space1_frame = tk.Frame(spots_main_frame, bg='#FFFFFF', width=220, height=200)
                attraction_space1_frame.grid(row=0, column=1)
                attraction_space2_frame = tk.Frame(spots_main_frame, bg='#FFFFFF', width=220, height=200)
                attraction_space2_frame.grid(row=0, column=2, padx=10)
                attraction_space3_frame = tk.Frame(spots_main_frame, bg='#FFFFFF', width=220, height=200)
                attraction_space3_frame.grid(row=1, column=0)
            elif num_results == 2:
                attraction_space2_frame = tk.Frame(spots_main_frame, bg='#FFFFFF', width=220, height=200)
                attraction_space2_frame.grid(row=0, column=2, padx=10)
                attraction_space3_frame = tk.Frame(spots_main_frame, bg='#FFFFFF', width=220, height=200)
                attraction_space3_frame.grid(row=1, column=0)
            elif num_results == 3:
                attraction_space3_frame = tk.Frame(spots_main_frame, bg='#FFFFFF', width=220, height=200)
                attraction_space3_frame.grid(row=1, column=0)
            attraction_frame.bind('<Button-1>',
                                  lambda event, n=name, r=formatted_rate, d=describe, p=formatted_price, a=address,
                                  c=contact, o=operation, t=tag, i=a_id:
                                  attraction_detail(n, r, d, p, a, c, o, t, i))
            for widgets in attraction_frame.winfo_children():
                widgets.bind('<Button-1>',
                             lambda event, n=name, r=formatted_rate, d=describe, p=formatted_price, a=address,
                             c=contact, o=operation, t=tag, i=a_id:
                             attraction_detail(n, r, d, p, a, c, o, t, i))

            column_value += 1
            if column_value > 2:
                column_value = 0
                row_value += 1

            def attraction_purchase(n1, i1, o1):
                for widget in spots_purchase_frame.winfo_children():
                    widget.destroy()

                cursor.execute('''SELECT * FROM price WHERE destination_id=%s''', (i1, ))
                prices = cursor.fetchone()
                p_infant = prices[2]
                p_child = prices[3]
                p_adult = prices[4]
                p_old = prices[5]

                def show_attraction3_date_frame():
                    attraction3_select_date_frame.tkraise()
                    attraction3_select_date_frame.place(x=22, y=80)

                def choose_attraction3_date():
                    attraction3_date_button.config(text=attraction3_select_date_calendar.get_date())
                    attraction3_select_date_frame.place_forget()

                def cancel_select_attraction3_date():
                    attraction3_select_date_frame.place_forget()

                def remove_attraction3_date():
                    attraction3_date_button.config(text='Pick a date')
                    attraction3_select_date_frame.place_forget()

                def show_attraction3_pay_method_menu():
                    pay_x = attraction3_pay_method_frame.winfo_rootx()
                    pay_y = attraction3_pay_method_frame.winfo_rooty() + attraction3_pay_method_frame.winfo_height()
                    attraction3_pay_method_menu.post(pay_x, pay_y)

                def select_payment_method(method):
                    attraction3_pay_method_label.configure(text=method)

                def ticket_quantity_add(p, q_label, label):
                    text = q_label.cget('text')
                    quantity = int(text)
                    quantity += 1
                    q_label.config(text=str(quantity))
                    total = p * quantity
                    formatted_total = "{:.2f}".format(total)
                    label.config(text='RM ' + str(formatted_total))
                    ticket_total()

                def ticket_quantity_minus(p, q_label, label):
                    text = q_label.cget('text')
                    quantity = int(text)
                    quantity -= 1
                    if quantity >= 0:
                        q_label.config(text=str(quantity))
                        total = p * quantity
                        formatted_total = "{:.2f}".format(total)
                        label.config(text='RM ' + str(formatted_total))
                    elif quantity <= 0:
                        pass
                    ticket_total()

                def ticket_total():
                    infant = attraction3_infant_total_label.cget('text')
                    infant_value = float(infant.split(' ')[1])
                    children = attraction3_children_total_label.cget('text')
                    children_value = float(children.split(' ')[1])
                    adults = attraction3_adults_total_label.cget('text')
                    adults_value = float(adults.split(' ')[1])
                    older = attraction3_older_total_label.cget('text')
                    older_value = float(older.split(' ')[1])
                    total = infant_value + children_value + adults_value + older_value
                    format_total = "{:.2f}".format(total)
                    attraction3_amount_label.config(text='RM ' + str(format_total))

                def purchase_ticket():
                    date = attraction3_date_button.cget('text')
                    closed_day = {}
                    per_day = o1.split('\n')
                    i_day = 0
                    for p in per_day:
                        d = p.split(' ')[0]
                        t = p.split(' ')[1]
                        if t == 'Closed':
                            closed_day[i_day] = d
                        i_day += 1
                    c_day_list = list(closed_day.keys())
                    if '-' in date:
                        year = int(date.split('-')[0])
                        month = int(date.split('-')[1])
                        day = int(date.split('-')[2])
                        current_datetime = datetime.datetime.now()
                        current_date = current_datetime.date()
                        purchase_date = current_date.replace(year=year, month=month, day=day)
                        if purchase_date > current_date:
                            if purchase_date.weekday() not in c_day_list:
                                infant = int(attraction3_infant_quantity_label.cget('text'))
                                children = int(attraction3_children_quantity_label.cget('text'))
                                adults = int(attraction3_adults_quantity_label.cget('text'))
                                older = int(attraction3_older_quantity_label.cget('text'))
                                number_guest = infant + children + adults + older
                                if number_guest >= 1:
                                    if attraction3_pay_method_label.cget('text') != 'Select payment method':
                                        messagebox.showinfo("Success", "Purchase successfully, thank you")
                                        select_content_spots()

                                        username = username1_entry.get()
                                        cursor.execute('''SELECT user_id FROM user WHERE user_name=%s''', (username,))
                                        user_id = cursor.fetchone()[0]
                                        formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
                                        cursor.execute('''INSERT INTO purchase_booking (user_id, destination_id, purchase_booking_date
                                                       ,purchase_booking_time, quantity_infant, quantity_children, quantity_adult, 
                                                       quantity_older, purchase_booking_datetime, purchase_booking_status) 
                                                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                                                       (user_id, i1, purchase_date, None,
                                                        infant, children, adults, older, formatted_datetime, 'Ready'))
                                        database.commit()

                                        cursor.execute('''SELECT purchase_booking_id FROM purchase_booking 
                                                        WHERE user_id=%s AND purchase_booking_datetime=%s''',
                                                       (user_id, formatted_datetime))
                                        purchase_booking_id = cursor.fetchone()[0]
                                        payment_method = attraction3_pay_method_label.cget('text')
                                        amount_text = attraction3_amount_label.cget('text')
                                        amount = float(amount_text.split(' ')[1])
                                        cursor.execute('''INSERT INTO payment (purchase_booking_id, payment_method, payment_status, 
                                                       payment_amount, payment_datetime) 
                                                       VALUES (%s, %s, %s, %s, %s)''',
                                                       (purchase_booking_id, payment_method, 1, amount, current_datetime))
                                        database.commit()

                                    else:
                                        messagebox.showerror("Error", 'Please select a payment method')
                                else:
                                    messagebox.showerror("Error", 'Please select the number of guests')
                            else:
                                chosen = purchase_date.weekday()
                                des = closed_day[chosen]
                                message = "The destination is closed on " + des + ' , select another date'
                                messagebox.showerror("Error", message)
                                attraction3_date_button.config(text='Pick a date')
                        elif purchase_date == current_date:
                            messagebox.showerror("Error", "Selected date must be at least one day from now")
                            attraction3_date_button.config(text='Pick a date')
                        else:
                            messagebox.showerror("Error", "Selected date is passed")
                            attraction3_date_button.config(text='Pick a date')
                    else:
                        messagebox.showerror('Error', 'Please select a date')

                attraction3_title_label = tk.Label(spots_purchase_frame, text=n1, bg='#FFFFFF', fg='#000000',
                                                   font=('Arial', 16, 'underline', 'bold'))
                attraction3_title_label.grid(row=0, column=0, padx=20, pady=10, sticky='w', columnspan=2)
                attraction3_date_frame = tk.Frame(spots_purchase_frame, bg='#F7F7F7', width=200, height=30)
                attraction3_date_frame.grid(row=1, column=0, padx=22, sticky='w', columnspan=2)

                attraction3_date_button = tk.Button(attraction3_date_frame, bg='#F7F7F7', image=calendar_tk_image, border=0,
                                                    text='Pick a date', fg='#A49C9C', compound=tk.LEFT,
                                                    font=('Arial', 10, 'bold'),
                                                    command=show_attraction3_date_frame, width=200, anchor='w')
                attraction3_date_button.place(x=5, y=2)
                attraction3_ticket_frame = tk.Frame(spots_purchase_frame, bg='#F7F7F7', width=890, height=250)
                attraction3_ticket_frame.grid(row=2, column=0, padx=22, pady=8, sticky='w', columnspan=2)
                attraction3_ticket_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                                    text='Tickets', font=('Arial', 12, 'bold'))
                attraction3_ticket_label.place(x=10, y=8)
                attraction3_infant_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                                    text='Infant (0-3)', font=('Arial', 10))
                attraction3_infant_label.place(x=12, y=50)
                attraction3_infant_price = p_infant
                format_attraction3_infant_price = "{:.2f}".format(attraction3_infant_price)
                attraction3_infant_price_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                                          text='RM ' + str(format_attraction3_infant_price), font=('Arial', 10))
                attraction3_infant_price_label.place(x=320, y=50)
                attraction3_infant_minus_button = tk.Button(attraction3_ticket_frame, bg='#F7F7F7', image=minus_tk_image,
                                                            border=0,
                                                            command=lambda: ticket_quantity_minus
                                                            (attraction3_infant_price, attraction3_infant_quantity_label,
                                                             attraction3_infant_total_label))
                attraction3_infant_minus_button.place(x=520, y=50)
                attraction3_infant_quantity_frame = tk.Frame(attraction3_ticket_frame, bg='#F7F7F7', height=22, width=30,
                                                             highlightbackground='#969695', highlightthickness=1)
                attraction3_infant_quantity_frame.place(x=564, y=48)
                attraction3_infant_quantity_label = tk.Label(attraction3_infant_quantity_frame, bg='#F7F7F7', fg='#000000',
                                                             font=('Arial', 8), text='0')
                attraction3_infant_quantity_label.place(relx=0.5, rely=0.5, anchor='center')
                attraction3_infant_add_button = tk.Button(attraction3_ticket_frame, bg='#F7F7F7', image=add_tk_image, border=0,
                                                          command=lambda: ticket_quantity_add(attraction3_infant_price,
                                                                                              attraction3_infant_quantity_label,
                                                                                              attraction3_infant_total_label))
                attraction3_infant_add_button.place(x=620, y=50)
                attraction3_infant_total_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                                          text='RM 0.00', font=('Arial', 10))
                attraction3_infant_total_label.place(x=780, y=50)
                attraction3_children_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                                      text='Children (4-12)', font=('Arial', 10))
                attraction3_children_label.place(x=12, y=90)
                attraction3_children_price = p_child
                format_attraction3_children_price = "{:.2f}".format(attraction3_children_price)
                attraction3_children_price_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                                            text='RM ' + str(format_attraction3_children_price),
                                                            font=('Arial', 10))
                attraction3_children_price_label.place(x=320, y=90)
                attraction3_children_minus_button = tk.Button(attraction3_ticket_frame, bg='#F7F7F7', image=minus_tk_image,
                                                              border=0,
                                                              command=lambda: ticket_quantity_minus
                                                              (attraction3_children_price, attraction3_children_quantity_label,
                                                               attraction3_children_total_label))
                attraction3_children_minus_button.place(x=520, y=90)
                attraction3_children_quantity_frame = tk.Frame(attraction3_ticket_frame, bg='#F7F7F7', height=22, width=30,
                                                               highlightbackground='#969695', highlightthickness=1)
                attraction3_children_quantity_frame.place(x=564, y=88)
                attraction3_children_quantity_label = tk.Label(attraction3_children_quantity_frame, bg='#F7F7F7', fg='#000000',
                                                               font=('Arial', 8), text='0')
                attraction3_children_quantity_label.place(relx=0.5, rely=0.5, anchor='center')
                attraction3_children_add_button = tk.Button(attraction3_ticket_frame, bg='#F7F7F7', image=add_tk_image, border=0,
                                                            command=lambda: ticket_quantity_add
                                                            (attraction3_children_price, attraction3_children_quantity_label,
                                                             attraction3_children_total_label))
                attraction3_children_add_button.place(x=620, y=90)
                attraction3_children_total_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                                            text='RM 0.00', font=('Arial', 10))
                attraction3_children_total_label.place(x=780, y=90)
                attraction3_adults_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                                    text='Adults (13-60)', font=('Arial', 10))
                attraction3_adults_label.place(x=12, y=130)
                attraction3_adults_price = p_adult
                format_attraction3_adults_price = "{:.2f}".format(attraction3_adults_price)
                attraction3_adults_price_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                                          text='RM ' + str(format_attraction3_adults_price), font=('Arial', 10))
                attraction3_adults_price_label.place(x=320, y=130)
                attraction3_adults_minus_button = tk.Button(attraction3_ticket_frame, bg='#F7F7F7', image=minus_tk_image,
                                                            border=0,
                                                            command=lambda: ticket_quantity_minus
                                                            (attraction3_adults_price, attraction3_adults_quantity_label,
                                                             attraction3_adults_total_label))
                attraction3_adults_minus_button.place(x=520, y=130)
                attraction3_adults_quantity_frame = tk.Frame(attraction3_ticket_frame, bg='#F7F7F7', height=22, width=30,
                                                             highlightbackground='#969695', highlightthickness=1)
                attraction3_adults_quantity_frame.place(x=564, y=128)
                attraction3_adults_quantity_label = tk.Label(attraction3_adults_quantity_frame, bg='#F7F7F7', fg='#000000',
                                                             font=('Arial', 8), text='0')
                attraction3_adults_quantity_label.place(relx=0.5, rely=0.5, anchor='center')
                attraction3_adults_add_button = tk.Button(attraction3_ticket_frame, bg='#F7F7F7', image=add_tk_image, border=0,
                                                          command=lambda: ticket_quantity_add(attraction3_adults_price,
                                                                                              attraction3_adults_quantity_label,
                                                                                              attraction3_adults_total_label))
                attraction3_adults_add_button.place(x=620, y=130)
                attraction3_adults_total_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                                          text='RM 0.00', font=('Arial', 10))
                attraction3_adults_total_label.place(x=780, y=130)
                attraction3_older_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                                   text='Older Adulthood (61-100+)', font=('Arial', 10))
                attraction3_older_label.place(x=12, y=170)
                attraction3_older_price = p_old
                format_attraction3_older_price = "{:.2f}".format(attraction3_older_price)
                attraction3_older_price_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                                         text='RM ' + str(format_attraction3_older_price), font=('Arial', 10))
                attraction3_older_price_label.place(x=320, y=170)
                attraction3_older_minus_button = tk.Button(attraction3_ticket_frame, bg='#F7F7F7', image=minus_tk_image, border=0,
                                                           command=lambda: ticket_quantity_minus(attraction3_older_price,
                                                                                                 attraction3_older_quantity_label,
                                                                                                 attraction3_older_total_label))
                attraction3_older_minus_button.place(x=520, y=170)
                attraction3_older_quantity_frame = tk.Frame(attraction3_ticket_frame, bg='#F7F7F7', height=22, width=30,
                                                            highlightbackground='#969695', highlightthickness=1)
                attraction3_older_quantity_frame.place(x=564, y=168)
                attraction3_older_quantity_label = tk.Label(attraction3_older_quantity_frame, bg='#F7F7F7', fg='#000000',
                                                            font=('Arial', 8), text='0')
                attraction3_older_quantity_label.place(relx=0.5, rely=0.5, anchor='center')
                attraction3_older_add_button = tk.Button(attraction3_ticket_frame, bg='#F7F7F7', image=add_tk_image, border=0,
                                                         command=lambda: ticket_quantity_add(attraction3_older_price,
                                                                                             attraction3_older_quantity_label,
                                                                                             attraction3_older_total_label))
                attraction3_older_add_button.place(x=620, y=170)
                attraction3_older_total_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                                         text='RM 0.00', font=('Arial', 10))
                attraction3_older_total_label.place(x=780, y=170)
                attraction3_total_label = tk.Label(attraction3_ticket_frame, font=('Arial', 12, 'bold'), bg='#F7F7F7',
                                                   fg='#000000',
                                                   text='Total')
                attraction3_total_label.place(x=678, y=210)
                attraction3_amount_label = tk.Label(attraction3_ticket_frame, font=('Arial', 12, 'bold'), bg='#F7F7F7',
                                                    fg='#000000',
                                                    text='RM 0.00')
                attraction3_amount_label.place(x=780, y=210)

                attraction3_back_button = tk.Button(spots_purchase_frame, text='Back', font=('Arial', 11, 'bold'), width=10,
                                                    height=1,
                                                    bg='#F9AA33', fg='#000000', border=0, command=select_attraction)
                attraction3_back_button.grid(row=3, column=0, padx=20, pady=8, sticky='w')
                attraction3_pay_method_frame = tk.Frame(spots_purchase_frame, width=210, height=30, bg='#F9AA33')
                attraction3_pay_method_frame.grid(row=3, column=1, padx=20, pady=8, sticky='e')
                attraction3_pay_method_label = tk.Label(attraction3_pay_method_frame, text='Select payment method', fg='#000000',
                                                        compound=tk.LEFT, image=payment_method_tk_image, bg='#F9AA33')
                attraction3_pay_method_label.place(x=0, y=2)
                attraction3_pay_method_button = tk.Button(attraction3_pay_method_frame, image=payment_method_button_tk_image,
                                                          bg='#F9AA33', border=0, command=show_attraction3_pay_method_menu)
                attraction3_pay_method_button.place(x=180, y=9)
                attraction3_pay_method_frame.bind('<Button-1>', lambda event: show_attraction3_pay_method_menu())
                attraction3_pay_method_label.bind('<Button-1>', lambda event: show_attraction3_pay_method_menu())
                attraction3_pay_method_menu = tk.Menu(spots_purchase_frame, tearoff=0)
                attraction3_pay_method_menu.configure(bg='#F9AA33')
                attraction3_pay_method_menu.add_command(label='TNG eWallet', font=('Arial', 10),
                                                        command=lambda: select_payment_method('TNG eWallet'))
                attraction3_pay_method_menu.add_command(label='Online Banking', font=('Arial', 10),
                                                        command=lambda: select_payment_method('Online Banking'))
                attraction3_pay_method_menu.add_command(label='Credit/Debit Card', font=('Arial', 10),
                                                        command=lambda: select_payment_method('Credit/Debit Card'))
                attraction3_pay_button = tk.Button(spots_purchase_frame, text='Pay', font=('Arial', 11, 'bold'), width=10,
                                                   height=1,
                                                   bg='#F9AA33', fg='#000000', border=0, command=purchase_ticket)
                attraction3_pay_button.grid(row=4, column=1, padx=20, sticky='e')

                attraction3_select_date_frame = tk.Frame(spots_purchase_frame, width=255, height=230, bg='#F7F7F7',
                                                         highlightbackground="#ADB0BC", highlightthickness=2)
                attraction3_select_date_calendar = Calendar(attraction3_select_date_frame, selectmode='day',
                                                            date_pattern='yyyy-mm-dd')
                attraction3_select_date_calendar.place(x=0, y=0)
                attraction3_select_date_button = tk.Button(attraction3_select_date_frame, text='Select', font=('Arial', 8),
                                                           bg='#F5F5F5', width=6, command=choose_attraction3_date)
                attraction3_select_date_button.place(x=160, y=195)
                attraction3_cancel_date_button = tk.Button(attraction3_select_date_frame, text='Cancel', font=('Arial', 8),
                                                           bg='#F5F5F5', width=6, command=cancel_select_attraction3_date)
                attraction3_cancel_date_button.place(x=40, y=195)

                attraction3_remove_date_button = tk.Button(attraction3_select_date_frame, text='Remove', font=('Arial', 8),
                                                           bg='#F5F5F5', width=6, command=remove_attraction3_date)
                attraction3_remove_date_button.place(x=100, y=195)

                select_purchase()

            def attraction_detail(n, r, d, p, a, c, o, t, i):
                for widget in spots_detail_frame.winfo_children():
                    widget.destroy()

                r_filtered_dict = {key: value for key, value in r_image_dict.items() if i in value}
                r_dict_list = list(r_filtered_dict.items())
                r_images = []
                for r_image_list in r_dict_list:
                    r_images.append(r_image_list[1][1])
                number_of_images = len(r_images)

                def previous_image_a():
                    index = int(current_image_index_label.cget('text'))
                    index -= 1
                    if index < 0:
                        index = number_of_images - 1
                    attraction2_label.config(image=r_images[index])
                    current_image_index_label.config(text=str(index))

                def next_image_a():
                    index = int(current_image_index_label.cget('text'))
                    index += 1
                    if index >= number_of_images:
                        index = 0
                    attraction2_label.config(image=r_images[index])
                    current_image_index_label.config(text=str(index))

                previous_button = tk.Button(spots_detail_frame, image=previous_tk_image, bg='#FFFFFF', border=0,
                                            command=previous_image_a)
                previous_button.grid(row=0, column=0, padx=10)
                current_image_index_label = tk.Label(food_beverage_detail_frame, text='0')
                current_image_index = int(current_image_index_label.cget('text'))
                attraction2_label = tk.Label(spots_detail_frame, image=r_images[current_image_index], bg='#FFFFFF')
                attraction2_label.grid(row=0, column=1, pady=20)
                next_button = tk.Button(spots_detail_frame, image=next_tk_image, bg='#FFFFFF', border=0,
                                        command=next_image_a)
                next_button.grid(row=0, column=2, padx=10)

                attraction2_title_label = tk.Label(spots_detail_frame, text=n, bg='#FFFFFF', fg='#000000',
                                                   font=('Arial', 16, 'underline', 'bold'))
                attraction2_title_label.grid(row=1, column=0, columnspan=2, sticky='w', padx=10)
                attraction2_rate_label = tk.Label(spots_detail_frame, bg='#FFFFFF', image=star_tk_image, text=' ' + str(r),
                                                  compound=tk.LEFT,
                                                  font=('Arial', 10, 'bold'))
                attraction2_rate_label.grid(row=1, column=2)
                attraction2_type_label = tk.Label(spots_detail_frame, text=t, bg='#FFFFFF', fg='#000000',
                                                  font=('Arial', 8))
                attraction2_type_label.grid(row=2, column=0, columnspan=3, sticky='w', padx=10)
                attraction2_detail_label = tk.Label(spots_detail_frame, text=d, bg='#FFFFFF', fg='#000000',
                                                    font=('Arial', 11), wraplength=600, justify='left')
                attraction2_detail_label.grid(row=3, column=0, columnspan=3, sticky='w', padx=10, pady=5)

                attraction_second_right_frame = tk.Frame(spots_detail_frame, bg='#FFFFFF', width=260, height=390)
                attraction_second_right_frame.grid(row=0, column=3, rowspan=3, padx=10)
                attraction2_address_title_label = tk.Label(attraction_second_right_frame, text='Address:', bg='#FFFFFF',
                                                           fg='#000000',
                                                           font=('Arial', 11, 'underline', 'bold'))
                attraction2_address_title_label.place(x=20, y=20)
                attraction2_address_label = tk.Label(attraction_second_right_frame, justify='left',
                                                     text=a, bg='#FFFFFF', fg='#000000', font=('Arial', 9), wraplength=230)
                attraction2_address_label.place(x=20, y=41)
                attraction2_contact_title_label = tk.Label(attraction_second_right_frame, text='Contact:', bg='#FFFFFF',
                                                           fg='#000000',
                                                           font=('Arial', 11, 'underline', 'bold'))
                attraction2_contact_title_label.place(x=20, y=80)
                attraction2_contact_label = tk.Label(attraction_second_right_frame, text=c, bg='#FFFFFF',
                                                     fg='#000000', font=('Arial', 9))
                attraction2_contact_label.place(x=20, y=101)
                attraction2_operation_title_label = tk.Label(attraction_second_right_frame, text='Operation hour:', bg='#FFFFFF',
                                                             fg='#000000', font=('Arial', 11, 'underline', 'bold'))
                attraction2_operation_title_label.place(x=20, y=125)
                attraction2_operation_label = tk.Label(attraction_second_right_frame,
                                                       text=o, bg='#FFFFFF', fg='#000000', font=('Arial', 9), justify='left')
                attraction2_operation_label.place(x=20, y=146)
                attraction2_estimated_title_label = tk.Label(attraction_second_right_frame, text='Estimated Price Per Pax:',
                                                             bg='#FFFFFF', fg='#000000', font=('Arial', 11, 'underline', 'bold'))
                attraction2_estimated_title_label.place(x=20, y=265)
                attraction2_estimated_label = tk.Label(attraction_second_right_frame, bg='#FFFFFF',
                                                       fg='#000000', font=('Arial', 9))
                attraction2_estimated_label.place(x=20, y=286)
                if p == '0.00':
                    attraction2_estimated_label.config(text='Free')
                else:
                    attraction2_estimated_label.config(text='RM ' + str(p))
                attraction2_back_button = tk.Button(attraction_second_right_frame, text='Back', border=0, fg='#000000',
                                                    bg='#F9AA33',
                                                    font=('Arial', 11, 'bold'), width=15, height=1, command=select_content_spots)
                attraction2_back_button.place(x=60, y=325)
                attraction2_purchase_button = tk.Button(attraction_second_right_frame, text='Purchase Ticket', border=0,
                                                        fg='#000000',
                                                        bg='#F9AA33', font=('Arial', 11, 'bold'), width=15, height=1,
                                                        command=lambda: attraction_purchase(n, i, o))
                attraction2_purchase_button.place(x=60, y=360)
                if p == '0.00':
                    attraction2_purchase_button.place_forget()

                select_attraction()


def search_filter_attraction():
    def insert_search():
        search_entry.delete(0, tk.END)
        search_entry.config(fg='#7A7373')
        if clear_button:
            clear_button.place_forget()
            search_button.place(x=145, y=4)

    def leave_search():
        s = search_entry.get()
        if s.strip() == '':
            search_entry.insert(0, 'Search')
            search_entry.config(fg='#A49C9C')

    def refresh_a():
        for widget in spots_main_frame.winfo_children():
            widget.destroy()
        cursor.execute('''SELECT * FROM destination WHERE destination_type=%s AND destination_status=%s''', ('attraction', 1))
        attractions = cursor.fetchall()
        various_attraction(attractions)
        search_filter_attraction()

    def clear_search_a():
        search_entry.delete(0, tk.END)
        search_entry.insert(0, 'Search')
        search_entry.config(fg='#A49C9C')
        search_filter_a()
        clear_button.place_forget()
        search_button.place(x=145, y=4)

    def search_filter_a():
        leave_search()
        main_window.focus_set()
        search_query = search_entry.get().strip()
        keys_list = list(checkbox.keys())
        tick_list = []
        for key in keys_list:
            if checkbox[key][1].get() == 1:
                tick_list.append(key)
            if checkbox[key][1].get() == 0:
                if key in tick_list:
                    tick_list.remove(key)
                else:
                    pass

        for widget in spots_main_frame.winfo_children():
            if widget is not spots_content_right_frame:
                widget.destroy()

        if search_query == '' or search_query.isspace() or search_entry.cget('fg') == '#A49C9C':
            if not tick_list:
                cursor.execute('''SELECT * FROM destination WHERE destination_type=%s AND destination_status=%s''',
                               ('attraction', 1))
                attractions = cursor.fetchall()
                various_attraction(attractions)
            elif tick_list:
                query = "SELECT * FROM destination WHERE destination_type=%s AND destination_status=%s AND ("
                query += " OR ".join(["destination_tag=%s" for _ in tick_list])
                query += ")"
                query_args = ('attraction', 1) + tuple(tick for tick in tick_list)
                cursor.execute(query, query_args)
                filter_result = cursor.fetchall()
                various_attraction(filter_result)
        elif search_query:
            search_button.place_forget()
            clear_button.place(x=145, y=4)
            if not tick_list:
                cursor.execute('''SELECT * FROM destination WHERE destination_type=%s AND destination_status=%s AND 
                               (destination_name LIKE %s OR destination_address LIKE %s)''',
                               ('attraction', 1, '%' + search_query + '%', '%' + search_query + '%'))
                search_result = cursor.fetchall()
                various_attraction(search_result)
            if tick_list:
                query = "SELECT * FROM destination WHERE destination_type=%s AND destination_status=%s AND " \
                        "(destination_name LIKE %s OR destination_address LIKE %s)AND ("
                query += " OR ".join(["destination_tag=%s" for _ in tick_list])
                query += ")"
                query_args = ('attraction', 1, '%' + search_query + '%', '%' + search_query + '%') + tuple(tick
                                                                                                           for tick in tick_list)
                cursor.execute(query, query_args)
                search_filter_result = cursor.fetchall()
                various_attraction(search_filter_result)

    spots_content_right_frame = tk.Frame(spots_main_frame, bg='#FFFFFF', width=250, height=455)
    spots_content_right_frame.grid(row=0, column=3, rowspan=3, sticky='n')

    search_frame = tk.Frame(spots_content_right_frame, width=170, height=30, bg='#F7F7F7')
    search_frame.place(x=20, y=20)
    search_entry = tk.Entry(search_frame, width=14, bg='#F7F7F7', font=('Arial', 12), fg='#A49C9C', border=0)
    search_entry.place(x=4, y=4)
    search_entry.insert(0, 'Search')
    search_entry.bind('<FocusIn>', lambda event: insert_search())
    search_entry.bind('<FocusOut>', lambda event: leave_search())
    search_entry.bind('<Return>', lambda event: search_filter_a())
    search_button = tk.Button(search_frame, image=search_tk_image, border=0, bg='#F7F7F7', command=search_filter_a)
    search_button.place(x=145, y=4)
    clear_button = tk.Button(search_frame, image=clear_tk_image, border=0, bg='#F7F7F7',
                             command=clear_search_a)
    refresh_button = tk.Button(spots_content_right_frame, image=refresh_tk_image, border=0, bg='#FFFFFF',
                               command=refresh_a)
    refresh_button.place(x=198, y=23)

    cursor.execute('''SELECT DISTINCT destination_tag FROM destination WHERE destination_type='attraction' ''')
    tags = cursor.fetchall()
    y_tag = 60
    checkbox = {}
    for tag in tags:
        a_tag = tag[0]
        filter_option_var = tk.BooleanVar()
        filter_option_checkbox = tk.Checkbutton(spots_content_right_frame, text=a_tag, font=('Arial', 10),
                                                bg='#FFFFFF', fg='#A49C9C', variable=filter_option_var)
        filter_option_checkbox.place(x=20, y=y_tag)
        checkbox[a_tag] = [filter_option_checkbox, filter_option_var]
        filter_option_checkbox.config(command=search_filter_a)
        y_tag += 25


# Public transportation (Complete)
transport_frame = tk.Frame(content_frame, width=950, height=455, bg='#FFFFFF')
transport_frame.place(x=0, y=65)
transport_canvas = tk.Canvas(transport_frame, height=435, width=950, bg='#FFFFFF', highlightthickness=0)
transport_canvas.place(x=0, y=0)
transport_scrollbar = tk.Scrollbar(transport_frame, orient='vertical')
transport_scrollbar.place(x=933, y=0, height=455)
transport_canvas.configure(yscrollcommand=transport_scrollbar.set)
transport_scrollbar.configure(command=transport_canvas.yview)

transport_content_frame = tk.Frame(transport_canvas, bg='#FFFFFF')

image_cursor.execute('''SELECT transportation_id, transportation_image FROM transportation''')
t_images = image_cursor.fetchall()
t_images_dict = {}
for t_image in t_images:
    transportation_id = t_image[0]
    t_image_stream = BytesIO(t_image[1])
    t_img = Image.open(t_image_stream)
    t_resized_img = t_img.resize((200, 200), Image.LANCZOS)
    t_tk_image = ImageTk.PhotoImage(t_resized_img)
    t_images_dict[transportation_id] = t_tk_image


def various_transport():
    cursor.execute('''SELECT * FROM transportation''')
    transports = cursor.fetchall()
    x_value = 32
    y_value = 0
    count = 0

    def open_link(url):
        webbrowser.open(url)

    for transport in transports:
        t_id = transport[0]
        name = transport[1]
        describe = transport[3]
        web = transport[4]

        if count % 2 == 0:
            y_value = 20
        transport_type_frame = tk.Frame(transport_content_frame, height=230, width=870, bg='#EAEAEA')
        transport_type_frame.pack(padx=x_value, pady=y_value)

        transport_label = tk.Label(transport_type_frame, image=t_images_dict[t_id], bg='#EAEAEA')
        transport_label.place(x=40, y=15)

        transport_name_label = tk.Label(transport_type_frame, text=name, font=('Arial', 17, 'underline', 'bold'),
                                        bg='#EAEAEA', fg='#000000')
        transport_name_label.place(x=280, y=50)
        transport_description_label = tk.Label(transport_type_frame, text=describe,
                                               font=('Arial', 12), bg='#EAEAEA', fg='#000000')
        transport_description_label.place(x=280, y=90)
        transport_link_label = tk.Label(transport_type_frame, wraplength=540, justify='left',
                                        text=web,
                                        font=('Arial', 12, 'underline'), bg='#EAEAEA', fg='blue')
        transport_link_label.place(x=280, y=120)

        transport_link_label.bind("<Button-1>", lambda event, url=web: open_link(url))
        count += 1


# Food & Beverage (Complete)
food_beverage_frame = tk.Frame(content_frame, width=950, height=455)
food_beverage_frame.place(x=0, y=65)


def select_content_food_beverage():
    food_beverage_content_frame.place(x=0, y=0)
    food_beverage_second_frame.place_forget()
    food_beverage_third_frame.place_forget()
    food_beverage_canvas.create_window((0, 0), window=food_beverage_main_frame, anchor="nw")
    food_beverage_main_frame.update_idletasks()
    food_beverage_canvas.configure(scrollregion=food_beverage_canvas.bbox("all"))


def select_restaurant():
    food_beverage_content_frame.place_forget()
    food_beverage_second_frame.place(x=0, y=0)
    food_beverage_third_frame.place_forget()
    food_beverage_second_canvas.create_window((0, 0), window=food_beverage_detail_frame, anchor="nw")
    food_beverage_detail_frame.update_idletasks()
    food_beverage_second_canvas.configure(scrollregion=food_beverage_second_canvas.bbox("all"))


def select_booking():
    food_beverage_content_frame.place_forget()
    food_beverage_second_frame.place_forget()
    food_beverage_third_frame.place(x=0, y=0)
    food_beverage_third_canvas.create_window((0, 0), window=food_beverage_booking_frame, anchor="nw")
    food_beverage_booking_frame.update_idletasks()
    food_beverage_third_canvas.configure(scrollregion=food_beverage_third_canvas.bbox("all"))


# Food & Beverage - Content/Main
food_beverage_content_frame = tk.Frame(food_beverage_frame, width=950, height=455, bg='#FFFFFF')
food_beverage_content_frame.place(x=0, y=0)
food_beverage_canvas = tk.Canvas(food_beverage_content_frame, height=435, width=950, bg='#FFFFFF',
                                 highlightthickness=0)
food_beverage_canvas.place(x=0, y=0)
food_beverage_scrollbar = tk.Scrollbar(food_beverage_content_frame, orient='vertical')
food_beverage_scrollbar.place(x=933, y=0, height=455)
food_beverage_canvas.configure(yscrollcommand=food_beverage_scrollbar.set)
food_beverage_scrollbar.configure(command=food_beverage_canvas.yview)

food_beverage_main_frame = tk.Frame(food_beverage_canvas, bg='#FFFFFF')

# Food & Beverage - Detail
food_beverage_second_frame = tk.Frame(food_beverage_frame, width=950, height=455, bg='#FFFFFF')
food_beverage_second_canvas = tk.Canvas(food_beverage_second_frame, height=435, width=950, bg='#FFFFFF',
                                        highlightthickness=0)
food_beverage_second_canvas.place(x=0, y=0)
food_beverage_second_scrollbar = tk.Scrollbar(food_beverage_second_frame, orient='vertical')
food_beverage_second_scrollbar.place(x=933, y=0, height=455)
food_beverage_second_canvas.configure(yscrollcommand=food_beverage_second_scrollbar.set)
food_beverage_second_scrollbar.configure(command=food_beverage_second_canvas.yview)

food_beverage_detail_frame = tk.Frame(food_beverage_second_canvas, bg='#FFFFFF')

# Food & Beverage - Booking
food_beverage_third_frame = tk.Frame(food_beverage_frame, width=950, height=455, bg='#FFFFFF')
food_beverage_third_canvas = tk.Canvas(food_beverage_third_frame, height=435, width=950, bg='#FFFFFF',
                                       highlightthickness=0)
food_beverage_third_canvas.place(x=0, y=0)
food_beverage_third_scrollbar = tk.Scrollbar(food_beverage_third_frame, orient='vertical')
food_beverage_third_scrollbar.place(x=933, y=0, height=455)
food_beverage_third_canvas.configure(yscrollcommand=food_beverage_third_scrollbar.set)
food_beverage_third_scrollbar.configure(command=food_beverage_third_canvas.yview)

food_beverage_booking_frame = tk.Frame(food_beverage_third_canvas, bg='#FFFFFF')

# Time icon image
time_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/time.png")
time_resize_image = time_image.resize((20, 20), Image.LANCZOS)
time_tk_image = ImageTk.PhotoImage(time_resize_image)


def various_restaurant(restaurant_list):
    num_results = len(restaurant_list)
    row_value = 0
    column_value = 0

    if num_results == 0:
        restaurant_space0_frame = tk.Frame(food_beverage_main_frame, bg='#FFFFFF', width=220, height=200)
        restaurant_space0_frame.grid(row=0, column=0, padx=10)
        restaurant_space1_frame = tk.Frame(food_beverage_main_frame, bg='#FFFFFF', width=220, height=200)
        restaurant_space1_frame.grid(row=0, column=1)
        restaurant_space2_frame = tk.Frame(food_beverage_main_frame, bg='#FFFFFF', width=220, height=200)
        restaurant_space2_frame.grid(row=0, column=2, padx=10)
        restaurant_space3_frame = tk.Frame(food_beverage_main_frame, bg='#FFFFFF', width=220, height=200)
        restaurant_space3_frame.grid(row=1, column=0)
    else:
        for restaurant in restaurant_list:
            name = restaurant[1]
            rate = restaurant[2]
            formatted_rate = "{:.1f}".format(rate)
            price = restaurant[4]
            formatted_price = "{:.2f}".format(price)

            describe = restaurant[3]
            address = restaurant[5]
            contact = restaurant[6]
            operation = restaurant[7]
            tag = restaurant[9]

            if column_value == 0 or column_value == 2:
                x_value = 10
            else:
                x_value = 0

            if row_value % 2 == 0:
                y_value = 20
            else:
                y_value = 0

            restaurant_frame = tk.Frame(food_beverage_main_frame, bg='#EAEAEA', width=220, height=200)
            restaurant_frame.grid(row=row_value, column=column_value, padx=x_value, pady=y_value)

            r_id = restaurant[0]
            filtered_dict = {key: value for key, value in image_dict.items() if r_id in value}
            dict_list = list(filtered_dict.items())
            k = dict_list[0][0]
            restaurant_image_label = tk.Label(restaurant_frame, bg='#EAEAEA', image=image_dict[k][1])
            restaurant_image_label.place(x=3, y=3)

            restaurant_title_label = tk.Label(restaurant_frame, text=name, font=('Arial', 12, 'bold'),
                                              bg='#EAEAEA')
            restaurant_title_label.place(x=3, y=130)
            restaurant_rate_label = tk.Label(restaurant_frame, bg='#EAEAEA', image=star_tk_image,
                                             text=' '+str(formatted_rate),
                                             compound=tk.LEFT, font=('Arial', 10, 'bold'))
            restaurant_rate_label.place(x=3, y=153)
            restaurant_price_label = tk.Label(restaurant_frame, bg='#EAEAEA', text='RM '+str(formatted_price),
                                              font=('Arial', 10, 'bold'))
            restaurant_price_label.place(x=4, y=176)
            if num_results == 1:
                restaurant_space1_frame = tk.Frame(food_beverage_main_frame, bg='#FFFFFF', width=220, height=200)
                restaurant_space1_frame.grid(row=0, column=1)
                restaurant_space2_frame = tk.Frame(food_beverage_main_frame, bg='#FFFFFF', width=220, height=200)
                restaurant_space2_frame.grid(row=0, column=2, padx=10)
                restaurant_space3_frame = tk.Frame(food_beverage_main_frame, bg='#FFFFFF', width=220, height=200)
                restaurant_space3_frame.grid(row=1, column=0)
            elif num_results == 2:
                restaurant_space2_frame = tk.Frame(food_beverage_main_frame, bg='#FFFFFF', width=220, height=200)
                restaurant_space2_frame.grid(row=0, column=2, padx=10)
                restaurant_space3_frame = tk.Frame(food_beverage_main_frame, bg='#FFFFFF', width=220, height=200)
                restaurant_space3_frame.grid(row=1, column=0)
            elif num_results == 3:
                restaurant_space3_frame = tk.Frame(food_beverage_main_frame, bg='#FFFFFF', width=220, height=200)
                restaurant_space3_frame.grid(row=1, column=0)
            restaurant_frame.bind('<Button-1>',
                                  lambda event, n=name, r=formatted_rate, d=describe, p=formatted_price, a=address,
                                  c=contact, o=operation, t=tag, i=r_id: restaurant_detail(n, r, d, p, a, c, o, t, i))
            for widgets in restaurant_frame.winfo_children():
                widgets.bind('<Button-1>',
                             lambda event, n=name, r=formatted_rate, d=describe, p=formatted_price, a=address,
                             c=contact, o=operation, t=tag, i=r_id: restaurant_detail(n, r, d, p, a, c, o, t, i))

            column_value += 1
            if column_value > 2:
                column_value = 0
                row_value += 1

            def restaurant_booking(n1, i1, o1):
                for widget in food_beverage_booking_frame.winfo_children():
                    widget.destroy()

                def show_restaurant3_date_frame():
                    restaurant3_select_date_frame.tkraise()
                    restaurant3_select_date_frame.place(x=22, y=80)

                def choose_restaurant3_date():
                    restaurant3_date_button.config(text=restaurant3_select_date_calendar.get_date())
                    restaurant3_select_date_frame.place_forget()

                def cancel_select_restaurant3_date():
                    restaurant3_select_date_frame.place_forget()

                def remove_restaurant3_date():
                    restaurant3_date_button.config(text='Pick a date')
                    restaurant3_select_date_frame.place_forget()

                def show_restaurant3_time_frame():
                    restaurant3_select_time_frame.tkraise()
                    restaurant3_select_time_frame.place(x=322, y=80)

                def choose_restaurant3_time():
                    hour = restaurant3_hour_spinbox.get()
                    minutes = restaurant3_minutes_spinbox.get()
                    if hour.isdigit() and len(hour) == 2 and minutes.isdigit() and len(minutes) == 2:
                        int_hour = int(hour)
                        int_minutes = int(minutes)
                        if 0 <= int_hour <= 23 and 0 <= int_minutes <= 59:
                            restaurant3_time_button.config(text=hour + ':' + minutes)
                            restaurant3_select_time_frame.place_forget()
                        else:
                            messagebox.showerror("Error", "Invalid time format")
                            restaurant3_hour_spinbox.delete(0, tk.END)
                            restaurant3_hour_spinbox.insert(0, "00")
                            restaurant3_minutes_spinbox.delete(0, tk.END)
                            restaurant3_minutes_spinbox.insert(0, "00")
                    else:
                        messagebox.showerror("Error", "Invalid time format")
                        restaurant3_hour_spinbox.delete(0, tk.END)
                        restaurant3_hour_spinbox.insert(0, "00")
                        restaurant3_minutes_spinbox.delete(0, tk.END)
                        restaurant3_minutes_spinbox.insert(0, "00")

                def cancel_select_restaurant3_time():
                    restaurant3_select_time_frame.place_forget()

                def remove_restaurant3_time():
                    restaurant3_time_button.config(text='Select a time')
                    restaurant3_select_time_frame.place_forget()

                def booking_quantity_add(q_label):
                    text = q_label.cget('text')
                    quantity = int(text)
                    quantity += 1
                    q_label.config(text=str(quantity))
                    booking_total()

                def booking_quantity_minus(q_label):
                    text = q_label.cget('text')
                    quantity = int(text)
                    quantity -= 1
                    if quantity >= 0:
                        q_label.config(text=str(quantity))
                    elif quantity <= 0:
                        pass
                    booking_total()

                def booking_total():
                    infant = int(restaurant3_infant_quantity_label.cget('text'))
                    children = int(restaurant3_children_quantity_label.cget('text'))
                    adults = int(restaurant3_adults_quantity_label.cget('text'))
                    older = int(restaurant3_older_quantity_label.cget('text'))
                    total = infant + children + adults + older
                    if 0 <= total <= 1:
                        restaurant3_guest_label.config(text=str(total) + ' guest')
                    elif total > 1:
                        restaurant3_guest_label.config(text=str(total) + ' guests')

                def book_restaurant():
                    time = restaurant3_time_button.cget('text')
                    date = restaurant3_date_button.cget('text')
                    closed_day = {}
                    per_day = o1.split('\n')
                    open_hour = {}
                    i_day = 0
                    for p in per_day:
                        d = p.split(' ')[0]
                        t = p.split(' ')[1]
                        if t == 'Closed':
                            closed_day[i_day] = d
                        elif t != 'Closed':
                            t_o = t.split('-')[0].strip()
                            t_c = t.split('-')[1].strip()
                            time_format = "%I.%M%p"
                            t_o_format = datetime.datetime.strptime(t_o, time_format).time()
                            t_c_format = datetime.datetime.strptime(t_c, time_format).time()
                            open_hour[i_day] = [d, t_o, t_c, t_o_format, t_c_format]
                        i_day += 1
                    c_day_list = list(closed_day.keys())
                    if ':' in time and '-' in date:
                        hour = int(time.split(':')[0])
                        minutes = int(time.split(':')[1])
                        year = int(date.split('-')[0])
                        month = int(date.split('-')[1])
                        day = int(date.split('-')[2])
                        current_datetime = datetime.datetime.now()
                        booking_datetime = current_datetime.replace(year=year, month=month, day=day,
                                                                    hour=hour, minute=minutes,
                                                                    second=0, microsecond=0)
                        if booking_datetime > current_datetime:
                            guest = restaurant3_guest_label.cget('text')
                            number_guest = float(guest.split(' ')[0])

                            chosen = booking_datetime.weekday()
                            if chosen == 0:
                                previous = 6
                            else:
                                previous = chosen-1
                            s1 = chosen not in c_day_list and (open_hour[chosen][3] <= booking_datetime.time() <= open_hour[chosen][4] or
                                                               (open_hour[chosen][3] >= open_hour[chosen][4] and
                                                                (open_hour[chosen][3] <= booking_datetime.time()
                                                                 or booking_datetime.time() <= open_hour[chosen][4])))
                            s2 = chosen in c_day_list and previous not in c_day_list and (open_hour[previous][3] >=
                                                                                          open_hour[previous][4] >=
                                                                                          booking_datetime.time())
                            if s1 or s2:
                                if number_guest >= 1:
                                    messagebox.showinfo("Success", "Booking successfully, thank you")
                                    select_content_food_beverage()

                                    username = username1_entry.get()
                                    cursor.execute('''SELECT user_id FROM user WHERE user_name=%s''', (username,))
                                    user_id = cursor.fetchone()[0]
                                    booking_date = booking_datetime.date()
                                    booking_time = booking_datetime.time()
                                    formatted_date = booking_date.strftime('%Y-%m-%d')
                                    formatted_time = booking_time.strftime('%H:%M')
                                    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
                                    q_infant = int(restaurant3_infant_quantity_label.cget('text'))
                                    q_children = int(restaurant3_children_quantity_label.cget('text'))
                                    q_adult = int(restaurant3_adults_quantity_label.cget('text'))
                                    q_older = int(restaurant3_older_quantity_label.cget('text'))
                                    cursor.execute('''INSERT INTO purchase_booking (user_id, destination_id, purchase_booking_date,
                                                   purchase_booking_time, quantity_infant, quantity_children,
                                                   quantity_adult, quantity_older, purchase_booking_datetime, purchase_booking_status) 
                                                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                                                   (user_id, i1, formatted_date, formatted_time,
                                                    q_infant, q_children, q_adult, q_older, formatted_datetime, 'Ready'))
                                    database.commit()
                                else:
                                    messagebox.showerror("Error", 'Please select the number of guests')
                            else:
                                message = "The destination is closed on your selected date and time.\n\nHere is the operating hours:\n" \
                                          + o1 + '\n\nPlease select another date and time'
                                messagebox.showerror("Error", message)
                                restaurant3_date_button.config(text='Pick a date')
                                restaurant3_time_button.config(text='Select a time')
                        else:
                            messagebox.showerror("Error", "Selected booking date and time is passed")
                            restaurant3_date_button.config(text='Pick a date')
                            restaurant3_time_button.config(text='Select a time')
                    else:
                        messagebox.showerror('Error', 'Please select a booking date and time')

                restaurant3_title_label = tk.Label(food_beverage_booking_frame, text=n1, bg='#FFFFFF',
                                                   fg='#000000',
                                                   font=('Arial', 16, 'underline', 'bold'))
                restaurant3_title_label.grid(row=0, column=0, padx=20, pady=10, sticky='w', columnspan=3)
                restaurant3_date_frame = tk.Frame(food_beverage_booking_frame, bg='#F7F7F7', width=200, height=30)
                restaurant3_date_frame.grid(row=1, column=0, padx=22, sticky='w')
                restaurant3_date_button = tk.Button(restaurant3_date_frame, bg='#F7F7F7', image=calendar_tk_image,
                                                    text='Pick a date', fg='#A49C9C', compound=tk.LEFT,
                                                    font=('Arial', 10, 'bold'), border=0,
                                                    command=show_restaurant3_date_frame, width=200, anchor='w')
                restaurant3_date_button.place(x=5, y=2)
                restaurant3_time_frame = tk.Frame(food_beverage_booking_frame, bg='#F7F7F7', width=200, height=30)
                restaurant3_time_frame.grid(row=1, column=1, padx=22, sticky='e')
                restaurant3_time_button = tk.Button(restaurant3_time_frame, bg='#F7F7F7', image=time_tk_image, border=0,
                                                    text='Select a time', fg='#A49C9C', compound=tk.LEFT,
                                                    font=('Arial', 10, 'bold'),
                                                    width=200, anchor='w', command=show_restaurant3_time_frame)
                restaurant3_time_button.place(x=5, y=2)

                restaurant3_ticket_frame = tk.Frame(food_beverage_booking_frame, bg='#F7F7F7', width=500, height=250)
                restaurant3_ticket_frame.grid(row=2, column=0, padx=22, pady=8, sticky='w', columnspan=2)
                restaurant3_ticket_label = tk.Label(restaurant3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                                    text='Tickets', font=('Arial', 12, 'bold'))
                restaurant3_ticket_label.place(x=10, y=8)
                restaurant3_infant_label = tk.Label(restaurant3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                                    text='Infant (0-3)', font=('Arial', 10))
                restaurant3_infant_label.place(x=12, y=50)
                restaurant3_infant_minus_button = tk.Button(restaurant3_ticket_frame, bg='#F7F7F7', image=minus_tk_image,
                                                            border=0,
                                                            command=lambda: booking_quantity_minus(
                                                                restaurant3_infant_quantity_label))
                restaurant3_infant_minus_button.place(x=340, y=50)
                restaurant3_infant_quantity_frame = tk.Frame(restaurant3_ticket_frame, bg='#F7F7F7', height=22, width=30,
                                                             highlightbackground='#969695', highlightthickness=1)
                restaurant3_infant_quantity_frame.place(x=384, y=48)
                restaurant3_infant_quantity_label = tk.Label(restaurant3_infant_quantity_frame, bg='#F7F7F7',
                                                             font=('Arial', 8), fg='#000000', text='0')
                restaurant3_infant_quantity_label.place(relx=0.5, rely=0.5, anchor='center')
                restaurant3_infant_add_button = tk.Button(restaurant3_ticket_frame, bg='#F7F7F7', image=add_tk_image,
                                                          border=0,
                                                          command=lambda: booking_quantity_add(
                                                              restaurant3_infant_quantity_label))
                restaurant3_infant_add_button.place(x=440, y=50)
                restaurant3_children_label = tk.Label(restaurant3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                                      text='Children (4-12)', font=('Arial', 10))
                restaurant3_children_label.place(x=12, y=90)
                restaurant3_children_minus_button = tk.Button(restaurant3_ticket_frame, bg='#F7F7F7', image=minus_tk_image,
                                                              border=0,
                                                              command=lambda: booking_quantity_minus(
                                                                  restaurant3_children_quantity_label))
                restaurant3_children_minus_button.place(x=340, y=90)
                restaurant3_children_quantity_frame = tk.Frame(restaurant3_ticket_frame, bg='#F7F7F7', height=22, width=30,
                                                               highlightbackground='#969695', highlightthickness=1)
                restaurant3_children_quantity_frame.place(x=384, y=88)
                restaurant3_children_quantity_label = tk.Label(restaurant3_children_quantity_frame, bg='#F7F7F7',
                                                               fg='#000000',
                                                               font=('Arial', 8), text='0')
                restaurant3_children_quantity_label.place(relx=0.5, rely=0.5, anchor='center')
                restaurant3_children_add_button = tk.Button(restaurant3_ticket_frame, bg='#F7F7F7', image=add_tk_image,
                                                            border=0,
                                                            command=lambda: booking_quantity_add(
                                                                restaurant3_children_quantity_label))
                restaurant3_children_add_button.place(x=440, y=90)
                restaurant3_adults_label = tk.Label(restaurant3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                                    text='Adults (13-60)', font=('Arial', 10))
                restaurant3_adults_label.place(x=12, y=130)
                restaurant3_adults_minus_button = tk.Button(restaurant3_ticket_frame, bg='#F7F7F7', image=minus_tk_image,
                                                            border=0,
                                                            command=lambda: booking_quantity_minus(
                                                                restaurant3_adults_quantity_label))
                restaurant3_adults_minus_button.place(x=340, y=130)
                restaurant3_adults_quantity_frame = tk.Frame(restaurant3_ticket_frame, bg='#F7F7F7', height=22, width=30,
                                                             highlightbackground='#969695', highlightthickness=1)
                restaurant3_adults_quantity_frame.place(x=384, y=128)
                restaurant3_adults_quantity_label = tk.Label(restaurant3_adults_quantity_frame, bg='#F7F7F7', fg='#000000',
                                                             font=('Arial', 8), text='0')
                restaurant3_adults_quantity_label.place(relx=0.5, rely=0.5, anchor='center')
                restaurant3_adults_add_button = tk.Button(restaurant3_ticket_frame, bg='#F7F7F7', image=add_tk_image,
                                                          border=0,
                                                          command=lambda: booking_quantity_add(
                                                              restaurant3_adults_quantity_label))
                restaurant3_adults_add_button.place(x=440, y=130)
                restaurant3_older_label = tk.Label(restaurant3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                                   text='Older Adulthood (61-100+)', font=('Arial', 10))
                restaurant3_older_label.place(x=12, y=170)
                restaurant3_older_minus_button = tk.Button(restaurant3_ticket_frame, bg='#F7F7F7', image=minus_tk_image,
                                                           border=0,
                                                           command=lambda: booking_quantity_minus(
                                                               restaurant3_older_quantity_label))
                restaurant3_older_minus_button.place(x=340, y=170)
                restaurant3_older_quantity_frame = tk.Frame(restaurant3_ticket_frame, bg='#F7F7F7', height=22, width=30,
                                                            highlightbackground='#969695', highlightthickness=1)
                restaurant3_older_quantity_frame.place(x=384, y=168)
                restaurant3_older_quantity_label = tk.Label(restaurant3_older_quantity_frame, bg='#F7F7F7', fg='#000000',
                                                            font=('Arial', 8), text='0')
                restaurant3_older_quantity_label.place(relx=0.5, rely=0.5, anchor='center')
                restaurant3_older_add_button = tk.Button(restaurant3_ticket_frame, bg='#F7F7F7', image=add_tk_image,
                                                         border=0,
                                                         command=lambda: booking_quantity_add(
                                                             restaurant3_older_quantity_label))
                restaurant3_older_add_button.place(x=440, y=170)
                restaurant3_total_label = tk.Label(restaurant3_ticket_frame, font=('Arial', 12, 'bold'), bg='#F7F7F7',
                                                   fg='#000000',
                                                   text='Total')
                restaurant3_total_label.place(x=290, y=210)
                restaurant3_guest_label = tk.Label(restaurant3_ticket_frame, font=('Arial', 12, 'bold'), bg='#F7F7F7',
                                                   fg='#000000',
                                                   text='0 guest')
                restaurant3_guest_label.place(x=392, y=210)

                restaurant3_right_frame = tk.Frame(food_beverage_booking_frame, bg='#FFFFFF', width=365, height=250)
                restaurant3_right_frame.grid(row=2, column=2, pady=8, sticky='e')
                restaurant3_reminder_title_label = tk.Label(restaurant3_right_frame, font=('Arial', 10, 'bold'),
                                                            bg='#FFFFFF',
                                                            fg='#000000', text='*** Reminder ***')
                restaurant3_reminder_title_label.place(x=130, y=5)
                restaurant3_reminder_label = tk.Label(restaurant3_right_frame, font=('Arial', 10), bg='#FFFFFF',
                                                      fg='#000000',
                                                      text='Kindly remember to check in for your reservation within 15 minutes '
                                                           'of the scheduled time, or else it will be automatically cancelled. '
                                                           'Thank you.', wraplength=360, justify='left')
                restaurant3_reminder_label.place(x=3, y=30)

                restaurant3_back_button = tk.Button(food_beverage_booking_frame, text='Back', font=('Arial', 11, 'bold'),
                                                    width=10,
                                                    height=1, bg='#F9AA33', fg='#000000', border=0,
                                                    command=select_restaurant)
                restaurant3_back_button.grid(row=3, column=0, padx=20, pady=8, sticky='w')
                restaurant3_book_button = tk.Button(food_beverage_booking_frame, text='Book', font=('Arial', 11, 'bold'),
                                                    width=10, height=1, bg='#F9AA33', fg='#000000', border=0,
                                                    command=book_restaurant)
                restaurant3_book_button.grid(row=3, column=2, padx=5, sticky='e')

                restaurant3_select_date_frame = tk.Frame(food_beverage_booking_frame, width=255, height=230, bg='#F7F7F7',
                                                         highlightbackground="#ADB0BC", highlightthickness=2)
                restaurant3_select_date_calendar = Calendar(restaurant3_select_date_frame, selectmode='day',
                                                            date_pattern='yyyy-mm-dd')
                restaurant3_select_date_calendar.place(x=0, y=0)
                restaurant3_select_date_button = tk.Button(restaurant3_select_date_frame, text='Select', font=('Arial', 8),
                                                           bg='#F5F5F5', width=6, command=choose_restaurant3_date)
                restaurant3_select_date_button.place(x=160, y=195)
                restaurant3_cancel_date_button = tk.Button(restaurant3_select_date_frame, text='Cancel', font=('Arial', 8),
                                                           bg='#F5F5F5', width=6, command=cancel_select_restaurant3_date)
                restaurant3_cancel_date_button.place(x=40, y=195)

                restaurant3_remove_date_button = tk.Button(restaurant3_select_date_frame, text='Remove', font=('Arial', 8),
                                                           bg='#F5F5F5', width=6, command=remove_restaurant3_date)
                restaurant3_remove_date_button.place(x=100, y=195)

                restaurant3_select_time_frame = tk.Frame(food_beverage_booking_frame, width=255, height=100, bg='#F7F7F7',
                                                         highlightbackground="#ADB0BC", highlightthickness=2)
                restaurant3_24_label = tk.Label(restaurant3_select_time_frame, text='24-hour format',
                                                font=('Arial', 10, 'underline'),
                                                bg='#F5F5F5')
                restaurant3_24_label.place(x=80, y=7)
                restaurant3_hour_spinbox = tk.Spinbox(restaurant3_select_time_frame, from_=00, to=23, width=4,
                                                      justify='center',
                                                      format='%02.0f')
                restaurant3_hour_spinbox.place(x=70, y=36)
                restaurant3_minutes_spinbox = tk.Spinbox(restaurant3_select_time_frame, from_=00, to=59, width=4,
                                                         justify='center',
                                                         format='%02.0f')
                restaurant3_minutes_spinbox.place(x=140, y=36)
                restaurant3_select_time_button = tk.Button(restaurant3_select_time_frame, text='Select', font=('Arial', 8),
                                                           bg='#F5F5F5', width=6, command=choose_restaurant3_time)
                restaurant3_select_time_button.place(x=160, y=65)
                restaurant3_cancel_time_button = tk.Button(restaurant3_select_time_frame, text='Cancel', font=('Arial', 8),
                                                           bg='#F5F5F5', width=6, command=cancel_select_restaurant3_time)
                restaurant3_cancel_time_button.place(x=40, y=65)

                restaurant3_remove_time_button = tk.Button(restaurant3_select_time_frame, text='Remove', font=('Arial', 8),
                                                           bg='#F5F5F5', width=6, command=remove_restaurant3_time)
                restaurant3_remove_time_button.place(x=100, y=65)

                select_booking()

            def restaurant_detail(n, r, d, p, a, c, o, t, i):
                for widget in food_beverage_detail_frame.winfo_children():
                    widget.destroy()

                r_filtered_dict = {key: value for key, value in r_image_dict.items() if i in value}
                r_dict_list = list(r_filtered_dict.items())
                r_images = []
                for r_image_list in r_dict_list:
                    r_images.append(r_image_list[1][1])
                number_of_images = len(r_images)

                def previous_image_r():
                    index = int(current_image_index_label.cget('text'))
                    index -= 1
                    if index < 0:
                        index = number_of_images-1
                    restaurant2_label.config(image=r_images[index])
                    current_image_index_label.config(text=str(index))

                def next_image_r():
                    index = int(current_image_index_label.cget('text'))
                    index += 1
                    if index >= number_of_images:
                        index = 0
                    restaurant2_label.config(image=r_images[index])
                    current_image_index_label.config(text=str(index))

                previous_fb_button = tk.Button(food_beverage_detail_frame, image=previous_tk_image, bg='#FFFFFF',
                                               border=0, command=previous_image_r)
                previous_fb_button.grid(row=0, column=0, padx=10)
                current_image_index_label = tk.Label(food_beverage_detail_frame, text='0')
                current_image_index = int(current_image_index_label.cget('text'))
                restaurant2_label = tk.Label(food_beverage_detail_frame, image=r_images[current_image_index],
                                             bg='#FFFFFF')
                restaurant2_label.grid(row=0, column=1, pady=20)
                next_fb_button = tk.Button(food_beverage_detail_frame, image=next_tk_image, bg='#FFFFFF', border=0,
                                           command=next_image_r)
                next_fb_button.grid(row=0, column=2, padx=10)

                restaurant2_title_label = tk.Label(food_beverage_detail_frame, text=n, bg='#FFFFFF',
                                                   fg='#000000',
                                                   font=('Arial', 16, 'underline', 'bold'))
                restaurant2_title_label.grid(row=1, column=0, columnspan=2, sticky='w', padx=10)
                restaurant2_rate_label = tk.Label(food_beverage_detail_frame, bg='#FFFFFF', image=star_tk_image,
                                                  text=' '+str(r),
                                                  compound=tk.LEFT, font=('Arial', 10, 'bold'))
                restaurant2_rate_label.grid(row=1, column=2)
                restaurant2_type_label = tk.Label(food_beverage_detail_frame, text=t, bg='#FFFFFF', fg='#000000',
                                                  font=('Arial', 8))
                restaurant2_type_label.grid(row=2, column=0, columnspan=3, sticky='w', padx=10)
                restaurant2_detail_label = tk.Label(food_beverage_detail_frame, text=d, bg='#FFFFFF',
                                                    fg='#000000',
                                                    font=('Arial', 11), wraplength=600, justify='left')
                restaurant2_detail_label.grid(row=3, column=0, columnspan=3, sticky='w', padx=10, pady=5)

                restaurant_second_right_frame = tk.Frame(food_beverage_detail_frame, bg='#FFFFFF', width=260,
                                                         height=390)
                restaurant_second_right_frame.grid(row=0, column=3, rowspan=3, padx=10)
                restaurant2_address_title_label = tk.Label(restaurant_second_right_frame, text='Address:', bg='#FFFFFF',
                                                           fg='#000000',
                                                           font=('Arial', 11, 'underline', 'bold'))
                restaurant2_address_title_label.place(x=20, y=20)
                restaurant2_address_label = tk.Label(restaurant_second_right_frame,
                                                     text=a,
                                                     bg='#FFFFFF', fg='#000000', font=('Arial', 9), wraplength=230,
                                                     justify='left')
                restaurant2_address_label.place(x=20, y=41)
                restaurant2_contact_title_label = tk.Label(restaurant_second_right_frame, text='Contact:', bg='#FFFFFF',
                                                           fg='#000000',
                                                           font=('Arial', 11, 'underline', 'bold'))
                restaurant2_contact_title_label.place(x=20, y=80)
                restaurant2_contact_label = tk.Label(restaurant_second_right_frame, text=c, bg='#FFFFFF',
                                                     fg='#000000', font=('Arial', 9))
                restaurant2_contact_label.place(x=20, y=101)
                restaurant2_operation_title_label = tk.Label(restaurant_second_right_frame, text='Operation hour:',
                                                             bg='#FFFFFF',
                                                             fg='#000000', font=('Arial', 11, 'underline', 'bold'))
                restaurant2_operation_title_label.place(x=20, y=125)
                restaurant2_operation_label = tk.Label(restaurant_second_right_frame,
                                                       text=o,
                                                       bg='#FFFFFF', fg='#000000', font=('Arial', 9), justify='left')
                restaurant2_operation_label.place(x=20, y=146)
                restaurant2_estimated_title_label = tk.Label(restaurant_second_right_frame, text='Estimated Price Per Pax:',
                                                             bg='#FFFFFF', fg='#000000',
                                                             font=('Arial', 11, 'underline', 'bold'))
                restaurant2_estimated_title_label.place(x=20, y=265)
                restaurant2_estimated_label = tk.Label(restaurant_second_right_frame, text='RM '+str(p),
                                                       bg='#FFFFFF',
                                                       fg='#000000', font=('Arial', 9))
                restaurant2_estimated_label.place(x=20, y=286)
                restaurant2_back_button = tk.Button(restaurant_second_right_frame, text='Back', border=0, fg='#000000',
                                                    bg='#F9AA33',
                                                    font=('Arial', 11, 'bold'), width=15, height=1,
                                                    command=select_content_food_beverage)
                restaurant2_back_button.place(x=60, y=325)
                restaurant2_booking_button = tk.Button(restaurant_second_right_frame, text='Make Booking', border=0,
                                                       fg='#000000',
                                                       bg='#F9AA33', font=('Arial', 11, 'bold'), width=15, height=1,
                                                       command=lambda: restaurant_booking(n, i, o))
                restaurant2_booking_button.place(x=60, y=360)

                select_restaurant()


def search_filter_restaurant():
    def insert_search_fb():
        search_fb_entry.delete(0, tk.END)
        search_fb_entry.config(fg='#7A7373')
        if clear_fb_button:
            clear_fb_button.place_forget()
            search_fb_button.place(x=145, y=4)

    def leave_search_fb():
        s = search_fb_entry.get()
        if s.strip() == '':
            search_fb_entry.insert(0, 'Search')
            search_fb_entry.config(fg='#A49C9C')

    def refresh():
        for widget in food_beverage_main_frame.winfo_children():
            widget.destroy()
        cursor.execute('''SELECT * FROM destination WHERE destination_type=%s AND destination_status=%s''', ('restaurant', 1))
        restaurants = cursor.fetchall()
        various_restaurant(restaurants)
        search_filter_restaurant()

    def clear_search():
        search_fb_entry.delete(0, tk.END)
        search_fb_entry.insert(0, 'Search')
        search_fb_entry.config(fg='#A49C9C')
        search_filter()
        clear_fb_button.place_forget()
        search_fb_button.place(x=145, y=4)

    def search_filter():
        leave_search_fb()
        main_window.focus_set()
        search_query = search_fb_entry.get().strip()
        keys_list = list(checkbox.keys())
        tick_list = []
        for key in keys_list:
            if checkbox[key][1].get() == 1:
                tick_list.append(key)
            if checkbox[key][1].get() == 0:
                if key in tick_list:
                    tick_list.remove(key)
                else:
                    pass

        for widget in food_beverage_main_frame.winfo_children():
            if widget is not fb_content_right_frame:
                widget.destroy()

        if search_query == '' or search_query.isspace() or search_fb_entry.cget('fg') == '#A49C9C':
            if not tick_list:
                cursor.execute('''SELECT * FROM destination WHERE destination_type=%s AND destination_status=%s''',
                               ('restaurant', 1))
                restaurants = cursor.fetchall()
                various_restaurant(restaurants)
            elif tick_list:
                query = "SELECT * FROM destination WHERE destination_type=%s AND destination_status=%s AND ("
                query += " OR ".join(["destination_tag=%s" for _ in tick_list])
                query += ")"
                query_args = ('restaurant', 1) + tuple(tick for tick in tick_list)
                cursor.execute(query, query_args)
                filter_result = cursor.fetchall()
                various_restaurant(filter_result)
        elif search_query:
            search_fb_button.place_forget()
            clear_fb_button.place(x=145, y=4)
            if not tick_list:
                cursor.execute('''SELECT * FROM destination WHERE destination_type=%s AND destination_status=%s AND 
                               (destination_name LIKE %s OR destination_address LIKE %s)''',
                               ('restaurant', 1, '%'+search_query+'%', '%'+search_query+'%'))
                search_result = cursor.fetchall()
                various_restaurant(search_result)
            if tick_list:
                query = "SELECT * FROM destination WHERE destination_type=%s AND destination_status=%s AND " \
                        "(destination_name LIKE %s OR destination_address LIKE %s)AND ("
                query += " OR ".join(["destination_tag=%s" for _ in tick_list])
                query += ")"
                query_args = ('restaurant', 1, '%'+search_query+'%', '%'+search_query+'%') + tuple(tick
                                                                                                   for tick in tick_list)
                cursor.execute(query, query_args)
                search_filter_result = cursor.fetchall()
                various_restaurant(search_filter_result)

    fb_content_right_frame = tk.Frame(food_beverage_main_frame, bg='#FFFFFF', width=250, height=435)
    fb_content_right_frame.grid(row=0, column=3, rowspan=2, sticky='n')

    search_fb_frame = tk.Frame(fb_content_right_frame, width=170, height=30, bg='#F7F7F7')
    search_fb_frame.place(x=20, y=20)
    search_fb_entry = tk.Entry(search_fb_frame, width=14, bg='#F7F7F7', font=('Arial', 12), fg='#A49C9C', border=0)
    search_fb_entry.place(x=4, y=4)
    search_fb_entry.insert(0, 'Search')
    search_fb_entry.bind('<FocusIn>', lambda event: insert_search_fb())
    search_fb_entry.bind('<FocusOut>', lambda event: leave_search_fb())
    search_fb_entry.bind('<Return>', lambda event: search_filter())
    search_fb_button = tk.Button(search_fb_frame, image=search_tk_image, border=0, bg='#F7F7F7',
                                 command=search_filter)
    search_fb_button.place(x=145, y=4)
    clear_fb_button = tk.Button(search_fb_frame, image=clear_tk_image, border=0, bg='#F7F7F7',
                                command=clear_search)
    refresh_fb_button = tk.Button(fb_content_right_frame, image=refresh_tk_image, border=0, bg='#FFFFFF',
                                  command=refresh)
    refresh_fb_button.place(x=198, y=23)

    cursor.execute('''SELECT DISTINCT destination_tag FROM destination WHERE destination_type='restaurant' ''')
    tags = cursor.fetchall()
    y_tag = 60
    checkbox = {}
    for tag in tags:
        r_tag = tag[0]
        filter_option_fb_var = tk.BooleanVar()
        filter_option_fb_checkbox = tk.Checkbutton(fb_content_right_frame, text=r_tag, font=('Arial', 10),
                                                   bg='#FFFFFF', fg='#A49C9C', variable=filter_option_fb_var)
        filter_option_fb_checkbox.place(x=20, y=y_tag)
        checkbox[r_tag] = [filter_option_fb_checkbox, filter_option_fb_var]
        filter_option_fb_checkbox.config(command=search_filter)
        y_tag += 25


# Games
games_content_frame = tk.Frame(content_frame, width=950, height=455, bg='#FFFFFF')


shuffled_options = {}
def fetch_and_shuffle_options(question_id):
    if question_id not in shuffled_options:
        query = "SELECT games_option1_correct, games_option2, games_option3, " \
                "games_option4 FROM games WHERE games_id = %s"
        cursor.execute(query, (question_id,))
        result = cursor.fetchone()
        options = list(result)
        random.shuffle(options)
        shuffled_options[question_id] = options
    return shuffled_options[question_id]


def fetch_question_text(question_id):
    query = "SELECT games_question FROM games WHERE games_id = %s"
    cursor.execute(query, (question_id,))
    result = cursor.fetchone()
    return result[0]


def fetch_correct_option(question_id):
    query = "SELECT games_option1_correct FROM games WHERE games_id = %s"
    cursor.execute(query, (question_id,))
    result = cursor.fetchone()
    return result[0]


def fetch_all_questions():
    query = "SELECT games_id, games_question FROM games"
    cursor.execute(query)
    questions = cursor.fetchall()
    return questions


def display_questions_list():
    questions = fetch_all_questions()

    # Clear any existing text on the buttons and reset their color
    for button in [question_button, question1_button, question2_button, question3_button, question4_button,
                   question5_button, question6_button, question7_button, question8_button]:
        button.config(text="", fg='#7F7C7C')

    # Clear the images from the option labels
    games_option1_label.config(image="")
    games_option2_label.config(image="")
    games_option3_label.config(image="")
    games_option4_label.config(image="")

    # Display the first five questions with numbering
    for i in range(min(10, len(questions))):
        question_id, question_text = questions[i]
        button = None

        # Determine which button to use based on the iteration
        if i == 0:
            button = question_button
        elif i == 1:
            button = question1_button
        elif i == 2:
            button = question2_button
        elif i == 3:
            button = question3_button
        elif i == 4:
            button = question4_button
        elif i == 5:
            button = question5_button
        elif i == 6:
            button = question6_button
        elif i == 7:
            button = question7_button
        elif i == 8:
            button = question8_button

        # Display the question with numbering and set its color to white
        if i == current_question_index:
            button.config(
                text=f"{question_id}. {question_text}",
                fg='#FFFFFF',
                command=lambda question_id=question_id: display_questions(question_id)
            )
        else:
            button.config(
                text=f"{question_id}. {question_text}",
                command=lambda question_id=question_id: display_questions(question_id)
            )

def load_user_answers(user_id):
    try:
        query = "SELECT games_id, user_option_choice FROM gameshistory WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        results = cursor.fetchall()
        user_answers = {}

        for result in results:
            question_id, selected_option = result
            user_answers[question_id] = {
                'selected_option': selected_option,
            }

        return user_answers
    except Exception as e:
        print("Error loading user answers:", e)
        return {}


current_question_index = 0
def display_questions(question_id):
    global current_question_index

    current_question_index = questions.index((question_id, fetch_question_text(question_id)))

    # Fetch and display the question text and games_id
    question_text = fetch_question_text(question_id)
    games_question_label.config(text=f"{question_id}. {question_text}")

    options = fetch_and_shuffle_options(question_id)

    # Update option buttons and labels
    games_option1_button.config(text=options[0], command=lambda: check_answer(options[0], question_id))
    games_option2_button.config(text=options[1], command=lambda: check_answer(options[1], question_id))
    games_option3_button.config(text=options[2], command=lambda: check_answer(options[2], question_id))
    games_option4_button.config(text=options[3], command=lambda: check_answer(options[3], question_id))

    # Clear answer labels and images
    games_option1_label.config(text="")
    games_option2_label.config(text="")
    games_option3_label.config(text="")
    games_option4_label.config(text="")

    # Display the correct or wrong images based on the user's previous answers
    if question_id in user_answers:
        selected_option = user_answers[question_id]['selected_option']
        correct = user_answers[question_id]['correct']
        option_labels = {
            games_option1_button.cget("text"): games_option1_label,
            games_option2_button.cget("text"): games_option2_label,
            games_option3_button.cget("text"): games_option3_label,
            games_option4_button.cget("text"): games_option4_label,
        }

        for option_text, option_label in option_labels.items():
            if option_text == selected_option:
                if correct:
                    option_label.config(image=correct_tk_image)
                else:
                    option_label.config(image=wrong_tk_image)
            elif option_text == fetch_correct_option(question_id):
                option_label.config(image=correct_tk_image)
            else:
                option_label.config(image=wrong_tk_image)
    if question_id in user_answers:
        games_option1_button.config(state="disabled")
        games_option2_button.config(state="disabled")
        games_option3_button.config(state="disabled")
        games_option4_button.config(state="disabled")

    update_arrow_next_state()
    update_arrow_back_state()
    close_games_list()


user_name = username1_entry.get()
cursor.execute('SELECT user_id FROM USER where user_name=%s', (user_name,))
user_id = cursor.fetchone()

user_answers = load_user_answers(user_id)


def check_answer(selected_option, question_id):
    correct_option = fetch_correct_option(question_id)

    # Determine which option label corresponds to the selected option
    option_labels = {
        games_option1_button.cget("text"): games_option1_label,
        games_option2_button.cget("text"): games_option2_label,
        games_option3_button.cget("text"): games_option3_label,
        games_option4_button.cget("text"): games_option4_label,
    }

    # Store the user's answer and whether it's correct
    user_answers[question_id] = {
        'selected_option': selected_option,
        'correct': selected_option == correct_option
    }

    user_name = username1_entry.get()
    cursor.execute('SELECT user_id FROM USER where user_name=%s', (user_name,))
    user_id = cursor.fetchone()

    record_user_answer(user_id, question_id, selected_option)

    # Disable option buttons after user answers
    games_option1_button.config(state="disabled", disabledforeground="white")
    games_option2_button.config(state="disabled", disabledforeground="white")
    games_option3_button.config(state="disabled", disabledforeground="white")
    games_option4_button.config(state="disabled", disabledforeground="white")

    # Show the correct or wrong image based on the answer
    for option_text, option_label in option_labels.items():
        if option_text == selected_option:
            if option_text == correct_option:
                option_label.config(image=correct_tk_image)
            else:
                option_label.config(image=wrong_tk_image)
        elif option_text == correct_option:
            option_label.config(image=correct_tk_image)
        else:
            option_label.config(image=wrong_tk_image)


questions = fetch_all_questions()
def next_question():
    global current_question_index

    # Enable option buttons for the next question
    games_option1_button.config(state="normal")
    games_option2_button.config(state="normal")
    games_option3_button.config(state="normal")
    games_option4_button.config(state="normal")

    # Clear correct and wrong images on labels
    games_option1_label.config(image="")
    games_option2_label.config(image="")
    games_option3_label.config(image="")
    games_option4_label.config(image="")

    current_question_index += 1
    if current_question_index < len(questions):
        question_id, _ = questions[current_question_index]
        display_questions(question_id)
        update_arrow_back_state()
        update_arrow_next_state()
    else:
        arrow_next_button.config(state='disabled')
        pass


def update_arrow_back_state():
    # Enable or disable the arrow back button based on the current_question_index
    if current_question_index > 0:
        arrow_back_button.config(state="normal")
    else:
        arrow_back_button.config(state="disabled")


def update_arrow_next_state():
    # Enable or disable the arrow next button based on the current_question_index
    if current_question_index < len(questions) - 1:
        arrow_next_button.config(state="normal")
    else:
        arrow_next_button.config(state="disabled")


def previous_question():
    global current_question_index

    games_option1_button.config(state="normal")
    games_option2_button.config(state="normal")
    games_option3_button.config(state="normal")
    games_option4_button.config(state="normal")

    games_option1_label.config(image="")
    games_option2_label.config(image="")
    games_option3_label.config(image="")
    games_option4_label.config(image="")

    # Ensure we don't go back beyond the first question
    if current_question_index > 0:
        current_question_index -= 1
        question_id, _ = questions[current_question_index]
        display_questions(question_id)
        update_arrow_back_state()
        update_arrow_next_state()
        arrow_next_button.config(image=arrow_next_tk_image)


def record_user_answer(user_id, question_id, selected_option):
    try:
        if user_id is not None and question_id is not None:
            # Extract the values from the tuple
            user_id = user_id[0]  # Assuming user_id is the first element in the tuple
            question_id = question_id

            # Insert a new record into gameshistory with the selected option
            is_correct = selected_option == fetch_correct_option(question_id)
            query = "INSERT INTO gameshistory (user_id, games_id, user_option_choice, is_correct) " \
                    "VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (user_id, question_id, selected_option, is_correct))
            database.commit()

        else:
            print("Error recording user answer: user_id or question_id is None or invalid.")
    except Exception as e:
        print("Error recording user answer:", e)


def on_mouse_wheel(event):
    games_question_list_canvas.yview_scroll(-1*(event.delta//120), "units")


def open_games_list():
    games_question_list_frame.place(x=150, y=20)
    games_question_list_canvas.create_window((0, 0), window=question_list_frame, anchor="nw")
    question_list_frame.update_idletasks()
    games_question_list_canvas.configure(scrollregion=games_question_list_canvas.bbox("all"))
    games_question_list_canvas.bind_all("<MouseWheel>", on_mouse_wheel)
    display_questions_list()
    arrow_back_button.config(image='')
    arrow_next_button.config(image='')


def close_games_list():
    games_question_list_frame.place_forget()
    arrow_back_button.config(image=arrow_back_tk_image)
    arrow_next_button.config(image=arrow_next_tk_image)


games_board_frame = tk.Frame(games_content_frame, width=650, height=190, bg='#232F34')
games_board_frame.place(x=150, y=20)
games_list_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/list.png")
games_list_resize_image = games_list_image.resize((30, 30), Image.LANCZOS)
games_list_tk_image = ImageTk.PhotoImage(games_list_resize_image)
games_list_button = tk.Button(games_board_frame, border=0, bg='#232F34', image=games_list_tk_image,
                              command=open_games_list)
games_list_button.place(x=10, y=8)

games_question_label = tk.Label(games_board_frame, bg='#232F34', fg='#FFFFFF', wraplength=530, justify='left',
                                font=('Arial', 12))
games_question_label.place(x=50, y=45)
games_option1_button = tk.Button(games_content_frame, width=78, height=2, bg='#4A6572', border=0,
                                 fg='#FFFFFF', anchor='w')
games_option1_button.place(x=198, y=230)
games_option2_button = tk.Button(games_content_frame, width=78, height=2, bg='#4A6572', border=0,
                                 fg='#FFFFFF', anchor='w')
games_option2_button.place(x=198, y=285)
games_option3_button = tk.Button(games_content_frame, width=78, height=2, bg='#4A6572', border=0,
                                 fg='#FFFFFF', anchor='w')
games_option3_button.place(x=198, y=340)
games_option4_button = tk.Button(games_content_frame, width=78, height=2, bg='#4A6572', border=0,
                                 fg='#FFFFFF', anchor='w')
games_option4_button.place(x=198, y=395)

correct_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/correct.png")
correct_resize_image = correct_image.resize((30, 30), Image.LANCZOS)
correct_tk_image = ImageTk.PhotoImage(correct_resize_image)
wrong_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/wrong.png")
wrong_resize_image = wrong_image.resize((30, 30), Image.LANCZOS)
wrong_tk_image = ImageTk.PhotoImage(wrong_resize_image)
games_option1_label = tk.Label(games_content_frame, bg='#FFFFFF')
games_option1_label.place(x=760, y=230)
games_option2_label = tk.Label(games_content_frame, bg='#FFFFFF')
games_option2_label.place(x=760, y=285)
games_option3_label = tk.Label(games_content_frame, bg='#FFFFFF')
games_option3_label.place(x=760, y=340)
games_option4_label = tk.Label(games_content_frame, bg='#FFFFFF')
games_option4_label.place(x=760, y=395)

games_question_list_frame = tk.Frame(games_content_frame, width=650, height=420)
games_question_list_canvas = tk.Canvas(games_question_list_frame, height=420, width=650, bg='#232F34')
games_question_list_canvas.place(x=0, y=0)
games_question_list_scrollbar = tk.Scrollbar(games_question_list_frame, orient='vertical')
games_question_list_scrollbar.place(x=633, y=1, height=419)
games_question_list_canvas.configure(yscrollcommand=games_question_list_scrollbar.set)
games_question_list_scrollbar.configure(command=games_question_list_canvas.yview)

question_list_frame = tk.Frame(games_question_list_canvas, bg='#232F34')

close_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/close.png")
close_resize_image = close_image.resize((30, 30), Image.LANCZOS)
close_tk_image = ImageTk.PhotoImage(close_resize_image)
close_button = tk.Button(question_list_frame, border=0, bg='#232F34', image=close_tk_image,
                         command=close_games_list)
close_button.grid(row=0, column=0, padx=8, pady=8)
question_button = tk.Button(question_list_frame, bg='#232F34', fg='#FFFFFF', wraplength=530, justify='left',
                            font=('Arial', 12), border=0,
                            command=display_questions)
question_button.grid(row=1, column=1, sticky=tk.W)
question1_button = tk.Button(question_list_frame, bg='#232F34', fg='#7F7C7C', wraplength=530, justify='left',
                             font=('Arial', 12), border=0,
                             command=display_questions)
question1_button.grid(row=2, column=1, pady=8, sticky=tk.W)
question2_button = tk.Button(question_list_frame, bg='#232F34', fg='#7F7C7C', wraplength=530, justify='left',
                             font=('Arial', 12), border=0,
                             command=display_questions)
question2_button.grid(row=3, column=1, pady=8, sticky=tk.W)
question3_button = tk.Button(question_list_frame, bg='#232F34', fg='#7F7C7C', wraplength=530, justify='left',
                             font=('Arial', 12), border=0,
                             command=display_questions)
question3_button.grid(row=4, column=1, pady=8, sticky=tk.W)
question4_button = tk.Button(question_list_frame, bg='#232F34', fg='#7F7C7C', wraplength=530, justify='left',
                             font=('Arial', 12), border=0,
                             command=display_questions)
question4_button.grid(row=5, column=1, pady=8, sticky=tk.W)
question5_button = tk.Button(question_list_frame, bg='#232F34', fg='#7F7C7C', wraplength=530, justify='left',
                             font=('Arial', 12), border=0,
                             command=display_questions)
question5_button.grid(row=6, column=1, pady=8, sticky=tk.W)
question6_button = tk.Button(question_list_frame, bg='#232F34', fg='#7F7C7C', wraplength=530, justify='left',
                             font=('Arial', 12), border=0,
                             command=display_questions)
question6_button.grid(row=7, column=1, pady=8, sticky=tk.W)
question7_button = tk.Button(question_list_frame, bg='#232F34', fg='#7F7C7C', wraplength=530, justify='left',
                             font=('Arial', 12), border=0,
                             command=display_questions)
question7_button.grid(row=8, column=1, pady=8, sticky=tk.W)
question8_button = tk.Button(question_list_frame, bg='#232F34', fg='#7F7C7C', wraplength=530, justify='left',
                             font=('Arial', 12), border=0,
                             command=display_questions)
question8_button.grid(row=9, column=1, pady=8, sticky=tk.W)

arrow_next_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/games_next.png")
arrow_next_resize_image = arrow_next_image.resize((30, 30), Image.LANCZOS)
arrow_next_tk_image = ImageTk.PhotoImage(arrow_next_resize_image)
arrow_next_button = tk.Button(games_content_frame, border=0, bg='#232F34', image=arrow_next_tk_image,
                              command=next_question)
arrow_next_button.place(x=750, y=170)
arrow_back_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/games_back.png")
arrow_back_resize_image = arrow_back_image.resize((30, 30), Image.LANCZOS)
arrow_back_tk_image = ImageTk.PhotoImage(arrow_back_resize_image)
arrow_back_button = tk.Button(games_content_frame, border=0, bg='#232F34', image=arrow_back_tk_image,
                              command=previous_question)
arrow_back_button.place(x=170, y=170)

if questions:
    first_question_id, _ = questions[0]
    display_questions(first_question_id)
    update_arrow_back_state()
    update_arrow_next_state()

# Map Page
map_frame = tk.Frame(center_frame, width=950, height=520, bg='#FFFFFF')

map_title_frame = tk.Frame(map_frame, width=950, height=65, bg='#E5F2F8')
map_title_frame.place(x=0, y=0)

map_title_text = tk.Label(map_title_frame, text='Maps', font=('Times New Roman', 18),
                          bg='#E5F2F8', fg='#000000')
map_title_text.place(relx=0.5, rely=0.5, anchor='center')

back_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/back.png")
back_resize_image = back_image.resize((30, 30), Image.LANCZOS)
back_tk_image = ImageTk.PhotoImage(back_resize_image)
map_back_button = tk.Button(map_title_frame, border=0, bg='#E5F2F8', image=back_tk_image,
                            command=switch_to_main)
map_back_button.place(x=25, y=18)

# Feedback Page (Complete)
feedback_frame = tk.Frame(center_frame, width=950, height=520, bg='#FFFFFF')

feedback_title_frame = tk.Frame(feedback_frame, width=950, height=65, bg='#E5F2F8')
feedback_title_frame.place(x=0, y=0)

feedback_title_text = tk.Label(feedback_title_frame, text='User Feedback Form', font=('Times New Roman', 18),
                               bg='#E5F2F8', fg='#000000')
feedback_title_text.place(relx=0.5, rely=0.5, anchor='center')

feedback_back_button = tk.Button(feedback_title_frame, border=0, bg='#E5F2F8', image=back_tk_image,
                                 command=switch_to_main)
feedback_back_button.place(x=25, y=18)

feedback_canvas = tk.Canvas(feedback_frame, height=455, width=950, bg='#FFFFFF')
feedback_canvas.place(x=0, y=65)
feedback_scrollbar = tk.Scrollbar(feedback_frame, orient='vertical')
feedback_scrollbar.place(x=933, y=65, height=455)
feedback_canvas.configure(yscrollcommand=feedback_scrollbar.set)
feedback_scrollbar.configure(command=feedback_canvas.yview)

feedback_content_frame = tk.Frame(feedback_canvas, bg='#FFFFFF')


def create_feedback_form():
    for widget in feedback_content_frame.winfo_children():
        widget.destroy()

    def submit_form():
        s_keys_list = list(s_dict.keys())
        s_tick_list = []
        for key in s_keys_list:
            if s_dict[key][1].get() == 1:
                s_tick_list.append(key)
            if s_dict[key][1].get() == 0:
                if key in s_tick_list:
                    s_tick_list.remove(key)
                else:
                    pass

        i_keys_list = list(i_dict.keys())
        i_tick_list = []
        for key in i_keys_list:
            if i_dict[key][1].get() == 1:
                i_tick_list.append(key)
            if i_dict[key][1].get() == 0:
                if key in i_tick_list:
                    i_tick_list.remove(key)
                else:
                    pass

        count_true = sum(var.get() for var in f_type_list)
        text_detail = f_detail.get('1.0', 'end-1c')

        if count_true == 1:
            if s_tick_list and i_tick_list:
                if text_detail.strip() and not text_detail.isspace():
                    messagebox.showinfo('Success', 'Submit successfully, thanks for your feedback')
                    switch_to_feedback()

                    username = username1_entry.get()
                    cursor.execute('''SELECT user_id FROM user WHERE user_name=%s''', (username,))
                    user_id = cursor.fetchone()[0]
                    feedback_type = 'None'
                    if f_type_list[0].get() == 1:
                        feedback_type = 'Suggestion'
                    elif f_type_list[1].get() == 1:
                        feedback_type = 'Compliment'
                    elif f_type_list[2].get() == 1:
                        feedback_type = 'Complaint'
                    feedback_detail = text_detail
                    feedback_datetime = datetime.datetime.now()
                    formatted_datetime = feedback_datetime.strftime('%Y-%m-%d %H:%M:%S')
                    cursor.execute('''INSERT INTO feedback (user_id, feedback_type, feedback_details, feedback_datetime)
                                   VALUES (%s, %s, %s, %s)''', (user_id, feedback_type, feedback_detail, formatted_datetime))
                    database.commit()
                    cursor.execute('''SELECT feedback_id FROM feedback WHERE user_id=%s AND feedback_datetime=%s''',
                                   (user_id, formatted_datetime))
                    feedback_id = cursor.fetchone()[0]
                    for s_ticked_id in s_tick_list:
                        cursor.execute('''INSERT INTO feedback_service (feedback_id, service_id) 
                                       VALUES (%s, %s)''', (feedback_id, s_ticked_id))
                        database.commit()
                    for i_ticked_id in i_tick_list:
                        cursor.execute('''INSERT INTO feedback_issue (feedback_id, issue_id) 
                                       VALUES (%s, %s)''', (feedback_id, i_ticked_id))
                        database.commit()
                else:
                    messagebox.showerror('Error', 'Please fill in the details for better clarity')
            elif not s_tick_list:
                messagebox.showerror('Error', 'Please select AT LEAST ONE service for the feedback')
            elif not i_tick_list:
                messagebox.showerror('Error', 'Please select AT LEAST ONE issue for the feedback')
        elif count_true > 1:
            messagebox.showerror('Error', 'Please select ONLY ONE type for this feedback form')
        elif count_true < 1:
            messagebox.showerror('Error', 'Please select AT LEAST ONE type for this feedback form')

    f_first_frame = tk.Frame(feedback_content_frame, bg='#FFFFFF', width=950, height=80)
    f_first_frame.grid(row=0, column=0, columnspan=2)
    f_second_frame = tk.Frame(feedback_content_frame, bg='#FFFFFF', width=475, height=250)
    f_second_frame.grid(row=1, column=0)
    f_third_frame = tk.Frame(feedback_content_frame, bg='#FFFFFF', width=475, height=250)
    f_third_frame.grid(row=1, column=1)
    f_forth_frame = tk.Frame(feedback_content_frame, bg='#FFFFFF', width=950, height=300)
    f_forth_frame.grid(row=2, column=0, columnspan=2)

    f_first_label = tk.Label(f_first_frame, bg='#FFFFFF', fg='#000000', text='1. This feedback form is a :',
                             font=('Arial', 12, 'bold'))
    f_first_label.place(x=25, y=25)
    f_suggest_var = tk.BooleanVar()
    f_suggest_box = tk.Checkbutton(f_first_frame, bg='#FFFFFF', fg='#000000', text='Suggestion', variable=f_suggest_var,
                                   font=('Arial', 12))
    f_suggest_box.place(x=320, y=23)
    f_comp_var = tk.BooleanVar()
    f_comp_box = tk.Checkbutton(f_first_frame, bg='#FFFFFF', fg='#000000', text='Compliment', variable=f_comp_var,
                                font=('Arial', 12))
    f_comp_box.place(x=530, y=23)
    f_complaint_var = tk.BooleanVar()
    f_complaint_box = tk.Checkbutton(f_first_frame, bg='#FFFFFF', fg='#000000', text='Complaint', variable=f_complaint_var,
                                     font=('Arial', 12))
    f_complaint_box.place(x=740, y=23)
    f_separate_frame = tk.Frame(f_first_frame, bg='#A49C9C', width=950, height=2)
    f_separate_frame.place(x=0, y=78)
    f_type_list = [f_suggest_var, f_comp_var, f_complaint_var]

    f_second_label = tk.Label(f_second_frame, bg='#FFFFFF', fg='#000000', text='2. About which service(s)?',
                              font=('Arial', 12, 'bold'))
    f_second_label.place(x=25, y=20)
    cursor.execute('''SELECT DISTINCT service_type FROM service ''')
    services = cursor.fetchall()
    y_service = 50
    s_id = 1
    s_dict = {}
    for service in services:
        service_name = service[0]
        s_var = tk.BooleanVar()
        s_checkbox = tk.Checkbutton(f_second_frame, text=service_name, font=('Arial', 12),
                                    bg='#FFFFFF', fg='#000000', variable=s_var)
        s_checkbox.place(x=40, y=y_service)
        s_dict[s_id] = [s_checkbox, s_var, service_name]
        y_service += 30
        s_id += 1

    f_third_label = tk.Label(f_third_frame, bg='#FFFFFF', fg='#000000', text='3. About what issue(s)?',
                             font=('Arial', 12, 'bold'))
    f_third_label.place(x=25, y=20)
    cursor.execute('''SELECT DISTINCT issue_type FROM issue ''')
    issues = cursor.fetchall()
    y_issue = 50
    i_id = 1
    i_dict = {}
    for issue in issues:
        issue_name = issue[0]
        i_var = tk.BooleanVar()
        i_checkbox = tk.Checkbutton(f_third_frame, text=issue_name, font=('Arial', 12),
                                    bg='#FFFFFF', fg='#000000', variable=i_var)
        i_checkbox.place(x=40, y=y_issue)
        i_dict[i_id] = [i_checkbox, i_var, issue_name]
        y_issue += 30
        i_id += 1

    s_separate_frame = tk.Frame(f_forth_frame, bg='#A49C9C', width=950, height=2)
    s_separate_frame.place(x=0, y=0)
    f_forth_label = tk.Label(f_forth_frame, bg='#FFFFFF', fg='#000000', text='4. Please write details of your feedback here :',
                             font=('Arial', 12, 'bold'))
    f_forth_label.place(x=25, y=22)
    f_detail = tk.Text(f_forth_frame, bg='#FFFFFF', fg='#000000', font=('Arial', 12), width=97, height=10)
    f_detail.place(x=25, y=60)
    f_submit_button = tk.Button(f_forth_frame, bg='#F9AA33', fg='#000000', font=('Arial', 12, 'bold'), border=0, text='Submit',
                                width=7, height=1, command=submit_form)
    f_submit_button.place(x=830, y=258)


# Profile (Completed)
profile_frame = tk.Frame(center_frame, width=950, height=520, bg='#FFFFFF')

profile_title_frame = tk.Frame(profile_frame, width=950, height=65, bg='#E5F2F8')
profile_title_frame.place(x=0, y=0)

profile_title_text = tk.Label(profile_title_frame, text='Profile', font=('Times New Roman', 18),
                              bg='#E5F2F8', fg='#000000')
profile_title_text.place(relx=0.5, rely=0.5, anchor='center')

profile_back_button = tk.Button(profile_title_frame, border=0, bg='#E5F2F8', image=back_tk_image,
                                command=switch_to_main)
profile_back_button.place(x=25, y=18)


def change_password_profile():
    enter_username = fg_username_entry.get()
    new_password = new_password_entry.get()
    confirm_password = confirm_password_entry.get()

    if enter_username == '' or enter_username != username1_entry.get():
        display_error_message('Please fill in your username')
        return
    elif new_password == '' and confirm_password == '':
        display_error_message('Please enter your new password')
        return
    elif new_password != confirm_password:
        display_error_message('Password does not match')
        return
    elif len(new_password) < 8:
        display_error_message('Minimum 8 characters of Password is required')
        return
    else:
        cursor.execute("UPDATE USER SET user_password = %s WHERE user_name = %s", (new_password, enter_username,))
        database.commit()
        messagebox.showinfo("Success", "Password updated successfully.")
        close_forgot_password()
        profile()


def profile():
    for widget in profile_frame.winfo_children():
        if widget is not profile_title_frame:
            widget.destroy()

    username = username1_entry.get()
    cursor.execute('''SELECT * FROM user WHERE user_name=%s''', (username, ))
    user_detail = cursor.fetchone()
    user_email = user_detail[3]
    user_password = user_detail[2]
    encrypt_password = len(user_password) * '*'

    username_title_label = tk.Label(profile_frame, text='Username: ', bg='#FFFFFF', fg='#000000',
                                    font=('Arial', 12))
    username_title_label.place(x=350, y=110)
    email_title_label = tk.Label(profile_frame, text='Email: ', bg='#FFFFFF', fg='#000000',
                                 font=('Arial', 12))
    email_title_label.place(x=350, y=150)
    password_title_label = tk.Label(profile_frame, text='Password: ', bg='#FFFFFF', fg='#000000',
                                    font=('Arial', 12))
    password_title_label.place(x=350, y=190)
    username_label = tk.Label(profile_frame, text=username, bg='#FFFFFF', fg='#000000',
                              font=('Arial', 12))
    username_label.place(x=530, y=110)
    email_label = tk.Label(profile_frame, text=user_email, bg='#FFFFFF', fg='#000000',
                           font=('Arial', 12))
    email_label.place(x=530, y=150)
    password_label = tk.Label(profile_frame, text=encrypt_password, bg='#FFFFFF', fg='#000000',
                              font=('Arial', 12))
    password_label.place(x=530, y=190)
    reset_password_button = tk.Button(profile_frame, width=15, height=2,
                                      bg='#F9AA33', fg='#000000', text='Reset Password', border=0, command=switch_forgot_password)
    reset_password_button.place(x=535, y=250)

    def view_password():
        if view_password_status.cget('text') == 'Close':
            view_password_button.configure(image=openEyeButton_image)
            password_label.config(text=user_password)
            view_password_status.configure(text='Open')
        elif view_password_status.cget('text') == 'Open':
            view_password_button.configure(image=closeEyeButton_image)
            password_label.config(text=encrypt_password)
            view_password_status.configure(text='Close')

    view_password_status = tk.Label(profile_frame, text='Close')
    view_password_button = tk.Button(profile_frame, border=0, bg='#FFFFFF', image=closeEyeButton_image, command=view_password)
    view_password_button.place(x=325, y=194)


def update_ph_bh():
    cursor.execute('''SELECT purchase_booking.*, destination.destination_type
                   FROM purchase_booking
                   INNER JOIN destination
                   ON purchase_booking.destination_id = destination.destination_id''')
    ph_bh = cursor.fetchall()
    for history in ph_bh:
        target_date = history[3]
        target_time = history[4]
        status = history[10]
        ph_bh_id = history[0]
        current_datetime = datetime.datetime.now()
        if status == 'Ready' and history[11] == 'attraction':
            current_date = current_datetime.date()
            if target_date >= current_date:
                pass
            elif target_date < current_date:
                cursor.execute('''UPDATE purchase_booking
                               SET purchase_booking_status='Expired'
                               WHERE purchase_booking_id=%s''', (ph_bh_id,))
                database.commit()
        elif status == 'Ready' and history[11] == 'restaurant':
            target_datetime = datetime.datetime.strptime(str(target_date) + ' ' + str(target_time), '%Y-%m-%d %H:%M:%S')
            if target_datetime >= current_datetime:
                pass
            elif target_datetime < current_datetime:
                cursor.execute('''UPDATE purchase_booking
                               SET purchase_booking_status='Expired'
                               WHERE purchase_booking_id=%s''', (ph_bh_id,))
                database.commit()


def send_email(e, u_n, pb_id, d_n, d, t, q, d_t, d_i):
    cursor.execute('''SELECT * FROM image WHERE destination_id=%s''', (d_i, ))
    images = cursor.fetchall()
    i_data = images[0][2]
    image = MIMEImage(i_data)
    image.add_header('Content-ID', '<image001@example.com>')
    image.add_header('Content-Disposition', 'attachment', filename=d_n)

    quantity_html = q.replace('\n', '<br>')

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_name = "PIK"
    sender_email = 'your_email'
    sender_password = 'your_password'

    recipient = e
    subject = 'Penang Information Kiosk'
    if d_t == 'attraction':
        subject = subject + ' Purchasing'
    elif d_t == 'restaurant':
        subject = subject + ' Booking'
    email_content = f"""
    <html>
    <body>
    <p>Dear {u_n},</p>
    <p>Here is your ticket.</p>
    <img src="cid:image001@example.com" alt="Image" width="250" height="150">
    <p>ID: {pb_id}</p>
    <p>Destination: {d_n}</p>
    <p>Date: {d}</p>
    {f'<p>Time: {t}</p>' if t is not None else ''}
    <p>Number of pax: <br>{quantity_html}</p>
    <p>Thank you.</p>
    </body>
    </html>
    """

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    msg = MIMEMultipart()
    msg['From'] = sender_name + ' <' + sender_email + '>'
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(email_content, 'html'))
    msg.attach(image)

    server.sendmail(sender_email, recipient, msg.as_string())
    server.quit()
    messagebox.showinfo("Success", "Email sent successfully!")


# Purchase History (Complete)
purchase_history_frame = tk.Frame(center_frame, width=950, height=520, bg='#FFFFFF')

purchase_history_title_frame = tk.Frame(purchase_history_frame, width=950, height=65, bg='#E5F2F8')
purchase_history_title_frame.place(x=0, y=0)

purchase_history_title_text = tk.Label(purchase_history_title_frame, text='Purchase History',
                                       font=('Times New Roman', 18), bg='#E5F2F8', fg='#000000')
purchase_history_title_text.place(relx=0.5, rely=0.5, anchor='center')

purchase_history_back_button = tk.Button(purchase_history_title_frame, border=0, bg='#E5F2F8',
                                         image=back_tk_image, command=switch_to_main)
purchase_history_back_button.place(x=25, y=18)

purchase_history_canvas = tk.Canvas(purchase_history_frame, height=435, width=950, bg='#FFFFFF',
                                    highlightthickness=0)
purchase_history_canvas.place(x=0, y=65)
purchase_history_scrollbar = tk.Scrollbar(purchase_history_frame, orient='vertical')
purchase_history_scrollbar.place(x=933, y=65, height=455)
purchase_history_canvas.configure(yscrollcommand=purchase_history_scrollbar.set)
purchase_history_scrollbar.configure(command=purchase_history_canvas.yview)

purchase_history_content_frame = tk.Frame(purchase_history_canvas, bg='#FFFFFF')


def purchase_history():
    for widget in purchase_history_content_frame.winfo_children():
        widget.destroy()
    username = username1_entry.get()
    cursor.execute('''SELECT user_id, user_email FROM user WHERE user_name=%s''', (username, ))
    user_detail = cursor.fetchone()
    user_id = user_detail[0]
    user_email = user_detail[1]
    d_type = 'attraction'

    cursor.execute('''SELECT purchase_booking.*, payment.payment_status, destination.destination_name
                   FROM purchase_booking
                   INNER JOIN payment
                   ON purchase_booking.purchase_booking_id = payment.purchase_booking_id
                   INNER JOIN destination
                   ON purchase_booking.destination_id = destination.destination_id
                   WHERE user_id=%s AND payment_status=%s AND destination_type=%s
                   ORDER BY purchase_booking.purchase_booking_status DESC, purchase_booking.purchase_booking_date''',
                   (user_id, 1, d_type))
    ph_list = cursor.fetchall()
    count = 0
    for ph in ph_list:
        y_ph = 0
        if count % 2 == 0:
            y_ph = 20
        elif count % 2 != 0:
            y_ph = 0
        purchase_history_detail_frame = tk.Frame(purchase_history_content_frame, width=870, height=200, bg='#FFFFFF')
        purchase_history_detail_frame.pack(padx=32, pady=y_ph)

        purchase_id = ph[0]
        date = ph[3]
        d_name = ph[12]

        quantity = {'Infant x': ph[5],
                    'Children x': ph[6],
                    'Adult x': ph[7],
                    'Older x': ph[8]}
        with_quantity = []
        guests = ''
        for i in quantity:
            if quantity[i] != 0:
                with_quantity.append(i)
        for i in with_quantity:
            describe = i
            number = quantity[describe]
            guests = guests + describe + str(number) + "\n"

        d_id = ph[2]
        filtered_dict = {key: value for key, value in h_image_dict.items() if d_id in value}
        dict_list = list(filtered_dict.items())
        picture = dict_list[0][1][1]

        ticket = ph[10]
        ph_status_label = tk.Label(purchase_history_detail_frame, text='', bg='#FFFFFF', fg='#ED2629',
                                   font=('Arial', 15, 'bold'))
        ph_status_label.place(x=740, y=60)
        if ticket == 'Expired':
            ph_status_label.config(text='Expired')
        elif ticket == 'Ready':
            pass

        ph_label = tk.Label(purchase_history_detail_frame, image=picture, bg='#FFFFFF')
        ph_label.place(x=50, y=22)
        ph_title_label = tk.Label(purchase_history_detail_frame, text=d_name,
                                  font=('Arial', 17, 'underline', 'bold'), bg='#FFFFFF', fg='#000000')
        ph_title_label.place(x=275, y=35)
        ph_date_label = tk.Label(purchase_history_detail_frame, text=date, bg='#FFFFFF', fg='#000000',
                                 font=('Arial', 12))
        ph_date_label.place(x=275, y=70)
        ph_ticket_label = tk.Label(purchase_history_detail_frame, text=guests, bg='#FFFFFF', fg='#000000',
                                   font=('Arial', 12), justify='left')
        ph_ticket_label.place(x=275, y=95)
        ph_email_button = tk.Button(purchase_history_detail_frame, text='Send to email', bg='#F9AA33', fg='#000000',
                                    font=('Arial', 10, 'bold'), width=12, height=1,
                                    command=lambda e=user_email, u_n=username, pb_id=purchase_id, d_n=d_name,
                                    d=date, t=None, q=guests, d_t=d_type, d_i=d_id:
                                    send_email(e, u_n, pb_id, d_n, d, t, q, d_t, d_i))
        ph_email_button.place(x=728, y=90)

        count += 1


# Booking History (Complete)
booking_history_frame = tk.Frame(center_frame, width=950, height=520, bg='#FFFFFF')

booking_history_title_frame = tk.Frame(booking_history_frame, width=950, height=65, bg='#E5F2F8')
booking_history_title_frame.place(x=0, y=0)

booking_history_title_text = tk.Label(booking_history_title_frame, text='Booking History',
                                      font=('Times New Roman', 18), bg='#E5F2F8', fg='#000000')
booking_history_title_text.place(relx=0.5, rely=0.5, anchor='center')

booking_history_back_button = tk.Button(booking_history_title_frame, border=0, bg='#E5F2F8',
                                        image=back_tk_image, command=switch_to_main)
booking_history_back_button.place(x=25, y=18)

booking_history_canvas = tk.Canvas(booking_history_frame, height=435, width=950, bg='#FFFFFF',
                                   highlightthickness=0)
booking_history_canvas.place(x=0, y=65)
booking_history_scrollbar = tk.Scrollbar(booking_history_frame, orient='vertical')
booking_history_scrollbar.place(x=933, y=65, height=455)
booking_history_canvas.configure(yscrollcommand=booking_history_scrollbar.set)
booking_history_scrollbar.configure(command=booking_history_canvas.yview)

booking_history_content_frame = tk.Frame(booking_history_canvas, bg='#FFFFFF')


def booking_history():
    for widget in booking_history_content_frame.winfo_children():
        widget.destroy()
    username = username1_entry.get()
    cursor.execute('''SELECT user_id, user_email FROM user WHERE user_name=%s''', (username, ))
    user_detail = cursor.fetchone()
    user_id = user_detail[0]
    user_email = user_detail[1]
    d_type = 'restaurant'

    cursor.execute('''SELECT purchase_booking.*, destination.destination_name
                   FROM purchase_booking
                   INNER JOIN destination
                   ON purchase_booking.destination_id = destination.destination_id
                   WHERE user_id=%s AND destination_type=%s
                   ORDER BY purchase_booking.purchase_booking_status DESC, purchase_booking.purchase_booking_date''',
                   (user_id, d_type))
    bh_list = cursor.fetchall()
    count = 0
    for bh in bh_list:
        y_bh = 0
        if count % 2 == 0:
            y_bh = 20
        elif count % 2 != 0:
            y_bh = 0
        booking_history_detail_frame = tk.Frame(booking_history_content_frame, width=870, height=200, bg='#FFFFFF')
        booking_history_detail_frame.pack(padx=32, pady=y_bh)

        booking_id = bh[0]
        date = bh[3]
        time = bh[4]
        formatted_time = str(time)
        formatted_time = formatted_time[:-3]
        formatted_time = formatted_time.rjust(5, '0')
        r_name = bh[11]

        quantity = {'Infant x': bh[5],
                    'Children x': bh[6],
                    'Adult x': bh[7],
                    'Older x': bh[8]}
        with_quantity = []
        guests = ''
        for i in quantity:
            if quantity[i] != 0:
                with_quantity.append(i)
        for i in with_quantity:
            describe = i
            number = quantity[describe]
            guests = guests + describe + str(number) + "\n"

        d_id = bh[2]
        filtered_dict = {key: value for key, value in h_image_dict.items() if d_id in value}
        dict_list = list(filtered_dict.items())
        picture = dict_list[0][1][1]

        ticket = bh[10]
        bh_status_label = tk.Label(booking_history_detail_frame, text='', bg='#FFFFFF', fg='#ED2629',
                                   font=('Arial', 15, 'bold'))
        bh_status_label.place(x=740, y=60)
        if ticket == 'Expired':
            bh_status_label.config(text='Expired')
        elif ticket == 'Ready':
            pass

        bh_label = tk.Label(booking_history_detail_frame, image=picture, bg='#FFFFFF')
        bh_label.place(x=50, y=22)
        bh_title1_label = tk.Label(booking_history_detail_frame, text=r_name,
                                   font=('Arial', 17, 'underline', 'bold'), bg='#FFFFFF', fg='#000000')
        bh_title1_label.place(x=275, y=35)
        bh_date_label = tk.Label(booking_history_detail_frame, text=date, bg='#FFFFFF', fg='#000000',
                                 font=('Arial', 12))
        bh_date_label.place(x=275, y=70)
        bh_time_label = tk.Label(booking_history_detail_frame, text=formatted_time, bg='#FFFFFF', fg='#000000',
                                 font=('Arial', 12))
        bh_time_label.place(x=425, y=70)
        bh_ticket_label = tk.Label(booking_history_detail_frame, text=guests,
                                   bg='#FFFFFF', fg='#000000', font=('Arial', 12), justify='left')
        bh_ticket_label.place(x=275, y=95)
        bh_email_button = tk.Button(booking_history_detail_frame, text='Send to email', bg='#F9AA33', fg='#000000',
                                    font=('Arial', 10, 'bold'), width=12, height=1,
                                    command=lambda e=user_email, u_n=username, pb_id=booking_id, d_n=r_name,
                                    d=date, t=formatted_time, q=guests, d_t=d_type, d_i=d_id:
                                    send_email(e, u_n, pb_id, d_n, d, t, q, d_t, d_i))
        bh_email_button.place(x=728, y=90)


# View Feedback (Complete)
view_feedback_frame = tk.Frame(center_frame, width=950, height=520, bg='#FFFFFF')

view_feedback_title_frame = tk.Frame(view_feedback_frame, width=950, height=65, bg='#E5F2F8')
view_feedback_title_frame.place(x=0, y=0)

view_feedback_title_text = tk.Label(view_feedback_title_frame, text='View Feedback', font=('Times New Roman', 18),
                                    bg='#E5F2F8', fg='#000000')
view_feedback_title_text.place(relx=0.5, rely=0.5, anchor='center')

view_feedback_back_button = tk.Button(view_feedback_title_frame, border=0, bg='#E5F2F8', image=back_tk_image,
                                      command=switch_to_main)
view_feedback_back_button.place(x=25, y=18)

view_feedback_list = tk.Listbox(view_feedback_frame, width=45, height=26, activestyle='none')
view_feedback_list.place(x=80, y=82)


def all_feedback():
    for widget in view_content_frame.winfo_children():
        widget.destroy()
    view_feedback_list.delete(0, tk.END)
    view_feedback_list.selection_clear(0, tk.END)
    cursor.execute('''SELECT feedback.*, user_name 
                   FROM feedback
                   INNER JOIN user
                   ON feedback.user_id = user.user_id''')
    forms = cursor.fetchall()
    for form in forms:
        f_id = form[0]
        user_name = form[5]
        f_type = form[2]
        f_title = str(f_id) + '. ' + user_name + ' - ' + f_type
        view_feedback_list.insert(0, f_title)

    s_dict = {}
    cursor.execute('''SELECT * FROM service''')
    services = cursor.fetchall()
    for service in services:
        s_dict[service[0]] = service[1]
    i_dict = {}
    cursor.execute('''SELECT * FROM issue''')
    issues = cursor.fetchall()
    for issue in issues:
        i_dict[issue[0]] = issue[1]

    def select_feedback(selection):
        for widgets in view_content_frame.winfo_children():
            widgets.destroy()

        select = selection.split('. ')
        feedback_id = int(select[0])
        cursor.execute('''SELECT feedback.*, user_name, user_email FROM feedback 
                       INNER JOIN user
                       ON feedback.user_id = user.user_id
                       WHERE feedback_id=%s''', (feedback_id, ))
        detail = cursor.fetchone()
        feedback_type = detail[2]
        feedback_text = detail[3]
        feedback_user = detail[5]
        user_email = detail[6]

        feedback_user_label = tk.Label(view_content_frame, text='User: '+feedback_user, font=('Arial', 10, 'bold'),
                                       bg='#FFFFFF', fg='#000000')
        feedback_user_label.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        feedback_email_label = tk.Label(view_content_frame, text='Email: '+user_email, font=('Arial', 10, 'bold'),
                                        bg='#FFFFFF', fg='#000000')
        feedback_email_label.grid(row=1, column=0, padx=5, sticky='w')
        feedback_id_label = tk.Label(view_content_frame, text='ID: '+str(feedback_id), font=('Arial', 10, 'bold'),
                                     bg='#FFFFFF', fg='#000000')
        feedback_id_label.grid(row=2, column=0, pady=5, padx=5, sticky='w')
        feedback_type_label = tk.Label(view_content_frame, text='Feedback Type: '+feedback_type+'\n', font=('Arial', 10, 'bold'),
                                       bg='#FFFFFF', fg='#000000')
        feedback_type_label.grid(row=3, column=0, padx=5, sticky='w')

        f_services_list = []
        cursor.execute('''SELECT * FROM feedback_service WHERE feedback_id=%s''', (feedback_id, ))
        f_services = cursor.fetchall()
        for f_service in f_services:
            f_services_list.append(f_service[2])
        f_issues_list = []
        cursor.execute('''SELECT * FROM feedback_issue WHERE feedback_id=%s''', (feedback_id,))
        f_issues = cursor.fetchall()
        for f_issue in f_issues:
            f_issues_list.append(f_issue[2])

        service_text = 'Service(s): \n'
        for i in f_services_list:
            service_text = service_text + s_dict[i] + '\n'
        feedback_service_label = tk.Label(view_content_frame, text=service_text, font=('Arial', 10),
                                          bg='#FFFFFF', fg='#000000', justify='left')
        feedback_service_label.grid(row=4, column=0, pady=5, padx=5, sticky='w')
        issue_text = 'Issue(s): \n'
        for i in f_issues_list:
            issue_text = issue_text + i_dict[i] + '\n'
        feedback_issue_label = tk.Label(view_content_frame, text=issue_text, font=('Arial', 10),
                                        bg='#FFFFFF', fg='#000000', justify='left')
        feedback_issue_label.grid(row=5, column=0, padx=5, sticky='w')
        feedback_describe_label = tk.Label(view_content_frame, text='Describe: \n'+feedback_text, font=('Arial', 10),
                                           wraplength=450, bg='#FFFFFF', fg='#000000', justify='left')
        feedback_describe_label.grid(row=6, column=0, pady=5, padx=5, sticky='w')

        view_feedback_canvas.create_window((0, 0), window=view_content_frame, anchor="nw")
        view_content_frame.update_idletasks()
        view_feedback_canvas.configure(scrollregion=view_feedback_canvas.bbox("all"))

    view_feedback_list.bind("<<ListboxSelect>>",
                            lambda event: select_feedback(view_feedback_list.get(view_feedback_list.curselection())))


view_feedback_canvas = tk.Canvas(view_feedback_frame, height=420, width=490, bg='#FFFFFF')
view_feedback_canvas.place(x=380, y=82)
view_feedback_scrollbar = tk.Scrollbar(view_feedback_frame, orient='vertical')
view_feedback_scrollbar.place(x=855, y=82, height=420)
view_feedback_canvas.configure(yscrollcommand=view_feedback_scrollbar.set)
view_feedback_scrollbar.configure(command=view_feedback_canvas.yview)

view_content_frame = tk.Frame(view_feedback_canvas, bg='#FFFFFF')

clear_signup2_frame()
login_window.mainloop()

image_cursor.close()
cursor.close()
database.close()
