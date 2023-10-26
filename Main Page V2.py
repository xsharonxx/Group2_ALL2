import tkinter as tk
from PIL import ImageTk, Image
from tkcalendar import Calendar
from tkinter import messagebox
import webbrowser
import mysql.connector
import datetime

database = mysql.connector.connect(host="localhost", user="root", password="xueer.1014", database="pik")
cursor = database.cursor()

#cursor.execute()
#database.commit()

def switch_to_map():
    feedback_frame.place_forget()
    profile_frame.place_forget()
    purchase_history_frame.place_forget()
    booking_history_frame.place_forget()
    content_frame.place_forget()
    map_frame.place(x=0, y=80)


def switch_to_feedback():
    map_frame.place_forget()
    profile_frame.place_forget()
    purchase_history_frame.place_forget()
    booking_history_frame.place_forget()
    content_frame.place_forget()
    feedback_frame.place(x=0, y=80)


def switch_to_main():
    map_frame.place_forget()
    feedback_frame.place_forget()
    profile_frame.place_forget()
    purchase_history_frame.place_forget()
    booking_history_frame.place_forget()
    content_frame.place(x=0, y=80)


def switch_to_profile():
    content_frame.forget()
    map_frame.place_forget()
    feedback_frame.place_forget()
    purchase_history_frame.place_forget()
    booking_history_frame.place_forget()
    profile_frame.place(x=0, y=80)


def switch_to_purchase_history():
    content_frame.forget()
    map_frame.place_forget()
    feedback_frame.place_forget()
    booking_history_frame.place_forget()
    profile_frame.place_forget()
    purchase_history_frame.place(x=0, y=80)
    purchase_history_canvas.create_window((0, 0), window=purchase_history_content_frame, anchor="nw")
    purchase_history_content_frame.update_idletasks()
    purchase_history_canvas.configure(scrollregion=purchase_history_canvas.bbox("all"))


def switch_to_booking_history():
    content_frame.forget()
    map_frame.place_forget()
    feedback_frame.place_forget()
    purchase_history_frame.place_forget()
    profile_frame.place_forget()
    booking_history_frame.place(x=0, y=80)
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
    x = profile_button.winfo_rootx()
    y = profile_button.winfo_rooty() + profile_button.winfo_height()
    profile_menu.post(x, y)


def sign_out():
    main_window.withdraw()
    root_window.deiconify()


def ticket_quantity_add(price, q_label, label):
    text = q_label.cget('text')
    quantity = int(text)
    quantity += 1
    q_label.config(text=str(quantity))
    total = price * quantity
    formatted_total = "{:.2f}".format(total)
    label.config(text='RM ' + str(formatted_total))
    ticket_total()


def ticket_quantity_minus(price, q_label, label):
    text = q_label.cget('text')
    quantity = int(text)
    quantity -= 1
    if quantity >= 0:
        q_label.config(text=str(quantity))
        total = price * quantity
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
    total = infant_value+children_value+adults_value+older_value
    format_total = "{:.2f}".format(total)
    attraction3_amount_label.config(text='RM '+str(format_total))


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
    total = infant+children+adults+older
    if 0 <= total <= 1:
        restaurant3_guest_label.config(text=str(total)+' guest')
    elif total > 1:
        restaurant3_guest_label.config(text=str(total) + ' guests')


# Root_window
def success_login():
    switch_to_main()
    navigate_to_spots()
    select_content_spots()
    root_window.withdraw()
    main_window.deiconify()


root_window = tk.Tk()
root_window.title('Penang Information Kiosk')
root_window.geometry('950x600')
root_window.iconphoto(False,
                      tk.PhotoImage(file='C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/icon.png'))
root_button = tk.Button(root_window, text='LOGIN', command=success_login)
root_button.pack()


# Main Page
main_window = tk.Toplevel(root_window)
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

map_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/map.png")
map_resize_image = map_image.resize((50, 40), Image.LANCZOS)
map_tk_image = ImageTk.PhotoImage(map_resize_image)
map_button = tk.Button(title_frame, bg='#344955', image=map_tk_image, border=0, command=switch_to_map)
map_button.place(x=790, y=20)

chatbot_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/chatbot.png")
chatbot_resize_image = chatbot_image.resize((42, 40), Image.LANCZOS)
chatbot_tk_image = ImageTk.PhotoImage(chatbot_resize_image)
chatbot_button = tk.Button(title_frame, bg='#344955', image=chatbot_tk_image, border=0)
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

# Local Attraction Spots
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
    clear_purchase_frame()

def select_purchase():
    spots_content_frame.place_forget()
    spots_second_frame.place_forget()
    spots_third_frame.place(x=0, y=0)
    spots_third_canvas.create_window((0, 0), window=spots_purchase_frame, anchor="nw")
    spots_purchase_frame.update_idletasks()
    spots_third_canvas.configure(scrollregion=spots_third_canvas.bbox("all"))

# Attraction Spots - Content/Main
spots_content_frame = tk.Frame(spots_frame, width=950, height=455)
spots_content_frame.place(x=0, y=0)
spots_canvas = tk.Canvas(spots_content_frame, height=455, width=950, bg='#FFFFFF')
spots_canvas.place(x=0, y=0)
spots_scrollbar = tk.Scrollbar(spots_content_frame, orient='vertical')
spots_scrollbar.place(x=933, y=0, height=455)
spots_canvas.configure(yscrollcommand=spots_scrollbar.set)
spots_scrollbar.configure(command=spots_canvas.yview)

spots_main_frame = tk.Frame(spots_canvas, bg='#FFFFFF')

attraction_frame = tk.Frame(spots_main_frame, bg='#EAEAEA', width=220, height=200)
attraction_frame.grid(row=0, column=0, padx=10, pady=20)
the_top_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/thetoppenang.png")
the_top_resize_image = the_top_image.resize((210, 125), Image.LANCZOS)
the_top_tk_image = ImageTk.PhotoImage(the_top_resize_image)
attraction_image_label = tk.Label(attraction_frame, bg='#EAEAEA', image=the_top_tk_image)
attraction_image_label.place(x=3, y=3)
attraction_title_label = tk.Label(attraction_frame, text='The Top Penang', font=('Arial', 12, 'bold'), bg='#EAEAEA')
attraction_title_label.place(x=3, y=130)
star_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/star.png")
star_resize_image = star_image.resize((15, 15), Image.LANCZOS)
star_tk_image = ImageTk.PhotoImage(star_resize_image)
attraction_rate_label = tk.Label(attraction_frame, bg='#EAEAEA', image=star_tk_image, text=' 4.6', compound=tk.LEFT,
                                 font=('Arial', 10, 'bold'))
attraction_rate_label.place(x=3, y=153)
attraction_price_label = tk.Label(attraction_frame, bg='#EAEAEA', text='RM 65', font=('Arial', 10, 'bold'))
attraction_price_label.place(x=4, y=176)
attraction_space1_frame = tk.Frame(spots_main_frame, bg='#FFFFFF', width=220, height=200)
attraction_space1_frame.grid(row=0, column=1)
attraction_space2_frame = tk.Frame(spots_main_frame, bg='#FFFFFF', width=220, height=200)
attraction_space2_frame.grid(row=0, column=2, padx=10)
attraction_space3_frame = tk.Frame(spots_main_frame, bg='#FFFFFF', width=220, height=200)
attraction_space3_frame.grid(row=1, column=0)
attraction_frame.bind('<Button-1>', lambda event: select_attraction())

def insert_search():
    search_entry.delete(0, tk.END)
    search_entry.config(fg='#7A7373')

def leave_search():
    search_entry.get()
    if search_entry.get() == '':
        search_entry.insert(0, 'Search')
        search_entry.config(fg='#A49C9C')

