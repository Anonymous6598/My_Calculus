from My_Calculus import Program
from tkinter.messagebox import showwarning 
import customtkinter, pickle

with open("my_calculus_settings.pickle", "rb") as data:
    language_data: str = pickle.load(data)

with open("my_calculus_text_color.pickle", "rb") as text_color_data:
	text_color: str = pickle.load(text_color_data)

with open("my_calculus_expression_entry_color.pickle", "rb") as expression_entry_color_data:
	expression_entry_color: str = pickle.load(expression_entry_color_data)

with open("my_calculus_expression_entry_text_color.pickle", "rb") as expression_entry_text_color_data:
	expression_entry_text_color: str = pickle.load(expression_entry_text_color_data)

with open("my_calculus_button_color.pickle", "rb") as button_color_data:
	button_color: str = pickle.load(button_color_data)

class Settings_window(customtkinter.CTkToplevel):
     
    WIDTH: int = 655 
    HEIGHT: int = 471
    TITLE: str = "My Calculus settings window"
    WINDOW: str = "-toolwindow"

    def __init__(self, *args, **kwargs) -> None:
        customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

        self.minsize(width=self.WIDTH, height=self.HEIGHT)
        self.resizable(False, False)
        self.title(self.TITLE)
        self.attributes(self.WINDOW, True)

        self.main_screen_settings_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text="Подешавања", text_color=text_color, font=("Roman", 75))
        self.main_screen_settings_text.place(x=0, y=0)

        self.main_screen_language_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text="Језици", text_color=text_color, font=("Roman", 50))
        self.main_screen_language_text.place(x=0, y=87)

        self.main_screen_settings_language_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self, values=["Српски", "English", "Русский"], selected_color=button_color, command=self.__language_settings__)
        self.main_screen_settings_language_option.place(x=15, y=147)

        self.main_screen_settings_language_option.set(language_data)
        
        self.main_screen_settings_customatization_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text="Спољни изглед", text_color=text_color, font=("Roboto Bold", 36))
        self.main_screen_settings_customatization_text.place(x=15, y=207)

        self.main_screen_settings_customatization_table: customtkinter.CTkTabview = customtkinter.CTkTabview(master=self, height=50, width=400, border_width=1, border_color=("black", "white"), segmented_button_selected_color=button_color, text_color=text_color)
        self.main_screen_settings_customatization_table.place(x=15, y=243)

        self.main_screen_settings_customatization_table.add("1")
        self.main_screen_settings_customatization_table.add("2")
        self.main_screen_settings_customatization_table.add("3")

        self.main_screen_settings_customatization_text_color_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self.main_screen_settings_customatization_table.tab("1"), text="Боја текста", text_color=text_color, font=("Roboto Bold", 36))
        self.main_screen_settings_customatization_text_color_text.grid(column=0, row=0)

        self.main_screen_settings_customatization_text_color_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self.main_screen_settings_customatization_table.tab("1"), text_color=text_color, values=["red", "blue", "green", "black", "white"], selected_color=button_color, command=self.__change_text_color__)
        self.main_screen_settings_customatization_text_color_option.grid(column=0, row=1)


        self.main_screen_settings_customatization_expression_entry_color_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self.main_screen_settings_customatization_table.tab("2"), text="Боја поља", text_color=text_color, font=("Roboto Bold", 36))
        self.main_screen_settings_customatization_expression_entry_color_text.grid(column=0, row=0)

        self.main_screen_settings_customatization_expression_entry_color_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self.main_screen_settings_customatization_table.tab("2"), values=["red", "blue", "green", "black", "white", "transparent"], text_color=text_color, selected_color=button_color, command=self.__change_expression_entry_color__)
        self.main_screen_settings_customatization_expression_entry_color_option.grid(column=0, row=1)

        self.main_screen_settings_customatization_expression_entry_color_text_color_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self.main_screen_settings_customatization_table.tab("2"), text="Боја текста поља", text_color=text_color, font=("Roboto Bold", 36))
        self.main_screen_settings_customatization_expression_entry_color_text_color_text.grid(column=0, row=2)

        self.main_screen_settings_customatization_expression_entry_text_color_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self.main_screen_settings_customatization_table.tab("2"), values=["red", "blue", "green", "black", "white"], text_color=text_color, selected_color=button_color, command=self.__change_expression_entry_text_color__)
        self.main_screen_settings_customatization_expression_entry_text_color_option.grid(column=0, row=3)


        self.main_screen_settings_customatization_button_color_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self.main_screen_settings_customatization_table.tab("3"), text="Боја дугма", text_color=text_color, font=("Roboto Bold", 36))
        self.main_screen_settings_customatization_button_color_text.grid(column=0, row=0)

        self.main_screen_settings_customatization_button_color_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self.main_screen_settings_customatization_table.tab("3"), values=["red", "blue", "green", "black", "orange", "yellow", "purple"], text_color=text_color, selected_color=button_color, command=self.__change_button_color__)
        self.main_screen_settings_customatization_button_color_option.grid(column=0, row=1)

        self.main_screen_settings_customatization_text_color_option.set(text_color)

        self.main_screen_settings_customatization_expression_entry_color_option.set(expression_entry_color)

        self.main_screen_settings_customatization_expression_entry_text_color_option.set(expression_entry_text_color)

        self.main_screen_settings_customatization_button_color_option.set(button_color)

        if language_data == "Српски":
            self.main_screen_settings_text.configure(text="Подешавања")
            self.main_screen_language_text.configure(text="Језици")
            self.main_screen_settings_customatization_text.configure(text="Спољни изглед")
            self.main_screen_settings_customatization_text_color_text.configure(text="Боја текста")
            self.main_screen_settings_customatization_expression_entry_color_text.configure(text="Боја поља")
            self.main_screen_settings_customatization_expression_entry_color_text_color_text.configure(text="Боја текста поља")
            self.main_screen_settings_customatization_button_color_text.configure(text="Боја дугма")

        elif language_data == "English":
            self.main_screen_settings_text.configure(text="Settings")
            self.main_screen_language_text.configure(text="Languages")
            self.main_screen_settings_customatization_text.configure(text="Customatization")
            self.main_screen_settings_customatization_text_color_text.configure(text="Text color")
            self.main_screen_settings_customatization_expression_entry_color_text.configure(text="Expression entry color")
            self.main_screen_settings_customatization_expression_entry_color_text.configure(text="Expression entry text color")
            self.main_screen_settings_customatization_button_color_text.configure(text="Button color")

        else:
            self.main_screen_settings_text.configure(text="Настройки")
            self.main_screen_language_text.configure(text="Языки")
            self.main_screen_settings_customatization_text.configure(text="Внешний вид")
            self.main_screen_settings_customatization_text_color_text.configure(text="Цвет текста")
            self.main_screen_settings_customatization_expression_entry_color_text.configure(text="Цвет поля")
            self.main_screen_settings_customatization_expression_entry_color_text.configure(text="Цвет текста поля")
            self.main_screen_settings_customatization_button_color_text.configure(text="Цвет кнопки")

    def __language_settings__(self, pickle_serializer: pickle) -> None:
        self.main_screen_settings_language_option_data: str = self.main_screen_settings_language_option.get()
        with open("my_calculus_settings.pickle", "wb") as self.data:
            pickle.dump(self.main_screen_settings_language_option_data, self.data)

        if self.main_screen_settings_language_option_data == "Српски":
            showwarning(title="Пажња", message="Рестартуј програм")

        elif self.main_screen_settings_language_option_data == "English":
            showwarning(title="Warning", message="Restart program")
            
        else:
            showwarning(title="Внимание", message="Перезагрузите программу")
    
    def __change_text_color__(self, pickle_serializer: pickle) -> None:
        self.main_screen_settings_customatization_text_color_option_data: str = self.main_screen_settings_customatization_text_color_option.get()
        with open("my_calculus_text_color.pickle", "wb") as self.text_color_data:
            pickle.dump(self.main_screen_settings_customatization_text_color_option_data, self.text_color_data)            

        if language_data == "Српски":        
            showwarning(title="Пажња", message="Рестартуј програм")
            
        elif language_data == "English":
            showwarning(title="Warning", message="Restart program")
            
        else:
            showwarning(title="Внимание", message="Перезагрузите программу")

    def __change_expression_entry_color__(self, pickle_serialization: pickle) -> None:
        self.main_screen_settings_customatization_expression_entry_color_option_data: str = self.main_screen_settings_customatization_expression_entry_color_option.get()
        with open("my_calculus_expression_entry_color.pickle", "wb") as self.expression_entry_color_data:
            pickle.dump(self.main_screen_settings_customatization_expression_entry_color_option_data, self.expression_entry_color_data)

        if language_data == "Српски":
            showwarning(title="Пажња", message="Рестартуј програм")

        elif language_data == "English":
            showwarning(title="Warning", message="Restart program")

        else:
            showwarning(title="Внимание", message="Перезагрузите программу")

    def __change_expression_entry_text_color__(self, pickle_serialization: pickle) -> None:
        self.main_screen_settings_customatization_expression_entry_text_color_option_data: str = self.main_screen_settings_customatization_expression_entry_text_color_option.get()
        with open("my_calculus_expression_entry_text_color.pickle", "wb") as self.expression_entry_text_color_data:
            pickle.dump(self.main_screen_settings_customatization_expression_entry_text_color_option_data, self.expression_entry_text_color_data)

        if language_data == "Српски":
            showwarning(title="Пажња", message="Рестартуј програм")

        elif language_data == "English":
            showwarning(title="Warning", message="Restart program")

        else:
            showwarning(title="Внимание", message="Перезагрузите программу")

    def __change_button_color__(self, pickle_serialization: pickle) -> None:
        self.main_screen_settings_customatization_button_color_option_data: str = self.main_screen_settings_customatization_button_color_option.get()
        with open("my_calculus_button_color.pickle", "wb") as self.button_color_data:
            pickle.dump(self.main_screen_settings_customatization_button_color_option_data, self.button_color_data)

        if language_data == "Српски":
            showwarning(title="Пажња", message="Рестартуј програм")

        elif language_data == "English":
            showwarning(title="Warning", message="Restart program")

        else:
            showwarning(title="Внимание", message="Перезагрузите программу")        

program: Program = Program()