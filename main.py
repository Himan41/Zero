from flet import (
    Page, TextField, ElevatedButton, Image, Column,
    FilePicker, FilePickerResultEvent, Container, Text, alignment, app
)

PASSWORD = "1234"

def main(page: Page):
    page.title = "عارض الصور"
    page.bgcolor = "cyan"
    page.scroll = "auto"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    
    password_input = TextField(
        label="Enter Password",
        password=True,
        can_reveal_password=True,
        width=300,
    )

    # زر الدخول
    login_btn = ElevatedButton(text="Login")
    
    # عارض الصور
    images_column = Column(scroll="auto")

    # أداة رفع الملفات (الصور)
    file_picker = FilePicker()

    def login(e):
        if password_input.value == PASSWORD:
            page.clean()
            page.add(
                Container(
                    content=Column(
                        [
                            Text("ارفع صورك من هنا:", color="white"),
                            ElevatedButton(
                                text="اختر الصور",
                                icon="upload",
                                on_click=lambda _: file_picker.pick_files(
                                    allow_multiple=True,
                                    file_type="image"
                                ),
                            ),
                            images_column
                        ]
                    ),
                    alignment=alignment.center
                )
            )
            page.update()
        else:
            password_input.error_text = "كلمة السر غير صحيحة"
            page.update()

    # عند اختيار الصور
    def on_files_selected(e: FilePickerResultEvent):
        if e.files:
            for f in e.files:
                images_column.controls.append(
                    Image(src=f.path, width=300, height=300, fit="contain")
                )
            page.update()

    file_picker.on_result = on_files_selected
    page.overlay.append(file_picker)
    login_btn.on_click = login

    page.add(password_input, login_btn)

app(target=main)
