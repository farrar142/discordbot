class Formatter(str):
    def __call__(self,text:str):
        self = Formatter(text)
        return self
    
    def new_line(self,text=""):
        if text:
            return Formatter(self+text+"\n")
        else:
            return Formatter(self+"\n")
    
    def italic(self,text:str=""):
        if text:
            return Formatter(f"{self}*{text}*")
        else:
            return Formatter(f"*{self}*")
            
    
    def bold(self,text:str=""):
        if text:
            return Formatter(f"{self}**{text}**")
        else:
            return Formatter(f"**{self}**")
    
    def underline(self,text:str=""):
        if text:
            return Formatter(f"{self}__{text}__")
        else:
            return Formatter(f"__{self}__")
    
    def striket_hrough(self,text:str=""):
        if text:
            return Formatter(f"{self}~~{text}~~")
        else:
            return Formatter(f"~~{self}~~")
    
    def hide(self,text:str=""):
        if text:
            return Formatter(f"{self}||{text}||")
        else:
            return Formatter(f"||{self}||")
    
    def single_block(self,text:str=""):
        if text:
            return Formatter(f"{self}> {text}")
        else:
            return Formatter(f"> {self}")
    
    def single_code_block(self,text:str=""):
        if text:
            return Formatter(f"{self}`{text}`")
        else:
            return Formatter(f"`{self}`")
    
    def multiple_code_block(self,text:str,code="python"):
        return Formatter(f"""```{code}
{text}
```""")