# Speed-Reader
A speed reading application that allows the user to select different parts of their screen, then read the text of that portion of the screen rapidly in single-word sections at a specified rate

## Guide
In order to run the application, first go to the dependencies folder and execute dependencies.bat. Then use run.bat to initialize the program. 

Once the program is running, you can start the reading process by pressing <kbd>CTRL + ALT + SHIFT + A</kbd>. After this, click once to the top left of where you want to read, followed by one click to the bottom right of the desired reading location.
The application will now open a pop-up window. You can click anywhere in this window to begin reading and click anywhere again to pause/unpause. For now, you will need to edit the source code to change the reading rate or other parts of the program, however in-app support for this is planned to be added at a later date.

When there is no more text to read, the popup will close. You can then press <kbd>CTRL + ALT + SHIFT + A</kbd> to repeat the above process. In order to close the application, simply close the window in the terminal.

## Dependencies
This application requires two dependencies: ![Tesseract Open Source OCR Engine](https://github.com/tesseract-ocr/tesseract) and ![Python](https://www.python.org/downloads/).
If you do not have either of these, do not attempt to run the application.
