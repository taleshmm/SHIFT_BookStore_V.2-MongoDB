from model.category import Category

class CategoryDAO:
    def __init__(self):
        self.__categorys: list[Category] = list()

    def getAll(self) -> list[Category]:
        return self.__categorys
    
    def create(self, category: Category) -> None:
        self.__categorys.append(category)

    def delete(self, category_id: int) -> bool:
        find = False
        for i in self.__categorys:
            if category_id == i.id:
              index = self.__categorys.index(i)
              del self.__categorys[index]
              find = True
              break
        return find
    
    def getById(self, category_id: int) -> Category:
        find_category = None
        for i in self.__categorys:
          if i.id == category_id:
            find_category = i
            break
        return find_category
    
    def getLastId(self) -> int:
       if len(self.__categorys) != 0:
          return self.__categorys[-1].id
       else:
          return 0

    def getByName(self, category_name: str) -> Category:
       find_category = None
       for i in self.__categorys:
        if i.name == category_name:
           find_category = i
           break
       return find_category