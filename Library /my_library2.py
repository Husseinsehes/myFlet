from flet import *
import sqlite3

# إنشاء قاعدة البيانات
con = sqlite3.connect("MyDB.db", check_same_thread=False)
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS library (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    author TEXT,
    nationality TEXT,
    date TEXT
)""")
con.commit()


# الوظيفة الرئيسية للتطبيق
def main(page: Page):
    page.title = "My Library"
    page.window_width = 400
    page.window_height = 700
    page.theme_mode = ThemeMode.LIGHT

    # حقول الإدخال
    name_field = TextField(label="Book Name")
    author_field = TextField(label="Author Name")
    nationality_field = TextField(label="Nationality")
    date_field = TextField(label="Publication Date")

    # عنصر لعرض الكتب
    books_container = Column()

    # وظيفة لإضافة كتاب
    def add_book(e):
        # التحقق من أن الحقول ليست فارغة
        if not name_field.value or not author_field.value or not nationality_field.value or not date_field.value:
            page.snack_bar = SnackBar(
                Text("Please fill in all fields!", color="white"),
                bgcolor="red"
            )
            page.snack_bar.open()
            return

        # إدخال الكتاب في قاعدة البيانات
        cursor.execute(
            "INSERT INTO library (name, author, nationality, date) VALUES (?, ?, ?, ?)",
            (name_field.value, author_field.value, nationality_field.value, date_field.value)
        )
        con.commit()

        # تفريغ الحقول بعد الإضافة
        name_field.value = ""
        author_field.value = ""
        nationality_field.value = ""
        date_field.value = ""
        page.snack_bar = SnackBar(
            Text("Book added successfully!", color="white"),
            bgcolor="green"
        )
        page.snack_bar.open()
        page.update()

    # وظيفة لعرض الكتب
    def show_books(e):
        books_container.controls.clear()  # مسح المحتويات السابقة
        cursor.execute("SELECT * FROM library")
        books = cursor.fetchall()

        if not books:
            books_container.controls.append(Text("No books found.", color="red"))
        else:
            for book in books:
                books_container.controls.append(
                  Row([
                    Card(
                        content=Container(
                            padding=10,
                            content=Column([
                                Text(f"Name: {book[1]}"),
                                Text(f"Author: {book[2]}"),
                                Text(f"Nationality: {book[3]}"),
                                Text(f"Date: {book[4]}"),
                            ])
                        )

                  )
                  ]) 
                )
        page.update()

    # واجهة التطبيق
    page.add(
        Column([
            Text("Library App", size=24, weight="bold"),
            name_field,
            author_field,
            nationality_field,
            date_field,
            Row([
                ElevatedButton("Add Book", on_click=add_book),
                ElevatedButton("Show Books", on_click=show_books),
            ], alignment=MainAxisAlignment.CENTER),
            Divider(),
            books_container
        ], alignment=MainAxisAlignment.START, spacing=20)
    )


# تشغيل التطبيق
app(target=main)
