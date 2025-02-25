





#=========مشروع واجهة تسجيل دخول وانشاء صفحات ======

#home rout "/"
#logig route "/login"
#signup rout "/signup"
#back دالة الرجوع للخلف

#كلهم داخل دالة الmain والصفحات داخل دالة اخري خاصة بالتنقل بين الصفحات واول صفحة الهجوم غالبا بتكون بدون شرط تحقق وباقي الصفحات لازم تكون بشرط تحقق وطرق عمل الصفحة 
#def name of func(rout):
#    page.views.clear()
#    page.views.append(
#        View(
#            "/",
#            [
#            #العناصر هنا النصوص ولازرار والصفوف وغيره
#            ],
#        )
#    )
# #صفحة أخري
#    if page == "/login":
#        page.views.append(
#        View(
#            "/",
#            [
#            #العناصر هنا النصوص ولازرار والصفوف وغيره
#            ],
#        )
#    )

#ولو هعتمل صف مثلا هتعمله كده 
#Row([

#],alignment=MainAxisAlignment CENTRE), هذه الخاصية تقوم بمحاذاة العناصر رأسيا يعني أما تجيب العناصر بالوسط رأسيا من فوق ومن أسفل تجيبهم بالنص أو تخليهم من فوق اعلي الشاشة أو أسفل الشاشة كلهم أو تخلي بينهم مساحات فراغ رأسية متساوية وبتاخد start of end or center or space between or space evenly 

#CrossAlignment نفس الخصائص السابقة لكن دي تقوم بالمحاذاة الأفقية للمكونات أو العناصر أما تخليهم كلهم ع اليسار البداية أو في نهاية المحور الافقي أو في نص المحور الافقي الخ 

#.go("/login")#دالة الذهاب للصفحة

#in_click=... يعني ماتعملش خطأ وانا بطور عشان التطبيق مايقفش وانا ببرمج  
#========================================





from flet import *
import os
def main(page: Page):
    #محلوظة .الابعاد دي والتحكم في الشاشة دي لأغراض التطوير فقط لكن اقدر استغني عنها لانه المكتبة بتعمل تجاوب تلقائي مع مختلف الشاشات  ويفضل استخدام ال Row ووضع العناصر فيه إذا كانت صور أو ازرار أو نصوص عشان يعمل تجاوب افضل 
    page.title = "project app"
    page.window.width=390
    page.window.height=740
    page.window.top=1
    page.window.left=960    
    page.theme_mode=ThemeMode.LIGHT
#لعمل صفحات التطبيق يجب عمل دالة اوضع فيها المسارات 
 #اول صفحة الهوم من غيرif والباقي لازم اعمل if 
    def route_change(route):
        page.views.clear()#ا
 #========= home page ===========
     #في الصفحة قم بعروضات المعروضات التي تلحق لك 
        page.views.append(
            #العرض الاول ومابه من عناصر 
            View(
                "/",
                #====عمل ناف بار علوي=======
                [
                    AppBar(#بيظهر فيه سهم الرجوع
                        title=Text("Flet app"), 
                        bgcolor=Colors.PINK,
                        color="white"),

                    Text("Welcome ....."), 
                    #صف فيه الصورة والنص وبه []
                    Row([
                     Image(src="/workspaces/myFlet/src/Route/budget.png",
                       width=270)
                    ],alignment=MainAxisAlignment.CENTER),
                     #صف للزرارين
                    Row( [ 
                    ElevatedButton("login", bgcolor=colors.PURPLE,color=colors.WHITE, width=150, on_click=lambda _: page.go("/login")),
                    ElevatedButton("signup",bgcolor=colors.PURPLE,color=colors.WHITE, width=150,on_click=lambda _: page.go("/signup")),          
#محاذا العناصر في الوسط علي المحور الرئيسي الراسي من اعلي لاس
                    ],alignment= MainAxisAlignment.CENTER),
                ],
            )
        )
        #========= end home page =======        
                    
                        
                            
        #========= login page ===========
        if page.route == "/login":
            page.views.append(
                View(
                  "/login",
                 [
               AppBar(  #بيظهر فيه سهم الرجوع
               title=Text("back"),
               color=colors.WHITE,
               bgcolor=colors.PINK),

               Text("Welcome to login page"),
               TextField(label="Email write h@yahoo.com"),
               TextField(label="password write 1234"),
               
               Row([ 
               ElevatedButton("login",
               width=150,
               style=ButtonStyle(bgcolor=colors.PURPLE,
               color=colors.WHITE)),
               
               ElevatedButton("new count",
               width=150,
               style=ButtonStyle(bgcolor=colors.PURPLE,
               color="white"),
               on_click=lambda _:page.go("/signup")
               ),
             
              ],alignment=MainAxisAlignment.CENTER),
             
             ],
            )
           )
            

   #========= end login page =======
       
         #====== page advices about sporting and health====
 
      
          
            
           
          
              
            
             
            
             
              
                         
             
             
             
           
       
        

         
                



 
        

          
             
            

         
             

             
            
             
           
          
             
              
            

             
              
            
             
            




            

            
         
         
            
             
             
             
           
               
               

             



             
           
              
            
        
          
         

      
             
            
 #======= end page advices ==================  
               
   #====== create acount page =====

             
            
        if page.route == "/signup":
            page.views.append(
            View(
            "/signup",
            [
            AppBar(  #بيظهر فيه سهم الرجوع
               title=Text("back"),
               color="white",
               bgcolor=colors.PINK
               ),
               
            Text("Create a new acount",size=15,
               color="black",width=470,
               text_align="center"),
               #===================={{{=
            TextField(label="Full name"),
            TextField(label="Email"),
            TextField(label="password"),
            TextField(label="confirm password"),
               
            Row([
               ElevatedButton("create",
               style=ButtonStyle(bgcolor=colors.PURPLE,
               color=colors.WHITE),width=150),
                         
               ElevatedButton("you have aco",
               width=150,         
               style=ButtonStyle(bgcolor=colors.PURPLE,
               color=colors.WHITE),
               on_click=lambda _:page.go("/login")
               ),
                
              ],alignment=MainAxisAlignment.CENTER),
            ],
           )
        )
        
          
       
        page.update()# وضع تحديث الصفحة بعد نهاية ع
                #عمل الصفحات عشان يظهرون عند التشغيل ولا توض
                        #ع في نهاية التطبيق لانه هتشغل خصائص التطبيق وإبعاده فقط وتسيب الصفحات الرواس وعناصرها
                                
 #======== def back page ========
    def view_pop(view):
        page.views.pop()#احذف الصفحة الحالية بعد رجو
        top_view = page.views[-1]#وانت راجع نقص 1
        page.go(top_view.route)#وروح للمسار اللي
                #اتحدد عند عمل رجوع اي الصفحة اللي جات بعدها

#===== استدعاء الدالتين السابقتين =≠========
  
      #on_route_chane
         #تفعيل حدث تغيير الصفحات في الصفحة لما تتغير المسارات في الصفحة عند تشغيل دالة الصفحات 
    page.on_route_change = route_change
    #on_view_pop
        #حدث يتم تفعيله عند عمل رجوع وإزالة الصفحة الحالية اي  عند تشغيل دالة الرجوع
    page.on_view_pop = view_pop
    #page.route يعني روح للمسار الحالي اللي تم الوصول اليه بعد الرجوع أو عند تحميل التطبيق في النهاية 
    page.go(page.route)
#====== end def back page ======

app(target=main,view=AppView.WEB_BROWSER)