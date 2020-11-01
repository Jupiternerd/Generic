# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.
label pre:

  #pre game stuff like defining chars



label start:


  $ chapter = 1

  python:
      class person:
          def __init__(self, pen):
             self.who = pen

      x = person("Wai")

  call chap1


  e "test2"
return
