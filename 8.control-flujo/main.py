tx_1 = {
    'customer_id': 123,
    'amount': 500.00,
    'destination_customer': 234,
}

# if (si)
if tx_1['amount'] >= 500.00:
    print("Dar bonificación :3")


# else (si no)
# if tx_1['destination_customer'] == 235:
#     print("Fraude detectado! D:")
# else:
#     print("Continua con la transacción normal :D")

# else if - elif
tx_1['amount'] = 200.00
amount = tx_1['amount']

if amount == 100.00:
    print("Dar bonificación :3")
    print("Dar bonificación :3")
    print("Dar bonificación :3")
    if amount == 900:
        print("Dar bonificación :3")
elif amount == 200.00:
    print("Dar DOBLE bonificación :3")

elif amount == 300.00:
    print("Dar TRIPLE bonificación :3")
else:
    print("Sin bonificación :(")
