from googletrans import Translator
from random import randint
import cv2
import numpy as np
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
cap = cv2.VideoCapture("TheHellWalk.mp4")
cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("TheHellWalk.mp4",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    cv2.imshow('Frame',frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
      break
  else:
    break
cap.release()
cv2.destroyAllWindows()
print("  /$$$$$$                      /$$                                                            "+
"\n /$$__  $$                    |__/                                                            "+
"\n| $$  \ $$ /$$$$$$$  /$$$$$$$  /$$ /$$   /$$  /$$$$$$  /$$$$$$$                               "+
"\n| $$$$$$$$| $$__  $$| $$__  $$| $$| $$  | $$ |____  $$| $$__  $$                              "+
"\n| $$__  $$| $$  \ $$| $$  \ $$| $$| $$  | $$  /$$$$$$$| $$  \ $$                              "+
"\n| $$  | $$| $$  | $$| $$  | $$| $$| $$  | $$ /$$__  $$| $$  | $$                              "+
"\n| $$  | $$| $$  | $$| $$  | $$| $$|  $$$$$$$|  $$$$$$$| $$  | $$                              "+
"\n|__/  |__/|__/  |__/|__/  |__/|__/ \____  $$ \_______/|__/  |__/                              "+
"\n                                   /$$  | $$                                                  "+
"\n                                  |  $$$$$$/                                                  "+
"\n                                   \______/                                                   "+
"\n                         /$$                                             /$$               /$$"+
"\n                  | $$                                            | $$              | $$"+
"\n /$$  /$$  /$$  /$$$$$$ | $$$$$$$         /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$ | $$"+
"\n| $$ | $$ | $$ /$$__  $$| $$__  $$       /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/   |____  $$| $$"+
"\n| $$ | $$ | $$| $$$$$$$$| $$  \ $$      | $$  \ $$| $$  \ $$| $$  \__/  | $$      /$$$$$$$| $$"+
"\n| $$ | $$ | $$| $$_____/| $$  | $$      | $$  | $$| $$  | $$| $$        | $$ /$$ /$$__  $$| $$"+
"\n|  $$$$$/$$$$/|  $$$$$$$| $$$$$$$/      | $$$$$$$/|  $$$$$$/| $$        |  $$$$/|  $$$$$$$| $$"+
"\n \_____/\___/  \_______/|_______/       | $$____/  \______/ |__/         \___/   \_______/|__/"+
"\n                                        | $$                                                  "+
"\n                                        | $$                                                  "+
"\n                                     |__/                                                  "+
"\n"
)

translator=Translator()
result=translator.translate(input("குற்றவாளிகளின் பெயர்:\t").title(),dest='ta')
name=result.text
result=translator.translate(input(" குற்றம்:\t"),dest='ta')
kutram=result.text

result=translator.translate(input(" அடயலம்:\t"),dest='ta')
atayalam=result.text
count=randint(1,7)
if(count==1):
    punishment="கார் விபத்து காரணமாக இறந்துவிடுவார்"
elif(count==2):
    punishment="கொரோனா காரணமாக இறந்துவிடுவார்"
elif(count==3):
    punishment="சிரித்து சிரித்து இறந்துவிடுவார்"
elif(count==4):
    punishment="ஒரு பல்லியை விழுங்கி இறப்பான்"
elif(count==5):
    punishment="அறியப்படாத நபரால் கொல்லப்படுவார்"
elif(count==6):
    punishment=" ஒரு கரப்பான் பூச்சி சாப்பிட்டு இறந்துவிடுவார்"
elif(count==7):
    punishment=" MINECRAFT விளையாடி இறந்துவிடுவார்"
elif(count==8):
    punishment=" பேட்மேனால் தாக்கப்பட்டதால் இறந்தார்"
elif(count==9):
    punishment=" கரடி குகையில் முகாமிட்டதால் இறந்துவிட்டார்"
elif(count==10):
    punishment=" Harry Potter போல விளக்குமாறு பறக்க முயன்றார், கட்டிடத்திலிருந்து குதித்து இறந்தார்"
print(
    "      %%% %%%%%%%            |#|"
+"\n    %%%% %%%%%%%%%%%        |#|####"
+"\n  %%%%% %         %%%       |#|=#####"
+"\n %%%%% %   @    @   %%      | | ==####"
+"\n%%%%%% % (_  ()  )  %%     | |    ===##"
+"\n%%  %%% %  \_    | %%      | |       =##"
+"\n%    %%%% %  u^uuu %%     | |         ==#"
+"\n      %%%% %%%%%%%%%      | |           V "
+"\n\n")
filename='hitlist.txt'
with open(filename,'a') as file_object:
    file_object.write(name+" என்ற பெயருடன் "+atayalam+" அடயலம் கோண்டா நவர் "+kutram+" செய்த காரணத்தினால் "+punishment+'\n')
print(name+" என்ற பெயருடன் "+atayalam+" அடயலம் கோண்டா நவர் "+kutram+" செய்த காரணத்தினால் "+punishment)
c=input("Press 'F' to pay respect:\t")
while(c.lower()!='f'):
    c=input("\n pay respect properly:(press F)\t")

