import tkinter as tk
import calculation as calculation
import utility as utils

from PIL import Image, ImageTk
from tkcalendar import Calendar

def display() :
    windows = tk.Tk()
    windows.geometry("600x680")

    deploy_component(windows)

    windows.mainloop()

def deploy_component(frame) :
    #define callback for change image (home team)
    def image_callback_home(var, indx, mode) :
        load = Image.open(utils.get_image_path(home_team_dropdown_var.get()))
        load = load.resize((200, 200))
        render = ImageTk.PhotoImage(load)
        img = tk.Label(frame, image=render)
        img.image = render
        img.place(x=70, y= 160)

    #define callback for change image (away team)
    def image_callback_away(var, indx, mode) :
        load = Image.open(utils.get_image_path(away_team_dropdown_var.get()))
        load = load.resize((200, 200))
        render = ImageTk.PhotoImage(load)
        img = tk.Label(frame, image=render)
        img.image = render
        img.place(x=310, y= 160)

    #define callback for calculate
    def calculate():
        return True

    #define the "Home Team" Label
    home_team_label = tk.Label(frame, 
                               text="Home Team",
                               font=("Helvetica", 15))
    
    #define the "Away Team" Label
    away_team_label = tk.Label(frame, 
                               text="Away Team",
                               font=("Helvetica", 15))

    #define the "Date" Label
    date_label = tk.Label(frame,
                          text="Date",
                          font=("Helvetiva", 16)) 

    #define the home team dropdown
    home_team_dropdown_var = tk.StringVar(frame)
    home_team_dropdown_var.set("Home Team")
    home_team_dropdown_var.trace('w', image_callback_home)
    home_team_dropdown = tk.OptionMenu(frame, home_team_dropdown_var, *utils.get_team_list())
    home_team_dropdown.config(width=25)

    #define the away team dropdown
    away_team_dropdown_var = tk.StringVar(frame)
    away_team_dropdown_var.set("Away Team")
    away_team_dropdown_var.trace('w', image_callback_away)
    away_team_dropdown = tk.OptionMenu(frame, away_team_dropdown_var, *utils.get_team_list())
    away_team_dropdown.config(width=25)

    #define the calendar
    cal = Calendar(frame, selectmode="day", date_pattern="dd/mm/yyyy", year=2019)
    
    #define the button
    calculate_button = tk.Button(frame, text="Calculate", command=calculate)

    #deploying
    home_team_label.place(x=120.0, y=50.0)
    away_team_label.place(x=350.0, y=50.0)
    date_label.place(x=270, y=370)
    home_team_dropdown.place(x=70, y=120)
    away_team_dropdown.place(x=310, y=120)
    cal.place(x=170, y=400)
    calculate_button.place(x=260, y=630)


        

