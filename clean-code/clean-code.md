# Clean Code
cringing on how bad was my past self code, so here's some notes on how to be a better coder.

## principles:
Clean code is code that is easy to read, understand, and maintain. It follows a set of principles that are designed to make the code more readable, testable, and less error-prone.

- <b>Clarity:</b>The code should be easy to read and understand.
- <b>Simplicity:</b> The code should be as simple as possible, avoiding unnecessary complexity.
- <b>Comments:</b> Comments should be used sparingly and only when necessary to explain complex or non-obvious code.
- <b>Naming:</b> Variables, functions, and classes should have meaningful and descriptive names.
- <b>Formatting:</b> The code should be consistently formatted to improve readability.
- <b>Functionality:</b> The code should be organized into small, single-purpose functions and classes.
- <b>Error handling:</b> The code should handle errors in a consistent and predictable way.
- <b>Testing:</b> The code should be testable and have a high test coverage.
- <b>Reusability:</b> The code should be designed to be reusable and modular.
- <b>Performance:</b> The code should be designed to be efficient and performant.

## application and examples:

## - avoid unecessary nesting, throw and return early
sometimes, you can find a way other than nesting.
<br>
- bad:
```python
def validateUser(user, isSusbcribe):
    if(user):
        if(user >= 18):
            if(isSusbcribe):
                print("nice")
            else:
                print("subscribe bro")
        else:
            print("bro u need to be 18+")
    else:
        print("user not found")
```
- better:
```python
def validateUser(user, isSusbcribe):
    if(user == None):
        print("user not found")
    elif(user < 18):
        print("bro u need to be 18+")
    elif(not isSusbcribe):
        print("subscribe bro")
    else:
        print("nice")  
```
#

## - be clear
clear code avoid ambiguity, better readibility
``` typescript
// bad:
checkPassword(): boolean
// better:
isPasswordValid(): boolean 
```
isPasswordValid is better name because its indicate the return type boolean and will return true if valid.
``` typescript
// bad:
const MIN_PASSWORD = 8
// better:
const MIN_PASSWORD_LENGTH = 8
```
also be better at commenting: comment if necessary and explain complex code only

## - consistency 
check if this consistent: indent, spacing, quotes, caps, ;
- bad:
``` typescript
const MIN_PASSWORD_LENGTH = 8;
const minName_length = 8
let AGE_MINIMUM = 18;

function logAllConst(){
    console.log(MIN_PASSWORD)
        console.log(min_name_length)
    console.log(AGE_MINIMUM);
}
```
- better: 
``` typescript
const MIN_PASSWORD_LENGTH = 8
const MIN_NAME_LENGTH = 8
const MIN_AGE = 18

function logAllConst(){
    console.log(MIN_PASSWORD_LENGTH)
    console.log(MIN_NAME_LENGTH)
    console.log(MIN_AGE)
}
```
## - don't hardcode, use const
why hardcode variables when you can use const(?)
- bad:
``` typescript
if(transactionType = "1" && userAge > 18)
    console.log("you can proceed")
```
- better: 
``` typescript
const MIN_USER_AGE = 8
const TRANSACTION_TYPE_ADULT = 1

if(transactionType = TRANSACTION_TYPE_ADULT && userAge > MIN_USER_AGE)
    console.log("you can proceed")
}
```
## - avoid updating global variables inside a small specific function
avoid updating variables inside a function specified to calculate or process things that used multiple times, return the value instead.
- bad:
``` typescript
let area = 0
let volume = 0

function getAreaAndVolume(radius){
    area = Math.PI * radius * radius
    volume = area * radius * 4/3
}
```
- better: 
``` typescript
let area = 0
let volume = 0

function getAreaByRadius(radius){
    return Math.PI * radius * radius
}

function getVolumeByRadius(radius){
    return Math.PI * radius * radius * radius * 4/3

area = getArreaByRadius(5)
```
## - single responsibility principle, and keep it short
every method should have a single sole purpose.
- bad:
``` typescript
let area = 0

function updateAreaByRadius(radius){
    area = Math.PI * radius * radius
}
```
- better: 
``` typescript
let area = 0

function getArreaByRadius(radius){
    return Math.PI * radius * radius
}

area = getArreaByRadius(5)
```

## - reusability
its better if its reusable. it avoid clone codes too. (still single responsibility)
- bad:
``` typescript
function logUserLogIn(){
    console.log("user logged in on:" + new Date())
}
function logUserLogOut(){
    console.log("user logged out on:" + new Date())
}
```
- better: 
``` typescript
function logAction(action){
    console.log("user " + action +  " on:" + new Date())
}

logAction("logged in")
logAction("logged out")

##
references:
- https://roadmap.sh/software-design-architecture/clean-code-principles
- https://www.youtube.com/watch?v=wSDyiEjhp8k
- https://www.youtube.com/watch?v=MKaLJyPOS4U
