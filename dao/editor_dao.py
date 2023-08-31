from model.editor import Editor
from database.connection_factory import ConnectionFactory

class EditorDAO:
    def __init__(self):
        self.__connection_factory = ConnectionFactory()
    
    def getAll(self) -> list[Editor]:
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM publishers")
        rows = cursor.fetchall()
        editors = list()
        for row in rows:
            editorRow = Editor(row[1], row[2], row[3], row[0])
            editors.append(editorRow)
        cursor.close()
        connect.close()
        return editors
    
    def create(self, editor: Editor) -> None:
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.execute("INSERT INTO publishers (name, address, phone) VALUES (%s, %s, %s)", (editor.name, editor.address, editor.phone))
        connect.commit()
        cursor.close()
        connect.close()
        

    def delete(self, editor_id: int) -> bool:
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.execute("DELETE FROM publishers WHERE id = %s", (editor_id,))
        rows_deleted = cursor.rowcount
        connect.commit()
        cursor.close()
        connect.close()
        if rows_deleted > 0:
            return True
        return False

    
    def getById(self, editor_id: id) -> Editor:
       connect = self.__connection_factory.get_connection()
       cursor = connect.cursor()
       cursor.execute("SELECT * FROM publishers WHERE id = %s", (editor_id,))
       row = cursor.fetchone()
       cursor.close()
       connect.close()
       find_editor = None
       if row:
           find_editor = Editor(row[1], row[2], row[3], row[0])
       return find_editor     
    
    def getByName(self, editor_name: str) -> Editor:
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM publishers WHERE name = %s", (editor_name,))
        row = cursor.fetchone()
        cursor.close()
        connect.close()
        find_editor = None
        if row:
           find_editor = Editor(row[1], row[2], row[3], row[0])
        return find_editor   