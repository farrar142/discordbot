from typing import List, Union
from typing_extensions import Self
from peewee import ForeignKeyField,CharField,TextField,BaseQuery

from server.base.models import BaseModel
from server.users.models import User

class Message(BaseModel):
    user = ForeignKeyField(User)
    title = CharField()
    context = TextField()

    @classmethod
    def memo(cls,user_id:int,title:str,context:str):
        instance = cls.create(user=user_id,title=title,context=context)
        instance.save()

    @classmethod
    def memo_converter(cls,memos:List[Self]):
        results:List[str]=[]

        for idx,memo in enumerate(memos):
          text= f"{memo.id}:{memo.title}\n{memo.context}"
          results.append(text)
          if idx<len(memos):
              results.append("")
        
        if len(results)>=1:
            return "\n".join(results)
        else:
            return "메모가 없어요"

    @classmethod
    def my_memos_filter(cls,user_id:int,title:str):
        memos:List[cls] = cls.select().join(User).where(cls.title.contains(title),cls.user.id==user_id)
        return cls.memo_converter(memos)
      
    @classmethod
    def my_memos(cls,user_id:int):
        memos:List[cls] =  cls.select().join(User).where(cls.user.id==user_id)
        return cls.memo_converter(memos)

    @classmethod
    def delete_memo(cls,memo_id:int):
        memo:Union[cls,None] = cls.get_or_none(id=memo_id)
        if memo:
            memo.delete_instance()
            return True
        else:
            return False