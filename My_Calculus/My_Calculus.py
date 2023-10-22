from math import *
from My_Calculus_math_functions import *
import customtkinter, tkinter, tkinter.messagebox, pickle, unicodedata, sys, numpy, matplotlib, matplotlib.pyplot, functools, typing, My_Calculus_interface

with open("my_calculus_settings.pickle", "rb+") as data:
    language_data: str = pickle.load(data)

with open("my_calculus_text_color.pickle", "rb+") as text_color_data:
	text_color: str = pickle.load(text_color_data)

with open("my_calculus_expression_entry_color.pickle", "rb+") as expression_entry_color_data:
	expression_entry_color: str = pickle.load(expression_entry_color_data)

with open("my_calculus_expression_entry_text_color.pickle", "rb+") as expression_entry_text_color_data:
	expression_entry_text_color: str = pickle.load(expression_entry_text_color_data)

with open("my_calculus_button_color.pickle", "rb+") as button_color_data:
	button_color: str = pickle.load(button_color_data)

matplotlib.use("TKAgg")

class Program(customtkinter.CTk, My_Calculus_interface.My_Calculus_interface):

    WIDTH: typing.Final[int] = 500
    HEIGHT: typing.Final[int] = 565
    TITLE: typing.Final[str] = "My Calculus"
    COLOR_THEME: typing.Final[str] = "dark-blue"
    ICON: typing.Final[str] = "my calculus icon.ico"
    WIDGET_SCALING: typing.Final[float] = 1.251

    def __init__(self, *args, **kwargs) -> None:
        customtkinter.CTk.__init__(self, *args, **kwargs)

        customtkinter.set_widget_scaling(self.WIDGET_SCALING)
        customtkinter.set_default_color_theme(self.COLOR_THEME)
        customtkinter.deactivate_automatic_dpi_awareness()

        self.minsize(width=self.WIDTH, height=self.HEIGHT)
        self.resizable(False, False)
        self.title(self.TITLE)
        self.iconbitmap(self.ICON)
        self.protocol("WM_DELETE_WINDOW", lambda: sys.exit())

        self.main_screen_entry_frame: customtkinter.CTkFrame = customtkinter.CTkFrame(master=self, width=480, height=200, fg_color=expression_entry_color)
        self.main_screen_entry_frame.grid(column=0, row=0, columnspan=5000)

        self.main_screen_expression_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self.main_screen_entry_frame, width=475, height=120, fg_color="transparent", border_width=0, text_color=expression_entry_text_color, font=("Roboto Bold", 135))
        self.main_screen_expression_entry.place(x=2, y=2)

        self.main_screen_result_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self.main_screen_entry_frame, width=475, height=20, fg_color="transparent", border_width=0, text_color=expression_entry_text_color, font=("Roboto Bold", 25), state="disabled")
        self.main_screen_result_entry.place(x=2, y=165)

        self.main_screen_procent_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="%", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=self.__procent__)
        self.main_screen_procent_button.grid(column=0, row=1, sticky="w")

        self.main_screen_sqrt_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="\/", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("sqrt()"))
        self.main_screen_sqrt_button.grid(column=1, row=1, sticky="w")

        self.main_screen_one_divided_by_x_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="1/x", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("1/"))
        self.main_screen_one_divided_by_x_button.grid(column=2, row=1, sticky="w")

        self.main_screen_number_in_second_degree_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="x2", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("**2"))
        self.main_screen_number_in_second_degree_button.grid(column=3, row=1, sticky="w")

        self.main_screen_clear_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="C", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.main_screen_expression_entry.delete("0", tkinter.END))
        self.main_screen_clear_button.grid(column=4, row=1, sticky="w")
        
        self.main_screen_clear_everything_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="CE", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=self.__clear_everything__)
        self.main_screen_clear_everything_button.grid(column=5, row=1, sticky="w")

        self.main_screen_clear_number_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="<-", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.main_screen_expression_entry.delete(len(self.main_screen_expression_entry.get()) - 1, tkinter.END))
        self.main_screen_clear_number_button.grid(column=6, row=1, sticky="w")

        self.main_screen_plus_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="+", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("+"))
        self.main_screen_plus_button.grid(column=7, row=1, sticky="w")

        self.main_screen_minus_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="-", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("-"))
        self.main_screen_minus_button.grid(column=7, row=2, sticky="w")

        self.main_screen_multiply_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="*", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("*"))
        self.main_screen_multiply_button.grid(column=7, row=3, sticky="e")

        self.main_screen_divide_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="/", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("/"))
        self.main_screen_divide_button.grid(column=7, row=4, sticky="e")

        self.main_screen_equal_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="=", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=self.__equation__)
        self.main_screen_equal_button.grid(column=7, row=5, sticky="e")

        self.main_screen_number_one_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="1", height=67, width=100, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("1"))
        self.main_screen_number_one_button.place(x=0, y=250)
        
        self.main_screen_number_two_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="2", height=67, width=100, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("2"))
        self.main_screen_number_two_button.place(x=100, y=250)

        self.main_screen_number_three_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="3", height=67, width=100, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("3"))
        self.main_screen_number_three_button.place(x=200, y=250)

        self.main_screen_number_four_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="4", height=67, width=100, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("4"))
        self.main_screen_number_four_button.place(x=0, y=317.5)

        self.main_screen_number_five_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="5", height=67, width=100, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("5"))
        self.main_screen_number_five_button.place(x=100, y=317.5)

        self.main_screen_number_six_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="6", height=67, width=100, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("6"))
        self.main_screen_number_six_button.place(x=200, y=317.5)

        self.main_screen_number_seven_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="7", height=67, width=100, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("7"))
        self.main_screen_number_seven_button.place(x=0, y=385)

        self.main_screen_number_eight_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="8", height=67, width=100, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("8"))
        self.main_screen_number_eight_button.place(x=100, y=385)

        self.main_screen_number_nine_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="9", height=67, width=100, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("9"))
        self.main_screen_number_nine_button.place(x=200, y=385)

        self.main_screen_number_zero_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="0", height=50, width=119.902, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("0"))
        self.main_screen_number_zero_button.place(x=300, y=250)

        self.main_screen_negative_number_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="+/-", height=50, width=119.902, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("-"))
        self.main_screen_negative_number_button.place(x=300, y=300.5)

        self.main_screen_comma_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=".", height=50, width=119.902, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("."))
        self.main_screen_comma_button.place(x=300, y=351)

        self.main_screen_mode_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="режим", height=50, width=119.902, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=self.__mode_option__)
        self.main_screen_mode_button.place(x=300, y=401)

        self.main_screen_pi_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=unicodedata.lookup("GREEK SMALL LETTER PI"), height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("pi"))

        self.main_screen_e_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="e", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("e"))

        self.main_screen_cbrt_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="3\/", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("cbrt()"))

        self.main_screen_number_in_third_degree_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="x3", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("**3"))

        self.main_screen_number_module_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="|x|", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("fabs()"))

        self.main_screen_factorial_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="x!", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("factorial()"))

        self.main_screen_left_bracket_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="(", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("("))

        self.main_screen_right_bracket_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=")", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__(")"))   

        self.main_screen_base_option: customtkinter.CTkComboBox = customtkinter.CTkComboBox(master=self, values=["binary-octal", "binary-decimal", "binary-hexadecimal", "octal-binary", "octal-decimal", "octal-hexadecimal", "decimal-binary", "decimal-octal", "decimal-hexadecimal", "hexadecimal-binary", "hexadecimal-octal", "hexadecimal-decimal"], height=50, width=479.7,  fg_color=button_color, border_color=button_color, button_color=button_color, button_hover_color=button_color, dropdown_fg_color=button_color, text_color=text_color, dropdown_text_color=text_color, font=("Roboto Bold", 32), dropdown_font=("Roboto Bold", 32), command=self.__change_base__)  

        self.main_screen_x_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="x", height=50, width=60, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: self.__button_operation__("x"))        

        if language_data == "Српски":
            self.main_screen_mode_button.configure(text="режим")

        elif language_data == "English":
            self.main_screen_mode_button.configure(text="mode")

        else:
            self.main_screen_mode_button.configure(text="режим")

    def __classical__(self) -> None:
        self.main_screen_expression_entry.configure(height=120)
        self.main_screen_equal_button.configure(command=self.__equation__)

        self.minsize(width=self.WIDTH, height=self.HEIGHT)
        
        self.main_screen_result_entry.place(x=2, y=165)

        self.main_screen_number_zero_button.configure(width=119.902)
        self.main_screen_negative_number_button.configure(width=119.902)
        self.main_screen_comma_button.configure(width=119.902)
        self.main_screen_mode_button.configure(width=119.902)

        self.main_screen_procent_button.grid(column=0, row=1, sticky="w")
        self.main_screen_sqrt_button.grid(column=1, row=1, sticky="w")
        self.main_screen_one_divided_by_x_button.grid(column=2, row=1, sticky="w")
        self.main_screen_number_in_second_degree_button.grid(column=3, row=1, sticky="w")
        self.main_screen_clear_button.grid(column=4, row=1, sticky="w")
        self.main_screen_clear_everything_button.grid(column=5, row=1, sticky="w")
        self.main_screen_clear_number_button.grid(column=6, row=1, sticky="w")
        self.main_screen_plus_button.grid(column=7, row=1, sticky="w")
        self.main_screen_minus_button.grid(column=7, row=2, sticky="w")
        self.main_screen_multiply_button.grid(column=7, row=3, sticky="e")
        self.main_screen_divide_button.grid(column=7, row=4, sticky="e")
        self.main_screen_equal_button.grid(column=7, row=5, sticky="e")

        self.main_screen_number_one_button.place(x=0, y=250)
        self.main_screen_number_two_button.place(x=100, y=250)
        self.main_screen_number_three_button.place(x=200, y=250)
        self.main_screen_number_four_button.place(x=0, y=317.5)
        self.main_screen_number_five_button.place(x=100, y=317.5)
        self.main_screen_number_six_button.place(x=200, y=317.5)
        self.main_screen_number_seven_button.place(x=0, y=385)
        self.main_screen_number_eight_button.place(x=100, y=385)
        self.main_screen_number_nine_button.place(x=200, y=385)

        self.main_screen_number_zero_button.place(x=300, y=250)
        self.main_screen_negative_number_button.place(x=300, y=300.5)
        self.main_screen_comma_button.place(x=300, y=351)
        self.main_screen_mode_button.place(x=300, y=401)

        self.main_screen_pi_button.grid_forget()
        self.main_screen_e_button.grid_forget()
        self.main_screen_cbrt_button.grid_forget()
        self.main_screen_number_in_third_degree_button.grid_forget()
        self.main_screen_number_module_button.grid_forget()
        self.main_screen_factorial_button.grid_forget()
        self.main_screen_left_bracket_button.grid_forget()
        self.main_screen_right_bracket_button.grid_forget()

        try:
            self.main_screen_scientific_calculator_additional_layout.destroy()
            self.main_screen_graphical_calculator_additional_layout.destroy()

        except AttributeError:
            pass

        self.main_screen_base_option.place_forget()
        self.main_screen_x_button.grid_forget()

    def __scientific__(self) -> None: 
        self.main_screen_expression_entry.configure(height=120) 
        self.main_screen_equal_button.configure(command=self.__equation__)
        
        self.minsize(width=self.WIDTH, height=628)
        
        self.main_screen_result_entry.place(x=2, y=165)

        self.main_screen_number_zero_button.configure(width=119.902)
        self.main_screen_negative_number_button.configure(width=119.902)
        self.main_screen_comma_button.configure(width=119.902)
        self.main_screen_mode_button.configure(width=119.902)

        self.main_screen_pi_button.grid(column=0, row=1, sticky="w")
        self.main_screen_e_button.grid(column=1, row=1, sticky="w")
        self.main_screen_cbrt_button.grid(column=2, row=1, sticky="w")
        self.main_screen_number_in_third_degree_button.grid(column=3, row=1, sticky="w")
        self.main_screen_number_module_button.grid(column=4, row=1, sticky="w")
        self.main_screen_factorial_button.grid(column=5, row=1, sticky="w")
        self.main_screen_left_bracket_button.grid(column=6, row=1, sticky="w")
        self.main_screen_right_bracket_button.grid(column=7, row=1, sticky="w")

        self.main_screen_procent_button.grid(column=0, row=2, sticky="w")
        self.main_screen_sqrt_button.grid(column=1, row=2, sticky="w")
        self.main_screen_one_divided_by_x_button.grid(column=2, row=2, sticky="w")
        self.main_screen_number_in_second_degree_button.grid(column=3, row=2, sticky="w")
        self.main_screen_clear_button.grid(column=4, row=2, sticky="w")
        self.main_screen_clear_everything_button.grid(column=5, row=2, sticky="w")
        self.main_screen_clear_number_button.grid(column=6, row=2, sticky="w")
        self.main_screen_plus_button.grid(column=7, row=2, sticky="w")
        self.main_screen_minus_button.grid(column=7, row=3, sticky="w")
        self.main_screen_multiply_button.grid(column=7, row=4, sticky="e")
        self.main_screen_divide_button.grid(column=7, row=5, sticky="e")
        self.main_screen_equal_button.grid(column=7, row=6, sticky="e")

        self.main_screen_number_one_button.place(x=0, y=300)
        self.main_screen_number_two_button.place(x=100, y=300)
        self.main_screen_number_three_button.place(x=200, y=300)
        self.main_screen_number_four_button.place(x=0, y=367.5)
        self.main_screen_number_five_button.place(x=100, y=367.5)
        self.main_screen_number_six_button.place(x=200, y=367.5)
        self.main_screen_number_seven_button.place(x=0, y=436)
        self.main_screen_number_eight_button.place(x=100, y=436)
        self.main_screen_number_nine_button.place(x=200, y=436)

        self.main_screen_number_zero_button.place(x=300, y=300)
        self.main_screen_negative_number_button.place(x=300, y=350.5)
        self.main_screen_comma_button.place(x=300, y=401)
        self.main_screen_mode_button.place(x=300, y=452)

        self.main_screen_base_option.place_forget()
        self.main_screen_x_button.grid_forget()

        self.main_screen_scientific_calculator_additional_layout: Scientific_calculator_additional_layout = Scientific_calculator_additional_layout()
        
        try:
            self.main_screen_graphical_calculator_additional_layout.destroy()

        except AttributeError:
            pass

    def __programming__(self) -> None:
        self.main_screen_expression_entry.configure(height=120)
        self.main_screen_equal_button.configure(command=self.__equation__)
        
        self.minsize(width=self.WIDTH, height=self.HEIGHT)
        
        self.main_screen_result_entry.place(x=2, y=165)

        self.main_screen_number_zero_button.configure(width=179.902)
        self.main_screen_negative_number_button.configure(width=179.902)
        self.main_screen_comma_button.configure(width=179.902)
        self.main_screen_mode_button.configure(width=179.902)

        self.main_screen_base_option.place(x=0, y=200)

        self.main_screen_number_one_button.place(x=0, y=250)
        self.main_screen_number_two_button.place(x=100, y=250)
        self.main_screen_number_three_button.place(x=200, y=250)
        self.main_screen_number_four_button.place(x=0, y=317.5)
        self.main_screen_number_five_button.place(x=100, y=317.5)
        self.main_screen_number_six_button.place(x=200, y=317.5)
        self.main_screen_number_seven_button.place(x=0, y=385)
        self.main_screen_number_eight_button.place(x=100, y=385)
        self.main_screen_number_nine_button.place(x=200, y=385)

        self.main_screen_number_zero_button.place(x=300, y=250)
        self.main_screen_negative_number_button.place(x=300, y=300.5)
        self.main_screen_comma_button.place(x=300, y=351)
        self.main_screen_mode_button.place(x=300, y=401)

        self.main_screen_pi_button.grid_forget()
        self.main_screen_e_button.grid_forget()
        self.main_screen_cbrt_button.grid_forget()
        self.main_screen_number_in_third_degree_button.grid_forget()
        self.main_screen_number_module_button.grid_forget()
        self.main_screen_factorial_button.grid_forget()
        self.main_screen_left_bracket_button.grid_forget()
        self.main_screen_right_bracket_button.grid_forget()

        self.main_screen_procent_button.grid_forget()
        self.main_screen_sqrt_button.grid_forget()
        self.main_screen_one_divided_by_x_button.grid_forget()
        self.main_screen_number_in_second_degree_button.grid_forget()
        self.main_screen_clear_button.grid_forget()
        self.main_screen_clear_everything_button.grid_forget()
        self.main_screen_clear_number_button.grid_forget()
        self.main_screen_plus_button.grid_forget()
        self.main_screen_minus_button.grid_forget()
        self.main_screen_multiply_button.grid_forget()
        self.main_screen_divide_button.grid_forget()
        self.main_screen_equal_button.grid_forget()
        self.main_screen_x_button.grid_forget()

        try:
            self.main_screen_scientific_calculator_additional_layout.destroy()
            self.main_screen_graphical_calculator_additional_layout.destroy()

        except AttributeError:
            pass
        
    def __graphical__(self) -> None:
        self.main_screen_expression_entry.configure(height=195)
        self.main_screen_equal_button.configure(command=self.__plot__)

        self.main_screen_base_option.place_forget()
        
        self.main_screen_result_entry.place_forget()
        
        self.minsize(width=self.WIDTH, height=self.HEIGHT)

        self.main_screen_number_zero_button.configure(width=119.902)
        self.main_screen_negative_number_button.configure(width=119.902)
        self.main_screen_comma_button.configure(width=119.902)
        self.main_screen_mode_button.configure(width=119.902)

        self.main_screen_left_bracket_button.grid(column=0, row=1, sticky="w")
        self.main_screen_right_bracket_button.grid(column=1, row=1, sticky="w")
        self.main_screen_one_divided_by_x_button.grid(column=2, row=1, sticky="w")
        self.main_screen_number_in_second_degree_button.grid(column=3, row=1, sticky="w")
        self.main_screen_x_button.grid(column=4, row=1, sticky="w")
        self.main_screen_clear_everything_button.grid(column=5, row=1, sticky="w")
        self.main_screen_clear_number_button.grid(column=6, row=1, sticky="w")
        self.main_screen_plus_button.grid(column=7, row=1, sticky="w")
        self.main_screen_minus_button.grid(column=7, row=2, sticky="w")
        self.main_screen_multiply_button.grid(column=7, row=3, sticky="e")
        self.main_screen_divide_button.grid(column=7, row=4, sticky="e")
        self.main_screen_equal_button.grid(column=7, row=5, sticky="e")

        self.main_screen_number_one_button.place(x=0, y=250)
        self.main_screen_number_two_button.place(x=100, y=250)
        self.main_screen_number_three_button.place(x=200, y=250)
        self.main_screen_number_four_button.place(x=0, y=317.5)
        self.main_screen_number_five_button.place(x=100, y=317.5)
        self.main_screen_number_six_button.place(x=200, y=317.5)
        self.main_screen_number_seven_button.place(x=0, y=385)
        self.main_screen_number_eight_button.place(x=100, y=385)
        self.main_screen_number_nine_button.place(x=200, y=385)

        self.main_screen_number_zero_button.place(x=300, y=250)
        self.main_screen_negative_number_button.place(x=300, y=300.5)
        self.main_screen_comma_button.place(x=300, y=351)
        self.main_screen_mode_button.place(x=300, y=401)

        self.main_screen_sqrt_button.grid_forget()
        self.main_screen_pi_button.grid_forget()
        self.main_screen_e_button.grid_forget()
        self.main_screen_cbrt_button.grid_forget()
        self.main_screen_number_in_third_degree_button.grid_forget()
        self.main_screen_number_module_button.grid_forget()
        self.main_screen_factorial_button.grid_forget()
        self.main_screen_procent_button.grid_forget()
        self.main_screen_clear_button.grid_forget()

        self.main_screen_graphical_calculator_additional_layout: Graphical_claculator_adittional_layout = Graphical_claculator_adittional_layout()
        
        try:
            self.main_screen_scientific_calculator_additional_layout.destroy()

        except AttributeError:
            pass

    def __button_operation__(self, button: str) -> None:
        self.button: str = button
        self.main_screen_expression_entry_data: str = self.main_screen_expression_entry.get()
        self.main_screen_expression_entry.delete("0", tkinter.END)
        self.main_screen_expression_entry.insert("0", f"{self.main_screen_expression_entry_data + self.button}")
        
    def __equation__(self) -> None:
        self.main_screen_expression_entry_data: str = self.main_screen_expression_entry.get()
        self.main_screen_result: str = eval(f"{self.main_screen_expression_entry_data}")

        self.main_screen_result_entry.configure(state="normal")
        self.main_screen_result_entry.delete("0", tkinter.END)
        if language_data == "Српски":
            self.main_screen_result_entry.insert("0", f"резултат је {self.main_screen_result}")

        elif language_data == "English":
            self.main_screen_result_entry.insert("0", f"result is {self.main_screen_result}")
            
        else:
            self.main_screen_result_entry.insert("0", f"результат {self.main_screen_result}")
            
        self.main_screen_result_entry.configure(state="disabled")

    def __procent__(self) -> None:
        self.main_screen_expression_entry_data: str = self.main_screen_expression_entry.get()
        self.main_screen_result: str = eval(f"{self.main_screen_expression_entry_data} / 100")

        self.main_screen_result_entry.configure(state="normal")
        self.main_screen_result_entry.delete("0", tkinter.END)
        if language_data == "Српски":
            self.main_screen_result_entry.insert("0", f"резултат је {self.main_screen_result}")

        elif language_data == "English":
            self.main_screen_result_entry.insert("0", f"result is {self.main_screen_result}")
            
        else:
            self.main_screen_result_entry.insert("0", f"результат {self.main_screen_result}")
        
        self.main_screen_result_entry.configure(state="disabled")

    def __clear_everything__(self) -> None:
        self.main_screen_expression_entry.delete("0", tkinter.END)

        self.main_screen_result_entry.configure(state="normal")
        self.main_screen_result_entry.delete("0", tkinter.END)
        self.main_screen_result_entry.configure(state="disabled") 

    def __mode_option__(self) -> None:
        try:  
            self.main_screen_mode_option: Menu_Option = Menu_Option()

        except ImportError:
            if language_data == "Српски":
                tkinter.messagebox.showerror(title="Грешка", message="Нема те фајл са подешавањима")

            elif language_data == "English":
                tkinter.messagebox.showerror(title="Error", message="You don't have settings file")

            else:
                tkinter.messagebox.showerror(title="Ошибка", message="У вас нет файла с настройками")
                                                                                     
    def __change_base__(self, configure: str) -> None:
        self.main_screen_count_system_result: str
        self.main_screen_expression_entry_data: str = self.main_screen_expression_entry.get()
        self.main_screen_base_data: str = self.main_screen_base_option.get()
        if self.main_screen_base_data == "binary-octal":
           self.main_screen_count_system_result = oct(int(self.main_screen_expression_entry_data, 2))[2:]

        elif self.main_screen_base_data == "binary-decimal":
           self.main_screen_count_system_result = int(self.main_screen_expression_entry_data, 2)

        elif self.main_screen_base_data == "binary-hexadecimal":
           self.main_screen_count_system_result = hex(int(self.main_screen_expression_entry_data, 2))[2:]

        elif self.main_screen_base_data == "octal-binary":
           self.main_screen_count_system_result = bin(int(self.main_screen_expression_entry_data, 8))[2:]

        elif self.main_screen_base_data == "octal-decimal":
           self.main_screen_count_system_result = int(self.main_screen_expression_entry_data, 8)

        elif self.main_screen_base_data == "octal-hexadecimal":
           self.main_screen_count_system_result = hex(int(self.main_screen_expression_entry_data, 8))[2:]

        elif self.main_screen_base_data == "decimal-binary":
           self.main_screen_count_system_result = bin(int(self.main_screen_expression_entry_data))[2:]

        elif self.main_screen_base_data == "decimal-octal":
           self.main_screen_count_system_result = oct(int(self.main_screen_expression_entry_data))[2:]

        elif self.main_screen_base_data == "decimal-hexadecimal":
           self.main_screen_count_system_result = hex(int(self.main_screen_expression_entry_data))[2:]

        elif self.main_screen_base_data == "hexadecimal-binary":
           self.main_screen_count_system_result = bin(int(self.main_screen_expression_entry_data, 16))[2:]

        elif self.main_screen_base_data == "hexadecimal-octal":
           self.main_screen_count_system_result = oct(int(self.main_screen_expression_entry_data, 16))[2:]

        else:
           self.main_screen_count_system_result = int(self.main_screen_expression_entry_data, 16)

        self.main_screen_result_entry.configure(state="normal")
        self.main_screen_result_entry.delete("0", tkinter.END)
        if language_data == "Српски":
            self.main_screen_result_entry.insert("0", f"резултат је {self.main_screen_count_system_result}")

        elif language_data == "English":
            self.main_screen_result_entry.insert("0", f"result is {self.main_screen_count_system_result}")
            
        else:
            self.main_screen_result_entry.insert("0", f"результат {self.self.main_screen_count_system_result}")
            
        self.main_screen_result_entry.configure(state="disabled")
        
    def __plot__(self) -> None:
        matplotlib.pyplot.style.use('_mpl-gallery')
        matplotlib.pyplot.title("My Calculus graphical calculator")
        
        self.main_screen_expression_entry_data: str = self.main_screen_expression_entry.get()
        x: numpy.linspace = numpy.linspace(-20, 20, 400)
        y: numpy.array = eval(f"{self.main_screen_expression_entry_data}")

        matplotlib.pyplot.plot(x, y, linewidth=1.0)

        matplotlib.pyplot.show()

    def __settings__(self) -> None:
        import My_Calculus_settings_menu
        
        self.main_screen_settings_window: My_Calculus_settings_menu.Settings_window = My_Calculus_settings_menu.Settings_window()
    
    @functools.cache
    def __run__(self) -> None:
        self.mainloop()

