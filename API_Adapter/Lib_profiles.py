import json

class profiles():
    def __init__(self) -> None:
        pass
    def get_profile(self,name):
        '''
        Returns a comment from the API according to the user's selected filter
            Parameters:
                    name (string) : comment id
            Returns:
                   One or more comments depending on the filters (format: JSON) if it worked (200 code) otherwise will return the error code
        '''
        headers = { 'accept': "application/json" }
        if name:
            self.conn.request("GET", "/profile/", headers=headers)
        res = self.conn.getresponse()
        if res.code == 200:
            data = res.read()
            json_dict = data.decode("utf-8")
            return json.loads(json_dict)
        else: return res.code

    def create_profile(self,name, method="POST"):
        '''
        Create or Update a profile from the API
            Parameters:
                    name (string): profile name
            Returns:
                   The just created/updated profile (format: JSON) if it worked (200 code) otherwise will return the error code
        '''        
        headers = {
            'accept': "application/json",
            'content-type': "application/json"
            }
        payload = json.dumps({
            "name": f"{name}"
        })   
        if method in ["POST","PATCH","PUT"]:self.conn.request(method, "/profile/", payload.encode('utf-8'), headers)
        else: return "Invalid method"
        
        res = self.conn.getresponse()
        if res.code == 200:
            data = res.read()
            json_dict = data.decode("utf-8")
            return json.loads(json_dict)
        else: return res.code   