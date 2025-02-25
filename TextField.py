













#================flet => TextFeild ===============

from flet import *

def main (page:Page):
   
    page.window.width=390
    page.window.height=740
    page.window.top=1
    page.window.left=960
    page.bgcolor=colors.GREEN
    
    #انواع واشكال حقول الادخال 
    #inp1=TextField("first name",width=50, 
#    height=20,color="black")
#    
#    #label عند الضغط ع الحقل ترتفع الكلمة اعلي الحقل
#    inp2=TextField(label="emai",
#    helper_text="g@yahoo.com")#يظهر تحت الحقل للمساعد
#    
#    inp3=TextField(hint_text="link")#تظهر داخل الحقل
#    
#    inp4=TextField(label="your site",
#    prefix_text="https://") #بداية اي رابط وتكمل عليه 
#    
#    inp5=TextField(label="search",
#    icon=icons.SEARCH)#حقل بحث مع أيقونة البحث 
#    
#    inp6=TextField(label="Email",icon=icons.MAIL)
#    
#    inp7=TextField(label="password",
#    icon=icons.PASSWORD,password=True,
#    can_reveal_password=True)

#    #icon.PASSWORD أيقونة تعبر عن أنه ده حقل باس
#    #password=true اخفاء الباس
#    #can_reveal_password=true) اظهار الباس
#    
#    page.add(inp1,inp2,inp3,inp4,inp5,inp6,inp7)

    #=================== images ==================
    
    img1=Image(src=f"MyImagess/img1.jpg",width=100)#مسار الصورة في الجهاز يفضل كتابة fقبل المسار لضمان تشغيل المسار دون اخطاء
    #img2=Image(src="")#طريقة جلب من النت وضع الرابط
    page.add(img1)
    # عمل معرض صور بجانب بعض ب الفور لوب 
    #اذا كانت صور كتير ومش تحملها جانب الملف ممكن فيه 
    #طريقة انك تطلبها من النت مباشرة بوضع الرابط
    
    #اولا انشاء صف بةRow وتخليه لايلتف ويشغل السكرول
    #لان ده اللي هلحق بيه الصور اللي نعرضها
     
    #salary=Row (wrap=False,scroll="always")
    #for img in range(0,7):
        #salary.controls.append(#تحكم ف الصور دي والح
            #Image( #هي دي 
                #src=f"MyImagess/{img}",
                #width=50, height=50,
                #fit=ImageFit.NONE, # ماتخليها تملأ شا
                #repeat=ImageRepeat.NO_REPEAT,#لاتكرر
                #border_radius=border_radius.all(10)
                
            #)
        #)
    #page.add(salary)
    
    #شريط التقدم 
    bar =ProgressBar(color="blue",bgcolor="white",value=0.1,width=500, height=50,tooltip="your progress")
    page.add(bar)

     #======== ProgressRing ع شكل دايرة============= 
    ring=ProgressRing(color="yellow", bgcolor="white",
    value=2, width=100,height=100,
    tooltip="your progress or lodaing")
    page.add(ring)

# الكون
    container=Container(
        content=Text("this is Container", bgcolor="blue",color="white"),padding=padding.all(10),
        margin=margin.symmetric(horizontal=5,vertical=5),
        width=400,height=400
    )
    page.add(container)
    #========================================
    
    page.update()
    
app(main)