class Menu_Option(customtkinter.CTkToplevel):

    WIDTH: typing.Final[int] = 300
    HEIGHT: typing.Final[int] = 300
    WINDOW: typing.Final[str] = "-toolwindow"
    TITLE: typing.Final[str] = "My Calculus menu option"

    def __init__(self, *args, **kwargs) -> None:
        customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

        self.minsize(width=self.WIDTH, height=self.HEIGHT)
        self.resizable(False, False)
        self.title(self.TITLE)
        self.attributes(self.WINDOW, True)

        self.main_screen_classical_mode_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="класични", height=50, width=250, fg_color="green", text_color=text_color, font=("Roboto Bold", 25), command=program.__classical__)
        self.main_screen_classical_mode_button.grid(column=0, row=0)

        self.main_screen_scientific_mode_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="научни", height=50, width=250, fg_color="green", text_color=text_color, font=("Roboto Bold", 25), command=program.__scientific__)
        self.main_screen_scientific_mode_button.grid(column=0, row=1)

        self.main_screen_programming_mode_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="програмерски", height=50, width=250, fg_color="green", text_color=text_color, font=("Roboto Bold", 25), command=program.__programming__)
        self.main_screen_programming_mode_button.grid(column=0, row=2)
        
        self.main_screen_graphical_mode_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="графички", height=50, width=250, fg_color="green", text_color=text_color, font=("Roboto Bold", 25), command=program.__graphical__)
        self.main_screen_graphical_mode_button.grid(column=0, row=3)

        self.main_screen_settings_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="подешавања", height=50, width=250, fg_color="green", text_color=text_color, font=("Roboto Bold", 25), command=program.__settings__)
        self.main_screen_settings_button.grid(column=0, row=4)

        if language_data == "Српски":
            self.main_screen_classical_mode_button.configure(text="класични")
            self.main_screen_scientific_mode_button.configure(text="научни")
            self.main_screen_programming_mode_button.configure(text="програмерски")
            self.main_screen_graphical_mode_button.configure(text="графички")
            self.main_screen_settings_button.configure(text="подешавања")

        elif language_data == "English":
            self.main_screen_classical_mode_button.configure(text="classic")
            self.main_screen_scientific_mode_button.configure(text="scientific")
            self.main_screen_programming_mode_button.configure(text="programming")
            self.main_screen_graphical_mode_button.configure(text="graphical")
            self.main_screen_settings_button.configure(text="settings")

        else:
            self.main_screen_classical_mode_button.configure(text="классический")
            self.main_screen_scientific_mode_button.configure(text="научный")
            self.main_screen_programming_mode_button.configure(text="программный")
            self.main_screen_graphical_mode_button.configure(text="графический")
            self.main_screen_settings_button.configure(text="настройки")
            

