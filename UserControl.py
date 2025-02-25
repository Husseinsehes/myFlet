








#=======UserControl in flet==========
#تجميع مجموعة عناصر وبيانات مستخدم أو مجموعة ازرار أو عناصر بشكل عمودي لتسهيل التعامل معه وإعادة استخدامه أو صيانته يعني مجموعة من ال widgets عناصر واجهة المستخدم تعرضها بشكل مرتب وسهل  وهو عبارة عن كلاس بتعمل لها إرث لمستخدمه 
#يعني كانك بتعمل واجهة مستخدم مخصصة داخل الواجهة الأساسية بها مجموعة بيانات أو عناصر ازرار أو نص ص وغيره كا كارت تعرضهم لوحدهم سواء في شكل عمودي أو Row 
from flet import *

#def choice(e):
    #page.window.bgcolor=color_dropdown.value # type: ignore
    #page.update()
def main (page:Page):
    page.theme_mode=ThemeMode.DARK
    
    class Info(UserControl):
        def __init__(self,name,address,progress):
            super().__init__()
            self.name=name
            self.address=address
            self.progress=progress
            
       #دالة بلد غالبا اسمها كده بتبني العناصر في عمود وترجع العنصر أو المتغير اللي بيحفظهم وهي اللي بتعمل واجهة المستخدم المخصصة بةUserControl 
        def build(self):
            widget=Column(controls=[
            Text(self.name),Text(self.address),
            ProgressBar(color="green",
            bgcolor="white",tooltip="your progress",value=self.progress)
            ])
            return widget
    info=Info(name="Ali", address="Egypt",
    progress=0.3)
    
    page.add(info)
    def choice(e):
        selected_color=color_dropdown.value
        if selected_color == "Dark":
            page.bgcolor = "black"
        elif selected_color == "red":
            page.bgcolor = "red"
        elif selected_color == "green":
            page.bgcolor = "green"
        elif selected_color == "yellow":
            page.bgcolor = "yellow"
        page.update()
        
    color_dropdown=Dropdown(
        width=100,
        options=[
            dropdown.Option("red"),
            dropdown.Option("Dark"),
            dropdown.Option("yellow"),
            dropdown.Option("green")
        ]
    )
    submit=ElevatedButton("submit",on_click=choice)
    choiceing=Text("choice a color",color="white")
    page.add(color_dropdown,submit,choiceing)

    page.update()
    
app(target=main,view=AppView.WEB_BROWSER)
      