import abc

class My_Calculus_settings_window_interface(abc.ABC):
    
     @abc.abstractmethod
     def __language_settings__() -> None:
        pass
     
     @abc.abstractmethod
     def __change_text_color__() -> None:
        pass
     
     @abc.abstractmethod
     def __change_expression_entry_color__() -> None:
        pass
     
     @abc.abstractmethod
     def __change_expression_entry_text_color__() -> None:
        pass
     
     @abc.abstractmethod
     def __change_button_color__() -> None:
        pass
          