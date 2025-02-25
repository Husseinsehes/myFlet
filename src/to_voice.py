














#import pyttsx3

#engine = pyttsx3.init()
#engine.say("hello")
#engine.runAndWait()

from gtts import gTTS
import os

# النص الذي تريد تحويله إلى صوت
text = "مرحبًا، كيف حالك اليوم؟"

# تحديد اللغة (مثلاً: اللغة العربية)
language = 'ar'

# تحويل النص إلى صوت
tts = gTTS(text=text, lang=language, slow=False)

# حفظ الصوت في ملف
tts.save("output.mp3")

# تشغيل الصوت
os.system("mpg321 output.mp3")  # على linux

#sudo apt-get install mpg321