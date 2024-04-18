from dataclasses import dataclass

@dataclass
class Retailer:
    retailer_code: int #Primary Key
    retailer_name: str
    type: str
    country: str

    def __eq__(self, other):
        return self.retailer_code == other.retailer_code

    def __hash__(self):
        return hash(self.retailer_code)