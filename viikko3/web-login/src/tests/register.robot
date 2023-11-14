*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  alice
    Set Password  alice678
    Confrim Password  alice678
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  al
    Set Password  alice678
    Confrim Password  alice678
    Submit Register Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Invalid Password
    Set Username  alice
    Set Password  pelkkäätekstiä
    Confrim Password  pelkkäätekstiä
    Submit Register Credentials
    Register Should Fail With Message  Password is not valid

Register With Nonmatching Password And Password Confirmation
    Set Username  alice
    Set Password  balice678
    Confrim Password  alice678
    Submit Register Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  bob
    Set Password  bob123678
    Confrim Password  bob123678
    Submit Register Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  bob
    Set Password  bob123678
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  al
    Set Password  alice678
    Confrim Password  alice678
    Submit Register Credentials
    Register Should Fail With Message  Username is too short
    Go To Login Page
    Set Username  al
    Set Password  alice678
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open


Submit Register Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confrim Password
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}