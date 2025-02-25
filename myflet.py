













#================== flet library ==================#

#في فلا التطبيق كله عبارة عن دالة بداخله ياخد كائن من كلاس ال Page اللي في مكتبة فلت وبسمي الكائن ده باي اسم وفي الغالب كان بيسموه page سمول وكولون واسم الكلاس

from flet import *

def main (page:Page):
    #التحكم في ابعاد الشاشة الموبايل
    page.window.width=390
    page.window.height=740
    page.window.top=1
    page.window.left=960
    page.bgcolor=colors.BLUE #الدخول الي دالة الالوان 
    #في المكتبة واختيار اللون كابيتال ومن الممكن اختيار 
    #اللون مباشرة ="blackc" 
    
    #كتابة النص ب Text والإضافة ب add باكثر من طريقة
    lb1=Text("welcome to flet firstvwat to add",
    color="black")
    lb2=Text("by programmer rakuwan",color="yellow")
    
    #طريقة أخري لإضافة نص معمول ب """ """
    info= """
        deferent way to add
        name:ali
        age:40
        
        """
    varo="last way to add"
    
    page.add(
        lb1,
        lb2,
    
        Text('this another way to add direct',
        color="green"),
        
        Text(info,color="red"),
        
        Text(varo,color="blue",size=18
        ,font_family="Cascadia Mono"),
        
        #تغيير اتجاه الكتابة عند اللغة العربية والمحاماة
        #ولابد من تشغيل العرض حتي تشتغل هذه الخصائ
        
        Text("السلام عليكم ورحمه الله وبركاته ",
            width=390, #يكون بعرض شاشة التطبيق
            rtl=True ,
            text_align="center",
            size=16,
            color="green", 
            selectable =True #للقدرة علي تحديد ونسخ
        )
        
    )
    
    #اءن طرق الاضافة منها اولا عن طريق كتابة نص بText با
    #الهارج وإضافتها ب add  ثانيا الاضافة المباشرة في ad
    #ثالثا عمل النص بالخارج وإضافة المتغير بadd كالمعتاد
    #لكن الخصائص كاللون وغيره تعطي وهو في add وليس 
    #بالخارج بالطريقة الأولي 
    #رابعا إضافة نص كبير ب الكوتيشن """  وإضافتها ب 
    #Text في add مع إضافة الخصائص وفي كالا الأحوال
    #اي نص هيصاف من غير Textvفي الخارج هضيفه بيها
    #في ال add لانه لازم يضاف من خلالها 
    
    #==============Buttons=============
    #هناك أكثر من نوع للازرار 
    btn1=TextButton("search in my app",
    icon="SEARCH",tooltip="search btn")
    btn2=TextButton("search in my app2",
    icon=icons.SEARCH)#ممكن من اللي في المكتبة
    btn3=TextButton("search in my app2",
    icon=icons.SEARCH_OFF,icon_color="RED")
    
    btn4=ElevatedButton(
        "ElevateButton",
        color="white",
        bgcolor="RED"
    )
    
    page.add(btn1,btn2,btn3,btn4 ,
        #الاضافة المباشرة
        FilledButton(
            "FilledButton",
            icon="add",
            disabled=True
        ),
        IconButton(
            icon=icons.SEARCH,
            icon_color="blue",
            icon_size=10
        ),
        OutlinedButton( #الاكثر استخدام للتحكم به اكثر
            text="OutlinedButton",
            icon=icons.SEARCH_OFF_SHARP,
            style=ButtonStyle(color="black",
            bgcolor="amber",
            shape=RoundedRectangleBorder(radius=5))
        )#تحديد الدوران للزر
    )
    
    
    page.update()#لاظهار النصوص والمضافة الجديدة 
    #باستمرار
    
app(main)#اظهار الصفحة 
