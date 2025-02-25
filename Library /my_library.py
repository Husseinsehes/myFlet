










       #==========library app ==============
       

from flet import *
import sqlite3 
import os
#========== create db ==========
con = sqlite3.connect("Data.db",check_same_thread=False)#
cursor=con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS  library(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name Text,author Text,nationality Text,date Text
)""")
#========== end db ==============


#====== main def ===============
def main (page:Page):
    page.title ="My Library"
    page.window.width=390
    page.window.height=740
    page.window.top=1
    page.window.left=960
    page.scroll="auto"
    page.theme_mode=ThemeMode.LIGHT
    #===تغيير خلفية التطبيق ========
    def dark_mode(e):

        if switch.value == True :
            page.theme_mode = ThemeMode.DARK   
        else:
            page.theme_mode = ThemeMode.LIGHT
        page.update()

    switch=Switch(label="dark mode", 
    value=False,on_change=dark_mode)
    #page.update()
  #===تغيير خلفية التطبيق ======== 
    #توجد أيضا خاصية لتكييف التطبيق مع مختلف الشاشات
    page.adaptive = True 
    #===================

    name=TextField(label="name book")
    author=TextField(label="author nam")
    nationality=TextField(label="Nationality")
    date=TextField(label="date book")

    delete_book=TextField(label="delete..")

     # حقل اختيار الكتاب للتعديل
    book_name_to_edit = TextField("Enter book name to edit")

      # حقل التعديل
    edit_name = TextField(label="Edit name book")
    edit_author = TextField(label="Edit author name")
    edit_nationality = TextField(label="Edit nationality")
    edit_date = TextField(label="Edit date book")

#عمل متغير يتم الحاق البيانات اليه بعد جلبها من قاعدة البيانات تمهيدا لعرض تلك البيانات مرة واحدة في للصفحة عند طلب عرضها باستخدام controls.append وليس page.add حتي يتم تحديث الصفحة مرة زليس علي دفعات عند استخدام الadd لانه مش هيعرض او يضيف البيانات كله دفعه واحدة في الصفحة مما يجعل التطبيق غير سلس وتقيل وبطئ تحديث الواجهة او الصفحة 
    books_container = Column()
    
    def add(e):
        cursor.execute("INSERT INTO library (name,author,nationality,date) VALUES(?,?,?,?)",(name.value,author.value,nationality.value,date.value))
        con.commit()

        # Clear the input fields after adding
        name.value = ""
        author.value = ""
        nationality.value = ""
        date.value = ""
        #page.snack_bar=SnackBar(
        #Text("Added Sucssfully",width=100,color=colors.GREEN)
        #)
        alert=AlertDialog(
            title=Text("added successfully",color=colors.GREEN)
        )
        page.overlay.append(alert)
        alert.open=True
        page.update()


    def show(e):
        books_container.clean()
        display=con.cursor()
        display.execute("SELECT * FROM library")
        books=display.fetchall()
      
        #print(books)
        if not books :
            books_container.controls.append(Text("No books found.", color="red"))

        else:
         for book in books:
            page.add(
               books_container.controls.append(
                Card(
                color="#213555",
                    content=Container(
                       content=Row([
                         Text(f"Book :{book[1]} ,Author {book[2]}, Nationality :{book[3]} ,Date : {book[4]}",color="white",size=18,italic=True,width=300)

                  
                ],alignment=MainAxisAlignment.CENTER)
            )
            )
            )
            )
        page.update()


    def Delete(e):
        Val=delete_book.value.strip()
        if Val =="":
            page.add(Text("please put a book name",
            color="red"))
            page.update()
            return 
        cursor.execute("SELECT * FROM library WHERE name =?",(Val,) )
   
        Book=cursor.fetchone()#واحد بس
        if Book is None:#لو مش موجود
             page.add(Text(f"no name like this{Val}",color="red")
               ) 
             page.update()
             return
               

        cursor.execute("DELETE FROM library WHERE name = ?", (Val,))
        con.commit()
        delete_book.value=""
      
        alert=AlertDialog(title=Text("deleted Sucssfully",color=colors.GREEN))
        page.overlay.append(alert)
        alert.open=True
        page.update()



        show(None) #عرض الكتب من جديد

    #============== update ==============
    def update(e):
        Val =book_name_to_edit.value.strip()
        if Val == "":
            page.add(Text("Please provide a book name to edit", color="red"))
            page.update()
            return
        
        cursor.execute("SELECT * FROM library WHERE name = ?", (Val,))
        book = cursor.fetchone()
        
        if book is None:
            page.add(Text(f"No book found with the name {Val}", color="red"))
            page.update()
            return
     
        # إذا كان الكتاب موجودًا، نقوم بتعبئة الحقول بالبيانات القديمة
        edit_name.value = book[1]
        edit_author.value = book[2]
        edit_nationality.value = book[3]
        edit_date.value = book[4]

        page.update()

    # تنفيذ التعديل
    def Add(e):
        Val =book_name_to_edit.value.strip()

        cursor.execute("""
            UPDATE library 
            SET name = ?, author = ?, nationality = ?, date = ? 
            WHERE name = ?
        """, (edit_name.value, edit_author.value, edit_nationality.value, edit_date.value,Val))
        
        con.commit()
        edit_name.value=""
        edit_author.value=""
        edit_nationality.value=""
        edit_date.value=""
        
        alert=AlertDialog(title=Text("Updated Sucssfully",color=colors.GREEN))
        page.overlay.append(alert)
        alert.open=True

        page.update()

    #============== end update ============
        
    def route_change(route):
        page.views.clear()
        page.views.append(
        #=======home page ======
            View(
               "/",
               [
               

               AppBar(  
               title=Text("Home"),
               color="white",
               bgcolor=colors.RED
               ),
               
                Text(" Welcome To The Library ..",
                bgcolor="#001A6E",color="white",size=30,font_family="Arail",weight=FontWeight.BOLD,italic=True
                ),

            switch,
                Row([
                 Image(src="/workspaces/myFlet/Library/book.jpeg",width=580)
                ],alignment=MainAxisAlignment.
                  CENTER),


                Row([
                ElevatedButton("go to add",
                bgcolor=colors.PURPLE,color="white",
                width=150,#عند الضغط روح لصفحة الدخو
                on_click=lambda _:page.go("/add")
                ),

                 ElevatedButton("go update", 
                    bgcolor=colors.PURPLE,
                    color="white",width=150,
                    on_click=lambda _: page.go("/update")),      
               ],alignment=MainAxisAlignment.
                CENTER)
                 
            ],
            
        )
     )                  

        #=====end home page =====
       

        #=======add page ======
        if page.route == "/add":
            page.views.append(
            
              View(
              "/add",
              [
               AppBar(  #بيظهر فيه سهم الرجوع
               title=Text("back"),
               color="white",
               bgcolor=colors.PINK
               ),
               Text("Welcome to add page",
                bgcolor="#001A6E",color="white",size=30,font_family="Arial",weight=FontWeight.BOLD,italic=True
                ),
                switch,

               
               Column([
                     name,author,nationality,date,Divider(),delete_book,
               Row([ 
               ElevatedButton("add", 
               width=150,
               style=ButtonStyle(bgcolor=colors.
               PURPLE,color=colors.WHITE),
               on_click=add),
               
               ElevatedButton("go to display",
               width=150,
               style=ButtonStyle(bgcolor=colors.
               PURPLE,color=colors.WHITE),
               on_click=lambda _:page.go("/display")
               ),

               ElevatedButton("delete",
                    width=150,        
                  style=ButtonStyle(bgcolor=colors.
              PURPLE,color=colors.WHITE),             
               on_click=Delete),
             
              ],alignment=MainAxisAlignment.CENTER)
              ])
             ],
             )
            )
        
        #=====end add page =====

        #=======show page ======
        if page.route == "/display":
         
            page.views.append(
            
              View(
              "/display",
              [
               AppBar(  #بيظهر فيه سهم الرجوع
               title=Text("back"),
               color="white",
               bgcolor=colors.PINK
               ),



               Text("Welcome to display page",
                bgcolor="#001A6E",color="white",size=30,font_family="Arial",weight=FontWeight.BOLD,italic=True),
               
               switch,


               Row([
                   ElevatedButton("Show",bgcolor="blue",
                   color="white",on_click=show),
                   
               ],alignment=MainAxisAlignment.CENTER),
               Divider(),#عمل خط فاصل بين البياناات 
               books_container#استدعاء حافظ الكتب لاظهارهم هنا والذي تم الحاقهم به بعد جلبهم من قاعدة البيانات 
             ],
             )
            )
          
         #=====end show page =====  
        if page.route == "/update":
            page.views.append(
                View(
                    "/update",
                    [
                        AppBar(title=Text("back"), 
                        color="white", 
                        bgcolor=colors.PINK),
                   Text("Welcome to the update page",
                        bgcolor="#001A6E", 
                        color="white",size=30,font_family="Arial",weight=FontWeight.NORMAL,italic=True),

                        switch, 

                        
                        Column([
                            book_name_to_edit,
                            Divider(),
                            edit_name,
                            edit_author,
                            edit_nationality,
                            edit_date,
                
                            Row([
                               ElevatedButton("Old data", width=150, style=ButtonStyle(bgcolor=colors.PURPLE, color=colors.WHITE), on_click=update),

                               ElevatedButton("Add", width=150, style=ButtonStyle(bgcolor=colors.PURPLE, color=colors.WHITE), on_click=Add),
 ], alignment=MainAxisAlignment.CENTER),
                        ]),
                    ],
                )
            )

     
        page.update()




    def come_back(view):
       page.views.pop()#احذف الصفحة الحالية بعد ر
       back_page=page.views[-1]#وانت راجع نقص 1
       page.go(back_page.route)
        
    page.on_route_change=route_change
    page.on_view_pop=come_back
    page.go(page.route)

    page.update()
app(target=main,view=AppView.WEB_BROWSER)
