class Formatter:
    
    def italic(self,text:str):
        return f"*{text}*"
    
    def bold(self,text:str):
        return f"**{text}**"
    
    def underline(self,text:str):
        return f"__{text}__"
    
    def striket_hrough(self,text:str):
        return f"~~{text}~~"
    
    def hide(self,text:str):
        return f"||{text}||"
    
    def single_block(self,text:str):
        return f"> {text}"
    
    def single_code_block(self,text:str):
        return f"`{text}`"
    
    def multiple_code_block(self,text:str,code="python"):
        return f"""```{code}
{text}
```"""