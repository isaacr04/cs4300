# Rounds number to nearest hundredth of a decimal
def calculate_discount(price, discount_percent):
    return round(price - price * discount_percent / 100, 2)