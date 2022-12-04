*** Settings ***

Library           API_Adapter/API_Core.py    localhost


*** Variables ***
${result_api}    ${None}


*** Test Cases ***
Create Profile
    ${result_api}    API Create Profiles    Alexandro    
    
Get Profile
    API Get Profiles    ${result_api}["id"]
    
Delete Profile
    API Delete Profiles    ${result_api}["id"]