import http.client
import ssl
import os
import subprocess
from API_Adapter.Lib_profiles import profiles
from API_Adapter.Lib_posts import posts
from API_Adapter.Lib_comments import comments


#home = expanduser('~')
dir_path = os.path.dirname(os.path.realpath(__file__))

class API_Core(comments,posts,profiles):
    ROBOT_LIBRARY_SCOPE = 'SUITE'
    def __init__(self,url="localhost") -> None:
        ssl._create_default_https_context = ssl._create_unverified_context
        self.conn = http.client.HTTPConnection(url,3000)
        self.dir = os.path.dirname(dir_path)+"\\json_server\\"
        self.process = subprocess.Popen('json-server --watch db.json',shell=True,cwd=self.dir)
        
        super(API_Core, self).__init__()

    def __exit__(self):
        self.process.kill()

    def API_Get_Comments(self,id,postId=None,body=None):
        return self.get_comments(id,postId,body)

    def API_Create_Comments(self,body,postId):
        return  self.create_comments(body,postId)
    def API_Update_Comments(self,id,body,postId):
        return  self.update_comments(id,body,postId)    
    def API_Delete_Comments(self,id):
        return  self.delete_comments(id) 

    def API_Get_Posts(self,id,author=None,title=None):
        return  self.get_posts(id,author,title)
    def API_Create_Posts(self,title,author):
        return  self.create_posts(title,author)
    def API_Update_Posts(self,id,title,author):
        return  self.update_posts(id,title,author)
    def API_Delete_Posts(self,id):
        return  self.delete_posts(id)             

    def API_Get_Profiles(self,id,author=None,title=None):
        return  self.get_posts(id,author,title)
    def API_Create_Profiles(self,title,author):
        return  self.create_posts(title,author)
    def API_Update_Profiles(self,id,title,author):
        return  self.update_posts(id,title,author)  
 