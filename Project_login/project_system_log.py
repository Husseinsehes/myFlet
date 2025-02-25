from flet import *
import os
def main(page: Page):
    page.title = Text("Images TextField")
    page.window.width = 390
    page.window.height = 740
    page.window.top = 1
    page.window.left = 960
    page.bgcolor =colors.BLACK
    page.vertical_alignment = "center"  # توسيط عمودي
    page.horizontal_alignment = "center"  # توسيط الكل أفقي

    # ===================================
    # القسم العلوي النافبار العلوي appBar
    page.appbar = AppBar(
        bgcolor=colors.RED,
        title=Text("above app"),
        center_title=True,
        leading=Icon(icons.HOME),
        leading_width=40,
        # زر الجرس والثلاث نقاط فوق بعض
        actions=[
            IconButton(icons.NOTIFICATIONS),  # زر الجرس
            PopupMenuButton(  # ٣ نقط عند النقر يظهر هذا
                items=[
                    PopupMenuItem(text="profile"),
                    PopupMenuItem(text="settings"),
                    PopupMenuItem(text="about us"),
                    PopupMenuItem(),  # خط
                    PopupMenuItem(text="Exit")
                ]
            )
        ]
    )
    
    # ===================================
    # دالة التحقق من تسجيل الدخول
    def show(e):  # لازم تمرر لها بارامتر ولو مالوش وظيفة
        Ent1 = email.value
        Ent2 = password.value
        
        if Ent1 == "h" and Ent2 == "9":
            alert1 = AlertDialog(
                title=Text("Welcome admin", color="green")
            )
            # إضافة الإشعار للصفحة
            page.overlay.append(alert1)
            alert1.open = True  # القدرة على فتح الإشعار
            page.update()
        else:
            alert1 = AlertDialog(
                title=Text("Invalid", color="red")
            )
            # إضافة الإشعار للصفحة
            page.overlay.append(alert1)
            alert1.open = True  # القدرة على فتح الإشعار
            page.update()
    
    # ===================================
    # الجزء الأوسط الصورة وتسجيل الدخول
    #IMage=Image(src="https://www.alamy.com/stock-photo-login-icon-122161261.html?imageid=90FDBCF0-EBBD-447E-B4E0-AB24F75D4774&p=353194&pn=1&searchId=e4bfc132d17c373cf3c8c138819368a0&searchtype=0",
    #width=150)

    img = Image(src="Project_login/login.png", width=170)
    #img_path = os.path.join(os.getcwd(), "login.png")  # المسار المطلق بناءً على الدليل الحالي
    #mypath = Image(src=img_path,width=150)
    #print(f"the image path{os.path.abspath("login.png")}")

    text = Text("Login System", color="white", size=25)
    email = TextField(label="Email", icon=icons.EMAIL,color="white")
    password = TextField(label="Password", color="white",icon=icons.PASSWORD, password=True, can_reveal_password=True)
    btn = ElevatedButton("Login", on_click=show)
    
    # ===================================
    page.add(img, text, email, password, btn)
    #print(f"the image path{os.path.abspath("login.png")}")
    

    # ===================================
    # الجزء السفلي النافبار
    page.navigation_bar = CupertinoNavigationBar(
        bgcolor=colors.RED,
        inactive_color=colors.BLACK,  # تغيير اللون عند النقر
        destinations=[
            NavigationBarDestination(icon=icons.CALL, label="Call"),  # علامة الاتصال وكلمة اتصال تحتها
            NavigationBarDestination(icon=icons.CAMERA, label="Camera"),  # أيقونة الكاميرا
            NavigationBarDestination(icon=icons.CONTACT_PHONE, label="Contact Phone")
        ]
    )
    
    page.update()

app(main)