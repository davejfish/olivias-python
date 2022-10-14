name = input("Type your name: ")
print("Welcome", name, "can you escape The Door???")

answer = input(
  "You approach a door, do you ring the doorbell or knock? Type 'doorbell' or 'knock': " ).lower()

if answer == "doorbell":
  doorbell = input(
    "You reach for the doorbell and notice the door is cracked open, do you go in or close the door? Type 'go in' or 'close door': "
  )
  if doorbell == "go in":
      goIn = input(
        "You go inside and see a room with a lit fireplace and a staircase, where do you go? Type 'fireplace' or 'stairs': "
        )
      if goIn == "stairs":
        stairs = input(
          "You head up the stair taking you to a hallway, to your left you see what looks like a bedroom and on the right what appears to be a bathroom, where do you go? Type 'left' or 'right': "
          )
        if stairs == "left":
            left = input(
              "You walk into the bedroom and see a mirror next to a window, which do you walk up to? Type 'window' or 'mirror': "
            )
            if left == "mirror":
              print('You look in the mirror and looking back at you... is a door')

            elif left == "window":
              print("You want to look out at the view from the bedroom and when you walk up to the window a door comes out of nowhere, falling on you and pushing you through the window, you land safely on your back but the door falls out too. Landing on you and killing you")

        elif stairs == "right":
          print("You head towards the bathroom because you have to pee, as you enter and close the door behind you it falls on you and you die")

        else:
          print('Not an option, the door behind you fell on you and you died')
        
      
      elif goIn == "fireplace":
        print("You approach the fireplace and notice the kindling is a door, the door leaps out at you and you die via door fire")
      else:
        print('Not an option, the door behind you fell on you and you died')

  elif doorbell == "close door":
      print('You close the door, it falls on you and you die')
  else:
    print('Not an option, the door fell on you and you died')


elif answer == "knocker":
  knocker = input(
    "You decide to knock and notice a knocker attached to the door, do you use the knocker or your fist? Type 'knock' or 'fist'"
  )
  if knocker == "knock":
    print("You grab the handle and as you pull on it, the door falls on you and you die")
  elif knocker == "fist":
    print("You curl your hand into a fist and with your first knock you punch through the door, as you try to pull your hand out of the hole you made the door falls on you and you die")
  else:
    ('Not an option, the door fell on you and you died')
else:
  print('Not an option, the door fell on you and you died')