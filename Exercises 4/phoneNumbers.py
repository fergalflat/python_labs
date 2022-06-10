# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 15:15:55 2021

@author: fflattery
"""
contacts = ["087 1234567", "090 9876543", "090 6468000", "112"]
option = input("[P]rint list [C]heck number [A]dd number [E]dit number [D]elete number [Q]uit: ").lower()

while option != "q":
    if option == "p":
        print("Numbers in your contacts list")
        count= 0
        for n in contacts:
            print(count , ":", n)
            count += 1        
            
        option = input("\n[P]rint list [C]heck number [A]dd number [E]dit number [D]elete number [Q]uit: ").lower()
    
    if option == "c":
        phnumber = input("Enter the number: ")
        if phnumber in contacts:
            print("Number", phnumber, "is in the list")
        else:
            print("Number", phnumber, "is not in the list")
            
        option = input("\n[P]rint list [C]heck number [A]dd number [E]dit number [D]elete number [Q]uit: ").lower()

  #  elif option == "c":
   #     phnumber2 = input("Enter the number: ")
    #    if phnumber2 not in contacts:
     #       print("Number", phnumber2, "is not in the list")
      #      
       #     option = input("\n[P]rint list [C]heck number [A]dd number [E]dit number [D]elete number [Q]uit: ").lower()                     
                   
    if option == "a":
        newnumber = input("Enter new number: ")
        contacts.append(newnumber)
        print("Added", newnumber, "to the list")     
        option = input("\n[P]rint list [C]heck number [A]dd number [E]dit number [D]elete number [Q]uit: ").lower()
        
    if option == "e":
        editnumber = input("Enter number to edit: ")
        newnumber2 = input("Enter the new number: ")
        if editnumber in contacts:
            index = contacts.index(editnumber)
            contacts[index] = newnumber2
            print("Replaced",editnumber,"with",newnumber2)
            
            option = input("\n[P]rint list [C]heck number [A]dd number [E]dit number [D]elete number [Q]uit: ").lower()
    
    if option == "d":
        deletenumber = input("Enter number to delete: ")
        if deletenumber in contacts:
            contacts.remove(deletenumber)
            print("Removed",deletenumber,"from the list")
            
            option = input("\n[P]rint list [C]heck number [A]dd number [E]dit number [D]elete number [Q]uit: ").lower()
            
        
        