spots_content_right_frame = tk.Frame(spots_main_frame, bg='#FFFFFF', width=250, height=455)
spots_content_right_frame.grid(row=0, column=3, rowspan=2, sticky='n')

search_frame = tk.Frame(spots_content_right_frame, width=190, height=30, bg='#F7F7F7')
search_frame.place(x=20, y=20)
search_entry = tk.Entry(search_frame, width=17, bg='#F7F7F7', font=('Arial', 12), fg='#A49C9C', border=0)
search_entry.place(x=4, y=4)
search_entry.insert(0, 'Search')
search_entry.bind('<FocusIn>', lambda event: insert_search())
search_entry.bind('<FocusOut>', lambda event: leave_search())
search_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/search.png")
search_resize_image = search_image.resize((20, 20), Image.LANCZOS)
search_tk_image = ImageTk.PhotoImage(search_resize_image)
search_button = tk.Button(search_frame, image=search_tk_image, border=0, bg='#F7F7F7')
search_button.place(x=160, y=4)
filter_option_var = tk.BooleanVar()
filter_option_checkbox = tk.Checkbutton(spots_content_right_frame, text='Adventure', font=('Arial', 10),
                                        bg='#FFFFFF', fg='#A49C9C', variable=filter_option_var)
filter_option_checkbox.place(x=20, y=60)

# Attraction Spots - Detail
spots_second_frame = tk.Frame(spots_frame, width=950, height=455)
spots_second_canvas = tk.Canvas(spots_second_frame, height=455, width=950, bg='#FFFFFF')
spots_second_canvas.place(x=0, y=0)
spots_second_scrollbar = tk.Scrollbar(spots_second_frame, orient='vertical')
spots_second_scrollbar.place(x=933, y=0, height=455)
spots_second_canvas.configure(yscrollcommand=spots_second_scrollbar.set)
spots_second_scrollbar.configure(command=spots_second_canvas.yview)

spots_detail_frame = tk.Frame(spots_second_canvas, bg='#FFFFFF')

previous_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/previous.png")
previous_resize_image = previous_image.resize((30, 50), Image.LANCZOS)
previous_tk_image = ImageTk.PhotoImage(previous_resize_image)
previous_button = tk.Button(spots_detail_frame, image=previous_tk_image, bg='#FFFFFF', border=0)
previous_button.grid(row=0, column=0, padx=10)
escape2_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/escape.png")
escape2_resize_image = escape2_image.resize((550, 290), Image.LANCZOS)
escape2_tk_image = ImageTk.PhotoImage(escape2_resize_image)
attraction2_label = tk.Label(spots_detail_frame, image=escape2_tk_image, bg='#FFFFFF')
attraction2_label.grid(row=0, column=1, pady=20)
next_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/next.png")
next_resize_image = next_image.resize((30, 50), Image.LANCZOS)
next_tk_image = ImageTk.PhotoImage(next_resize_image)
next_button = tk.Button(spots_detail_frame, image=next_tk_image, bg='#FFFFFF', border=0)
next_button.grid(row=0, column=2, padx=10)
attraction2_title_label = tk.Label(spots_detail_frame, text='ESCAPE Theme Park', bg='#FFFFFF', fg='#000000',
                                   font=('Arial', 16, 'underline', 'bold'))
attraction2_title_label.grid(row=1, column=0, columnspan=2, sticky='w', padx=10)
star2_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/star.png")
star2_resize_image = star2_image.resize((15, 15), Image.LANCZOS)
star2_tk_image = ImageTk.PhotoImage(star2_resize_image)
attraction2_rate_label = tk.Label(spots_detail_frame, bg='#FFFFFF', image=star_tk_image, text=' 4.6', compound=tk.LEFT,
                                  font=('Arial', 10, 'bold'))
attraction2_rate_label.grid(row=1, column=2)
attraction2_type_label = tk.Label(spots_detail_frame, text='Adventure', bg='#FFFFFF', fg='#000000',
                                  font=('Arial', 8))
attraction2_type_label.grid(row=2, column=0, columnspan=3, sticky='w', padx=10)
attraction2_detail_label = tk.Label(spots_detail_frame, text='Description', bg='#FFFFFF', fg='#000000',
                                    font=('Arial', 11), wraplength=600, justify='left')
attraction2_detail_label.grid(row=3, column=0, columnspan=3, sticky='w', padx=10, pady=5)

attraction_second_right_frame = tk.Frame(spots_detail_frame, bg='#FFFFFF', width=260, height=390)
attraction_second_right_frame.grid(row=0, column=3, rowspan=3, padx=10)
attraction2_address_title_label = tk.Label(attraction_second_right_frame, text='Address:', bg='#FFFFFF', fg='#000000',
                                           font=('Arial', 11, 'underline', 'bold'))
attraction2_address_title_label.place(x=20, y=20)
attraction2_address_label = tk.Label(attraction_second_right_frame,
                                     text='828, Jalan Teluk Bahang, Teluk Bahang, 11050 Tanjung Bungah, Pulau Pinang',
                                     bg='#FFFFFF', fg='#000000', font=('Arial', 9), wraplength=250, justify='left')
attraction2_address_label.place(x=20, y=41)
attraction2_contact_title_label = tk.Label(attraction_second_right_frame, text='Contact:', bg='#FFFFFF', fg='#000000',
                                           font=('Arial', 11, 'underline', 'bold'))
attraction2_contact_title_label.place(x=20, y=80)
attraction2_contact_label = tk.Label(attraction_second_right_frame, text='+6017-797 7529', bg='#FFFFFF',
                                     fg='#000000', font=('Arial', 9))
attraction2_contact_label.place(x=20, y=101)
attraction2_operation_title_label = tk.Label(attraction_second_right_frame, text='Operation hour:', bg='#FFFFFF',
                                             fg='#000000', font=('Arial', 11, 'underline', 'bold'))
attraction2_operation_title_label.place(x=20, y=125)
attraction2_operation_label = tk.Label(attraction_second_right_frame,
                                       text='Monday Closed\nTuesday 10am-6pm\nWednesday 10am-6pm\nThursday 10am-6pm\n'
                                            'Friday 10am-6pm\nSaturday 10am-6pm\nSunday 10am-6pm',
                                       bg='#FFFFFF', fg='#000000', font=('Arial', 9), justify='left')
attraction2_operation_label.place(x=20, y=146)
attraction2_estimated_title_label = tk.Label(attraction_second_right_frame, text='Estimated Price Per Pax:',
                                             bg='#FFFFFF', fg='#000000', font=('Arial', 11, 'underline', 'bold'))
attraction2_estimated_title_label.place(x=20, y=265)
attraction2_estimated_label = tk.Label(attraction_second_right_frame, text='RM 155.00', bg='#FFFFFF',
                                       fg='#000000', font=('Arial', 9))
attraction2_estimated_label.place(x=20, y=286)
attraction2_back_button = tk.Button(attraction_second_right_frame, text='Back', border=0, fg='#000000', bg='#F9AA33',
                                    font=('Arial', 11, 'bold'), width=15, height=1, command=select_content_spots)
attraction2_back_button.place(x=60, y=325)
attraction2_purchase_button = tk.Button(attraction_second_right_frame, text='Purchase Ticket', border=0, fg='#000000',
                                        bg='#F9AA33', font=('Arial', 11, 'bold'), width=15, height=1,
                                        command=select_purchase)
attraction2_purchase_button.place(x=60, y=360)

# Attraction Spots - Purchase

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
    x = attraction3_pay_method_frame.winfo_rootx()
    y = attraction3_pay_method_frame.winfo_rooty() + attraction3_pay_method_frame.winfo_height()
    attraction3_pay_method_menu.post(x, y)

def select_payment_method(method):
    attraction3_pay_method_label.configure(text=method)

