import requests
import sys               # import sys package
old_path = sys.path[:]   # make a copy of the old paths
sys.path.pop(0)          # remove the first one (usually the local)
import bs4               # import the package
sys.path = old_path 

class Enchant:
  
    @classmethod
    def get(cls,url:str):
        request = requests.get(url)
        if request.status_code <=300:
            return request.text
        return "<div></div>"

    @classmethod
    def soup(cls,url:str):
        return bs4.BeautifulSoup(cls.get(url),'html.parser')

    @classmethod
    def search(cls,name:str):
        enchants = cls.soup(f"https://biketago.com/enchant/?na={name}").select('html > body > main > section > article > table > tr')
        enchants.pop(0)
        result:list[str] = []
        
        if enchants[0].select('td')[0].attrs.get('class')==None:
            for idx,enchant in enumerate(enchants):
                enchant_name = enchant.select('td')[2].text
                enchant_rank = enchant.select('td')[1].text
                enchant_descs = enchant.select('div')
                result.append(enchant_name)
                result.append(enchant_rank)
                for desc in enchant_descs:
                    result.append(desc.text)
                if idx < len(enchants):
                    result.append("")
        else:
            result.append(f"{name}의 결과가 없어요.")
                
        return '\n'.join(result)