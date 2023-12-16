import ContactBook1
import sys
def main():
    contact_list=[]
    while True:
        choice = int(input("What would you like to do?\n"
                           "(1)Add contact\n"
                           "(2)Delete contact\n"
                           "(3)View contacts\n"
                           "(4)Update contact\n"
                           "(5)Search contact\n"
                           "(6)Exit\n"
                           "Enter your choice: "))
    
        if choice==1:
            ContactBook1.new_contact(contact_list)
        if choice==2:
            ContactBook1.remove_contact(contact_list)
        if choice==3:
            ContactBook1.view_contacts(contact_list)
        if choice==4:
            ContactBook1.modify_contact(contact_list)
        if choice==5:
            ContactBook1.search_contact(contact_list)
        if choice==6:
            sys.exit(0)
        
main()
