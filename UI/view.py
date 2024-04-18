import flet as ft

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.window_width = 1150
        self._page.title = "Applicazione per analizzare le vendite"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._ddAnno = None
        self._ddBrand = None
        self._ddRetailer = None
        self._btnTopVendite = None
        self._btnAnalizzaVendite = None
        self._txt_result = None
       
    def load_interface(self):
        # Row 0
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        
        row0 = ft.Row(spacing=340, controls=[self.__theme_switch, self._title],
                      alignment=ft.MainAxisAlignment.START)

        # Row 1
        self._ddAnno = ft.Dropdown(label="Anno",width=250)
        self._controller.fill_ddAnno()
        self._ddBrand = ft.Dropdown(label="Brand",width=250)
        self._controller.fill_ddBrand()
        self._ddRetailer = ft.Dropdown(label="Retailer",width=600)
        self._controller.fill_ddRetailer()

        row1 = ft.Row(controls=[self._ddAnno, self._ddBrand, self._ddRetailer],
                      alignment=ft.MainAxisAlignment.CENTER)
        
        # Row 2
        self._btnTopVendite = ft.ElevatedButton("Top Vendite", on_click=self._controller.handle_top_vendite)
        self._btnAnalizzaVendite = ft.ElevatedButton("Analizza Vendite", on_click=self._controller.handle_analizza_vendite)

        row2 = ft.Row(controls=[self._btnTopVendite, self._btnAnalizzaVendite],
                      alignment=ft.MainAxisAlignment.CENTER)
        
        # Row 3
        self._txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)

        self._page.add(row0, row1, row2, self._txt_result)
        self._page.update()

    def set_controller(self, controller):
        self._controller = controller

    def update(self):
        self._page.update()
    
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self._page.theme_mode = (
            ft.ThemeMode.DARK
            if self._page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self._page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        self._page.update()
