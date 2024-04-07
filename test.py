# def validateUser(user, isSusbcribe):
#     if(user):
#         if(user >= 18):
#             if(isSusbcribe):
#                 print("nice")
#             else:
#                 print("subscribe bro")
#         else:
#             print("bro u need to be 18+")
#     else:
#         print("user not found")

def validateUser(user, isSusbcribe):
    if(user == None):
        print("user not found")
    elif(user < 18):
        print("bro u need to be 18+")
    elif(not isSusbcribe):
        print("subscribe bro")
    else:
        print("nice")            

validateUser(19, True)
validateUser(19, False)
validateUser(16, False)
validateUser(None, False)