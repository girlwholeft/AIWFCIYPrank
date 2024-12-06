You will need a Windows computer, Python 3.9 or later, Visual Studio Code, Dropbox, a .mp3 file for All I Want For Christmas Is You, and a BAT to EXE converter (download here: https://bat-to-exe-converter-x64.en.softonic.com/)

Download the flappygame.py and mariahpocalypse.py files

Go to the terminal in Visual Studio Code and type: py -(your Python version) -m pip install pygame pyinstaller

Be sure to replace (your Python version) with your actual version, whether that be 3.9, 3.10, 3.11, or 3.12

To convert the flappygame.py file into an exe file, go to your termainal in VSCode and type: pyinstaller flappygame.py --onefile --noconsole

To convert the mariahpocalypse.py file into an exe file, go to your termainal in VSCode and type: pyinstaller mariahpocalypse.py --onefile --noconsole

Then, upload all of the files from image_and_mp3_files to Dropbox

Download the mariahpocalypse.bat file

Find a cool .ico file for the .exe file you want to make. These can easily be found on the internet

Open the mariahpocalypse.bat file in the BAT to EXE converter

Replace all of the placeholders with your download links from Dropbox, making sure to change "dl=0" to "dl=1"

Go to the right-hand menu, check the "Icon" button, and upload the .ico file

