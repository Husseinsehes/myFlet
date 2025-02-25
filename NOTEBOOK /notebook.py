










from flet import *

#كلاس النوت بزك فيه كل الدواا واتيراد كلا ال UserControl 
#وعمل حقل ادخال متعدد الاسطر ليستطيع المستخدم ادخال العديد من الاسطر وتمرير دالة الانشاء والحفظ في on_change لحفظ كل تغيير يتم تلقاييا
class TextEditor(UserControl):
    def __init__(self):
        super() .__init__()
        self.textfield=TextField(
         multiline=True,autofocus=True,
         on_change=self.save_text,content_padding=50,
         cursor_color="blue",border=InputBorder.NONE,
         min_lines=40

        )
    ## دالة انشاء وحفظ الملف النصي واخذ قيمته من حقل الادخال
    def save_text(self,e):
        with open("save txt","w") as file:
            file.write(self.textfield.value)
    # قراءة الملف يعني عندما يفتح المستخدم البرنامج يجد ماتم تدوينه موجود وما تم تغييره
    def text_read(self):
        try:
            with open ("save txt","r") as f:
                return f.read()
        except FileNotFoundError:
            self.textfield.hint_text="welcome to the Text Editor"
# دالة اظهار النصوص بجعل فيمة حقل الادخال هي التي تتم قراتها في الدالة text_read عشان ملاء الحقل وتستطع القراءة والتعديل ورجعلي حقل الادخال بعد كده
    def build(self):
        self.textfield.value=self.text_read()
        return self.textfield


#تشغيل الدالة الريسية لاظهار طل ماسبق اي الكلاس 
def main(page:Page):
    #===تغيير خلفية التطبيق ========
    #تم استخدام page.them_mode بدل ال bgcolor 
    def dark_mode(e):
        if switch.value == True :
            page.theme_mode = ThemeMode.DARK
        else:
            page.theme_mode = ThemeMode.LIGHT

        page.update()
    switch=Switch(label="dark mode", 
    value=False,on_change=dark_mode)

    def SAVE(e):
        alert=AlertDialog(
            title=Text("saved",color="green")
        )
        page.overlay.append(alert)
        alert.open=True
        page.update()

#نص ترحيبي واضافته داخل كونتينر لاستطيع اعمل بوردر راديوس عليه لانها لاتعمل مع النص مباشرة تطبق فقط علي الحاويات والكروت 
    
    text=Text("Welcome to Amazing NotBook",font_family="Arial",weight=FontWeight.BOLD,size=30,italic=True,color=colors.WHITE)

    container=Container(
        content=text,
        border_radius=20,padding=20,
        bgcolor=colors.INDIGO,
        alignment=alignment.center
    )

    btn=ElevatedButton ("Save",bgcolor=colors.BLUE_400,color=colors.WHITE,on_click=SAVE)
    
    page.add(switch,container,Divider(),btn)
    page.update()

  #استدعاء كلاس الTextEditor() هنا لاظهار كل ماسبق في الصفحة
    page.add(TextEditor())







    page.update()

app(target=main,view=AppView.WEB_BROWSER)