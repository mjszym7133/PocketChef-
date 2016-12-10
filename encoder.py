#Python Encryption program Version 1.0
#Proof of concept 


Input = ''
choice = ''
x = []


#This is the instruction text 
while choice != 'exit':
    choice = raw_input("\nDo you want to Encrypt or Decrypt the message?\nEnter Encrypt,"
                       "Decrypt, Exit Program, or view saved messages.: ")

#This is the logic for Encrypting a message 
    if choice == 'Encrypt':
        message = raw_input("\nEnter the message to encrypt: ")

        result = ''
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) - 2)
            

        print (result + '\n\n')

        save = raw_input("\nWould you like to save message?: ")
        if save == 'Yes':
            x.append((message, result))
            
 
 #This is the logic for Decrypting a message            


    elif choice == 'Decrypt':
        message = raw_input("\nEnter the message to decrypt: ")

        result = ''
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) + 2)

        print (result + '\n\n')
  
        save = raw_input("\nWould you like to save message?: ")
            
        if save == 'Yes':
            x.append((message, result))

    elif choice != 'Exit' and choice!= 'encrypt' and choice != 'decrypt' and \
         choice != 'Yes' and choice != 'View':
        print ("You have entered an invalid choice. Please try again.\n\n")

    elif choice == 'View':
        print("\n".join(map(str, x)))
        
  
 
        
