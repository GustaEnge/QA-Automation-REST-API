import json

class posts():
    def __init__(self) -> None:
        pass

    def get_posts(self,id=None,author=None,title=None):
        headers = { 'accept': "application/json" }
        if id:
            self.conn.request("GET", "/posts/%s/" % (id), headers=headers)
        if author:
            self.conn.request("GET", "/posts/?author_like=%s" % (author), headers=headers)
        if title:
            self.conn.request("GET", "/posts/?title_like=%s" % (title), headers=headers)    

        res = self.conn.getresponse()
        if res.code == 200:
            data = res.read()
            json_dict = data.decode("utf-8")
            return json.loads(json_dict)
        else: raise Exception(res.code)   
    
    def create_posts(self,title,author):  
        '''
        Create a post from the API
            Parameters:
                    title (string): the title of the post
                    author (string): the post's author
            Returns:
                   The just created post (format: JSON) if it worked (200 code) otherwise will return the error code
        '''        
        headers = {
            'accept': "application/json",
            'content-type': "application/json"
            }
        payload = json.dumps({
            "body": f"{title}",
            "postId": f"{'' if not author else author}"
        })   
        
        self.conn.request("POST", "/posts/",payload.encode('utf-8'), headers)
        res = self.conn.getresponse()
        if res.code == 201:
            data = res.read()
            json_dict = data.decode("utf-8")
            return json.loads(json_dict)
        else: raise Exception(res.code)   

    def update_posts(self,id,title=None,author=None):
        '''
        Update a post from the API by using PATCH or PUT depending on the parameters.
            Summary:
                    If it's using all the params so it will be used PUT otherwise PATCH
            Parameters:
                    id (string) : post id
                    title (string): the title of the post
                    author (string): the post's author
            Returns:
                   The just updated comment (format: JSON) if it worked (200 code) otherwise will return the error code
        '''        
        headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }
        payload = json.dumps({"title": f"{title}","author": f"{author}"}) if title and author else json.dumps({"title": f"{title}"}) if title else json.dumps({"author": f"{author}"})
        if title and author: self.conn.request("PUT", "/posts/%s" % (id),payload ,headers)
        else:  self.conn.request("PATCH", "/posts/%s" % (id), payload.encode('utf-8'), headers)
        
        
        res = self.conn.getresponse()     
        if res.code == 200:
            data = res.read()
            json_dict = data.decode("utf-8")
            return json.loads(json_dict)
        else: raise Exception(res.code)

    def delete_posts(self,id):
        '''
        Delete a post from the API
            Summary:
                    If it's using all the params so it will be used PUT otherwise PATCH
            Parameters:
                    id (string) : post id
            Returns:
                   200 code otherwise will return the error code
        '''            
        if id:
            self.conn.request("DELETE", "/posts/%s" % id)
        res = self.conn.getresponse()
        if res.code == 200:
            return json.loads(res.code)
        else: raise Exception(res.code)               