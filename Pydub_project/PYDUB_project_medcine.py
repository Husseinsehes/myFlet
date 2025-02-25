








#مكتية pydub
from pydub.playback import play
from pydub import*
import datetime 

import time
import os
#ادخال الوقت 
ent_time=input("Enter time alarm to take medicine:")
#تمرير الصوت اللي هينبهه بصيغة mp3 
#alarm=AudioSegment.from_mp3("Pydub_project/med.mp3")
#play(alarm)#تشغيل الصوت





#وضع الكود في حلقة تكرار عشان يفضل يقول طالما الوقت جه
while True:
    time_now=datetime.datetime.now()#الوقت الحالي
    now=time_now.strftime("%H:%M:%S")#يكتب كده
    #تحقق لو الوقت الحالي ع الجهاز توافق مع وقت اللي دخله المستخدم شغل الصوت الاتي
    if now == ent_time:
        medicine=AudioSegment.from_mp3(os.path.abspath("med.mp3"))
        play(medicine)
        #ولو عداه واو مجاش وقف 
    if now > ent_time:
        break
    time.sleep(1)#جعل التكرار كل ث فقط 

    #sudo apt update
    #
    # sudo apt install ffmpeg
