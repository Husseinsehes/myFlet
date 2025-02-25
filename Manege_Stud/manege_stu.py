















#=========== إدارة شؤون الطلاب=============
from flet import *
import sqlite3 
import os
#========== data bases============

con = sqlite3.connect("data.db",check_same_thread=False)#
cursor=con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name Text,email Text,phone Text,address Text,
    math INTEGER,Arabic INTEGER,french INTEGER,draw INTEGER,chemstry INTEGER
)""")


def main (page:Page):
    page.title ="flashlight"
    page.scroll="auto"
    #page.window.full_screen=True
    #page.window.title_bar_buttons_hidden=False#اخفاء جزء اللي فيه العنوان العلوي
    page.theme_mode=ThemeMode.LIGHT

    #====== count stud ======
    #عمل متغير باسم الجدول وعمل استعلام عليه بالعدد للكل اللي فيه وتنفيذ ذلك ثم الوصول لواحد منه بداية من صغر كل مايضيف يخزن واحد ويعرض كل الموجود 
    table_name="student"
    query =f"SELECT COUNT(*) FROM {table_name}"
    cursor.execute(query)
    result=cursor.fetchone()
    row_count=result[0]
    
    #=======add stud ==========
    def add(e):
        cursor.execute("INSERT INTO student (name,email,phone,address,math,Arabic,french,draw,chemstry) VALUES(?,?,?,?,?,?,?,?,?)",(name.value,email.value,phone.value,address.value,Math.value,Arabic.value,French.value,draw.value,chemstry.value))
        con.commit()
        alert=AlertDialog(
            title=Text("saved",color="green")
        )
        page.overlay.append(alert)
        alert.open=True
        page.update()


        page.update()
    #====== show stud======
    def show(e):
        page.clean()
        display=con.cursor()
        display.execute("SELECT * FROM student")
        users=display.fetchall()
        #for user in users:
        #print(user)#
                #العرض في الواجهة 
        # التحقق الاول لو ماكنش فاضي القاعدة هنعمل قاموس
        #مفتاخ وقيمة 
        if not users== "" :
            #المفاتيح اسماء الحقول في الجدول 
                keys=["id",
    "name","email","phone","address",
    "math","Arabic","french","draw","chemstry"]
            #عمل قاموس  المفتاح قيمته من متغير المفتاح
            #القيمة باخدها من متغير يوزر المخزن ففيه القيم
            #بحلقة فور في نفس القوس وبدمجمهم مع بعض في حلقة تكرار واحدة ب zip 
                result=[dict(zip(keys,values)) for 
                values in users]
            
            #==== العملية الحسابية للنجاح والرسوب
                for x in result:
                    m=x["math"]
                    a=x["Arabic"]
                    #e=x["English"]
                    f=x["french"]
                    d=x["draw"]
                    c=x["chemstry"]
                    res=m+a+f+d+c
                    if res not in range(50,301) :

                        a=Text("Faild",color="white")
                    else :


                        page.add(

                         AppBar(
                          title=Text("back"),
                          color="white",
                          bgcolor=Colors.PINK,

                            ElevatedButton("back", on_click=lambda _: main(page))  # زر يعود لشاشة الرئيسية
                             
                          
                   ),
                    Card(
                    color="black",
                    content=Container(
                        content=Column([
                        ListTile(
                        leading=Icon(icons.PERSON),
                        title=Text("Name:"+
                        x["name"],#الاسم اللي ف x
                        color="green"),
                        subtitle=Text("Email:"+
                        x["email"],#المخزن في x
                        color="green")
                        ),
                        
                        #صف للهاتف والعنوان
                        Row([
                        Text("Phone"+x["phone"],
                        color="green"),
                        Text("Address"+x["address"],
                        color="green")
                        ], alignment=MainAxisAlignment.CENTER),
                        
                         #صفوف المواد كل ٣ في صف
                         #حولت الحقل ليترينج عشان
                         #اعمل ربط+ من النص اللي قبله
                        Row([
                            Text("Math" +
                            str(x["math"]),
                            color="green"),
                            
                            Text("Arabic"+
                            str(x["Arabic"]),
                            color="green")
                            #,
                            #Text("english"+
                            #str(x["English"]),
                            #color="green") 
                             #
                              ],alignment=MainAxisAlignment.END),
                        #ال٣ الاخرين
                        Row([
                            Text("French"+
                            str(x["french"]),
                            color="green"),
                            
                            Text("Draw"+
                            str(x["draw"]),
                            color="green"),
                            
                           Text("Chemstry"+
                            str(x["chemstry"]),
                            color="green") ],alignment=MainAxisAlignment.END),
                        
                         #صف للنتجية
                        Row([
                        a 
                        ],alignment=MainAxisAlignment.CENTER)
                        
                        ])
                        ,
                        #التحكم في بادنج ومرجن الكونت
                    padding=padding.all(10),
                    margin=margin.all(10)
                    
                    #التحكم أكثر 
                    #padding=padding.only(left=5)
                    #margin=margin.only(top=5)
                    #ممكن جعل البادنجووالمارجن ع ال x y
                    #padding=padding.symetric(horizontal =10, vertical=5)
                    )




                )
                
        )
                
     #
        page.update()
    #=============routes=================
    def route_change(route):
        #page.views.clear()
        if page.route=="/articls":
           page.bgcolor="#2E5077",
           page.views.append(
            View(
                "/articls",
               
                [
                  
                    AppBar(  #بيظهر فيه سهم الرجوع
                       title=Text("back"),
                       color="white",
                       bgcolor=colors.PINK
                      ),
               
                    Row([
                    Text("Welcome to Articls Page",
                    bgcolor="#09122C",color="white"),
                    Text("Read The Articls and Fun",
                    bgcolor="#09122C",color="white")
                    ],alignment=MainAxisAlignment.
                    CENTER),

                    Row([
                        Card(
                           color="#3D3D3D",
                           content=Container(
                               content=Column([
                                   Text("First Articl",color="white"),
                                   Text("Sports play a crucial role in promoting physical and mental well-being. Engaging in regular physical activity helps improve cardiovascular health, build strong muscles, and enhance flexibility. Sports also contribute to weight management by burning calories and boosting metabolism. Beyond physical benefits, sports have a positive impact on mental health. They can reduce stress, anxiety, and depression by releasing endorphins, the body's natural mood boosters.", color="white")
                               ])
                           )

                        )


                    ],alignment=MainAxisAlignment.CENTER),

                    Row([
                        Card(
                           color="#3D3D3D",

                            content=Column([
                                Text("second articles",color="white"),
                                Text("Nutrition plays a vital role in maintaining overall health and well-being. A balanced diet, rich in fruits, vegetables, whole grains, and lean proteins, provides the essential nutrients the body needs to function properly. Proper nutrition supports the immune system, boosts energy levels, and promotes healthy growth and development",color="white")                                    ])
                                                                                           )
                            ]),


                
                ]
            )
        )
        ##صفخة معلومات ثقافية وحكم وامثال عامة 
        if page.route == "/culture":
            page.bgcolor="lightblue"
            page.views.append(
                View(
                "/culture",
                [
                    AppBar(
                           title=Text("back"),
                           color="white",
                           bgcolor=colors.PINK
                    ),
                          
                    Text("WELCOME TO CULTURE PAGE",
                    color="red"
                    ),
                    #كروت فيها المعلومات
                    Row([
                    Card(
                     #scroll="auto",
                     color="black",
                     content=Container(
                      content=Column([
                        Text("one info",color="white"),
                        Text("did you know that month of February is 28 day",color="white")
                    ])
                    
                    )
                  
                    ),
                    
                    Card(
                      color="black",

                      content=Container(
                       
                        content=Column([
                        Text("one info",color="white"),
                        Text("did you Know that Badrekbis a Baird but can not flay",color="white")
                    ])
                    )
                   
                    )
                    
                    ],alignment=MainAxisAlignment.CENTER),

                    # الصفةالثاني وبه عدد ٢ كارد كالستبق
                    

                ]
                )
            )
#==============settings page====================
        if page.route == "/settings":
            page.bgcolor="yellow",
            page.views.append(
                View(
                "/settings",
                [
                 
                          



                    AppBar(
                           title=Text("back"),
                           color="white",
                           bgcolor=colors.PINK
                    ),
                
                   Row([
                    Text("WELCOME TO settings PAGE",
                    bgcolor=colors.PURPLE,color="white"),
                   ],alignment=MainAxisAlignment.CENTER),
                   
                   switch,
                
                 Card(
                     content=Container(
                         content=Column([
                             Text("about appp"),
                             Text("This app About management the students and teachers how you can recording the students and show too ect ect")

                         ])
                     )
                 )

                



                ]
                )
            )
        page.update()
 #================end settings page===============
    def come_back(view):
       page.views.pop()#احذف الصفحة الحالية بعد ر
       back_page=page.views[-1]#وانت راجع نقص 1
       page.go(back_page.route)
        
    page.on_route_change=route_change
    page.on_view_pop=come_back
    page.go(page.route)
    #=============end routes=============
    
    #======TextField personal data=========
    name=TextField (label="name student",icon=icons.
    PERSON,height=38)
    email=TextField(label="email student",
    icon=icons.MAIL,height=38)
    phone=TextField(label="phon student",icon=icons.
    PHONE,height=38)
    address=TextField (label="adress student",
    icon=icons.LOCATION_CITY,height=38)
 #======== end personal data Feildes=========   
    
    #=====Text=======
    markes=Text("marks stud",
    text_align="center", weight="bold",size=30)
    #====end text============
    
 #======= TextFeild mowad===========   
    Math=TextField(label="Math",width=110,
    height=38)
    Arabic=TextField(label="arabic",width=110,
    height=38)
    French=TextField(label="french",width=110,
    height=38)
    #English=TextField("english",width=110,
    #height=38)
    draw=TextField(label="draw",width=110,
    height=38)
    chemstry=TextField(label="chemstry",width=110,
    height=38)
    #======end TextField mowad======
    
    
     #======Buttons===========
    addbtn =ElevatedButton("add studend",width=170,
     style=ButtonStyle(
         bgcolor="blue",color="white",padding=15
     ),
     on_click=add)
     
    showbtn=ElevatedButton("show studend",width=170,
     style=ButtonStyle(
         bgcolor="blue",color="white",padding=15
     ),
     on_click=show)
    
    Articls=ElevatedButton("Articls",width=170,
     style=ButtonStyle(
      bgcolor="blue",color="white",padding=15


        ),on_click=lambda _:page.go("/articls"
       ))
    
    #زر صفحة الثقافية
    culture=ElevatedButton("culture",
         width=170,
         style=ButtonStyle(bgcolor="blue",
            color="white",padding=15),
             on_click=lambda _:page.go("/culture"))
     #======end buttons======
    #===تغيير خلفية التطبيق ========
    def dark_mode(e):
        if switch.value == True :
            page.theme_mode = ThemeMode.DARK
        else:
            page.theme_mode = ThemeMode.LIGHT
        page.update()
        
    switch=Switch(label="dark mode", 
    value=False,on_change=dark_mode)

    #==========DropDown===========
    def choice_color(e):
        selected_color=color_dropdown.value
        if selected_color == "Dark" :
            page.bgcolor="black"
        elif selected_color == "red" :
            page.bgcolor="red"
        elif selected_color == "green" :
            page.bgcolor="green"
        elif selected_color == "yellow" :
            page.bgcolor="yellow"    
        elif selected_color =="white":
            page.bgcolor="white"

        page.update()
           
    color_dropdown=Dropdown(
            width=200,
            options=[
                dropdown.Option("Dark"),
                dropdown.Option("red"),
                dropdown.Option("green"),
                dropdown.Option("yellow"),
                dropdown.Option("white")

            ]
        )
        
    Submit_btn=ElevatedButton("submit",
    on_click=choice_color)
    choice=Text("choice color",color=colors.BLUE)
    
    page.add(color_dropdown,Submit_btn,choice)

   


    page.adaptive=True
    page.add(
        switch,
        #=========AppBar=============
         AppBar(
             bgcolor=colors.RED,
             title=Text("student app"),
             center_title=True,
             leading=Icon(icons.HOME),
             leading_width=40,
             
              actions=[
            IconButton(icons.NOTIFICATIONS),#جرس يمي

             #زر الاعدادات 
                IconButton(icons.SETTINGS,
                on_click=lambda _:page.go("/settings"))

               ] 
           ),
        #=========end AppBar=========
         Row([
             Image(src=os.path.abspath("Img.jpeg")
, width=280)
         ],alignment=MainAxisAlignment.CENTER),
         
        Row([
             SafeArea(Text('wkcome app Student and Teacher',
             size=20,color="black"))
         ],alignment=MainAxisAlignment.CENTER),
         
        Row([
             Text("number of studen enroll",size=20,
             color="black",
             font_family="IBM Plex Sans Arabic"),

             Text(row_count,size=20,color="black",
             font_family="IBM Plex Sans Arabic")
         ],alignment=MainAxisAlignment.CENTER),
         
        #=====إضافة حقول البيانات الشخصية ==========
        name, email,phone,address,
        #======نص علامات الطالب=========
        Row([
            markes
        ],alignment=MainAxisAlignment.CENTER),
    #======اول ثلاث حقول جنب بعض =======
       Row([
             Math,Arabic,French
         ],alignment=MainAxisAlignment.CENTER),
         
   #====== الثلاثة الالي بعدهم تحتهم جنب بعض=========
      Row([
             #English,
             draw,chemstry
         ],alignment=MainAxisAlignment.CENTER),
         
     #==== إضافة للزرارين في صف جنب بعض =======
     Row([
             addbtn, showbtn
         ],alignment=MainAxisAlignment.CENTER),

     Row([
           Articls,culture
          ],alignment=MainAxisAlignment.CENTER)
    


     #Row([
         #ElevatedButton("طلب إذن الكاميرا", bgcolor="black",color="white",on_click=request_camera_permission)
     #] ,alignment=MainAxisAlignment.CENTER),
     
     )
    
    #========التنبيه قبل إغلاق البرنامج من زر x قد يعمل اكثر مع عند جعل التطبيق يفتح علي سطح المكتب فقط بعمل target=main =======
    
    def when_press_close(e):
        if e.data == "close": #لو ضغط علي x غلق
            page.open(confirm_dialog)#اظهر التنبيه
            
        #تفعيل خاصية منع الإغلاق المباشر أو حتي اغلاق أو
        #اخفتء نافذة التنبيه عند النقر في أي مكان اخر
    page.window.prevent_close=True
        #استدعاء دالة فتح التنبيه عند سماع حدث الغلق 
        #نفذ الدالة بتاعة اظهار التنبيه الاول     
    page.window.on_event=when_press_close
    
    #دالة عند الضغط نعم بترجع اغلاق البرنامج تحطيم
    def yes_click(e):
        page.window.destroy()
   #دالة لا لا ليغلق نافذة التنبيه ويفضل البرنامج مفتوح
    def no_click(e):
        page.colse(confirm_dialog)
        
    #كلاس أو خاصية التنبيه جزاها مودال يعني تفعيلها 
    #وبتاخد عنوان واكشنز ازرار الاختيار
    confirm_dialog=AlertDialog(
        modal=True,
        title=Text("please confirm"),
        content=Text("Do you really want to exit"),
        actions=[
            ElevatedButton("yes",
            on_click=yes_click),
            OutlinedButton("no",on_click=no_click)
        ],
        alignment=MainAxisAlignment.END
    )
    #======================================
    
    
    page.update()
    
app(target=main,view=AppView.WEB_BROWSER) 