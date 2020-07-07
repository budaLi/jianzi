# Q9 - Q10
## variables #### DON'T CHANGE!!
input_price = {'Croissant':2000, 'Bagel' : 1500, 'FishBread' : 500}
################################

## your code here!
import sys
sys.path.append(".")
from store import Store

bakery = Store(input_price)

bakery.sell('Croissant',2)
bakery.sell('Bagel',4)





# print output
#Q9
print(bakery.price)
#Q10
print(bakery.revenue)
