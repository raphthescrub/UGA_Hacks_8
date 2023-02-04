# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Eileen")
define tourGuide = Character("Tour Guide")
define TSA_Member = Character("TSA Member")
define TSA_Boss = Character("TSA surperior")
# The game starts here.
#Python Logic
python:
    print("Python is owrking in terminal")
return

#In Game Logic
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #Defining Backgrounds
    image bg FlightRoom = "../images/bg FlightRoom.jpg"
    scene bg FlightRoom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    #Define Characters
    image TourGuide Happy = "../images/TourGuide Happy.png"
    show TourGuide Happy
    image TSAMemberImg = "../images/TSAMemberImg.png"
    #Defines the POV character name

    tourGuide "Welcome to Raphael and Ivan's Hackathon Project"
    tourGuide "We'll take ya on a journey of sustainaibily and happiness for travel."
    tourGuide "First I have to ask ...?"
    python:
        povname = renpy.input("What is your name")
        print("Here is the playername for futre reference:" + povname)
    label NameGiven:
        tourGuide "Hello [povname]!"
        tourGuide "I guess we should go and find somewhere to adventure!"
        tourGuide "Before we do that however, we need to go to TSA and get ourseves annoyed."
    label TSAtime:
        image TSABackGround = "../images/TSABackGround.jpg"
        scene TSABackGround
        show TSAMemberImg
        TSA_Member "Hey Kid! What're you doing here!"
        tourGuide "First of All He's not a kid!"
        show TSAMemberImg at right
        tourGuide "Second of all his name is [povname]"
        show TourGuide Happy at left
        TSA_Member "[povname] Eh?"
        
        TSA_Member "Sounds Foreign."
        TSA_Member "Are you smuggling any weapons and or illegal substances!"
        tourGuide "Remember [povname], When given a choice like this you have to be careful"
        tourGuide "When interacting with TSA you don't want to give them any opportunity to escalte the drama"
        tourGuide "That could land you in TSA prison"
        tourGuide "A pain I wouldn't even give to my worst enemy"
    menu:
        "Yes":
            #Create mini storyline where main characters go to jail and get stuck 
            tourGuide "Stupid! Now we'll get Arrested"
            jump TSABadEnding
        "No"  :      
            "Great Idea!"
            jump TSAGoodending
    label TSAGoodending:
        TSA_Member "Hmmmmmmmm"
        TSA_Member "Even though I don't like you I guess I have to let you go through"
        tourGuide "Hooray! We can finally get through to our flight."
        jump FlightPlane
    # This ends the game.
    label TSABadEnding:
        #Add Prison BackGround
        TSA_Member "Looks like I got a nice batch today. Tee hee"
        jump FlightPlane
    label FlightPlane:
        #Add Image of the inside of a flight 
        tourGuide "Hmpgh"
        tourGuide "TSA can be so weird"
        tourGuide "I mean like who gave theeem that inflated sense of confidence!"

    label Island:
        #Add Background of an Island
        tourGuide "We have landed on the island!"

    return


