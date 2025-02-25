









#استخدام هذا الكود علي الحاسوب لأن بايدرويد لايدعم مكتبات كا gtts أو pyttsx3

#from gtts import gTTS
#import os

# النص الذي تريد تحويله إلى صوت
#text = "مرحباً! كيف حالك؟"

# تحديد اللغة (على سبيل المثال، العربية)
#language = 'ar'

# إنشاء الصوت
#tts = gTTS(text=text, lang=language, slow=False)

# حفظ الصوت في ملف MP3
#tts.save("output.mp3")

# تشغيل الملف الصوتي
#os.system("start output.mp3")  # على Windows
#os.system('play output.mp3')#لينكس


#from gtts import gTTS
#import os

# النص الذي تريد تحويله إلى صوت
#text = "مرحباً! كيف حالك؟"

# تحديد اللغة (على سبيل المثال، العربية)
#language = 'ar'

# إنشاء الصوت
#tts = gTTS(text=text, lang=language, slow=False)

# حفظ الصوت في ملف MP3
#tts.save("output.mp3")

# تشغيل الملف الصوتي باستخدام تطبيق مدمج على الأندرويد
#os.system("termux-media-player play output.mp3")



#كود تشغيل المكتبة علي بايدرويد٣ باستخدام مكتبة pygame

from gtts import gTTS
import pygame

# النص الذي تريد تحويله إلى صوت
text = "مرحباً! كيف حالك؟"
# تحديد اللغة (على سبيل المثال، العربية)
language = 'ar'
# إنشاء الصوت
tts = gTTS(text=text, lang=language, slow=False)
# حفظ الصوت في ملف MP3
tts.save("output.mp3")

# تهيئة pygame
pygame.mixer.init()
# تحميل وتشغيل الصوت
pygame.mixer.music.load("output.mp3")
pygame.mixer.music.play()

# #الانتظار حتى ينتهي الصوت
while pygame.mixer.music.get_busy():
    continue











