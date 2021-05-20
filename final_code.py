def yes_no(question):
  valid = False
  while not valid:
   
    response = input(question).lower()
    if response == "yes" or response == "y":
     response = "yes"
     return response
  
    elif response == "no" or response == "n":
      response = "no"
      return response
     
    
    else:
     print(" please answer with yes/no")

def instructions():
  print("**** How to play ****")
  print()
  print("The rules of the game")
  print()
  return ""

def num_check(question, low, high):
  error = "Please choose a whole amount of money between $1 and $10\n"

  valid = False
  while not valid:
    try:

      response = int(input(question))

      if 0 < response <= high:
        return response
          
      
      else:
        print(error)
    
    except ValueError:
      print(error)

  


played_before = yes_no("Have you played this game before? ")

if played_before == "no":
  instructions()


how_much = num_check("How much would you like to play with? ", 0, 10)

print("So ${}".format(how_much))
  
print("Ok next question")
