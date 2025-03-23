import abc, typing

class My_Calculus_AI_interface(abc.ABC):
    
     @abc.abstractmethod
     def __response__(self: typing.Self, prompt: str) -> str:
        pass
