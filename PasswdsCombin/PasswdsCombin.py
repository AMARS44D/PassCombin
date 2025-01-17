

# This function lists passwords from your dictionary (let's say the dictionary contains n passwords)
def listing(input_path) : 
    passwdlst=''
    passwdpur=''
    password=''
    lst=[]
    with open(input_path,'r') as file :
            for passwd in file :
                passwdlst=''
                for caractere in passwd : 
                    if caractere !=' ' and caractere!='\n' : 
                        passwdlst +=caractere 
                    else : break
                lst.append(passwdlst)
    return lst
        

#This function makes combinations beetwen your passwords (two by two)(creates n^2 passwords)
def combin(output_path):
    i=0 
    j=0
    lst=listing(input_path)
    with open(output_path,'w') as file : 
        for i in range(len(lst)) :
            for j in range(len(lst)) :
                finalpass=lst[i]+lst[j]
                file.write(finalpass + '\n')


# This function modifies the file created by adding '@' to the generated combinations
#Now, the file contains the original combinations as well as a copy of them with an '@' at the end 
def adding_arobasc (output_path) :
    with open(output_path, 'r') as file:
        pass_generated = file.readlines()
    with open(output_path,'a') as file :  
        for passwd in pass_generated : 
            new_passwd='' 
            for caractere in passwd : 
                if caractere !=' 'and caractere!='\n':
                    new_passwd +=caractere
            file.write(new_passwd + '@' + '\n')




input_path=input('Write the path of your dictionnary or drop a file  (Don\'t forget the extension : .txt) : \n')
output_path=input('Write the path of your output file : \n')
combin(output_path)
adding_arobasc(output_path)


    


          
     

    
            
        

    
        