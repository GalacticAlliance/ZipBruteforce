from zipfile import ZipFile as ZipHandle # Import python's zip handing module

ZipFileName = input("Please enter the name of the ZIP file: ") # Ask user for name of zip
try: # Make sure the file exists
  ZipFile = ZipHandle(ZipFileName, "r") # Open it
  PasswordFileName = input("Please enter the name of the wordlist file: ") # Ask for wordlists
  try:
    PasswordFile = open(PasswordFileName, "r") # Open wordlist file if exists
    for Line in PasswordFile.readlines(): # Loop through each line
      try: # Try and use each password, if password is wrong, it will error
        ZipFile.extractall(pwd=bytes(Line, "utf-8")) # Try extract - we want it to carry on despite the error
        print("Password found! Password is: " + Line) # This line will be executed if the extraction is successful
        break
      except:
        print("Trying " + Line) # Incorrect password error handled, code will carry on trying words
  except:
    print("Invalid password file name")
except:
  print("Invalid zip file name")

