from API_Adapter.API_Core import API_Core
from API_Adapter.Lib_database import dataBase
import pytest

class TestCases():
    def __init__(self,api) -> None:
        self.api_adapter = api
    def Post_Tests(self):
        #Unit Tests for POST verb
        post_result = self.api_adapter.API_Create_Posts('Brazil 2025','Gustavo')

        assert(type(post_result) == dict or type(post_result) == int, 'Test Failed for 201 and 404 code')
        assert(post_result is {'id':dataBase().getLastId('posts'),'title':'Brazil 2025','author':'Gustav0'}, 'Wrong data')

        #Unit Tests for GET verb
        get_result = self.api_adapter.API_Get_Posts(id=post_result['id'])

        assert(type(get_result) == dict or type(get_result) == int, 'Test Failed for 201 and 404 code')


        #Unit Tests for PUT/PATCH verb
        update_result = self.api_adapter.API_Update_Posts('Brazil 2028','Gustavo')

        assert(type(update_result) == dict or type(update_result) == int, 'Test Failed for 201 and 404 code')
        assert(update_result is {'id':dataBase().getLastId('posts'),'title':'Brazil 2028','author':'Gustavo'}, 'Wrong data')

if __name__=="__main__":
    test_obj = TestCases(API_Core())
    test_obj.Post_Tests()
    '''
    result = test_obj.api_adapter.API_Create_Posts('Brazil 2024','Gustavo')
    print(test_obj.api_adapter.API_Get_Posts(id=result['id']))
    test_obj.api_adapter.API_Update_Posts(result['id'],'Brazil 2028','Gustavo')
    print(test_obj.api_adapter.API_Get_Posts(id=result['id']))

    '''