"""Classes for melon orders."""


class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        self.species = species 
        self.qty = qty
        self.shipped = False
        # self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""
    
        base_price = 5

        if self.species == "christmas melon":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        print(f"${total:.2f}")

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08

#  def __init__(self):
    #     super().__init__(self, species, qty):
# "Initialize melon order attributes."""

# self.species = species
# self.qty = qty
# self.shipped = False
# self.order_type = "domestic"
    #     self.tax = 0.08

    # # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code

    def get_total(self):
        total = super().get_total()
        flat_fee = 3

        if self.qty < 10:
            total += flat_fee

        return total


    #     """Initialize melon order attributes."""

    # self.species = species
    #     # self.qty = qty
    #     self.country_code = country_code
    #     # self.shipped = False
    #     # self.order_type = "international"
    # #     self.tax = 0.17

    # # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    # #     self.shipped = True

    # def get_country_code(self, country_code):
    #     """Return the country code."""

    #     return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A Melons order fulfilled through Goverment contract, must call mark_inspection. """
    passed_inspection = False
    tax = 0

    def mark_inspection(self, passed):
        self.passed_inspection = passed

