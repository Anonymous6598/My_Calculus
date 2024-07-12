import customtkinter, tkinter, My_Calculus_AI_window_interface, typing, asyncio, My_Calculus_AI

class My_Calculus_AI_window(customtkinter.CTkToplevel, My_Calculus_AI_window_interface.My_Calculus_AI_window_interface):
	
	HEIGHT: typing.Final[int] = 375
	WIDTH: typing.Final[int] = 655
	TITLE: typing.Final[str] = f"My Claculus AI assistant"
	ICON: typing.Final[str] = f"my calculus icon.ico"

	def __init__(self: typing.Self, *args, **kwargs) -> None:
		customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

		self.title(self.TITLE)
		self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
		self.resizable(False, False)
		self.after(250, lambda: self.iconbitmap(self.ICON))

		self.ai_window_textbox: customtkinter.CTkTextbox = customtkinter.CTkTextbox(master=self, height=265, width=524, corner_radius=0, fg_color=f"transparent", text_color=(f"black", f"white"))
		self.ai_window_textbox.place(x=0, y=0)

		self.ai_window_textbox.configure(state=f"disabled")

		self.ai_window_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self, height=30, width=524, border_width=0, fg_color=f"transparent", placeholder_text=f"...")
		self.ai_window_entry.place(x=0, y=269)

		self.ai_window_entry.bind(f"<Return>", self.__response_from_ai__)

	@typing.override
	def __response_from_ai__(self: typing.Self, configure: str | None = None) -> None:
		self.ai_window_entry_data: str = self.ai_window_entry.get()

		self.ai_window_textbox.configure(state=f"normal")
		self.query: str = asyncio.run(My_Calculus_AI.My_Calculus_LM().__response__(self.ai_window_entry_data))

		self.ai_window_textbox.insert(tkinter.END, f"{self.query}\n", f"-1.0")
		self.ai_window_textbox.configure(state=f"disabled")
		self.ai_window_entry.delete(f"-1", tkinter.END)

