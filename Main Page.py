import tkinter as tk
from PIL import ImageTk, Image
from tkcalendar import Calendar
from tkinter import messagebox


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
    food_beverage_canvas.create_window((0, 0), window=food_beverage_content_frame, anchor="nw")
    food_beverage_content_frame.update_idletasks()
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
    spots_canvas.create_window((0, 0), window=spots_content_frame, anchor="nw")
    spots_content_frame.update_idletasks()
    spots_canvas.configure(scrollregion=spots_canvas.bbox("all"))


def show_profile_menu():
    x = profile_button.winfo_rootx()
    y = profile_button.winfo_rooty() + profile_button.winfo_height()
    profile_menu.post(x, y)


def sign_out():
    main_window.withdraw()
    root_window.deiconify()


# Root_window
def success_login():
    switch_to_main()
    navigate_to_spots()
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
spots_canvas = tk.Canvas(spots_frame, height=455, width=950, bg='#FFFFFF')
spots_canvas.place(x=0, y=0)
spots_scrollbar = tk.Scrollbar(spots_frame, orient='vertical')
spots_scrollbar.place(x=933, y=0, height=455)
spots_canvas.configure(yscrollcommand=spots_scrollbar.set)
spots_scrollbar.configure(command=spots_canvas.yview)

spots_content_frame = tk.Frame(spots_canvas)

# Public transportation
transport_frame = tk.Frame(content_frame, width=950, height=455)
transport_frame.place(x=0, y=65)
transport_canvas = tk.Canvas(transport_frame, height=455, width=950, bg='#FFFFFF')
transport_canvas.place(x=0, y=0)
transport_scrollbar = tk.Scrollbar(transport_frame, orient='vertical')
transport_scrollbar.place(x=933, y=0, height=455)
transport_canvas.configure(yscrollcommand=transport_scrollbar.set)
transport_scrollbar.configure(command=transport_canvas.yview)

transport_content_frame = tk.Frame(transport_canvas)

# Food & Beverage
food_beverage_frame = tk.Frame(content_frame, width=950, height=455)
food_beverage_frame.place(x=0, y=65)
food_beverage_canvas = tk.Canvas(food_beverage_frame, height=455, width=950, bg='#FFFFFF')
food_beverage_canvas.place(x=0, y=0)
food_beverage_scrollbar = tk.Scrollbar(food_beverage_frame, orient='vertical')
food_beverage_scrollbar.place(x=933, y=0, height=455)
food_beverage_canvas.configure(yscrollcommand=food_beverage_scrollbar.set)
food_beverage_scrollbar.configure(command=food_beverage_canvas.yview)

food_beverage_content_frame = tk.Frame(food_beverage_canvas)

# Games
games_content_frame = tk.Frame(content_frame, width=950, height=455, bg='#FFFFFF')

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

purchase_history_content_frame = tk.Frame(purchase_history_canvas)

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

booking_history_content_frame = tk.Frame(booking_history_canvas)

root_window.mainloop()
