import customtkinter, tkinter.messagebox, pickle, typing, My_Calculus_settings_window_interface, My_Calculus
from My_Calculus_interface import My_Calculus_interface

with open(f"my_calculus_settings.pickle", f"rb+") as data: language_data: str = pickle.load(data)

with open(f"my_calculus_text_color.pickle", f"rb+") as text_color_data: text_color: str = pickle.load(text_color_data)

with open(f"my_calculus_expression_entry_color.pickle", f"rb+") as expression_entry_color_data: expression_entry_color: str = pickle.load(expression_entry_color_data)

with open(f"my_calculus_expression_entry_text_color.pickle", f"rb+") as expression_entry_text_color_data: expression_entry_text_color: str = pickle.load(expression_entry_text_color_data)

with open(f"my_calculus_button_color.pickle", f"rb+") as button_color_data: button_color: str = pickle.load(button_color_data)

class Settings_window(customtkinter.CTkToplevel, My_Calculus_settings_window_interface.My_Calculus_settings_window_interface):
     
    WIDTH: typing.Final[int] = 655 
    HEIGHT: typing.Final[int] = 571
    TITLE: typing.Final[str] = f"My Calculus settings window"
    WINDOW: typing.Final[str] = f"-toolwindow"

    def __init__(self: typing.Self, *args, **kwargs) -> None:
        customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)
        self.title(self.TITLE)
        self.attributes(self.WINDOW, True)

        self.main_screen_settings_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text=f"Подешавања", text_color=text_color, font=(f"Roboto Bold", 75))
        self.main_screen_settings_text.place(x=0, y=0)

        self.main_screen_language_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text=f"Језици", text_color=text_color, font=(f"Roboto Bold", 50))
        self.main_screen_language_text.place(x=0, y=87)

        self.main_screen_settings_language_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self, values=[f"Српски", f"English", f"Русский"], selected_color=button_color, command=self.__language_settings__)
        self.main_screen_settings_language_option.place(x=15, y=147)

        self.main_screen_settings_language_option.set(language_data)
        
        self.main_screen_settings_customatization_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text=f"Спољни изглед", text_color=text_color, font=(f"Roboto Bold", 36))
        self.main_screen_settings_customatization_text.place(x=15, y=207)

        self.main_screen_settings_customatization_table: customtkinter.CTkTabview = customtkinter.CTkTabview(master=self, height=50, width=400, border_width=1, border_color=(f"black", f"white"), segmented_button_selected_color=button_color, text_color=text_color)
        self.main_screen_settings_customatization_table.place(x=15, y=243)

        self.main_screen_settings_customatization_table.add("1")
        self.main_screen_settings_customatization_table.add("2")
        self.main_screen_settings_customatization_table.add("3")

        self.main_screen_settings_customatization_text_color_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self.main_screen_settings_customatization_table.tab(f"1"), text=f"Боја текста", text_color=text_color, font=(f"Roboto Bold", 36))
        self.main_screen_settings_customatization_text_color_text.grid(column=0, row=0)

        self.main_screen_settings_customatization_text_color_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self.main_screen_settings_customatization_table.tab(f"1"), text_color=text_color, values=[f"red", f"blue", f"green", f"black", f"white"], selected_color=button_color, command=self.__change_text_color__)
        self.main_screen_settings_customatization_text_color_option.grid(column=0, row=1)


        self.main_screen_settings_customatization_expression_entry_color_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self.main_screen_settings_customatization_table.tab(f"2"), text=f"Боја поља", text_color=text_color, font=(f"Roboto Bold", 36))
        self.main_screen_settings_customatization_expression_entry_color_text.grid(column=0, row=0)

        self.main_screen_settings_customatization_expression_entry_color_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self.main_screen_settings_customatization_table.tab(f"2"), values=[f"red", f"blue", f"green", f"black", f"white", f"transparent"], text_color=text_color, selected_color=button_color, command=self.__change_expression_entry_color__)
        self.main_screen_settings_customatization_expression_entry_color_option.grid(column=0, row=1)

        self.main_screen_settings_customatization_expression_entry_color_text_color_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self.main_screen_settings_customatization_table.tab(f"2"), text=f"Боја текста поља", text_color=text_color, font=(f"Roboto Bold", 36))
        self.main_screen_settings_customatization_expression_entry_color_text_color_text.grid(column=0, row=2)

        self.main_screen_settings_customatization_expression_entry_text_color_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self.main_screen_settings_customatization_table.tab(f"2"), values=[f"red", f"blue", f"green", f"black", f"white"], text_color=text_color, selected_color=button_color, command=self.__change_expression_entry_text_color__)
        self.main_screen_settings_customatization_expression_entry_text_color_option.grid(column=0, row=3)


        self.main_screen_settings_customatization_button_color_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self.main_screen_settings_customatization_table.tab(f"3"), text=f"Боја дугма", text_color=text_color, font=(f"Roboto Bold", 36))
        self.main_screen_settings_customatization_button_color_text.grid(column=0, row=0)

        self.main_screen_settings_customatization_button_color_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self.main_screen_settings_customatization_table.tab(f"3"), values=[f"red", f"blue", f"green", f"black", f"orange", f"yellow", f"purple"], text_color=text_color, selected_color=button_color, command=self.__change_button_color__)
        self.main_screen_settings_customatization_button_color_option.grid(column=0, row=1)

        self.main_screen_settings_customatization_text_color_option.set(text_color)

        self.main_screen_settings_customatization_expression_entry_color_option.set(expression_entry_color)

        self.main_screen_settings_customatization_expression_entry_text_color_option.set(expression_entry_text_color)

        self.main_screen_settings_customatization_button_color_option.set(button_color)

        match language_data: 
            case "Српски":
                self.main_screen_settings_text.configure(text=f"Подешавања")
                self.main_screen_language_text.configure(text=f"Језици")
                self.main_screen_settings_customatization_text.configure(text=f"Спољни изглед")
                self.main_screen_settings_customatization_text_color_text.configure(text=f"Боја текста")
                self.main_screen_settings_customatization_expression_entry_color_text.configure(text=f"Боја поља")
                self.main_screen_settings_customatization_expression_entry_color_text_color_text.configure(text=f"Боја текста поља")
                self.main_screen_settings_customatization_button_color_text.configure(text=f"Боја дугма")

            case "English":
                self.main_screen_settings_text.configure(text=f"Settings")
                self.main_screen_language_text.configure(text=f"Languages")
                self.main_screen_settings_customatization_text.configure(text=f"Customatization")
                self.main_screen_settings_customatization_text_color_text.configure(text=f"Text color")
                self.main_screen_settings_customatization_expression_entry_color_text.configure(text=f"Expression entry color")
                self.main_screen_settings_customatization_expression_entry_color_text.configure(text=f"Expression entry text color")
                self.main_screen_settings_customatization_button_color_text.configure(text=f"Button color")

            case _:
                self.main_screen_settings_text.configure(text="Настройки")
                self.main_screen_language_text.configure(text="Языки")
                self.main_screen_settings_customatization_text.configure(text="Внешний вид")
                self.main_screen_settings_customatization_text_color_text.configure(text="Цвет текста")
                self.main_screen_settings_customatization_expression_entry_color_text.configure(text="Цвет поля")
                self.main_screen_settings_customatization_expression_entry_color_text.configure(text="Цвет текста поля")
                self.main_screen_settings_customatization_button_color_text.configure(text="Цвет кнопки")

    @typing.override
    def __language_settings__(self: typing.Self, pickle_serializer: pickle) -> None:
        self.main_screen_settings_language_option_data: str = self.main_screen_settings_language_option.get()
        with open(f"my_calculus_settings.pickle", f"wb+") as self.data: pickle.dump(self.main_screen_settings_language_option_data, self.data)

        match self.main_screen_settings_language_option_data:
            case "Српски": tkinter.messagebox.showwarning(title=f"Пажња", message=f"Рестартуј програм")

            case "English": tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")
            
            case _: tkinter.messagebox.showwarning(title=f"Внимание", message=f"Перезагрузите программу")
    
    @typing.override
    def __change_text_color__(self: typing.Self, pickle_serializer: pickle) -> None:
        self.main_screen_settings_customatization_text_color_option_data: str = self.main_screen_settings_customatization_text_color_option.get()
        with open(f"my_calculus_text_color.pickle", f"wb+") as self.text_color_data: pickle.dump(self.main_screen_settings_customatization_text_color_option_data, self.text_color_data)            

        match language_data: 
            case "Српски": tkinter.messagebox.showwarning(title=f"Пажња", message=f"Рестартуј програм")
            
            case "English": tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")
            
            case _: tkinter.messagebox.showwarning(title=f"Внимание", message=f"Перезагрузите программу")

    @typing.override
    def __change_expression_entry_color__(self: typing.Self, pickle_serialization: pickle) -> None:
        self.main_screen_settings_customatization_expression_entry_color_option_data: str = self.main_screen_settings_customatization_expression_entry_color_option.get()
        with open(f"my_calculus_expression_entry_color.pickle", f"wb+") as self.expression_entry_color_data: pickle.dump(self.main_screen_settings_customatization_expression_entry_color_option_data, self.expression_entry_color_data)

        match language_data: 
            case "Српски": tkinter.messagebox.showwarning(title=f"Пажња", message=f"Рестартуј програм")
            
            case "English": tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")
            
            case _: tkinter.messagebox.showwarning(title=f"Внимание", message=f"Перезагрузите программу")

    @typing.override
    def __change_expression_entry_text_color__(self: typing.Self, pickle_serialization: pickle) -> None:
        self.main_screen_settings_customatization_expression_entry_text_color_option_data: str = self.main_screen_settings_customatization_expression_entry_text_color_option.get()
        with open(f"my_calculus_expression_entry_text_color.pickle", f"wb+") as self.expression_entry_text_color_data: pickle.dump(self.main_screen_settings_customatization_expression_entry_text_color_option_data, self.expression_entry_text_color_data)

        match language_data: 
            case "Српски": tkinter.messagebox.showwarning(title=f"Пажња", message=f"Рестартуј програм")
            
            case "English": tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")
            
            case _: tkinter.messagebox.showwarning(title=f"Внимание", message=f"Перезагрузите программу")

    @typing.override
    def __change_button_color__(self: typing.Self, pickle_serialization: pickle) -> None:
        self.main_screen_settings_customatization_button_color_option_data: str = self.main_screen_settings_customatization_button_color_option.get()
        with open(f"my_calculus_button_color.pickle", f"wb+") as self.button_color_data: pickle.dump(self.main_screen_settings_customatization_button_color_option_data, self.button_color_data)

        match language_data: 
            case "Српски": tkinter.messagebox.showwarning(title=f"Пажња", message=f"Рестартуј програм")
            
            case "English": tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")
            
            case _: tkinter.messagebox.showwarning(title=f"Внимание", message=f"Перезагрузите программу")

program: My_Calculus.Program = My_Calculus.Program()
