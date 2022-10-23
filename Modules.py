# import converters
#
# print(converters.lbs_to_kg(70))

# from converters import kg_to_lbs
# print(kg_to_lbs(56))

# --------------------------------------------------
# import converters
# print(converters.find_max(input()))
# ----------------------------------------------
# Packages:
import eCommerce.shipping
eCommerce.shipping.calc_shipping()
# or
from eCommerce.shipping import calc_shipping
calc_shipping()
# or
from eCommerce import shipping
shipping.calc_shipping()