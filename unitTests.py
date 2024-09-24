#Laura Forero - Hw 3

#Unit tests

#Test cases for less_than method
# @Param number1 float
# @Param number2 float
# @Returns 1 if number1<number2, -1 if number1 > number2 and 0 otherwise
def less_than(number1, number2):
 pass

#Test 1: Numbers are not floats -> 0
def less_thansuite():
 if  less_than(1, 5) != 0:
    print('Test case 1 failed')

 #Test 2: number1 < number2  ->1
 if less_than(2.5, 3.5) != 1:
    print('Test case 2 failed')

 #Test 3: number1 > number2 -> -1
 if less_than(3.5, 2.5) != -1:
    print('Test case 3 failed')

#Test 4: number1 == number2 -> 0
 if less_than(3.5, 3.5) != 0:
    print('Test case 4 failed')

#Test cases for addLists method
# @Param list1
# @Param list2
# @Returns sum of lists if same size otherwise empty list
def addLists(lis1, list2):
    pass

#Test 1: Lists of the same size
def  addListsSuite():
 result = addLists([1, 2, 3],[4, 5, 6])
 if result != [5, 7, 9]:
    print('Test case 1 failed')

# Test 2: Lists are not the same size
 result = addLists([1, 2, 3, 5], [4, 5, 6])
 if result != []:
    print('Test case 2 failed, listst are not the same size')

# Test 3: sum is not correct
 result = addLists([1, 2, 3], [4, 5, 6])
 if result == [1, 8, 2]:
    print('Test case 3 failed, incorrect sum')

#Security class
class Security:
#Init method
   def __init__(self, login, password):
     self.login = login
     self.password = password
#getLogin method, returns login
   def getLogin(self):
    return self.login
#getPassword method, returns password
   def getPassword(self):
    return self.password

# checkCredentials method
# @Param login
# @Param password
# @Returns true if login and password provided match the login and password of the security object and false otherwise
   def checkCredentials(self, login, password):
     return True

# updatePassword method
# @Param login
# @Param old password
# @Param new password
# @Returns true if login and old password match and the new password has at least one lower-case letter, one upper-case letter, and one number
# and does not match any of the last 3 passwords used for that login otherwise returns false
   def updatePassword(self, login, oldPassword, newPassword):
     return True

#Test cases for init method
def initSuite():
    sec = Security('Bob', 'Fail')
#Test case 1: Ensure security object stores login correctly
    if sec.getLogin() != 'Bob':
        print('Test case 1 failed, incorrect login')
# Test case 2: Ensure security object stores  password correctly
    if sec.getPassword() != 'Fail':
        print('Test case 2 failed, incorrect password')

#Test cases for checkCredentials method
# Test case 1: Login and password match -> True
def checkCredentialsSuite():
    sec = Security('Bob','Fail')

    if not sec.checkCredentials('Bob', 'Fail'):
      print('Test case 1 failed')

# Test case 2:Login and password don't match -> False
    if sec.checkCredentials('Bob', 'Apple'):
     print('Test case 2 failed, login and password dont match')

#Test cases for updatePassword method
def updatePasswordSuite():
     sec = Security('Bob','Fail')
# Test case 1: Password updates correctly
     if not sec.updatePassword('Bob','Fail','Newpassword1'):
         print('Test case 1 failed')

#Test case 2: login and old password don't match
     sec = Security('Bob', 'Fail')
     if  sec.updatePassword('Bob','apple','Newpassword1'):
         print('Test case 2 failed, login and old password dont match')

#Test case 3: New password does not have a digit
     sec = Security('Bob','Fail')
     if  sec.updatePassword('Bob','Fail','Newpassword'):
         print('Test case 3 failed, new password is missing a number')

#Test case 4: New password does not have an uppercase letter
     sec = Security('Bob','Fail')
     if  sec.updatePassword('Bob','Fail','newpassword1'):
         print('Test case 4 failed, new password is missing an uppercase letter')

#Test case 5: New password does not have a lowercase letter
     sec = Security('Bob','Fail')
     if  sec.updatePassword('Bob','Fail','NEWPASSWORD1'):
         print('Test case 5 failed, new password is missing a lowercase letter')

#Test case 6: New password matches one of the last 3 passwords
     sec.updatePassword('Bob', 'Fail', 'Newpassword1')  #first Update
     sec.updatePassword('Bob', 'Newpassword1', 'Newpassword2')  #second Update
     sec.updatePassword('Bob', 'Newpassword2', 'Newpassword3') #Third update
     if sec.updatePassword('Bob', 'Newpassword3', 'Newpassword1'):  # reuse password
        print('Test case 6 failed, password matches one of the last 3 passwords')

def main():
    print('')
    print("Running less_than test suite")
    less_thansuite()

    print('')
    print("Running addLists test suite")
    addListsSuite()

    print('')
    print("Running init test suite")
    initSuite()

    print('')
    print("Running checkCredentials test suite")
    checkCredentialsSuite()

    print('')
    print("Running updatePassword test suite")
    updatePasswordSuite()

main()













