import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL Database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yenling12345_',
    database='pik'

)
cursor = connection.cursor()

"""# Create table
# Check if the table exists
cursor.execute("SHOW TABLES LIKE 'USER'")
table_exists = cursor.fetchone()

# If the table doesn't exist, create it
if not table_exists:
    # Create table
    cursor.execute("CREATE TABLE USER("
                   "user_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,"
                   "user_name VARCHAR(50) NOT NULL,"
                   "user_email VARCHAR(50) NOT NULL,"
                   "user_password VARCHAR(20) NOT NULL)")

    connection.commit()
"""


def database_signup():
    user_name = username2_entry.get()
    user_email = email2_entry.get()
    user_password = password2_entry.get()

    if user_name == "admin" and user_email == "admin@gmail.com":
        user_type = "admin"
    else:
        user_type = "user"
    # Insert value into table USER
    cursor.execute("INSERT INTO USER(user_name, user_email, user_password, user_type) VALUES (%s, %s, %s, %s)",
                   (user_name, user_email, user_password, user_type))

    connection.commit()


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
    clear_forgot_password()


def clear_forgot_password():
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
    user_name = username1_entry.get()
    user_password = password1_entry.get()
    cursor.execute('SELECT user_type FROM USER WHERE user_name=%s AND user_password=%s', (user_name, user_password,))
    user_type = cursor.fetchone()

    if user_type:
        user_type = user_type[0]
        if user_type == 'user':
            login_window.withdraw()
            main_window.deiconify()
        elif user_type == 'admin':
            admin_window = tk.Toplevel(main_window)
            admin_window.title("Admin Window")
            admin_window.geometry("400x400")
        else:
            display_error_message("Incorrect Username or Password")
    else:
        display_error_message("Incorrect Username or Password")


def sign_out():
    clear_login1_frame()
    signup_frame.place_forget()
    login_frame.place(relx=0.5, rely=0.5, anchor='center')
    login_window.deiconify()
    main_window.withdraw()
    clear_forgot_password()


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
    username = fg_username_entry.get()
    new_password = new_password_entry.get()
    confirm_password = confirm_password_entry.get()

    if new_password == '' and confirm_password == '':
        display_error_message('Please enter your new password')
        return
    elif new_password != confirm_password:
        display_error_message('Password does not match')
        return
    elif len(new_password) < 8:
        display_error_message('Minimum 8 characters of Password is required')
        return
    elif username == '':
        display_error_message('Please fill in your username')
        return
    else:
        cursor.execute("UPDATE USER SET user_password = %s WHERE user_name = %s", (new_password, username,))
        connection.commit()
        messagebox.showinfo("Success", "Password updated successfully.")
        forgot_password_window.destroy()


# GUI
login_window = tk.Tk()
login_window.title('Penang Information Kiosk')
login_window.geometry('950x600')

login_frame = tk.Frame(login_window, height=550, width=700, bg='#F5F5F5')
login_frame.place(relx=0.5, rely=0.5, anchor='center')

bg_image = Image.open('C:/Users/User/OneDrive/Documents/CS/Sem 3/4007CEM Computer Science ALL2/Sign Up.jpg')
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
openEye_image = Image.open('C:/Users/User/OneDrive/Documents/CS/Sem 3/4007CEM Computer Science ALL2/openeyes.png')
openEye_resize_image = openEye_image.resize((15, 15), Image.LANCZOS)
openEyeButton_image = ImageTk.PhotoImage(openEye_resize_image)
closeEye_image = Image.open('C:/Users/User/OneDrive/Documents/CS/Sem 3/4007CEM Computer Science ALL2/closeeyes.jpeg')
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
forgot_password_image = Image.open('C:/Users/User/OneDrive/Documents/CS/Sem 3/4007CEM Computer Science ALL2/'
                                   'ForgotPassword.jpg')
forgotPassword_resize = forgot_password_image.resize((100, 15), Image.LANCZOS)
forgotPassword_button_image = ImageTk.PhotoImage(forgotPassword_resize)
forgotPassword_button = tk.Button(login_frame, image=forgotPassword_button_image, bd=0, bg='white', cursor='hand2',
                                  command=switch_forgot_password)
forgotPassword_button.place(x=775, y=350)

# Forgot Password Window
forgot_password_window = tk.Toplevel(login_window)
forgot_password_window.title('Forgot Password')
forgot_password_window.geometry('400x200')
forgot_password_window.attributes('-topmost', 1)
forgot_password_window.configure(bg='#F5F5F5')
forgot_password_window.withdraw()
forgot_password_window.bind('<Return>', lambda event: switch_login1_frame())
forgot_password_window.protocol('WM_DELETE_WINDOW', switch_login1_frame)

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
signUpNow_image = Image.open('C:/Users/User/OneDrive/Documents/CS/Sem 3/4007CEM Computer Science ALL2/SignUpNow.jpg')
signUpNow_resize = signUpNow_image.resize((100, 15), Image.LANCZOS)
signUpNowButton_image = ImageTk.PhotoImage(signUpNow_resize)
signup1_button = tk.Button(login_frame, image=signUpNowButton_image, bd=0, bg='white',
                           cursor='hand2', command=switch_signup2_frame)
signup1_button.place(x=772, y=430)

signup_frame = tk.Frame(login_window, height=550, width=700, bg='#F5F5F5')
signup_frame.place(relx=0.5, rely=0.5, anchor='center')
signup_frame.bind('<Return>', lambda event: successful_submit())

signUpBg_image = Image.open('C:/Users/User/OneDrive/Documents/CS/Sem 3/4007CEM Computer Science ALL2/Login.jpg')
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
login_image = Image.open('C:/Users/User/OneDrive/Documents/CS/Sem 3/4007CEM Computer Science ALL2/Login(Button).jpg')
login_resize = login_image.resize((45, 15), Image.LANCZOS)
loginButton_image = ImageTk.PhotoImage(login_resize)
login2_button = tk.Button(signup_frame, image=loginButton_image, bd=0, bg='white', cursor='hand2',
                          command=switch_login1_frame)
login2_button.place(x=828, y=505)

# SignUp Successfully Window
signup_success_window = tk.Toplevel(login_window)
signup_success_window.title('Penang Information Kiosk')
signup_success_window.geometry('200x80')
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

# Main Window
main_window = tk.Toplevel(login_window)
main_window.title('Penang Information Kiosk')
main_window.geometry('800x500')
main_window.withdraw()
main_window.configure(bg='#F5F5F5')

clear_signup2_frame()

# Sign Out Button
signOut_button = tk.Button(main_window, text="Sign Out", command=sign_out)
signOut_button.place(x=720, y=28)
login_window.mainloop()
