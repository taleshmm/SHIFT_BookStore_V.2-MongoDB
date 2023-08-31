from model.category import Category
from database.connection_factory import ConnectionFactory

class CategoryDAO:
    def __init__(self): 
        self.__connection_factory = ConnectionFactory() 

    def getAll(self) -> list[Category]:
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.execute(f"SELECT * FROM categories")
        rows = cursor.fetchall()
        categories = list()
        for row in rows:
            categoryRow = Category(row[1], row[0])
            categories.append(categoryRow)
        cursor.close()
        connect.close()
        return categories
    
    def create(self, category: Category) -> None:
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.execute(f"INSERT INTO categories (name) VALUES ('{category.name}')")
        connect.commit()
        cursor.close()
        connect.close()

    def delete(self, category_id: int) -> bool:
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.execute(f"DELETE FROM categories WHERE id = '{category_id}'")
        rows_deleted = cursor.rowcount
        connect.commit()
        cursor.close()
        connect.close()
        if rows_deleted > 0:
            return True
        
        return False
    
    def getById(self, category_id: int) -> Category:
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM categories WHERE id = %s", (category_id))
        row = cursor.fetchone()
        find_category = None
        if row:
            find_category = Category(row[1], row[0])
        cursor.close()
        connect.close()
        return find_category

    def getByName(self, category_name: str) -> Category:
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM categories WHERE name = %s", (category_name))
        row = cursor.fetchaone()
        find_category = None
        if row:
            find_category = Category(row[0][1], row[0][0])
        cursor.close()
        connect.close()
        return find_category