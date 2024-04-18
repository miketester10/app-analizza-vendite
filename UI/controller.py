import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fill_ddAnno(self):
        anni = self._model.get_anni()
        for anno in anni:
            self._view._ddAnno.options.append(ft.dropdown.Option(text=anno))

    def fill_ddBrand(self):
        brands = self._model.get_brands()
        for brand in brands:
            self._view._ddBrand.options.append(ft.dropdown.Option(text=brand))

    def fill_ddRetailer(self):
        retailers = self._model.get_retailers()
        for retailer in retailers:
            self._view._ddRetailer.options.append(ft.dropdown.Option(key=retailer.retailer_code, 
                                                                     text=retailer.retailer_name,
                                                                     data=retailer,
                                                                     on_click=self.read_retailer))
    def handle_top_vendite(self, e):
        self.__clear()
        anno = self._view._ddAnno.value
        brand = self._view._ddBrand.value
        retailer = self._view._ddRetailer.value

        vendite = self._model.top_vendite(anno, brand, retailer) 
        for vendita in vendite:
            self._view._txt_result.controls.append(ft.Text(vendita))

        self._view.update()

    def handle_analizza_vendite(self, e):
        self.__clear()
        anno = self._view._ddAnno.value
        brand = self._view._ddBrand.value
        retailer = self._view._ddRetailer.value

        giro_di_affari, numero_vendite, numero_retailer_coinvolti, numero_prodotti_coinvolti = self._model.analizza_vendite(anno, brand, retailer) 
        self._view._txt_result.controls.append(ft.Text('Statistiche vendite:'))
        self._view._txt_result.controls.append(ft.Text(f'Giro di affari: {giro_di_affari}'))  
        self._view._txt_result.controls.append(ft.Text(f'Numero vendite: {numero_vendite}'))
        self._view._txt_result.controls.append(ft.Text(f'Numero retailer coinvolti: {numero_retailer_coinvolti}'))
        self._view._txt_result.controls.append(ft.Text(f'Numero prodotti coinvolti: {numero_prodotti_coinvolti}'))
        
        self._view.update()

    def read_retailer(self, e): # metodo disponibile solo all'interno del controller ma non utilizzato ai fini dell'applicazione, ogni volta che seleziono un retailer dal menù ddRetailer, mi restituisce l'oggetto Retailer.
        retailer = e.control.data
        # print(retailer)

    def __clear(self):
        self._view._txt_result.controls.clear()
