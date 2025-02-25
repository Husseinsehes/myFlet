












#pyinstaller --onefile --windowed flash.py


#=============== Flashlight app ==================
#ملحوظة طوال الفلاش اللي جربتها والبرمشن بتشتغل علي الاندرويد وليس ع الحاسوب لذلك لازم تحول الملف الي apk مثلا عشان تشتغل ع الحاسوب

from flet import *

def main (page:Page):
    page.title ="flashlight"
    page.window.width=390
    page.window.height=740
    page.window.top=1
    page.window.left=960      
    #page.theme_mode=ThemeMode.LIGHT
    
    #كاين من كلاس FlasLightلايشترط استيراده فقط تنزي
    flashlight=Flashlight()
    page.overlay.append(flashlight)
    
    
    #كاين من كلاس الأذونات الذي سنضعه في الضبط مع فنك
    #لنمررها لايقنة الضبط عند الضغط تظهر الاعدادات والاذونا
    ph=PermissionHandler()
    page.overlay.append(ph)#لطبقة أو عطاء يظهر فوق التطبيقات الحق للصفحة هذا الكائن عند التفاعل معه يظهر في الصفحة أو السماح له بالظهور فوق التطبيقات ليعمل
    
    def open_setting(e):
        ph.open_app_settings()
        #يا كائن الأذونات خش علي دالة فتح اعدادات التطبي
        
    
    
    
    #الاضافة المباشرة في add 
    page.add(
    #===============appbar==============
    AppBar(
        title=Text("FlasLight HA"),
        bgcolor=colors.PURPLE,color=colors.WHITE,
        #التفاعل أو الأحداث#ايقونه الضبط ع اليمين 
        actions=[
        IconButton(icons.SETTINGS,
        on_click=open_setting)
        ]
    ),
    #======text=======
    Row([
        Text("welcome to flashlight app",
        size=31,color=colors.BLACK)
    ],alignment=MainAxisAlignment.CENTER),
    
    #====== Image==========
    Row([
        Image(src="/workspaces/myFlet/Flashlight_project/assets/unnamed.png",width=360),       
    ],alignment=MainAxisAlignment.CENTER),
    
    #======Buttons===========
    Row([
        ElevatedButton("on",width=100,
        icon=icons.PLAY_ARROW,
        style=ButtonStyle(
            bgcolor=colors.PURPLE,
            color=colors.WHITE,
            padding=15,
            shape=ContinuousRectangleBorder(radius=100),
            
        ),
        on_click=lambda _:flashlight.turn_on()
        ),
        
        ElevatedButton("off",width=100,
        icon=icons.PLAY_DISABLED_SHARP,
        style=ButtonStyle(
            bgcolor=colors.PURPLE,
            color=colors.WHITE,
            padding=15,
            shape=ContinuousRectangleBorder(radius=100),
            
        ),
        on_click=lambda _:flashlight.turn_off()
        )
        
    ],alignment=MainAxisAlignment.CENTER),
    
    #======== last text ===========
    Row([
    Text("\n\n by HA 2025",size=15,
    color=colors.BLACK)
    ],alignment=MainAxisAlignment.CENTER)
    
    )
    
    page.update()
app(main)