class Scientific_calculator_additional_layout(customtkinter.CTkToplevel):
     
    WIDTH: typing.Final[int] = 965 
    HEIGHT: typing.Final[int] = 411
    WINDOW: typing.Final[str] = "-toolwindow"
    TITLE: typing.Final[str] = "My Calculus scientific calculator additional layout"

    def __init__(self, *args, **kwargs) -> None:
        customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

        self.minsize(width=self.WIDTH, height=self.HEIGHT)
        self.resizable(False, False)
        self.title(self.TITLE)
        self.attributes(self.WINDOW, True)

        self.main_screen_functions_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text="Functions", text_color=text_color, font=("Roboto Bold", 55))
        self.main_screen_functions_text.place(x=2, y=0)

        self.main_screen_logarith_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="logyX", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("log(x,y)"))
        self.main_screen_logarith_function_button.place(x=2, y=62)
        
        self.main_screen_natural_logarith_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="ln", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("log()"))
        self.main_screen_natural_logarith_function_button.place(x=72, y=62)

        self.main_screen_e_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="eX", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("e**"))
        self.main_screen_e_function_button.place(x=142, y=62)

        self.main_screen_root_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="y\/X", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("xyrt(number, x, y)"))
        self.main_screen_root_function_button.place(x=212, y=62)

        self.main_screen_number_in_y_degree_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="xY", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("**"))
        self.main_screen_number_in_y_degree_function_button.place(x=282, y=62)

        self.main_screen_two_in_x_degree_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="2X", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("2**"))
        self.main_screen_two_in_x_degree_function_button.place(x=352, y=62)

        self.main_screen_ten_in_x_degree_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="10X", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("10**"))
        self.main_screen_ten_in_x_degree_function_button.place(x=422, y=62)

        self.main_screen_trigonomical_functions_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text="Trigonomical functions", text_color=text_color, font=("Roboto Bold", 55))
        self.main_screen_trigonomical_functions_text.place(x=2, y=110)

        self.main_screen_sin_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="sin", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("sin()"))
        self.main_screen_sin_function_button.place(x=2, y=175)

        self.main_screen_cos_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="cos", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("cos()"))
        self.main_screen_cos_function_button.place(x=72, y=175)

        self.main_screen_tan_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="tan", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("tan()"))
        self.main_screen_tan_function_button.place(x=142, y=175)

        self.main_screen_cotan_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="cotan", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("cotan()"))
        self.main_screen_cotan_function_button.place(x=212, y=175)

        self.main_screen_asin_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="asin", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("asin()"))
        self.main_screen_asin_function_button.place(x=283, y=175)

        self.main_screen_acos_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="acos", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("acos()"))
        self.main_screen_acos_function_button.place(x=353, y=175)

        self.main_screen_atan_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="atan", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("atan()"))
        self.main_screen_atan_function_button.place(x=423, y=175)

        self.main_screen_acotan_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="acotan", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("acotan()"))
        self.main_screen_acotan_function_button.place(x=2, y=226)

        self.main_screen_sinh_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="sinh", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("sinh()"))
        self.main_screen_sinh_function_button.place(x=86, y=226)

        self.main_screen_cosh_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="cosh", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("cosh()"))
        self.main_screen_cosh_function_button.place(x=156, y=226)

        self.main_screen_tanh_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="tanh", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("cosh()"))
        self.main_screen_tanh_function_button.place(x=226, y=226)

        self.main_screen_cotanh_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="cotanh", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("cosh()"))
        self.main_screen_cotanh_function_button.place(x=296, y=226)

        self.main_screen_asinh_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="asinh", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("asinh()"))
        self.main_screen_asinh_function_button.place(x=380, y=226)

        self.main_screen_acosh_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="acosh", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("acosh()"))
        self.main_screen_acosh_function_button.place(x=450, y=226)

        self.main_screen_atanh_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="atanh", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("atanh()"))
        self.main_screen_atanh_function_button.place(x=2, y=277)

        self.main_screen_atanh_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="acotanh", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("acotanh()"))
        self.main_screen_atanh_function_button.place(x=75, y=277)

        self.main_screen_degree_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="deg", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("degrees()"))
        self.main_screen_degree_function_button.place(x=172, y=277)

        self.main_screen_radian_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="rad", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("radians()"))
        self.main_screen_radian_function_button.place(x=242, y=277)
        
        if language_data == "Српски":
            self.main_screen_functions_text.configure(text="Функције")
            self.main_screen_trigonomical_functions_text.configure(text="Тригонометричке функције")

        elif language_data == "English":
            self.main_screen_functions_text.configure(text="Functions")
            self.main_screen_trigonomical_functions_text.configure(text="Trigonometric functions")

        else:
            self.main_screen_functions_text.configure(text="Функции")
            self.main_screen_trigonomical_functions_text.configure(text="Тригонометрические функции")
   
        
