The purpose of this project is to prank your friends by making their computer play All I Want For Christmas Is You by Mariah Carey every 20-60 minutes. The code for this will be disguised as a Flappy Bird type of game.

You will need a Windows computer, Python 3.9 or later (download Python 3.12 here: https://www.python.org/downloads/release/python-3120/), Visual Studio Code, Dropbox, and a BAT to EXE converter (download here: https://bat-to-exe-converter-x64.en.softonic.com/)

Download the flappygame.py and mariahpocalypse.py files

Go to the terminal in Visual Studio Code and type: py -(your Python version) -m pip install pygame pyinstaller

Be sure to replace (your Python version) with your actual version, whether that be 3.9, 3.10, 3.11, or 3.12

To convert the flappygame.py file into an exe file, go to your termainal in VSCode and type: pyinstaller flappygame.py --onefile --noconsole

To do this with the mariahpocalypse.py file, go to your termainal in VSCode and type: pyinstaller mariahpocalypse.py --onefile --noconsole

Then, download all of the files from the image_and_mp3_files folder in this repository and upload them to Dropbox

Download the mariahpocalypse.bat file

Find a cool .ico file for the .exe file you want to make. These can easily be found on the internet

Open the mariahpocalypse.bat file in the BAT to EXE converter

Replace all of the placeholders with your download links from Dropbox, making sure to change "dl=0" to "dl=1"

Go to the right-hand menu, check the "Icon" button, and upload the .ico file

Under "Exe-Format", choose 32-bit Windows (Invisible)

Check "Request administrator privileges" under UAC

Click "Convert"

Lastly, upload your .exe file to Dropbox or Github, and get the download link to send to your friends.

To teach your friends how to reverse it, tell them to press ctrl+alt+delete and click task manager, and type mariahpocalypse into the search bar and right-click it to end the task.
