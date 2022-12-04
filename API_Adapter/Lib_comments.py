import json

class comments():

    def __init__(self) -> None:
        pass

    def get_comments(self,id=None,postId=None,body=None):
        '''
        Returns a comment from the API according to the user's selected filter
            Parameters:
                    id (string) : comment id
                    postId (string): post id where the comment was done
                    body (string): search through the string you pass and if it matches the body of the comment
            Returns:
                   One or more comments depending on the filters (format: JSON) if it worked (200 code) otherwise will return the error code
        '''
        headers = { 'accept': "application/json" }
        if id:
            self.conn.request("GET", "/comments/%s" % (id), headers=headers)
        if postId:
            self.conn.request("GET", "/comments/?postId=%s" % (postId), headers=headers)
        if body:
            self.conn.request("GET", "/comments/?body_like=%s" % (body), headers=headers)    

        res = self.conn.getresponse()
        if res.code == 200:
            data = res.read()
            json_dict = data.decode("utf-8")
            return json.loads(json_dict)
        else: 
            raise Exception(res.code)
    

    def create_comments(self,body,postId=None):
        '''
        Create a comment from the API
            Parameters:
                    postId (string): post id where you want to leave the comment
                    body (string): the body of the comment
            Returns:
                   The just created comment (format: JSON) if it worked (200 code) otherwise will return the error code
        '''        
        headers = {
            'accept': "application/json",
            'content-type': "application/json"
            }
        payload = json.dumps({
            "body": f"{body}",
            "postId": f"{'' if not postId else postId}"
        })   
        
        self.conn.request("POST", "/comments", payload.encode('utf-8'), headers)
        res = self.conn.getresponse()
        if res.code == 201:
            data = res.read()
            json_dict = data.decode("utf-8")
            return json.loads(json_dict)
        else: raise Exception(res.code)

    def update_comments(self,id,body=None,postId=None):
        '''
        Update a comment from the API by using PATCH or PUT depending on the parameters.
            Summary:
                    If it's using all the params so it will be used PUT otherwise PATCH
            Parameters:
                    id (string) : comment id
                    postId (string): post id where the comment was done
                    body (string): the body of the comment
            Returns:
                   The just updated comment (format: JSON) if it worked (200 code) otherwise will return the error code
        '''        
        headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }
        payload = json.dumps({"body": f"{body}","postId": f"{postId}"}) if body and postId else json.dumps({"body": f"{body}"}) if body else json.dumps({"postId": f"{postId}"})
        if body and postId: self.conn.request("PUT", "/comments/%s" % (id), payload.encode('utf-8'), headers)
        else:  self.conn.request("PATCH", "/comments/%s" % (id), payload.encode('utf-8'), headers)
        
        
        res = self.conn.getresponse()     
        if res.code == 200:
            data = res.read()
            json_dict = data.decode("utf-8")
            return json.loads(json_dict)
        else: raise Exception(res.code)

    def delete_comments(self,id):
        '''
        Delete a comment from the API
            Summary:
                    If it's using all the params so it will be used PUT otherwise PATCH
            Parameters:
                    id (string) : comment id
            Returns:
                   200 code otherwise will return the error code
        '''            
        if id:
            self.conn.request("DELETE", "/comments/%s" % (id), headers={})
        res = self.conn.getresponse()
        if res.code == 200:
            return res.code
        else: raise Exception(res.code)
        