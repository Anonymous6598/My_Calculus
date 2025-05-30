import g4f, g4f.Provider, typing, My_Calculus_AI_interface

class My_Calculus_LM(My_Calculus_AI_interface.My_Calculus_AI_interface):
    
    LANGUAGE_MODEL: typing.Final[str] = f"gpt-4o"
    
    def __init__(self: typing.Self) -> None:
       self.language_model: str = self.LANGUAGE_MODEL 

    @typing.override
    def __response__(self: typing.Self, prompt: str) -> str:
        self.user_query: list[dict[str, str]] = [{f"role": f"user", f"content": prompt}]
        
        self.response: str = g4f.ChatCompletion.create(model=self.language_model, messages=self.user_query)

        return self.response