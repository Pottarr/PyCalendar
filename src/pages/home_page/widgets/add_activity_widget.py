from customtkinter import *
import tkinter as tk
from datetime import datetime
import tkcalendar as tkcal
import services.activity_configuration as act_con


alphabet_blue = "#abcdef"
python_yellow = "#ffe873"
python_blue = "#306998"
python_blue_lighter = "#7bafe3"
very_light_gray = "#d3d3d3"

class AddActivityWidget(CTkFrame) :
    def __init__(self, master = None, parent_element = None, current_user = None, current_date = None, file_obj = None, **kwargs,) :
        super().__init__(master, **kwargs, fg_color = python_blue_lighter)
        print("AddActivityWidget was loaded")
        self.parent_element = parent_element
        self.current_user = current_user
        self.current_date = current_date
        self.file_obj = file_obj
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 9)
        self.grid_rowconfigure(1, weight = 1)
        
        
        
        self.add_activity_frame = CTkFrame(self, fg_color = very_light_gray)
        self.add_activity_frame.grid_columnconfigure((0, 1, 2), weight = 1)
        self.add_activity_frame.grid_rowconfigure((0, 1, 2, 4), weight = 1)
        self.add_activity_frame.grid_rowconfigure(3, weight = 9)
        self.add_activity_frame.grid_propagate(True)
        self.add_activity_frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.calendar_frame = CTkFrame(self.add_activity_frame)
        self.calendar_frame.grid(row = 0, column = 1, rowspan = 4, columnspan = 2, sticky = "nsew", padx = 10, pady = 10)
        
        self.calendar = tkcal.Calendar(self.calendar_frame, firstweekday = "sunday", showweeknumbers = False,
                                       background = python_blue, headersbackground = python_yellow,
                                       headersforeground = "#000000", selectbackground = python_blue,
                                       date_pattern = "dd/mm/yyyy")
        self.calendar.pack(fill = tk.BOTH, expand = True)
        
        
        
        self.new_activity_name_label = CTkLabel(self.add_activity_frame, text = "Name:")
        self.new_activity_name_label.grid(row = 0, column = 0, sticky = "nsw", padx = 5)
        
        self.new_activity_name_entry = CTkEntry(self.add_activity_frame, bg_color = very_light_gray)
        self.new_activity_name_entry.grid(row = 1, column = 0, sticky = "nsew", padx = 5)
        
        self.new_activity_description_label = CTkLabel(self.add_activity_frame, text = "Description:")
        self.new_activity_description_label.grid(row = 2, column = 0, sticky = "nsw", padx = 5)
        
        self.new_activity_description_textbox = CTkTextbox(self.add_activity_frame, bg_color = very_light_gray, border_color = "black")
        self.new_activity_description_textbox.grid(row = 3, column = 0, sticky = "nsew", padx = 5)
        
        self.new_activity_type_frame = CTkFrame(self.add_activity_frame, fg_color = very_light_gray)
        self.new_activity_type_frame.grid_columnconfigure((0, 1, 2, 3), weight = 1)
        self.new_activity_type_frame.grid_rowconfigure((0, 1), weight = 1)
        self.new_activity_type_frame.grid(row = 4, column = 0, columnspan = 2, sticky = "nsew", padx = 5, pady = 5)
        
        self.new_activity_type_label = CTkLabel(self.new_activity_type_frame, text  = "Type:")
        self.new_activity_type_label.grid(row = 0, column = 0, sticky = "nsw")
        
        self.chosen_type = StringVar(value = "None")
        # self.activity_type = "None"
        self.normal_type_radio_button = CTkRadioButton(self.new_activity_type_frame, text = "Normal", command = self.pick_activity_type, variable = self.chosen_type, value = "Normal")
        self.normal_type_radio_button.grid(row = 1, column = 0, sticky = "nsew")
        
        self.daily_type_radio_button = CTkRadioButton(self.new_activity_type_frame, text = "Daily", command = self.pick_activity_type, variable = self.chosen_type, value = "Daily")
        self.daily_type_radio_button.grid(row = 1, column = 1, sticky = "nsew")
        
        self.weekly_type_radio_button = CTkRadioButton(self.new_activity_type_frame, text = "Weekly", command = self.pick_activity_type, variable = self.chosen_type, value = "Weekly")
        self.weekly_type_radio_button.grid(row = 1, column = 2, sticky = "nsew")
        
        self.annually_type_radio_button = CTkRadioButton(self.new_activity_type_frame, text = "Annually", command = self.pick_activity_type, variable = self.chosen_type, value = "Annually")
        self.annually_type_radio_button.grid(row = 1, column = 3, sticky = "nsew")
        
        self.error_message_frame = CTkFrame(self.new_activity_type_frame, fg_color = very_light_gray)
        self.error_message_frame.grid_columnconfigure(0, weight = 1)
        self.error_message_frame.grid_rowconfigure(0, weight = 1)
        self.error_message_frame.grid(row = 1, column = 4, sticky = "nsew")
        
        self.error_message_label = CTkLabel(self.error_message_frame, text = "", text_color = "red")
        self.error_message_label.grid(row = 0, column = 0, sticky = "nsew")
        
        # self.date_of_activity = self.calendar.get_date()
        # self.date_of_activity_obj = datetime.strptime(self.date_of_activity, "%d/%m/%Y")
        # self.date_of_activity = self.date_of_activity_obj.strftime("%d/%m/%Y")
        # print(self.date_of_activity)
        # self.day_of_week = self.date_of_activity_obj.strftime("%A")
        
        # self.day_of_week_label = CTkLabel(self.misc_frame, text = self.day_of_week)
        
            
        self.footer_button_frame = CTkFrame(self, fg_color = python_blue_lighter)
        self.footer_button_frame.grid_columnconfigure((0, 1), weight = 1)
        self.footer_button_frame.grid_rowconfigure(0, weight = 1)
        self.footer_button_frame.grid(row = 1, column = 0, sticky = "nsew", pady = 10)
        
        self.save_button = CTkButton(self.footer_button_frame, fg_color = "green",
                                             hover_color = "green", text = "Save",
                                             command = self.save)
        self.save_button.grid(row = 0, column = 0, sticky = "nse", padx = 25)
        
        self.cancel_button = CTkButton(self.footer_button_frame, fg_color = "red",
                                             hover_color = "red", text = "Cancel",
                                             command = self.cancel)
        self.cancel_button.grid(row = 0, column = 1, sticky = "nsw", padx = 25)
        
    def pick_activity_type(self) :
        return self.chosen_type.get()
        
    def save(self) :
        
        name = self.new_activity_name_entry.get()
        description = self.new_activity_description_textbox.get("0.0", "end")
        
        self.date_of_activity = self.calendar.get_date()
        date_of_activity_obj = datetime.strptime(self.date_of_activity, "%d/%m/%Y").date()
        self.date_of_activity = date_of_activity_obj.strftime("%d/%m/%Y")
        
        self.day_of_week = date_of_activity_obj.strftime("%A")
        self.activity_type = self.pick_activity_type()
        
        print(self.activity_type)
        if len(self.new_activity_name_entry.get()) == 0 and self.activity_type == "None" :
            self.error_message_label.configure(text = "Error: Please carefully check your Input")
        elif len(self.new_activity_name_entry.get()) == 0 :
            self.error_message_label.configure(text = "Error: Need Activity Title")
        elif self.activity_type == "None" :
            self.error_message_label.configure(text = "Error: Please choose Activity Type")
        elif len(self.new_activity_name_entry.get()) != 0 and self.activity_type != "None" :
            self.error_message_label.configure(text = "")
            act_con.create_activity(self.current_user, name, description, self.date_of_activity, self.day_of_week, self.activity_type, self.file_obj)
            self.destroy()
            self.parent_element.display_activity_log()
            print("Save")
        else :
            self.error_message_label.configure(text = "Error: Something went wrong")
            
        
    
    def cancel(self) :
        print("Cancel")
        self.destroy()
        self.parent_element.display_activity_log(caller = "not none")