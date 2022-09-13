from typing import List,TypeVar
from typing_extensions import Self
class T(str):
    is_new_lined:bool
    lines:List[Self]
    
def new_line_checker(cb):
    def wrapper(formatter,*args,**kwargs):
        if formatter.is_new_lined:
            print(f"{formatter.is_new_lined}")
            no_new_lined:List[Formatter] = formatter.lines[0:-2]
            new_lines:Formatter = formatter.lines[-1]
            instance=  cb(new_lines,*args,**kwargs)
            instance.is_new_lined = True
            no_new_lined.append(instance)
            result = Formatter(''.join(no_new_lined))
            result.is_new_lined = True
            result.lines = no_new_lined
            print(f"new Lined {result}+{instance}")
            return result
        else:            
            instance=  cb(formatter,*args,**kwargs)
        return instance
    return wrapper

class Formatter(str):
    lines:List[Self] = []
    is_new_lined = False
    
    def __call__(self,text:str):
        self = Formatter(text)
        return self
        
    @classmethod
    def cat_speak(cls,cb):
        def wrapper(*args,**kwargs):
            return Formatter(f"{cb(*args,**kwargs)}").bold().italic().new_line()
        return wrapper
    
    @classmethod
    def narrate(cls,cb):
        def wrapper(*args,**kwargs):
            return Formatter(f"{cb(*args,**kwargs)}").bold().single_block().new_line()
        return wrapper
        
    @new_line_checker
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
        
        result.is_new_lined = True
        result.lines = self.lines
        return result
    
    @new_line_checker
    def append(self,text=""):
        return Formatter(self+text)
    
    @new_line_checker
    def italic(self,text:str=""):
        if text:
            return Formatter(f"{self}*{text}*")
        else:
            return Formatter(f"*{self}*")
            
    @new_line_checker
    def bold(self,text:str=""):
        if text:
            return Formatter(f"{self}**{text}**")
        else:
            return Formatter(f"**{self}**")
    
    @new_line_checker
    def underline(self,text:str=""):
        if text:
            return Formatter(f"{self}__{text}__")
        else:
            return Formatter(f"__{self}__")
    
    @new_line_checker
    def strike_through(self,text:str=""):
        if text:
            return Formatter(f"{self}~~{text}~~")
        else:
            return Formatter(f"~~{self}~~")
    
    @new_line_checker
    def hide(self,text:str=""):
        if text:
            return Formatter(f"{self}||{text}||")
        else:
            return Formatter(f"||{self}||")
    
    @new_line_checker
    def single_block(self,text:str=""):
        if text:
            return Formatter(f"{self}> {text}")
        else:
            return Formatter(f"> {self}")
    
    @new_line_checker
    def single_code_block(self,text:str=""):
        if text:
            return Formatter(f"{self}`{text}`")
        else:
            return Formatter(f"`{self}`")
    
    def multiple_code_block(self,text:str,code="python"):
        return Formatter(f"""```{code}
{text}
```""")
        