# Text_recognition_and_speech_generation
This project is an attempt to help visually impaired people to read digital content and other non Braille scripts. 
In this project we will be using pytesseract and tesseract OCR to fetch text from an image and then pass the recognised text into a 
gTTS engine which will help us convert the text into speech.

### Dependencies:
1. Pytesseract
2. Tesseract OCR
3. gTTS 

### Steps to execute this project using ".ipynb" file
1. Download the files from this repository 
2. Open Colab from google
3. Upload ".ipynb" file and connect
4. Now upload the text image upon which you would like to test.
5. Run each cell one after other.

### NOTE:
If you wish to use colab as your ide, then all the installations will be done automatically after you upload the .ipynb file and run it.
Else you can also run this code via any other .py ide such as spyder. But you'll have to setup your environment manually.

### Installation of dependencies (For manual installation):
1. Install pytesseract using anaconda prompt
"pip install pytesseract"
2.  Install gTTS using anaconda prompt
"pip install gTTS"
3.  Download tesseract executible file from: 
"https://github.com/UB-Mannheim/tesseract/wiki"
4.  Run that 'tesseract________.exe' file and install.

### Steps to execute this project using ".py" file                                                                  
1.  Download python idle from python.org 
2.  Install python using normal process 
3.  Download pycharm community edition 
4.  Install pycharm/spyder or any other .py ide.
5.  Install pytesseract using command prompt
"pip install pytesseract"
6.  Install gTTS using command prompt
"pip install gTTS"
7.  Download tesseract executible file from: 
"https://github.com/UB-Mannheim/tesseract/wiki"
8.  Run that 'tesseract________.exe' file and install.
9.  Download the 'files from this repository' 
10.Now open the python code file and run it.
11.Check for errors:
      If pytesseract not found error, try by changing the 
      command  from "import pytesseract" to 
      "from pytesseract import pytesseract" and
      from line 5, remove "pt" and from line 7,
      replace pt with pytesseract.
      Else any, check for the directory error and 
      check whether pytesseract,gTTS and tesseract ocr 
      are installed properly.

                                                                                                     - V.N.S. Satya Teja
