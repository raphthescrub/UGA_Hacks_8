#Python Logic
init python:
    print("Python is owrking in terminal")
    points = 0
return
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Eileen")
define tourGuide = Character("Tour Guide")
define TSA_Member = Character("TSA Member")
define TSA_Boss = Character("TSA Boss")
define Pilot = Character("Pilot")
define AirportKaren = Character("AirportKaren")

#The Dawn Character
define UkaranianPersonTall = ("Tall Person")
image TallPerson Side = "../images/DawnExplorationSide.jpg"
image Home = "../images/Home.png"
#The MY Character
define UkranianPersonShort = ("Short Person")
image ShortPersonSide = "../images/MyExploring.jpg"
image ShortPersonFront = "../images/MyExploration2.jpg"

image TourGuide Happy = "../images/TourGuide Happy.png"
show TourGuide Happy
image TSAMemberImg = "../images/TSAMemberImg.png"
image PlaneInterior = "PlaneInterior.jpg"
# The game starts here.



#In Game Logic
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #Defining Backgrounds
    image bg FlightRoom = "../images/bg FlightRoom.png"
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
        points = 0
        povname = renpy.input("What is your name")
        print("Here is the playername for future reference:" + povname)
    label NameGiven:
        tourGuide "Hello [povname]!"
        tourGuide "I guess we should go and find somewhere to adventure!"
        tourGuide "Before we do that however, we need to go to TSA and get ourseves annoyed."
    label TSAtime:
        image TSABackGround = "../images/TSABackGround.jpg"
        scene TSABackGround
        show TSAMemberImg at right
        TSA_Member "Hey Kid! What're you doing here!"
        show TourGuide Happy at left
        tourGuide "First of All He's not a kid!"
        tourGuide "Second of all his name is [povname]"
        show TourGuide Happy at center
        tourGuide "Kapish!"
        show TourGuide Happy at left
        tourGuide "I guess I was too Aggressive!"
        tourGuide "And maybe I shouldn't say Kapish"
        tourGuide "Being honest I don't even know what it means"
        #hide tourGuide Happy with dissolve
        #Do a close up
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
            $points = points + 1
        "No"  :      
            "Great Idea!"
            jump TSAGoodending
            $points = points - 1
    label TSAGoodending:
        TSA_Member "Hmmmmmmmm"
        TSA_Member "Even though I don't like you I guess I have to let you go through"
        tourGuide "Hooray! We can finally get through to our flight."
        jump FlightPlane
    # This ends the game.
    label TSABadEnding:
        #Add Prison BackGround
        image TSABoss = "TSA_Boss.jpg"
        image AirportJail = "../images/AirportJail.jpg"
        scene AirportJail
        show TSAMemberImg at left
        show TourGuide Happy
        TSA_Member "Looks like I got a nice batch today. Tee hee"    
        TSA_Boss "Let me deal with these Kevin!"
        TSA_Member "Yes sir ...."
        hide TSAMemberImg with fade
        show TSABoss at left
        #show TSA_Old Man
        TSA_Boss "Sorry about that sometimes we TSA can be a little annoying"
        TSA_Boss "One of those annoying people is me of course"
        TSA_Boss "Here's a Random Question on Travel"
        jump TSABadEndingQuestionIntro
    label TSABadEndingQuestionIntro:
        TSA_Boss "And Now I ask the Question!"
    menu:
        "Who are the considered the best tourists"

        "Americans":
            $points = points - 1
            "You and I know that isn't true"
            jump TSABadEndingQuestionIntro
        "Japanese":
            $points = points + 1
            "Wow You got it faster than expected"
            jump FlightPlane
        "Brits":
            $points = points - 1
            "That Answer makes me think you're Britsh"
            "Not saying that as an insult but just as a fact"
            jump TSABadEndingQuestionIntro
        "Karens":
            $points = points - 1
            "This is a joke answer why would you pick this"
            jump FlightPlane
    label FlightPlane:
        image Airport_Karen = "../images/Karen.png"
        #Add Image of the inside of a flight 
        scene PlaneInterior
        show TourGuide Happy at left
        tourGuide "Hmpgh"
        tourGuide "TSA can be so weird"
        tourGuide "I mean like who gave theeem that inflated sense of confidence!"
        tourGuide "But at least we're here on the flight"
        #PILOT will be a faceless character
        Pilot "Attention everybody please sit in you seats"
        tourGuide "Well that seems reasonable."
        show Airport_Karen at right with fade
        AirportKaren "NO I WILL NOT SIT DOWN. IT IS MY RIGHT AS AN AMERICAN TO STAND UP"
        tourGuide "I think your blowing this out of proportion a little"
        AirportKaren "I AM NOT GOING TO CALM DOWN. IF NOBODY CALMED DOWN THEN ABRAHAM LINCON WOULDN'T HAVE STOPPED THE DINOSUARS FROM DESTROYING AMERICA"
        tourGuide "........."
        tourGuide"........."
        tourGuide "I'm not dealing with this."
        tourGuide "Why don't you talk some sense into this person [povname]"
        hide TourGuide Happy with fade
        menu:
            "Fight!":
                "You Fight the Karen at the airport and almost die. Your Get off safely for this escapade however and go home"
                $points = points + 1
                jump Island
            "Agree":
                "You ask agree to stand on the plane and the pilot continues on the flight. Both you and the karen almost die"
                $points = points - 1
                jump Island
            
            "Call TSA":
                "TSA comes in and sends the karen away. They are happy they have someone to arrest"
                $points = points - 1
                jump Island
            "Ignore":
                "The karen complains throughout the flight and destorys your plane move experience"
                $points = points + 1
                jump Island
    label Island:
        image AirportPickup = "AirportPickup.png"
        scene AirportPickup
        show TourGuide Happy 
        AirportKaren "That was such a terrrrible flight."
        tourGuide "No thanks to you dinghead"
        #Hide AirportKaren Mad
        show ShortPersonSide at left:
            zoom .1
        tourGuide "Oh look, There's a person there, maybe we can talk to them to find something fun to do."
        show ShortPersonSide at left:
            zoom .2
        UkranianPersonShort "Oh hey you wanted to talk me"
        tourGuide "We saw that you were a tourist so we thought you could show us a few fun events"
        UkranianPersonShort "Ah yeah there are a few places I know:"
        menu:
            "Go To Resturaunt":
                jump Resturaunt
            "Go to Tunnel of Love":
                jump Tunnel
    label Resturaunt:
        image ResturauntInterior = "../images/ResturauntBackground.jpg"
        scene ResturauntInterior:
            zoom 1.5
        show TourGuide Happy at left
        show ShortPersonSide at right:
            zoom .2
        UkranianPersonShort "Here's the place"
        UkranianPersonShort "I think they have some pretty tasty food"
        show TallPerson Side at center: 
            zoom .1
        UkaranianPersonTall "Ah hello welcome to our resturaunt. Local Cuisine incorporated"
        UkaranianPersonTall "What would you like to eat here"
        menu:
            "Hamburger":
                "The Hamburger went hard"
                $points = points - 2
                jump FinalResturaunt
            "Potato Salad":
                "The Potatos were alright"
                $points = points - 1
                jump FinalResturaunt
            "Tofu Scramble":
                "Not to bad"
                $points = points + 1
                jump FinalResturaunt
        label FinalResturaunt:
            tourGuide "Looks like you enjoyed your meal"
            show TallPerson Side at center
            UkaranianPersonTall "So much will you tip"
            tourGuide "Ummmmmmm"
            menu:
                "Dont Pay!":
                    $points = points - 1
                    "You were caught shortly after"
                    jump EndOfAdventureQuick
                "Pay!":
                    $points = points + 1
                    "You peacefully walked home"
                    jump EndOfAdventure
    label Tunnel:
        #Tunnel of Love
    label EndOfAdventure:
        scene Home
        show TourGuide Happy at center 
        "The tourist went home and learned about the beauty of travel and niceness"
        tourGuide "Honeslty its great that we can leave a country without having to be deported"
        tourGuide "The last person I was with had us get deported from the country"
        tourGuide "Anyways man I hope you have a good rest of your day."
        tourGuide "I have to go home and get readay for UGA Hacks 9!"
        return
    label EndOfAdventureQuickEnd:
        "After Stealing from the resturaunt you were booted to you home country "
        tourGuide "Looks like you screwed us over. "
        tourGuide "Now we're banned and can't travel anymore"
        "And from now on we learn a a cautioanary tale of annoying others "
        return




