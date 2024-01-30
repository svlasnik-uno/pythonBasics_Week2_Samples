# 1. Modify this program to ask the user for the total invoice amount and
#    the percentage discount
# 2. Modify this program to add a repetition structure to allow the user
#    to continue to enter invoice totals and discount amounts until they choose to quit
#    Use -1 as the value to end the repetition structure
invoice_total = 1200
discount = .15
if invoice_total >= 500:
    discount_percent = .2
    print (invoice_total*discount_percent)
elif invoice_total >= 250:
    discount_percent = .1
    print(invoice_total * discount_percent)
elif invoice_total > 0:
    discount_percent = 0
    print(invoice_total * discount_percent)
else:
    print("Invoice total must be greater than zero.")
