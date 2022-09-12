class Formatter(str):
    def __call__(self,text:str):
        self = Formatter(text)
        return self
    
    def new_line(self,text=""):
        target = self if not text else text
        return target+"\n"
    
    def italic(self,text:str=""):
        target = self if not text else text
        return Formatter(f"*{target}*")
    
    def bold(self,text:str=""):
        target = self if not text else text
        return Formatter(f"**{target}**")
    
    def underline(self,text:str=""):
        target = self if not text else text
        return Formatter(f"__{target}__")
    
    def striket_hrough(self,text:str=""):
        target = self if not text else text
        return Formatter(f"~~{target}~~")
    
    def hide(self,text:str=""):
        target = self if not text else text
        return Formatter(f"||{target}||")
    
    def single_block(self,text:str=""):
        target = self if not text else text
        return Formatter(f"> {target}")
    
    def single_code_block(self,text:str=""):
        target = self if not text else text
        return Formatter(f"`{target}`")
    
    def multiple_code_block(self,text:str,code="python"):
        return Formatter(f"""```{code}
{text}
```""")