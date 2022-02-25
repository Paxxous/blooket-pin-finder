import json, random, threading
from urllib.request import urlopen


def getAndSee():

  while True:
    # Create a random pin
    pin = ''

    for i in range(6):
      pin += str(random.randint(1, 9))

    # Get the pin and then convert it to a readable dictionary
    response = urlopen(f'https://fb.blooket.com/c/firebase/id?id={pin}')
    formattedResponse = json.loads(response.read())

    # Read the dictionary and find if the game actually exists
    if formattedResponse['success'] == False:
      pass

    elif formattedResponse['success'] == True:

      # Append to a file
      f = open('pins.txt', 'a')
      f.write(pin + "\n")


    else:
      # If this happens idk what happened
      print("none")

# Get the number of threads and then run that number of threads
threadNumber = int(input("How many threads would you like to run?\n"))

for i in range(threadNumber):
  threading.Thread(target=getAndSee, args=()).start()
