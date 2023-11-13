*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  mikko  mikko1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  salasana1234
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  as  abc12345678
    Output Should Contain  Username is too short

Register With Enough Long But Invald Username And Valid Password
    Input Credentials  matti96  mikkejordan23
    Output Should Contain  Username is not valid

Register With Valid Username And Too Short Password
    Input Credentials  jaakkopetteri  y2k
    Output Should Contain  Password is too short 

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  viljamivalas  tämäonhyväsalasana
    Output Should Contain  Password is not valid

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle1234
    Input New Command