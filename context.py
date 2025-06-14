
class UserContext:
    def __init__(self):
        self.page_data = {
            "query": "",
            "pageNo": 1
        }
        
    def updatepage_Query(self,query):
        self.page_data["query"] = query
        
    def updatepage_PageNo(self,num):
        self.page_data["pageNo"] = int(num)
