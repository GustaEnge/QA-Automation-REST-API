*** Settings ***

Library           API_Adapter/API_Core.py    localhost


*** Variables ***
${result_api}
${id}


*** Test Cases ***
Create Comment
    ${result_api}   API Create Comments    Ipsum Lorem 3    3    
    ${id}=    Set Variable    ${result_api}[id]
    Set Global Variable    ${id} 
Get Comment
    API Get Comments    ${id}

Update Comment
    ${result_api}    API Update Comments    ${id}   Ipsum Lorem 89    3  

Delete Comment
    API Delete Comments    ${id}