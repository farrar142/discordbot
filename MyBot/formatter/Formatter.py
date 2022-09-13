from typing import List,TypeVar
from typing_extensions import Self
class T(str):
    is_new_lined:bool
    lines:List[Self]
    
def new_line_checker(cb):
    def wrapper(formatter,*args,**kwargs):
        if formatter.is_new_lined:
            prev:List[Formatter] = formatter.lines[0:-1]
            new_lines:Formatter = formatter.lines[-1]
            instance=  cb(new_lines,*args,**kwargs)
            instance.is_new_lined = True
            prev.append(instance)
            result = Formatter(''.join(prev))
            result.is_new_lined = True
            result.lines = prev
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
        
    def new_line(self):
        self.is_new_lined = True
        result = Formatter(''.join(self)+"\n")
        new = Formatter("")
        result.lines = [result,new]
        result.is_new_lined=True
        return result
    
    @new_line_checker
    def append(self,text=""):
        print(f"{self=},{text=}")
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

def debug(string:Formatter):
    print(f"{string.lines=},{string}")

string = Formatter("뉴라인").new_line().append("볼드").bold().new_line()
debug(string)