def clear_purchase_frame():
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date()
    attraction3_date_button.config(text='Pick a date')
    attraction3_infant_quantity_label.config(text='0')
    attraction3_infant_total_label.config(text='RM 0.00')
    attraction3_children_quantity_label.config(text='0')
    attraction3_children_total_label.config(text='RM 0.00')
    attraction3_adults_quantity_label.config(text='0')
    attraction3_adults_total_label.config(text='RM 0.00')
    attraction3_older_quantity_label.config(text='0')
    attraction3_older_total_label.config(text='RM 0.00')
    attraction3_pay_method_label.config(text='Select payment method')
    attraction3_select_date_calendar.selection_set(current_date)
    ticket_total()


def purchase_ticket():
    date = attraction3_date_button.cget('text')
    if '-' in date:
        year = int(date.split('-')[0])
        month = int(date.split('-')[1])
        day = int(date.split('-')[2])
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.date()
        purchase_date = current_date.replace(year=year, month=month, day=day)
        if purchase_date > current_date:
            infant = int(attraction3_infant_quantity_label.cget('text'))
            children = int(attraction3_children_quantity_label.cget('text'))
            adults = int(attraction3_adults_quantity_label.cget('text'))
            older = int(attraction3_older_quantity_label.cget('text'))
            number_guest = infant+children+adults+older
            if number_guest >= 1:
                if attraction3_pay_method_label.cget('text') != 'Select payment method':
                    messagebox.showinfo("Success", "Purchase successfully, thank you")
                    clear_purchase_frame()
                    select_content_spots()
                else:
                    messagebox.showerror("Error", 'Please select a payment method')
            else:
                messagebox.showerror("Error", 'Please select the number of guests')
        elif purchase_date == current_date:
            messagebox.showerror("Error", "Selected date must be at least one day from now")
            attraction3_date_button.config(text='Pick a date')
        else:
            messagebox.showerror("Error", "Selected date is passed")
            attraction3_date_button.config(text='Pick a date')
    else:
        messagebox.showerror('Error', 'Please select a date')

spots_third_frame = tk.Frame(spots_frame, width=950, height=455)
spots_third_canvas = tk.Canvas(spots_third_frame, height=455, width=950, bg='#FFFFFF')
spots_third_canvas.place(x=0, y=0)
spots_third_scrollbar = tk.Scrollbar(spots_third_frame, orient='vertical')
spots_third_scrollbar.place(x=933, y=0, height=455)
spots_third_canvas.configure(yscrollcommand=spots_third_scrollbar.set)
spots_third_scrollbar.configure(command=spots_third_canvas.yview)

spots_purchase_frame = tk.Frame(spots_third_canvas, bg='#FFFFFF')

attraction3_title_label = tk.Label(spots_purchase_frame, text='ESCAPE Theme Park', bg='#FFFFFF', fg='#000000',
                                   font=('Arial', 16, 'underline', 'bold'))
