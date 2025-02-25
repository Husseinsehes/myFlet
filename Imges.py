from flet import *

def main (page:Page):
    global list
    page.window.width=390
    page.window.height=740
    page.window.top=1
    page.window.left=960
    page.bgcolor=colors.GREEN_200


    #img1=Image(src=f"/workspaces/myFlet/MyImages/one.jpg",width=150)#مسار الصورة في الجهاز
    #تجربة تشغيلها بالمسار المطلق
    #import os
    #img1 = Image(src=os.path.abspath("MyImages/One.png"), width=100)

    
    import os #التامد من مسار الصورة 
    print(os.path.exists("MyImages/One.jpg"))  # سيطبع True إذا كان المسار صحيحًا

    #img2=Image(src="https://www.pinterest.com/pin/659777414138577193/")#طريقة جلب من النت وضع الرابط
    #page.add(img1)
    # عمل معرض صور بجانب بعض ب الفور لوب 
    #اذا كانت صور كتير ومش تحملها جانب الملف ممكن فيه 
    #طريقة انك تطلبها من النت مباشرة بوضع الرابط
    
    #اولا انشاء صف بةRow وتخليه لايلتف ويشغل السكرول
    #لان ده اللي هلحق بيه الصور اللي نعرضها
     
    salary=Row (wrap=False,scroll="always")
    for img in range(0,10):
        salary.controls.append(#تحكم ف الصور دي والح
            Image( #هي دي 
                src=f"https://picsum.photos/200/200{img}",
                #src=f"/workspaces/myFlet/MyImages{img}",
                width=400, height=150,
                fit=ImageFit.NONE, # ماتخليها تملأ شا
                repeat=ImageRepeat.NO_REPEAT,#لاتكرر
                border_radius=border_radius.all(10)
                
            )
        )
    page.add(salary)
   #الcheckbox
    list=[]
   
    def data1(e):
       global list
       if choice1== True:
           list.append(choice1.label)
           Txt.value=",".join(list)
           page.update()
       else  :
           list.remove(choice1.label)
           Txt.value=",".join(list)
           page.update()
    def data2(e):
       global list
       if choice2.value ==True:
          list.append(choice2.label)
          Txt.value=",".join(list)
          page.update()
       else  :
           list.remove(choice2.label)
           Txt.value=",".join(list)
           page.update()
   
    choice1 =Checkbox(label="student",value=False, 
    on_change=data1)
    choice2 = Checkbox(label="teacher",value=False,
    on_change=data2)
    Txt=Text(value=",".join(list))
    #page.add(choice1, choice2, Txt)
    page.controls.extend([choice1,choice2,Txt])

    #========================================
   # الRadio 
    TXT=Text(value="welcome",color="red")
   #عند اختيار زر تتبدل القيمة اللي في تكست به
    def RADIO(e):
       TXT.value="you are" + radio_group.value
       page.updat()
      
    radio_group=RadioGroup(content=Column([
       Radio(label="Male", value="mail"),
       Radio(label="Female", value="female")
   ]), on_change=RADIO,)
    
    page.add(radio_group,TXT)
    
    
    



    page.update()


app(main)


