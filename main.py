# Description : Script to handle complete flow of Consumer-Onboarding Request
# Steps can be listed as below-
# 1. First the location of folder containing the operational profiles to be loaded onto the server is requested.
# 2. Next the asn1 files are accessed to fetch the values of the iccid and the profileType defined.
# 3. ICCID values are extracted from the asn1 file and saved as a list.
# 4. Further the folder location is accessed for the der files and filenames within directory are compared against the iccid stored in list from asn1.
# 5. If the iccid name and der file nomenclature tally, then iccid and base64 format of the der file are mapped as key-value pair and stored in the dictionary.
# 6. The key-value pair can then be used to populate the api requests which will be triggered towards the DP+.
#  
# We start by asking the name for client creation and then create an account
# Next we try to get the bearer token for the client created in step 2
# This is followed by step wherein the uploadprofile is used

import os
import base64 
import os  
import yaml
import json
from functions import *
from create_client import  client_creation
# from cancel_order
# from confirm_order
# from delete_order
# from download_order
# from get_profile
from get_token import client_token
## Json folder modules
from datetime import datetime


class QrScript:
    iccid_list = []
    profile_type_list= []
    dict1 = {}
    dict2 = {}
    # user_input = []

    # def __init__(self):
    #     # self.iccid 
    #     # self.secret
    #     # self.profile_type

        

    # Welcome to the Consumer Onboarding scripts - 
    # These scripts will have an order starting with creation of clients 
    # This is followed by the fetching of token for the new client created in above step
    # In the next step if a user wants he can upload the operational profiles onto the server
    # Followed by the process of download order where in the profile is released for download to EID
    # Next the script will involve the confirm order where matching id is released for QR code generation.
    # Later the QR code will be generated and provided to customer for downloading profile on the device.
    def main(self, choice):
        user_input = input(""" Please carefully go through the options and choose the options separated by a comma(,).
                                ##########################################################################################
                                    1. Create/Validate a client
                                    2. Fetch bearer token
                                    3. Upload operational profiles onto the server 
                                    4. Create download order for the operational profiles
                                    5. Confirm order for the operational profiles
                                    6. Create a QR code for the operational profile's download on device.
                                    7. Exit\n\n 
                                    """).split(",")
        print(user_input)                        
        # for option in user_input: 
        if user_input == "1":
            clientId, secret = client_creation()
        elif user_input == "2":
            return bearer_token()   
        elif user_input == "3":
            return upload_profiles()
        elif user_input == "4":
            return download_order()
        elif user_input == "5":
            return confirm_order()   
        elif user_input == "6":
            return qr_code()  
        elif user_input == "exit":
            return exit()
        else:
            pass
        print("")



qr = QrScript()
flag = "true"
while flag == "true":
    choice = input("User wants to proceed with onboarding or exit choose option (press 1 to proceed, press 2 to exit):")
    if choice != "2" :
        qr.main(choice)
    else:
        flag = "false"  







 



