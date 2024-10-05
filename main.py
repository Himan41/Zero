from flet import *
def main(page: Page):
    page.bgcolor = "black"
    page.scroll = "auto"
    page.verical_alignment = "center"
    page.horizontal_alignment = "center"
    
    #==========AppBar===================
    
    page.appbar = AppBar(
        bgcolor = "red",
        title = Text("ZeroTube"),
        center_title = True,
        leading = Icon(icons.HOME),
        leading_width = 40,
        actions =[
            IconButton(icons.NOTIFICATIONS),   
            PopupMenuButton(
                items =[
                    PopupMenuItem(text = "Profile"),
                    PopupMenuItem(text = "Settings"),
                    PopupMenuItem(text = "About"),
                    PopupMenuItem(text = "Help"),
                    PopupMenuItem(),
                    PopupMenuItem(text = "Exit"),
                ]
            )  
        ]
    )
  #==============AppBar and=============
    def log(e):
        v1 = en1.value #Email
        v2 = en2.value #Password
        if v1 == "zero" and v2 == "1234":
            alert1 = AlertDialog(
                title = Text("Welcome.. Successful entry",size = 20,color="green")
        )
            page.overlay.append(alert1)
            alert1.open = True
            page.update()
        else:
            alert2 = AlertDialog(
                title = Text("Login Error404 ....",size = 20,color="red")
    )
            page.overlay.append(alert2)
            alert2.open = True
            page.update()
            
    photo = Image(src="assets/profile.jpg",width=200)
    text = Text("Login System ",color='red',size=25)
    en1 = TextField(label="Email",hint_text="Enter Your Email",color='white',width=300,icon=icons.EMAIL)
    en2 = TextField(label="Passwd",hint_text="Enter Your Password",color='white',width=300,icon=icons.PASSWORD, password=True,can_reveal_password=True)
    bt1 = ElevatedButton(text="Login",bgcolor='red',color='white',width=100, height=50,on_click=log)
    page.add(photo,text,en1,en2,bt1)
    #==========BottomBar===================
    page.navigation_bar = NavigationBar(
        bgcolor = "red",
        destinations=[
            NavigationDestination(icon=icons.CALL, label="Call"),
            NavigationDestination(icon=icons.CONTACT_PHONE, label="Contact"),
            NavigationDestination(icon=icons.BOOKMARK_BORDER,label="Explore",
            )
        ]
    )
    
    page.update()
app(target=main)
