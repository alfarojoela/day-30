#exception handling example

try: #something that might cause an exception
    file = open("a_file.txt")
    a_dictionary={"key": "value"}
    print(a_dictionary["asdf"])
except FileNotFoundError: #do if there is an exception
    #print("There was an error!")
    file=open("a_file.txt", "w") #will create if not existing due to w argument
    file.write("Someting")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else: #do if NO exceptions
    content = file.read()
    print(content)
finally: #do this no matter what happens
    file.close()


