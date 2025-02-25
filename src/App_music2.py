









from tkinter import *
from tkinter import filedialog
import pygame
import os

root = Tk()
root.geometry("1000x1000+200+200")
root.title("File Viewer and Music Player")
root.config(background="#424949")

photo=PhotoImage(file="music.png")
label_image=Label(root, image=photo)
label_image.place(x=0, y=0,width=1000,height=900)

pygame.init()

title = Label(root, text="Player and File Viewer", fg='white', bg="#21618C")
title.pack(fill=X)

# Label ظهور اسم الملف اللي هيظهر أو هيشتغل
file_label = Label(root, text="No file selected", fg='white', bg="#424949", font=("arial", 7))
file_label.place(x=10, y=100)

# Text widget to display file content,texteara مساحة لعرض الملف النصي أو بايثون  الwrap للالتفاف الكلام الزائد 
file_content = Text(root, wrap=WORD, width=100, height=10,bg="#424949")
file_content.place(x=00, y=600)

#فنكشن الدخول الي الجهاز ولم نقيد نوع محدد من الملفات جميع الانواع سواء كانت audio أو .txt أو .py تستطيع فتحها وقراءتها ملحوظة الpy فتح الملف كنص يعني قراءة الكود وليس تشغيل الملف كبرنامج وروية واجهته 
def play_selected_file():
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Audio Files", "*.mp3 *.ogg *.wav *.flac"),
            ("Text Files", "*.txt"),
            ("Python Files", "*.py"),
            ("All Files", "*.*")
        ])
    #لو الملف موجود او اختير خش علي النظام هات اسمه فقط وليس مساره كامل path.basename وتمرير المسار اللي اتخزنت في االقوسين وهيجيب من المسار ده الاسم وتمريره لليبول بتاعة اظهار اسم الملف اللي هيشتغل
    if file_path:
        file_name = os.path.basename(file_path)
        file_label.config(text=f"Selected: {file_name}")
        file_content.delete(1.0, END) # امسح القديم عند اختيار جديد 

        #لووالملف منتهي بأحد الصيغ دي اعمله تشغيل كصوت بواسطة مكتبة pygame
        if file_path.endswith(('.mp3', '.ogg', '.wav', '.flac')):
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play(loops=0)
       #ولو كان لينتهي ب .py يعني بايثون افتحه وأعماله r يعني قراءة واستدعي الخاصية .read)
        elif file_path.endswith('.txt') or file_path.endswith('.py'):
            with open(file_path, 'r') as file:#افتح واقرا ليه واعتبره ملف
                content = file.read()#واعمل متغيرافتحزبيه الملف ده
            file_content.insert(END, content) #وضيف للمساحه محتوي الملف ده المخزن في المتغير content 
            #ولولم يكن مما سبق قوله غير مدعوم 
        else: 
            file_content.insert(END, "Unsupported file type.")

def Stop():
    pygame.mixer.music.stop()
    file_label.config(text="Music Stopped")

btn_browse = Button(root, text="Browse and Play/View", bg="#2E86C1", fg="white", command=play_selected_file)
btn_browse.place(x=10, y=270)

btn_stop = Button(root, text="Stop", bg="#FF5733", fg="white", command=Stop)
btn_stop.place(x=675, y=270)

root.mainloop()




