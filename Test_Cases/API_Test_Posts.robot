*** Settings ***

Library           API_Adapter/API_Core.py    localhost

**Variables
${result_api}
${id}

*** Test Cases ***
Create Post
    ${result_api}    API Create Posts    Brazil 2025    Gustavo
    ${id}=    Set Variable    ${result_api}[id]
    Set Global Variable    ${id} 
    
Get Post
    API Get Posts    ${id}

Update Post
    ${result_api}    API Update Posts    ${id}    Brazil 2025    Caio    
    
Delete Post
    API Delete Posts   ${id}