# Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_text += alphabet[(index+shift)%26]
        else:
            encrypted_text+=char; 
    
    print("Encrypted Text: ",encrypted_text)


def decrypt(text, key):
    decrypted_text = ""
    for char in text: 
        if char in alphabet:
            index = alphabet.index(char);
            decrypted_text += alphabet[(index-key)%26]
        else:
            decrypted_text+=char
    print("Decrypted Text: ",decrypted_text)


def main():

    ascii_art = '''

  sSSs   .S_SSSs      sSSs    sSSs   .S_SSSs     .S_sSSs            sSSs   .S   .S_sSSs     .S    S.     sSSs   .S_sSSs    
 d%%SP  .SS~SSSSS    d%%SP   d%%SP  .SS~SSSSS   .SS~YS%%b          d%%SP  .SS  .SS~YS%%b   .SS    SS.   d%%SP  .SS~YS%%b   
d%S'    S%S   SSSS  d%S'    d%S'    S%S   SSSS  S%S   `S%b        d%S'    S%S  S%S   `S%b  S%S    S%S  d%S'    S%S   `S%b  
S%S     S%S    S%S  S%S     S%|     S%S    S%S  S%S    S%S        S%S     S%S  S%S    S%S  S%S    S%S  S%S     S%S    S%S  
S&S     S%S SSSS%S  S&S     S&S     S%S SSSS%S  S%S    d*S        S&S     S&S  S%S    d*S  S%S SSSS%S  S&S     S%S    d*S  
S&S     S&S  SSS%S  S&S_Ss  Y&Ss    S&S  SSS%S  S&S   .S*S        S&S     S&S  S&S   .S*S  S&S  SSS&S  S&S_Ss  S&S   .S*S  
S&S     S&S    S&S  S&S~SP  `S&&S   S&S    S&S  S&S_sdSSS         S&S     S&S  S&S_sdSSS   S&S    S&S  S&S~SP  S&S_sdSSS   
S&S     S&S    S&S  S&S       `S*S  S&S    S&S  S&S~YSY%b         S&S     S&S  S&S~YSSY    S&S    S&S  S&S     S&S~YSY%b   
S*b     S*S    S&S  S*b        l*S  S*S    S&S  S*S   `S%b        S*b     S*S  S*S         S*S    S*S  S*b     S*S   `S%b  
S*S.    S*S    S*S  S*S.      .S*P  S*S    S*S  S*S    S%S        S*S.    S*S  S*S         S*S    S*S  S*S.    S*S    S%S  
 SSSbs  S*S    S*S   SSSbs  sSS*S   S*S    S*S  S*S    S&S         SSSbs  S*S  S*S         S*S    S*S   SSSbs  S*S    S&S  
  YSSP  SSS    S*S    YSSP  YSS'    SSS    S*S  S*S    SSS          YSSP  S*S  S*S         SSS    S*S    YSSP  S*S    SSS  
               SP                          SP   SP                        SP   SP                 SP           SP          
               Y                           Y    Y                         Y    Y                  Y            Y                                                                                                                          
    '''
    print(ascii_art)

    while(True):
        
        print("\n\nMain Menu:\n===========")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("\nEnter Choice: ")
        
        if choice == '3':
            print("Quitting Program!")
            exit()
        elif choice=='1' or choice=='2':
            text = input("Type your message: ").lower()
            shift = int(input("Type the shift number: "))

            function_map = {'1':encrypt, '2':decrypt}
            
            function_map[choice](text, shift)
        else:
            print("Invalid Input!")



if __name__ == "__main__":
    main()