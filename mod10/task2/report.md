1. SELECT MAX(sold_count), phone_color  from  table_checkout -> Violet : 1120
2. SELECT MAX(sold_count), phone_color  from  table_checkout where phone_color in ('Red', 'Blue') -> Red: 64
3. SELECT MIN(sold_count), phone_color  from  table_checkout -> Goldenrod: 2