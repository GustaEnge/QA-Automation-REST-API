import json


class dataBase():
    def __init__(self) -> None:
        self.db = None

    def getDataBase(self):
        headers = { 'accept': "application/json" }
        self.conn.request("GET", "db", headers=headers)
       
        res = self.conn.getresponse()
        data = res.read()
        json_dict = data.decode("utf-8")
        result = json.loads(json_dict)

        self.db = result

    def getLastId(self,table):    
        db = self.db
        table = db[table]
        return len(table)