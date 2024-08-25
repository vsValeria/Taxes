from taxes_1 import Taxes

class Controller:
    def __init__ (self):
        self.taxes_1_1=Taxes()

    def filter_taxes(self, min_tax, max_tax):
        return self.taxes_1_1.request_sql(min_tax,max_tax)



