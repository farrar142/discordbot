from discord.ext.commands.context import Context
from server.cats.models import Cat

from server.users.models import Intimacy, User
from typing import TypedDict

class GiveChurrResult(TypedDict):
    cat:Cat
    result: bool
    hungry: int
    churr:int
    intimacy:int

class Interaction:
    def __init__(self,ctx:Context):
        self.ctx = ctx
        self.user = User.get_user_from_ctx(ctx)
        self.cat = Cat.get_default_cat()
        self.intimacy = Intimacy.get_intimacy(user_id=self.user.id,cat_id=self.cat.id)# type: ignore
        self.meow = SpeakMeow(user=self.user,cat=self.cat,intimacy=self.intimacy)
    
    def give_churr(self,amount=1):
        if self.cat.is_hungry and self.user.have_churr(amount=amount):
            self.cat.decrease_hungry(amount=amount)
            self.intimacy.increase_intimacy(amount=amount)
            self.user.decrease_churr(amount=amount)
            self.cat.refresh()
            self.intimacy.refresh()
            self.user.refresh()
            return GiveChurrResult(cat=self.cat,hungry=self.cat.hungry,intimacy=self.intimacy.intimacy,churr=self.user.call,result=True) # type: ignore
        else:
            return GiveChurrResult(cat=self.cat,hungry=self.cat.hungry,intimacy=self.intimacy.intimacy,churr=self.user.call,result=False) # type: ignore
        
class SpeakMeow:
    def __init__(self,user:User,cat:Cat,intimacy:Intimacy):
        self.user = user
        self.cat = cat
        self.intimacy = intimacy