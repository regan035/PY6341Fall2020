<h3>Full Name: Gen Li</h3>
<h3>Student ID #: 1060038<br />
<h3>Due Date: Tuesday, December 15th, 2020 at 11:59 pm.</h3>
<h3>MSITM 6341</h3>
<h3>Assignment Tittle: Final Python Project </h3>

## About the Project
 “Alien Invasion” is a game project implemented by Pygame framework. The goal of the project is building a python game that draws a ship that start at middle bottom of the window. The ship can move left, right and shoot bullets to alien fleets. The alien fleet will display on the top portion of the window, fly across the window, drop down and change direction. The alien will be removed when hit by bullet and score will be calculated and displayed. It will be level up and increase all speeds when all alien fleets been shoot. Once the alien fleets reach the bottom of window or collide with ship the game count lose. The top-score, current-score, level and remaining ship lives will be display on top of window. 

 ## Project Assumption
 To design the project with better user interface, experience and high performance, we made below adjustment and design:
* We set the background image with a dark space picture and adjust bullet color to bright red. 
* We set the game display in a window on default, and give the user an option to run game in full screen. Please read the instruction to setup the proper display mode.
* To minimize the CPU recourse, we set the maximum bullets allowed display as 3. Once been detected flying at top edge of screen or hit the alien rec, the bullet will be removed and a new bullet can be shot again.  User can adjust this number at settings.py line24.   
* To make the game more fun and challenge we set the alien ship move down by speed when flying to the edge of the screen. And each time when user clear all aliens in screen, the game speed and score will be increased by scale.
* To make the scoring system easy to calculate, we set the default shooting point is 500 each alien. User can adjust this point at setting.py line47.
* We set ship life as 3 initially and this number can be adjusted on settings.py line 17.  

## Running Instruction
Step1, Setup image paths: Before running the code please make sure to download all project files and update below image paths based on your computer disk6 locations: 
* alien.py line13: img_alien = ‘ ’
* settings.py line12: bg_img_path = ‘ ’
•	 * Step2, Setup proper display mode: The game will be run in a game window by default and we have an option to run the game in full screen. In alien_Invation.py there is an option to run the game either in full screen (line 20 to 22) or window(line 25). Please comment out the option that you not prefer. 
Step3, Run the code: To implement the project please open the alien_invation.py file and click the “Execute” button in your IDE. The game code will be executed, the screen will start drawing game contents and a “PLAY” button will be displayed in middle of game screen. After click “Play” button the alien fleet start flying. The use will need using keyboard left and right to control the ship and press “SPACE” to shoot the bullet.   

## Project Screenshot
![](images/01.gif)
![](images/02.gif)
![](images/03.gif)