class Graphical_claculator_adittional_layout(customtkinter.CTkToplevel):
    WIDTH: typing.Final[int] = 966 
    HEIGHT: typing.Final[int] = 56
    WINDOW: typing.Final[str] = "-toolwindow"
    TITLE: typing.Final[str] = "My Calculus graphical calculator additional layout"

    def __init__(self, *args, **kwargs) -> None:
        customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

        self.minsize(width=self.WIDTH, height=self.HEIGHT)
        self.resizable(False, False)
        self.title(self.TITLE)
        self.attributes(self.WINDOW, True)

        self.main_screen_functions_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text="Functions", text_color=text_color, font=("Roboto Bold", 55))
        self.main_screen_functions_text.place(x=2, y=0)
        
        self.main_screen_logarith_base_2_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="log2", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("numpy.log2()"))
        self.main_screen_logarith_base_2_function_button.place(x=0, y=70)

        self.main_screen_ln_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="ln", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("numpy.log()"))
        self.main_screen_ln_function_button.place(x=72, y=70)
        
        self.main_screen_logarith_base_10_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="log10", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("numpy.log10()"))
        self.main_screen_logarith_base_10_function_button.place(x=142, y=70)

        self.main_screen_e_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="eX", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("e**"))
        self.main_screen_e_function_button.place(x=212, y=70)

        self.main_screen_sqrt_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="\/", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("numpy.sqrt()"))
        self.main_screen_sqrt_function_button.place(x=282, y=70)

        self.main_screen_number_in_y_degree_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="xY", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("**"))
        self.main_screen_number_in_y_degree_function_button.place(x=352, y=70)

        self.main_screen_two_in_x_degree_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="2X", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("2**"))
        self.main_screen_two_in_x_degree_function_button.place(x=422, y=70)

        self.main_screen_ten_in_x_degree_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="10X", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("10**"))
        self.main_screen_ten_in_x_degree_function_button.place(x=492, y=70)

        self.main_screen_module_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="|X|", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("numpy.fabs()"))
        self.main_screen_module_function_button.place(x=562, y=70)

        self.main_screen_sin_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="sin", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("numpy.sin()"))
        self.main_screen_sin_function_button.place(x=632, y=70)

        self.main_screen_cos_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="cos", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__("numpy.cos()"))
        self.main_screen_cos_function_button.place(x=702, y=70)  
        
        if language_data == "Српски":
            self.main_screen_functions_text.configure(text="Функције")

        elif language_data == "English":
            self.main_screen_functions_text.configure(text="Functions")

        else:
            self.main_screen_functions_text.configure(text="Функции")

if __name__ == "__main__":
	try:
		program: Program = Program()
		program.__run__()
															 
	except FileNotFoundError:
		tkinter.messagebox.showerror(title="file not found error", message=f"срб: грешка: није нађен фајл \n eng: error: missing data file \nрус: ошибка: не найден файл")

	except tkinter.TclError:
		tkinter.messagebox.showerror(title="icon file not found error", message=f"срб: грешка: није нађен фајл иконица \neng: error: missing icon file \nрус: ошибка: не найден файл с иконкой")

	except EOFError:
		tkinter.messagebox.showerror(title="corrupted file error", message=f"срб: грешка: повређен фајл \n eng: error: corrupted data file \nрус: ошибка: повреждён файл")