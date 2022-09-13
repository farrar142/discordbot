from typing import List
from typing_extensions import Self

def new_line_checker(cb):
    def wrapper(*args,**kwargs):
        print(args,kwargs)
        return cb(*args,**kwargs)
    return wrapper
class Formatter(str):
    lines:List[Self] = []
    is_new_lined = False
    
    def __call__(self,text:str):
        self = Formatter(text)
        return self
    
    def get_new_line(self):
        if self.is_new_lined:
            return self.lines[len(self.lines)-1]
        else:
            return self
        
        
    def new_line(self,text=""):
        self.is_new_lined = True
        if text:
            result =  Formatter(self+text+"\n")
        else:
            result =  Formatter(self+"\n")
        self.lines.append(result)
        new_lines = Formatter('')
        new_lines.is_new_lined = True
        self.lines.append(new_lines)
        return result
    
    def append(self,text=""):
        return Formatter(self+text)
    
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
        