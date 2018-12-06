# KinectAvatar
112 Term Project

This game is called "The Last Airbender: Kinect ShowDown". 
This is essentially a “Streetfighter” fighting game of The Last Airbender that the user can play/control the character with the their hand motions through the Kinect against an AI.

This project should be run in Python 3.6, in an editor such as Pyzo, and have all the image files in the same directory.

To play, you will need to install PyKinect2, the Kinect SDK, a Microsoft Kinect and Pygame.

Game Controls:
•	Charge = Free (Hands together)
    •	 Serves as ammunition. If the player wants to shoot or mirror aka play offensive, they must charge. 
    •	Charging is a vulnerable state, as the player has the risk of being shot at, but also has the potential to shoot later.
    
•	Jump = Free (Clap Up)
    •	Jumping avoids any bullets if the CPU shoots at the player.
    •	Nothing is gained, so you won’t advance in the game if you continuously jump
    
•	Shoot = 1 charge ('lasso'/gun position)
    •	The player must choose to shoot strategically in the hopes that the opponent is vulnerable at that moment.
    •	Offensive move
    
•	Mirror = 1 charge (arms up)
    •	If the player “mirrors” and is shot at, the player can shield themselves and cause the CPU to lose points. 
    •	The player must be strategic because the player must charge before using this.
    •	This only benefits the player if the player is shot at.


This file has a pygame version you can use the keyboard to play if you dont have a Kinect. Keys "Space, enter, up, down, right, and left" are used.
To control the game with the Kinect, use the "Lasso" to skip ahead to the actual game.
To play the game, you must block with arms up, shoot with a "lasso" of hands, and hands together to charge.
