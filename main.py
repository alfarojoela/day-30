#exception handling example

#can have multiple exceptions
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

    #raise KeyError #allows to raise own exceptions.

#example:

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:  #although not an error with logic or computation, highly unlikely user will be over 3 meters.
    raise ValueError

bmi = weight / height **2
print(bmi)

#example
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
  try:
    total_likes = total_likes + post['Likes']

  except KeyError:
    total_likes = total_likes + 0  #or could use pass



print(total_likes)


