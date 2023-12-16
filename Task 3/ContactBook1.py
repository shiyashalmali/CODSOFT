def new_contact(contact_list):
    all_addresses=[]
    all_phone=[]
    all_email=[]
    contact={}
    contact["Name"]=input("Enter name:")
    # contact["Age"]=int(input("enter age:"))

    address=input("Enter address: ")
    all_addresses.append(address)
    contact["Address(es)"]=all_addresses

    phone=input("Enter phone number: ")
    all_phone.append(phone)
    contact["Phone number(s)"]=all_phone

    email=input("Enter email: ")
    all_email.append(email)
    contact["Email(s)"]=all_email
    contact_list.append(contact)

def remove_contact(contact_list):
    view_contacts(contact_list)
    remove=int(input("Which contact would you like to delete? "))
    if 0<remove<len(contact_list):
        del contact_list[remove-1]
        print("Contact deleted.")
    else:
        print("Error.")

def modify_contact(contact_list):
    view_contacts(contact_list)
    mod=int(input("Which contact would you like to update? Enter -1 to cancel. "))
    if mod==-1:
        pass
    if 0<=mod<=len(contact_list):
        mod_attribute=int(input("What would you like to modify? (1)Name (2)Address (3)Phone number (4)Email "))
    if mod_attribute==1:
        contact_list[mod-1]['Name']=input("Enter contact name: ")
    if mod_attribute==2:
        addresses=contact_list[mod-1]['Address(es)']
        for i in range(len(addresses)):
            print(i+1, addresses[i])
            choice=int(input("Would you like to (1)add a address, (2)delete an address, or (3)modify an address? "))

            if choice==1:
                new_address=input("Enter the new address: ")
                addresses.append(new_address)
                contact_list[mod-1]['Address(es)']=addresses
            if choice==2:
                address_num=int(input("Which address would you like to remove? "))
                del contact_list[mod-1]['Address(es)'][address_num-1]

            if choice==3:
                address_num=int(input("Which address would you like to modify? "))
                new_address=input("Enter new address: ")
                contact_list[mod-1]['Address(es)'][address_num-1]=new_address

    if mod_attribute==3:
        phone_nums=contact_list[mod-1]['Phone number(s)']
        for i in range(len(phone_nums)):
            print(i+1, phone_nums[i])
            choice=int(input("Would you like to (1)add a phone number, (2)delete a phone number, or (3)modify a phone number? "))

            if choice==1:
                new_phone=input("Enter the new phone number: ")
                phone_nums.append(new_phone)
                contact_list[mod-1]['Phone number(s)']=phone_nums
            if choice==2:
                phone_index=int(input("Which phone number would you like to remove? "))
                del contact_list[mod-1]['Phone number(s)'][phone_index-1]

            if choice==3:
                phone_index=int(input("Which phone number would you like to modify? "))
                new_phone=input("Enter new phone number: ")
                contact_list[mod-1]['Phone number(s)'][phone_index-1]=new_phone

    if mod_attribute==4:
        emails=contact_list[mod-1]['Email(s)']
        for i in range(len(emails)):
            print(i+1, emails[i])
            choice=int(input("Would you like to (1)add an email, (2)delete an email, or (3)modify an email? "))

            if choice==1:
                new_email=input("Enter the new email: ")
                emails.append(new_email)
                contact_list[mod-1]['Email(s)']=emails
            if choice==2:
                email_num=int(input("Which email would you like to remove? "))
                del contact_list[mod-1]['Email(s)'][email_num-1]

            if choice==3:
                email_num=int(input("Which email would you like to modify? "))
                new_email=input("Enter new email: ")
                contact_list[mod-1]['Email(s)'][email_num-1]=new_email

def view_contacts(contact_list):
    if len(contact_list)==0:
        print("No contacts!")
    else:
        for i in range(len(contact_list)):
            print(i+1, contact_list[i])

def search_contact(contact_list):
    search_term = input("Enter the name to search for: ")
    found_contacts = [contact for contact in contact_list if search_term.lower() in contact['Name'].lower()]
    if found_contacts:
        print("Found contacts:")
        for i, contact in enumerate(found_contacts):
            print(i + 1, contact)
    else:
        print("No contacts found.")
