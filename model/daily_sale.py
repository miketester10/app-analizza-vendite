from dataclasses import dataclass
import datetime

@dataclass
class Daily_sale:
    retailer_code: int #Foreign key
    product_number: int #Foreign key
    data: datetime.date
    ricavo: float

    def __str__(self):
        return f'Data: {self.data}; Ricavo: {self.ricavo}; Retailer: {self.retailer_code}; Product: {self.product_number}'

    def __eq__(self, other):
        return (self.retailer_code == other.retailer_code 
        and self.product_number == other.product_number)

    def __hash__(self):
        return hash(self.retailer_code, self.product_number)
