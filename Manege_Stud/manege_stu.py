#=========== إدارة شؤون الطلاب =============
#pip install 'flet[all]'
#تشغيل سطح المكتب 
#flet run myproj.py

# تشغيل كويب يعمل اي جهاز
# flet run --web myproj.py
from flet import *
from flet import AppView, run
import sqlite3
import os

# Linux,mac
#source myvenv/bin/ativate 
#pip install flet
#windows
#myvenv\Scripts\activate
#pip install flet 

#=========== DATABASE =======================
con = sqlite3.connect("data.db", check_same_thread=False)
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    math INTEGER,
    Arabic INTEGER,
    french INTEGER,
    draw INTEGER,
    chemstry INTEGER
)
""")
con.commit()


def main(page: Page):
    page.title = "Student Management"
    page.scroll = "auto"
    page.theme_mode = ThemeMode.LIGHT

    #=========== DARK MODE ===================
    def dark_mode(e):
        page.theme_mode = ThemeMode.DARK if switch.value else ThemeMode.LIGHT
        page.update()

    switch = Switch(label="Dark Mode", value=False, on_change=dark_mode)

    #=========== COUNT STUDENTS ==============
    cursor.execute("SELECT COUNT(*) FROM student")
    row_count = cursor.fetchone()[0]

    #=========== TEXTFIELDS ==================
    name = TextField(label="Student Name", icon=Icons.PERSON)
    email = TextField(label="Email", icon=Icons.MAIL)
    phone = TextField(label="Phone", icon=Icons.PHONE)
    address = TextField(label="Address", icon=Icons.LOCATION_CITY)

    Math = TextField(label="Math", width=110)
    Arabic = TextField(label="Arabic", width=110)
    French = TextField(label="French", width=110)
    draw = TextField(label="Draw", width=110)
    chemstry = TextField(label="Chemistry", width=110)

    #=========== ADD STUDENT =================
    def add(e):
        cursor.execute("""
        INSERT INTO student(name,email,phone,address,math,Arabic,french,draw,chemstry)
        VALUES(?,?,?,?,?,?,?,?,?)
        """, (
            name.value,
            email.value,
            phone.value,
            address.value,
            int(Math.value),
            int(Arabic.value),
            int(French.value),
            int(draw.value),
            int(chemstry.value)
        ))
        con.commit()

        dialog = AlertDialog(title=Text("Saved Successfully ✅", color="green"))
        page.overlay.append(dialog)
        dialog.open = True
        page.update()

    #=========== SHOW STUDENTS ===============
    def show(e):
        page.clean()

        cursor.execute("SELECT * FROM student")
        users = cursor.fetchall()

        page.add(
            AppBar(title=Text("Students"), bgcolor="pink", color="white")
        )

        if users:
            keys = ["id","name","email","phone","address","math","Arabic","french","draw","chemstry"]
            result = [dict(zip(keys, u)) for u in users]

            for x in result:
                total = x["math"] + x["Arabic"] + x["french"] + x["draw"] + x["chemstry"]
                status = Text("Passed", color="green") if total >= 250 else Text("Failed", color="red")

                page.add(
                    Card(
    
                        content=Container(
                            padding=10,
                            content=Column([
                                ListTile(
                                    leading=Icon(Icons.PERSON),
                                    title=Text(x["name"], color="green"),
                                    subtitle=Text(x["email"], color="green")
                                ),
                                Text(f"Phone: {x['phone']}", color="green"),
                                Text(f"Address: {x['address']}", color="green"),
                                Row([
                                    Text(f"Math: {x['math']}", color="green"),
                                    Text(f"Arabic: {x['Arabic']}", color="green"),
                                    Text(f"French: {x['french']}", color="green"),
                                ], alignment=MainAxisAlignment.SPACE_AROUND),
                                Row([
                                    Text(f"Draw: {x['draw']}", color="green"),
                                    Text(f"Chemistry: {x['chemstry']}", color="green"),
                                ], alignment=MainAxisAlignment.SPACE_AROUND),
                                status
                            ])
                        )
                    )
                )
        page.update()

    #=========== ROUTES ======================
    def route_change(route):
        page.views.clear()

        if page.route == "/articls":
            page.bgcolor = "#2E5077"
            page.views.append(
                View("/articls", [
                    AppBar(title=Text("Articles"), bgcolor="pink"),
                    Text("Welcome to Articles Page", color="white"),
                ])
            )

        elif page.route == "/culture":
            page.bgcolor = "lightblue"
            page.views.append(
                View("/culture", [
                    AppBar(title=Text("Culture"), bgcolor="pink"),
                    Text("Culture Page", color="red")
                ])
            )

        elif page.route == "/settings":
            page.bgcolor = "yellow"
            page.views.append(
                View("/settings", [
                    AppBar(title=Text("Settings"), bgcolor="pink"),
                    switch,
                    Text("About App"),
                    Text("Student management application")
                ])
            )

        page.update()

    page.on_route_change = route_change
    page.go("/")

    #=========== UI ==========================
    page.add(
        AppBar(
            title=Text("Student App"),
            center_title=True,
            bgcolor="red",
            actions=[
                IconButton(Icons.SETTINGS, on_click=lambda _: page.go("/settings"))
            ]
        ),
        Row([Text("Welcome to Student App", size=20)], alignment=MainAxisAlignment.CENTER),
        Row([Text("Total Students:"), Text(str(row_count))], alignment=MainAxisAlignment.CENTER),

        name, email, phone, address,

        Text("Marks", size=25, weight="bold"),
        Row([Math, Arabic, French], alignment=MainAxisAlignment.CENTER),
        Row([draw, chemstry], alignment=MainAxisAlignment.CENTER),

        Row([
            ElevatedButton("Add Student", on_click=add),
            ElevatedButton("Show Students", on_click=show)
        ], alignment=MainAxisAlignment.CENTER),

        Row([
            ElevatedButton("Articles", on_click=lambda _: page.go("/articls")),
            ElevatedButton("Culture", on_click=lambda _: page.go("/culture"))
        ], alignment=MainAxisAlignment.CENTER)
    )


run(main,view=AppView.WEB_BROWSER)