attraction3_title_label.grid(row=0, column=0, padx=20, pady=10, sticky='w', columnspan=2)
attraction3_date_frame = tk.Frame(spots_purchase_frame, bg='#F7F7F7', width=200, height=30)
attraction3_date_frame.grid(row=1, column=0, padx=22, sticky='w', columnspan=2)
calendar_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/calendar.png")
calendar_resize_image = calendar_image.resize((20, 20), Image.LANCZOS)
calendar_tk_image = ImageTk.PhotoImage(calendar_resize_image)
attraction3_date_button = tk.Button(attraction3_date_frame, bg='#F7F7F7', image=calendar_tk_image, border=0,
                                    text='Pick a date', fg='#A49C9C', compound=tk.LEFT, font=('Arial', 10, 'bold'),
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
attraction3_infant_price = 0.00
format_attraction3_infant_price = "{:.2f}".format(attraction3_infant_price)
attraction3_infant_price_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                          text='RM '+str(format_attraction3_infant_price), font=('Arial', 10))
attraction3_infant_price_label.place(x=320, y=50)
minus_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/minus.png")
minus_resize_image = minus_image.resize((15, 15), Image.LANCZOS)
minus_tk_image = ImageTk.PhotoImage(minus_resize_image)
add_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/add.png")
add_resize_image = add_image.resize((15, 15), Image.LANCZOS)
add_tk_image = ImageTk.PhotoImage(add_resize_image)
attraction3_infant_minus_button = tk.Button(attraction3_ticket_frame, bg='#F7F7F7', image=minus_tk_image, border=0,
                                            command=lambda: ticket_quantity_minus(attraction3_infant_price,
                                                                                  attraction3_infant_quantity_label,
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
attraction3_children_price = 111.00
format_attraction3_children_price = "{:.2f}".format(attraction3_children_price)
attraction3_children_price_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                            text='RM '+str(format_attraction3_children_price), font=('Arial', 10))
attraction3_children_price_label.place(x=320, y=90)
attraction3_children_minus_button = tk.Button(attraction3_ticket_frame, bg='#F7F7F7', image=minus_tk_image, border=0,
                                              command=lambda: ticket_quantity_minus(attraction3_children_price,
                                                                                    attraction3_children_quantity_label,
                                                                                    attraction3_children_total_label))
attraction3_children_minus_button.place(x=520, y=90)
attraction3_children_quantity_frame = tk.Frame(attraction3_ticket_frame, bg='#F7F7F7', height=22, width=30,
                                               highlightbackground='#969695', highlightthickness=1)
attraction3_children_quantity_frame.place(x=564, y=88)
attraction3_children_quantity_label = tk.Label(attraction3_children_quantity_frame, bg='#F7F7F7', fg='#000000',
                                               font=('Arial', 8), text='0')
attraction3_children_quantity_label.place(relx=0.5, rely=0.5, anchor='center')
attraction3_children_add_button = tk.Button(attraction3_ticket_frame, bg='#F7F7F7', image=add_tk_image, border=0,
                                            command=lambda: ticket_quantity_add(attraction3_children_price,
                                                                                attraction3_children_quantity_label,
                                                                                attraction3_children_total_label))
attraction3_children_add_button.place(x=620, y=90)
attraction3_children_total_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                            text='RM 0.00', font=('Arial', 10))
attraction3_children_total_label.place(x=780, y=90)
attraction3_adults_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                    text='Adults (13-60)', font=('Arial', 10))
attraction3_adults_label.place(x=12, y=130)
attraction3_adults_price = 167.00
format_attraction3_adults_price = "{:.2f}".format(attraction3_adults_price)
attraction3_adults_price_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                          text='RM '+str(format_attraction3_adults_price), font=('Arial', 10))
attraction3_adults_price_label.place(x=320, y=130)
attraction3_adults_minus_button = tk.Button(attraction3_ticket_frame, bg='#F7F7F7', image=minus_tk_image, border=0,
                                            command=lambda: ticket_quantity_minus(attraction3_adults_price,
                                                                                  attraction3_adults_quantity_label,
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
attraction3_older_price = 0.00
format_attraction3_older_price = "{:.2f}".format(attraction3_older_price)
attraction3_older_price_label = tk.Label(attraction3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                         text='RM '+str(format_attraction3_older_price), font=('Arial', 10))
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
attraction3_total_label = tk.Label(attraction3_ticket_frame, font=('Arial', 12, 'bold'), bg='#F7F7F7', fg='#000000',
                                   text='Total')
attraction3_total_label.place(x=678, y=210)
attraction3_amount_label = tk.Label(attraction3_ticket_frame, font=('Arial', 12, 'bold'), bg='#F7F7F7', fg='#000000',
                                    text='RM 0.00')
attraction3_amount_label.place(x=780, y=210)

attraction3_back_button = tk.Button(spots_purchase_frame, text='Back', font=('Arial', 11, 'bold'), width=10, height=1,
                                    bg='#F9AA33', fg='#000000', border=0, command=select_attraction)
attraction3_back_button.grid(row=3, column=0, padx=20, pady=8, sticky='w')
attraction3_pay_method_frame = tk.Frame(spots_purchase_frame, width=210, height=30, bg='#F9AA33')
attraction3_pay_method_frame.grid(row=3, column=1, padx=20, pady=8, sticky='e')
payment_method_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/payment_method.png")
payment_method_resize_image = payment_method_image.resize((20, 20), Image.LANCZOS)
payment_method_tk_image = ImageTk.PhotoImage(payment_method_resize_image)
attraction3_pay_method_label = tk.Label(attraction3_pay_method_frame, text='Select payment method', fg='#000000',
                                        compound=tk.LEFT, image=payment_method_tk_image, bg='#F9AA33')
attraction3_pay_method_label.place(x=0, y=2)
payment_method_button_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/payment_method_button.png")
payment_method_button_resize_image = payment_method_button_image.resize((12, 10), Image.LANCZOS)
payment_method_button_tk_image = ImageTk.PhotoImage(payment_method_button_resize_image)
attraction3_pay_method_button = tk.Button(attraction3_pay_method_frame, image=payment_method_button_tk_image,
                                          bg='#F9AA33', border=0, command=show_attraction3_pay_method_menu)
attraction3_pay_method_button.place(x=180, y=9)
attraction3_pay_method_menu = tk.Menu(spots_purchase_frame, tearoff=0)
attraction3_pay_method_menu.configure(bg='#F9AA33')
attraction3_pay_method_menu.add_command(label='TNG eWallet', font=('Arial', 10),
                                        command=lambda: select_payment_method('TNG eWallet'))
attraction3_pay_method_menu.add_command(label='Online Banking', font=('Arial', 10),
                                        command=lambda: select_payment_method('Online Banking'))
attraction3_pay_method_menu.add_command(label='Credit/Debit Card', font=('Arial', 10),
                                        command=lambda: select_payment_method('Credit/Debit Card'))
attraction3_pay_button = tk.Button(spots_purchase_frame, text='Pay', font=('Arial', 11, 'bold'), width=10, height=1,
                                   bg='#F9AA33', fg='#000000', border=0, command=purchase_ticket)
attraction3_pay_button.grid(row=4, column=1, padx=20, sticky='e')

attraction3_select_date_frame = tk.Frame(spots_purchase_frame, width=255, height=230, bg='#F7F7F7',
                                         highlightbackground="#ADB0BC", highlightthickness=2)
attraction3_select_date_calendar = Calendar(attraction3_select_date_frame, selectmode='day', date_pattern='yyyy-mm-dd')
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

# Public transportation
transport_frame = tk.Frame(content_frame, width=950, height=455)
transport_frame.place(x=0, y=65)
transport_canvas = tk.Canvas(transport_frame, height=455, width=950, bg='#FFFFFF')
transport_canvas.place(x=0, y=0)
transport_scrollbar = tk.Scrollbar(transport_frame, orient='vertical')
transport_scrollbar.place(x=933, y=0, height=455)
transport_canvas.configure(yscrollcommand=transport_scrollbar.set)
transport_scrollbar.configure(command=transport_canvas.yview)

transport_content_frame = tk.Frame(transport_canvas, bg='#FFFFFF')

transport_type_frame = tk.Frame(transport_content_frame, height=230, width=870, bg='#EAEAEA')
transport_type_frame.pack(padx=32, pady=20)  # for pady, first=20, second=no need, third=20 like this....
rapid_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/rapidPenang.png")
rapid_resize_image = rapid_image.resize((200, 200), Image.LANCZOS)
rapid_tk_image = ImageTk.PhotoImage(rapid_resize_image)
rapid_label = tk.Label(transport_type_frame, image=rapid_tk_image)
rapid_label.place(x=40, y=15)
transport_name_label = tk.Label(transport_type_frame, text='Rapid Penang', font=('Arial', 17, 'underline', 'bold'),
                                bg='#EAEAEA', fg='#000000')
transport_name_label.place(x=280, y=50)
transport_description_label = tk.Label(transport_type_frame, text='For Schedules, Routes and Stops: ',
                                       font=('Arial', 12), bg='#EAEAEA', fg='#000000')
transport_description_label.place(x=280, y=90)
transport_link_label = tk.Label(transport_type_frame, wraplength=540, justify='left',
                                text='https://moovitapp.com/index/en/public_transit-lines-Penang-5390-1122251',
                                font=('Arial', 12, 'underline'), bg='#EAEAEA', fg='blue')
transport_link_label.place(x=280, y=120)
def open_transport_link():
    transport_link = "https://moovitapp.com/index/en/public_transit-lines-Penang-5390-1122251"
    webbrowser.open(transport_link)
transport_link_label.bind("<Button-1>", lambda event: open_transport_link())

# Food & Beverage
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
    clear_booking_frame()

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
food_beverage_canvas = tk.Canvas(food_beverage_content_frame, height=455, width=950, bg='#FFFFFF')
food_beverage_canvas.place(x=0, y=0)
food_beverage_scrollbar = tk.Scrollbar(food_beverage_content_frame, orient='vertical')
food_beverage_scrollbar.place(x=933, y=0, height=455)
food_beverage_canvas.configure(yscrollcommand=food_beverage_scrollbar.set)
food_beverage_scrollbar.configure(command=food_beverage_canvas.yview)

food_beverage_main_frame = tk.Frame(food_beverage_canvas, bg='#FFFFFF')

restaurant_frame = tk.Frame(food_beverage_main_frame, bg='#EAEAEA', width=220, height=200)
restaurant_frame.grid(row=0, column=0, padx=10, pady=20)
over_above_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/over&above.png")
over_above_resize_image = over_above_image.resize((210, 125), Image.LANCZOS)
over_above_tk_image = ImageTk.PhotoImage(over_above_resize_image)
restaurant_image_label = tk.Label(restaurant_frame, bg='#EAEAEA', image=over_above_tk_image)
restaurant_image_label.place(x=3, y=3)
restaurant_title_label = tk.Label(restaurant_frame, text='Over & Above', font=('Arial', 12, 'bold'), bg='#EAEAEA')
restaurant_title_label.place(x=3, y=130)
restaurant_rate_label = tk.Label(restaurant_frame, bg='#EAEAEA', image=star_tk_image, text=' 4.6', compound=tk.LEFT,
                                 font=('Arial', 10, 'bold'))
restaurant_rate_label.place(x=3, y=153)
restaurant_price_label = tk.Label(restaurant_frame, bg='#EAEAEA', text='RM 55', font=('Arial', 10, 'bold'))
restaurant_price_label.place(x=4, y=176)
restaurant_space1_frame = tk.Frame(food_beverage_main_frame, bg='#FFFFFF', width=220, height=200)
restaurant_space1_frame.grid(row=0, column=1)
restaurant_space2_frame = tk.Frame(food_beverage_main_frame, bg='#FFFFFF', width=220, height=200)
restaurant_space2_frame.grid(row=0, column=2, padx=10)
restaurant_space3_frame = tk.Frame(food_beverage_main_frame, bg='#FFFFFF', width=220, height=200)
restaurant_space3_frame.grid(row=1, column=0)
restaurant_frame.bind('<Button-1>', lambda event: select_restaurant())

def insert_search_fb():
    search_fb_entry.delete(0, tk.END)
    search_fb_entry.config(fg='#7A7373')

def leave_search_fb():
    search_fb_entry.get()
    if search_fb_entry.get() == '':
        search_fb_entry.insert(0, 'Search')
        search_fb_entry.config(fg='#A49C9C')

fb_content_right_frame = tk.Frame(food_beverage_main_frame, bg='#FFFFFF', width=250, height=455)
fb_content_right_frame.grid(row=0, column=3, rowspan=2, sticky='n')

search_fb_frame = tk.Frame(fb_content_right_frame, width=190, height=30, bg='#F7F7F7')
search_fb_frame.place(x=20, y=20)
search_fb_entry = tk.Entry(search_fb_frame, width=17, bg='#F7F7F7', font=('Arial', 12), fg='#A49C9C', border=0)
search_fb_entry.place(x=4, y=4)
search_fb_entry.insert(0, 'Search')
search_fb_entry.bind('<FocusIn>', lambda event: insert_search_fb())
search_fb_entry.bind('<FocusOut>', lambda event: leave_search_fb())
search_fb_button = tk.Button(search_fb_frame, image=search_tk_image, border=0, bg='#F7F7F7')
search_fb_button.place(x=160, y=4)
filter_option_fb_var = tk.BooleanVar()
filter_option_fb_checkbox = tk.Checkbutton(fb_content_right_frame, text='Halal', font=('Arial', 10),
                                           bg='#FFFFFF', fg='#A49C9C', variable=filter_option_fb_var)
filter_option_fb_checkbox.place(x=20, y=60)

# Food & Beverage - Detail
food_beverage_second_frame = tk.Frame(food_beverage_frame, width=950, height=455, bg='#FFFFFF')
food_beverage_second_canvas = tk.Canvas(food_beverage_second_frame, height=455, width=950, bg='#FFFFFF')
food_beverage_second_canvas.place(x=0, y=0)
food_beverage_second_scrollbar = tk.Scrollbar(food_beverage_second_frame, orient='vertical')
food_beverage_second_scrollbar.place(x=933, y=0, height=455)
food_beverage_second_canvas.configure(yscrollcommand=food_beverage_second_scrollbar.set)
food_beverage_second_scrollbar.configure(command=food_beverage_second_canvas.yview)

food_beverage_detail_frame = tk.Frame(food_beverage_second_canvas, bg='#FFFFFF')

previous_fb_button = tk.Button(food_beverage_detail_frame, image=previous_tk_image, bg='#FFFFFF', border=0)
previous_fb_button.grid(row=0, column=0, padx=10)
over_above2_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/over&above.png")
over_above2_resize_image = over_above2_image.resize((550, 290), Image.LANCZOS)
over_above2_tk_image = ImageTk.PhotoImage(over_above2_resize_image)
restaurant2_label = tk.Label(food_beverage_detail_frame, image=over_above2_tk_image, bg='#FFFFFF')
restaurant2_label.grid(row=0, column=1, pady=20)
next_fb_button = tk.Button(food_beverage_detail_frame, image=next_tk_image, bg='#FFFFFF', border=0)
next_fb_button.grid(row=0, column=2, padx=10)
restaurant2_title_label = tk.Label(food_beverage_detail_frame, text='Over & Above', bg='#FFFFFF', fg='#000000',
                                   font=('Arial', 16, 'underline', 'bold'))
restaurant2_title_label.grid(row=1, column=0, columnspan=2, sticky='w', padx=10)
restaurant2_rate_label = tk.Label(food_beverage_detail_frame, bg='#FFFFFF', image=star_tk_image, text=' 4.6', compound=tk.LEFT,
                                  font=('Arial', 10, 'bold'))
restaurant2_rate_label.grid(row=1, column=2)
restaurant2_type_label = tk.Label(food_beverage_detail_frame, text='Japanese', bg='#FFFFFF', fg='#000000',
                                  font=('Arial', 8))
restaurant2_type_label.grid(row=2, column=0, columnspan=3, sticky='w', padx=10)
restaurant2_detail_label = tk.Label(food_beverage_detail_frame, text='Description', bg='#FFFFFF', fg='#000000',
                                    font=('Arial', 11), wraplength=600, justify='left')
restaurant2_detail_label.grid(row=3, column=0, columnspan=3, sticky='w', padx=10, pady=5)

restaurant_second_right_frame = tk.Frame(food_beverage_detail_frame, bg='#FFFFFF', width=260, height=390)
restaurant_second_right_frame.grid(row=0, column=3, rowspan=3, padx=10)
restaurant2_address_title_label = tk.Label(restaurant_second_right_frame, text='Address:', bg='#FFFFFF', fg='#000000',
                                           font=('Arial', 11, 'underline', 'bold'))
restaurant2_address_title_label.place(x=20, y=20)
restaurant2_address_label = tk.Label(restaurant_second_right_frame,
                                     text='828, Jalan Teluk Bahang, Teluk Bahang, 11050 Tanjung Bungah, Pulau Pinang',
                                     bg='#FFFFFF', fg='#000000', font=('Arial', 9), wraplength=250, justify='left')
restaurant2_address_label.place(x=20, y=41)
restaurant2_contact_title_label = tk.Label(restaurant_second_right_frame, text='Contact:', bg='#FFFFFF', fg='#000000',
                                           font=('Arial', 11, 'underline', 'bold'))
restaurant2_contact_title_label.place(x=20, y=80)
restaurant2_contact_label = tk.Label(restaurant_second_right_frame, text='+6017-797 7529', bg='#FFFFFF',
                                     fg='#000000', font=('Arial', 9))
restaurant2_contact_label.place(x=20, y=101)
restaurant2_operation_title_label = tk.Label(restaurant_second_right_frame, text='Operation hour:', bg='#FFFFFF',
                                             fg='#000000', font=('Arial', 11, 'underline', 'bold'))
restaurant2_operation_title_label.place(x=20, y=125)
restaurant2_operation_label = tk.Label(restaurant_second_right_frame,
                                       text='Monday 8am-2am\nTuesday Closed\nWednesday 8am-2am\nThursday 8am-2am\n'
                                            'Friday 8am-2am\nSaturday 8am-2am\nSunday 8am-2am',
                                       bg='#FFFFFF', fg='#000000', font=('Arial', 9), justify='left')
restaurant2_operation_label.place(x=20, y=146)
restaurant2_estimated_title_label = tk.Label(restaurant_second_right_frame, text='Estimated Price Per Pax:',
                                             bg='#FFFFFF', fg='#000000', font=('Arial', 11, 'underline', 'bold'))
restaurant2_estimated_title_label.place(x=20, y=265)
restaurant2_estimated_label = tk.Label(restaurant_second_right_frame, text='RM 55.00', bg='#FFFFFF',
                                       fg='#000000', font=('Arial', 9))
restaurant2_estimated_label.place(x=20, y=286)
restaurant2_back_button = tk.Button(restaurant_second_right_frame, text='Back', border=0, fg='#000000', bg='#F9AA33',
                                    font=('Arial', 11, 'bold'), width=15, height=1,
                                    command=select_content_food_beverage)
restaurant2_back_button.place(x=60, y=325)
restaurant2_booking_button = tk.Button(restaurant_second_right_frame, text='Make Booking', border=0, fg='#000000',
                                       bg='#F9AA33', font=('Arial', 11, 'bold'), width=15, height=1,
                                       command=select_booking)
restaurant2_booking_button.place(x=60, y=360)

# Food & Beverage - Booking

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
            restaurant3_time_button.config(text=hour+':'+minutes)
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

def clear_booking_frame():
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date()

    restaurant3_date_button.config(text='Pick a date')
    restaurant3_time_button.config(text='Select a time')
    restaurant3_infant_quantity_label.config(text='0')
    restaurant3_children_quantity_label.config(text='0')
    restaurant3_adults_quantity_label.config(text='0')
    restaurant3_older_quantity_label.config(text='0')
    restaurant3_select_date_calendar.selection_set(current_date)
    restaurant3_hour_spinbox.delete(0, tk.END)
    restaurant3_hour_spinbox.insert(0, "00")
    restaurant3_minutes_spinbox.delete(0, tk.END)
    restaurant3_minutes_spinbox.insert(0, "00")
    booking_total()

def book_restaurant():
    time = restaurant3_time_button.cget('text')
    date = restaurant3_date_button.cget('text')
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
            number_guest = int(guest.split(' ')[0])
            if number_guest >= 1:
                messagebox.showinfo("Success", "Booking successfully, thank you")
                clear_booking_frame()
                select_content_food_beverage()
            else:
                messagebox.showerror("Error", 'Please select the number of guests')
        else:
            messagebox.showerror("Error", "Selected booking date and time is passed")
            restaurant3_date_button.config(text='Pick a date')
            restaurant3_time_button.config(text='Select a time')
    else:
        messagebox.showerror('Error', 'Please select a booking date and time')

food_beverage_third_frame = tk.Frame(food_beverage_frame, width=950, height=455, bg='#FFFFFF')
food_beverage_third_canvas = tk.Canvas(food_beverage_third_frame, height=455, width=950, bg='#FFFFFF')
food_beverage_third_canvas.place(x=0, y=0)
food_beverage_third_scrollbar = tk.Scrollbar(food_beverage_third_frame, orient='vertical')
food_beverage_third_scrollbar.place(x=933, y=0, height=455)
food_beverage_third_canvas.configure(yscrollcommand=food_beverage_third_scrollbar.set)
food_beverage_third_scrollbar.configure(command=food_beverage_third_canvas.yview)

food_beverage_booking_frame = tk.Frame(food_beverage_third_canvas, bg='#FFFFFF')

restaurant3_title_label = tk.Label(food_beverage_booking_frame, text='Over & Above', bg='#FFFFFF', fg='#000000',
                                   font=('Arial', 16, 'underline', 'bold'))
restaurant3_title_label.grid(row=0, column=0, padx=20, pady=10, sticky='w', columnspan=3)
restaurant3_date_frame = tk.Frame(food_beverage_booking_frame, bg='#F7F7F7', width=200, height=30)
restaurant3_date_frame.grid(row=1, column=0, padx=22, sticky='w')
restaurant3_date_button = tk.Button(restaurant3_date_frame, bg='#F7F7F7', image=calendar_tk_image, border=0,
                                    text='Pick a date', fg='#A49C9C', compound=tk.LEFT, font=('Arial', 10, 'bold'),
                                    command=show_restaurant3_date_frame, width=200, anchor='w')
restaurant3_date_button.place(x=5, y=2)
restaurant3_time_frame = tk.Frame(food_beverage_booking_frame, bg='#F7F7F7', width=200, height=30)
restaurant3_time_frame.grid(row=1, column=1, padx=22, sticky='e')
time_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/time.png")
time_resize_image = time_image.resize((20, 20), Image.LANCZOS)
time_tk_image = ImageTk.PhotoImage(time_resize_image)
restaurant3_time_button = tk.Button(restaurant3_time_frame, bg='#F7F7F7', image=time_tk_image, border=0,
                                    text='Select a time', fg='#A49C9C', compound=tk.LEFT, font=('Arial', 10, 'bold'),
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
restaurant3_infant_minus_button = tk.Button(restaurant3_ticket_frame, bg='#F7F7F7', image=minus_tk_image, border=0,
                                            command=lambda: booking_quantity_minus(restaurant3_infant_quantity_label))
restaurant3_infant_minus_button.place(x=340, y=50)
restaurant3_infant_quantity_frame = tk.Frame(restaurant3_ticket_frame, bg='#F7F7F7', height=22, width=30,
                                             highlightbackground='#969695', highlightthickness=1)
restaurant3_infant_quantity_frame.place(x=384, y=48)
restaurant3_infant_quantity_label = tk.Label(restaurant3_infant_quantity_frame, bg='#F7F7F7', fg='#000000',
                                             font=('Arial', 8), text='0')
restaurant3_infant_quantity_label.place(relx=0.5, rely=0.5, anchor='center')
restaurant3_infant_add_button = tk.Button(restaurant3_ticket_frame, bg='#F7F7F7', image=add_tk_image, border=0,
                                          command=lambda: booking_quantity_add(restaurant3_infant_quantity_label))
restaurant3_infant_add_button.place(x=440, y=50)
restaurant3_children_label = tk.Label(restaurant3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                      text='Children (4-12)', font=('Arial', 10))
restaurant3_children_label.place(x=12, y=90)
restaurant3_children_minus_button = tk.Button(restaurant3_ticket_frame, bg='#F7F7F7', image=minus_tk_image, border=0,
                                              command=lambda: booking_quantity_minus(restaurant3_children_quantity_label))
restaurant3_children_minus_button.place(x=340, y=90)
restaurant3_children_quantity_frame = tk.Frame(restaurant3_ticket_frame, bg='#F7F7F7', height=22, width=30,
                                               highlightbackground='#969695', highlightthickness=1)
restaurant3_children_quantity_frame.place(x=384, y=88)
restaurant3_children_quantity_label = tk.Label(restaurant3_children_quantity_frame, bg='#F7F7F7', fg='#000000',
                                               font=('Arial', 8), text='0')
restaurant3_children_quantity_label.place(relx=0.5, rely=0.5, anchor='center')
restaurant3_children_add_button = tk.Button(restaurant3_ticket_frame, bg='#F7F7F7', image=add_tk_image, border=0,
                                            command=lambda: booking_quantity_add(restaurant3_children_quantity_label))
restaurant3_children_add_button.place(x=440, y=90)
restaurant3_adults_label = tk.Label(restaurant3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                    text='Adults (13-60)', font=('Arial', 10))
restaurant3_adults_label.place(x=12, y=130)
restaurant3_adults_minus_button = tk.Button(restaurant3_ticket_frame, bg='#F7F7F7', image=minus_tk_image, border=0,
                                            command=lambda: booking_quantity_minus(restaurant3_adults_quantity_label))
restaurant3_adults_minus_button.place(x=340, y=130)
restaurant3_adults_quantity_frame = tk.Frame(restaurant3_ticket_frame, bg='#F7F7F7', height=22, width=30,
                                             highlightbackground='#969695', highlightthickness=1)
restaurant3_adults_quantity_frame.place(x=384, y=128)
restaurant3_adults_quantity_label = tk.Label(restaurant3_adults_quantity_frame, bg='#F7F7F7', fg='#000000',
                                             font=('Arial', 8), text='0')
restaurant3_adults_quantity_label.place(relx=0.5, rely=0.5, anchor='center')
restaurant3_adults_add_button = tk.Button(restaurant3_ticket_frame, bg='#F7F7F7', image=add_tk_image, border=0,
                                          command=lambda: booking_quantity_add(restaurant3_adults_quantity_label))
restaurant3_adults_add_button.place(x=440, y=130)
restaurant3_older_label = tk.Label(restaurant3_ticket_frame, bg='#F7F7F7', fg='#000000',
                                   text='Older Adulthood (61-100+)', font=('Arial', 10))
restaurant3_older_label.place(x=12, y=170)
restaurant3_older_minus_button = tk.Button(restaurant3_ticket_frame, bg='#F7F7F7', image=minus_tk_image, border=0,
                                           command=lambda: booking_quantity_minus(restaurant3_older_quantity_label))
restaurant3_older_minus_button.place(x=340, y=170)
restaurant3_older_quantity_frame = tk.Frame(restaurant3_ticket_frame, bg='#F7F7F7', height=22, width=30,
                                            highlightbackground='#969695', highlightthickness=1)
restaurant3_older_quantity_frame.place(x=384, y=168)
restaurant3_older_quantity_label = tk.Label(restaurant3_older_quantity_frame, bg='#F7F7F7', fg='#000000',
                                            font=('Arial', 8), text='0')
restaurant3_older_quantity_label.place(relx=0.5, rely=0.5, anchor='center')
restaurant3_older_add_button = tk.Button(restaurant3_ticket_frame, bg='#F7F7F7', image=add_tk_image, border=0,
                                         command=lambda: booking_quantity_add(restaurant3_older_quantity_label))
restaurant3_older_add_button.place(x=440, y=170)
restaurant3_total_label = tk.Label(restaurant3_ticket_frame, font=('Arial', 12, 'bold'), bg='#F7F7F7', fg='#000000',
                                   text='Total')
restaurant3_total_label.place(x=290, y=210)
restaurant3_guest_label = tk.Label(restaurant3_ticket_frame, font=('Arial', 12, 'bold'), bg='#F7F7F7', fg='#000000',
                                   text='0 guest')
restaurant3_guest_label.place(x=392, y=210)

restaurant3_right_frame = tk.Frame(food_beverage_booking_frame, bg='#FFFFFF', width=365, height=250)
restaurant3_right_frame.grid(row=2, column=2, pady=8, sticky='e')
restaurant3_reminder_title_label = tk.Label(restaurant3_right_frame, font=('Arial', 10, 'bold'), bg='#FFFFFF',
                                            fg='#000000', text='*** Reminder ***')
restaurant3_reminder_title_label.place(x=130, y=5)
restaurant3_reminder_label = tk.Label(restaurant3_right_frame, font=('Arial', 10), bg='#FFFFFF', fg='#000000',
                                      text='Kindly remember to check in for your reservation within 15 minutes '
                                           'of the scheduled time, or else it will be automatically cancelled. '
                                           'Thank you.', wraplength=360, justify='left')
restaurant3_reminder_label.place(x=3, y=30)

restaurant3_back_button = tk.Button(food_beverage_booking_frame, text='Back', font=('Arial', 11, 'bold'), width=10,
                                    height=1, bg='#F9AA33', fg='#000000', border=0, command=select_restaurant)
restaurant3_back_button.grid(row=3, column=0, padx=20, pady=8, sticky='w')
restaurant3_book_button = tk.Button(food_beverage_booking_frame, text='Book', font=('Arial', 11, 'bold'), width=10,
                                    height=1, bg='#F9AA33', fg='#000000', border=0, command=book_restaurant)
restaurant3_book_button.grid(row=3, column=2, padx=5, sticky='e')

restaurant3_select_date_frame = tk.Frame(food_beverage_booking_frame, width=255, height=230, bg='#F7F7F7',
                                         highlightbackground="#ADB0BC", highlightthickness=2)
restaurant3_select_date_calendar = Calendar(restaurant3_select_date_frame, selectmode='day', date_pattern='yyyy-mm-dd')
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
restaurant3_24_label = tk.Label(restaurant3_select_time_frame, text='24-hour format', font=('Arial', 10, 'underline'),
                                bg='#F5F5F5')
restaurant3_24_label.place(x=80, y=7)
restaurant3_hour_spinbox = tk.Spinbox(restaurant3_select_time_frame, from_=00, to=23, width=4, justify='center',
                                      format='%02.0f')
restaurant3_hour_spinbox.place(x=70, y=36)
restaurant3_minutes_spinbox = tk.Spinbox(restaurant3_select_time_frame, from_=00, to=59, width=4, justify='center',
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

# Games
games_content_frame = tk.Frame(content_frame, width=950, height=455, bg='#FFFFFF')

def open_games_list():
    games_question_list_frame.place(x=150, y=20)
    games_question_list_canvas.create_window((0, 0), window=question_list_frame, anchor="nw")
    question_list_frame.update_idletasks()
    games_question_list_canvas.configure(scrollregion=games_question_list_canvas.bbox("all"))

def close_games_list():
    games_question_list_frame.place_forget()

games_board_frame = tk.Frame(games_content_frame, width=650, height=190, bg='#232F34')
games_board_frame.place(x=150, y=20)
games_list_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/list.png")
games_list_resize_image = games_list_image.resize((30, 30), Image.LANCZOS)
games_list_tk_image = ImageTk.PhotoImage(games_list_resize_image)
games_list_button = tk.Button(games_board_frame, border=0, bg='#232F34', image=games_list_tk_image,
                              command=open_games_list)
games_list_button.place(x=10, y=8)
games_question_label = tk.Label(games_board_frame, bg='#232F34', fg='#FFFFFF', wraplength=530, justify='left',
                                text='1. Question', font=('Arial', 12))
games_question_label.place(x=50, y=45)
games_next_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/games_next.png")
games_next_resize_image = games_next_image.resize((25, 25), Image.LANCZOS)
games_next_tk_image = ImageTk.PhotoImage(games_next_resize_image)
games_next_button = tk.Button(games_board_frame, border=0, bg='#232F34', image=games_next_tk_image)
games_next_button.place(x=610, y=150)
games_option1_button = tk.Button(games_content_frame, width=78, height=2, bg='#4A6572', border=0,
                                 text='   Option 1', fg='#FFFFFF', anchor='w')
games_option1_button.place(x=198, y=230)
games_option2_button = tk.Button(games_content_frame, width=78, height=2, bg='#4A6572', border=0,
                                 text='   Option 2', fg='#FFFFFF', anchor='w')
games_option2_button.place(x=198, y=285)
games_option3_button = tk.Button(games_content_frame, width=78, height=2, bg='#4A6572', border=0,
                                 text='   Option 3', fg='#FFFFFF', anchor='w')
games_option3_button.place(x=198, y=340)
games_option4_button = tk.Button(games_content_frame, width=78, height=2, bg='#4A6572', border=0,
                                 text='   Option 4', fg='#FFFFFF', anchor='w')
games_option4_button.place(x=198, y=395)
correct_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/correct.png")
correct_resize_image = correct_image.resize((30, 30), Image.LANCZOS)
correct_tk_image = ImageTk.PhotoImage(correct_resize_image)
wrong_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/wrong.png")
wrong_resize_image = wrong_image.resize((30, 30), Image.LANCZOS)
wrong_tk_image = ImageTk.PhotoImage(wrong_resize_image)
games_option1_label = tk.Label(games_content_frame, bg='#FFFFFF', image=correct_tk_image)
games_option1_label.place(x=760, y=230)
games_option2_label = tk.Label(games_content_frame, bg='#FFFFFF', image=wrong_tk_image)
games_option2_label.place(x=760, y=285)
games_option3_label = tk.Label(games_content_frame, bg='#FFFFFF', image=correct_tk_image)
games_option3_label.place(x=760, y=340)
games_option4_label = tk.Label(games_content_frame, bg='#FFFFFF', image=correct_tk_image)
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
                            text='1.Question', font=('Arial', 12), border=0)
question_button.grid(row=1, column=1, sticky=tk.W)
question1_button = tk.Button(question_list_frame, bg='#232F34', fg='#7F7C7C', wraplength=530, justify='left',
                             text='2.Question', font=('Arial', 12), border=0)
question1_button.grid(row=2, column=1, pady=8, sticky=tk.W)

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

# Feedback Page
feedback_frame = tk.Frame(center_frame, width=950, height=520, bg='#FFFFFF')

feedback_title_frame = tk.Frame(feedback_frame, width=950, height=65, bg='#E5F2F8')
feedback_title_frame.place(x=0, y=0)

feedback_title_text = tk.Label(feedback_title_frame, text='User Feedback Form', font=('Times New Roman', 18),
                               bg='#E5F2F8', fg='#000000')
feedback_title_text.place(relx=0.5, rely=0.5, anchor='center')

feedback_back_button = tk.Button(feedback_title_frame, border=0, bg='#E5F2F8', image=back_tk_image,
                                 command=switch_to_main)
feedback_back_button.place(x=25, y=18)

# Chatbot

# Profile
profile_frame = tk.Frame(center_frame, width=950, height=520, bg='#FFFFFF')

profile_title_frame = tk.Frame(profile_frame, width=950, height=65, bg='#E5F2F8')
profile_title_frame.place(x=0, y=0)

profile_title_text = tk.Label(profile_title_frame, text='Profile', font=('Times New Roman', 18),
                              bg='#E5F2F8', fg='#000000')
profile_title_text.place(relx=0.5, rely=0.5, anchor='center')

profile_back_button = tk.Button(profile_title_frame, border=0, bg='#E5F2F8', image=back_tk_image,
                                command=switch_to_main)
profile_back_button.place(x=25, y=18)

username_title_label = tk.Label(profile_frame, text='Username: ', bg='#FFFFFF', fg='#000000',
                                font=('Arial', 12))
username_title_label.place(x=350, y=110)
email_title_label = tk.Label(profile_frame, text='Email: ', bg='#FFFFFF', fg='#000000',
                             font=('Arial', 12))
email_title_label.place(x=350, y=150)
password_title_label = tk.Label(profile_frame, text='Password: ', bg='#FFFFFF', fg='#000000',
                                font=('Arial', 12))
password_title_label.place(x=350, y=190)
username_label = tk.Label(profile_frame, text='Michelle', bg='#FFFFFF', fg='#000000',
                          font=('Arial', 12))
username_label.place(x=530, y=110)
email_label = tk.Label(profile_frame, text='michelle0810@gmail.com', bg='#FFFFFF', fg='#000000',
                       font=('Arial', 12))
email_label.place(x=530, y=150)
password_label = tk.Label(profile_frame, text='********', bg='#FFFFFF', fg='#000000',
                          font=('Arial', 12))
password_label.place(x=530, y=190)
reset_password_button = tk.Button(profile_frame, width=15, height=2,
                                  bg='#F9AA33', fg='#000000', text='Reset Password', border=0)
reset_password_button.place(x=535, y=250)

# Purchase History
purchase_history_frame = tk.Frame(center_frame, width=950, height=520)

purchase_history_title_frame = tk.Frame(purchase_history_frame, width=950, height=65, bg='#E5F2F8')
purchase_history_title_frame.place(x=0, y=0)

purchase_history_title_text = tk.Label(purchase_history_title_frame, text='Purchase History',
                                       font=('Times New Roman', 18), bg='#E5F2F8', fg='#000000')
purchase_history_title_text.place(relx=0.5, rely=0.5, anchor='center')

purchase_history_back_button = tk.Button(purchase_history_title_frame, border=0, bg='#E5F2F8',
                                         image=back_tk_image, command=switch_to_main)
purchase_history_back_button.place(x=25, y=18)

purchase_history_canvas = tk.Canvas(purchase_history_frame, height=455, width=950, bg='#FFFFFF')
purchase_history_canvas.place(x=0, y=65)
purchase_history_scrollbar = tk.Scrollbar(purchase_history_frame, orient='vertical')
purchase_history_scrollbar.place(x=933, y=65, height=455)
purchase_history_canvas.configure(yscrollcommand=purchase_history_scrollbar.set)
purchase_history_scrollbar.configure(command=purchase_history_canvas.yview)

purchase_history_content_frame = tk.Frame(purchase_history_canvas, bg='#FFFFFF')

purchase_history_detail_frame = tk.Frame(purchase_history_content_frame, width=870, height=200, bg='#FFFFFF')
purchase_history_detail_frame.pack(padx=32, pady=20)
escape_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/escape.png")
escape_resize_image = escape_image.resize((200, 150), Image.LANCZOS)
escape_tk_image = ImageTk.PhotoImage(escape_resize_image)
escape_label = tk.Label(purchase_history_detail_frame, image=escape_tk_image, bg='#FFFFFF')
escape_label.place(x=50, y=22)
escape_title_label = tk.Label(purchase_history_detail_frame, text='ESCAPE Theme Park',
                              font=('Arial', 17, 'underline', 'bold'), bg='#FFFFFF', fg='#000000')
escape_title_label.place(x=275, y=35)
escape_date_label = tk.Label(purchase_history_detail_frame, text='10 October 2023', bg='#FFFFFF', fg='#000000',
                             font=('Arial', 12))
escape_date_label.place(x=275, y=70)
escape_ticket_label = tk.Label(purchase_history_detail_frame, text='Adults x2\nChildren x2', bg='#FFFFFF', fg='#000000',
                               font=('Arial', 12), justify='left')
escape_ticket_label.place(x=275, y=95)
escape_ticket_status_label = tk.Label(purchase_history_detail_frame, text='USED', bg='#FFFFFF', fg='#ED2629',
                                      font=('Arial', 15, 'bold'))
escape_ticket_status_label.place(x=755, y=80)  # EXPIRED = x725, y80

# Booking History
booking_history_frame = tk.Frame(center_frame, width=950, height=520)

booking_history_title_frame = tk.Frame(booking_history_frame, width=950, height=65, bg='#E5F2F8')
booking_history_title_frame.place(x=0, y=0)

booking_history_title_text = tk.Label(booking_history_title_frame, text='Booking History',
                                      font=('Times New Roman', 18), bg='#E5F2F8', fg='#000000')
booking_history_title_text.place(relx=0.5, rely=0.5, anchor='center')

booking_history_back_button = tk.Button(booking_history_title_frame, border=0, bg='#E5F2F8',
                                        image=back_tk_image, command=switch_to_main)
booking_history_back_button.place(x=25, y=18)

booking_history_canvas = tk.Canvas(booking_history_frame, height=455, width=950, bg='#FFFFFF')
booking_history_canvas.place(x=0, y=65)
booking_history_scrollbar = tk.Scrollbar(booking_history_frame, orient='vertical')
booking_history_scrollbar.place(x=933, y=65, height=455)
booking_history_canvas.configure(yscrollcommand=booking_history_scrollbar.set)
booking_history_scrollbar.configure(command=booking_history_canvas.yview)

booking_history_content_frame = tk.Frame(booking_history_canvas, bg='#FFFFFF')

booking_history_detail_frame = tk.Frame(booking_history_content_frame, width=870, height=200, bg='#FFFFFF')
booking_history_detail_frame.pack(padx=32, pady=20)
restaurant_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL2 (4007CEM)/Over&Above.png")
restaurant_resize_image = restaurant_image.resize((200, 150), Image.LANCZOS)
restaurant_tk_image = ImageTk.PhotoImage(restaurant_resize_image)
restaurant_label = tk.Label(booking_history_detail_frame, image=restaurant_tk_image, bg='#FFFFFF')
restaurant_label.place(x=50, y=22)
restaurant_title_label = tk.Label(booking_history_detail_frame, text='Over & Above',
                                  font=('Arial', 17, 'underline', 'bold'), bg='#FFFFFF', fg='#000000')
restaurant_title_label.place(x=275, y=35)
restaurant_date_label = tk.Label(booking_history_detail_frame, text='10 October 2023', bg='#FFFFFF', fg='#000000',
                                 font=('Arial', 12))
restaurant_date_label.place(x=275, y=70)
restaurant_time_label = tk.Label(booking_history_detail_frame, text='18:00', bg='#FFFFFF', fg='#000000',
                                 font=('Arial', 12))
restaurant_time_label.place(x=425, y=70)
restaurant_ticket_label = tk.Label(booking_history_detail_frame, text='Adults x2\nChildren x2\nInfant x1',
                                   bg='#FFFFFF', fg='#000000', font=('Arial', 12), justify='left')
restaurant_ticket_label.place(x=275, y=95)
restaurant_ticket_status_label = tk.Label(booking_history_detail_frame, text='USED', bg='#FFFFFF', fg='#ED2629',
                                          font=('Arial', 15, 'bold'))
restaurant_ticket_status_label.place(x=755, y=80)  # EXPIRED = x725, y80

root_window.mainloop()

cursor.close()
database.close()