time_of_the_championship = input()
ticket_type = input()
quantity = int(input())
photo = input()
ticket_price = 0

if time_of_the_championship == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.50
    elif ticket_type == "Premium":
        ticket_price = 105.20
    elif ticket_type == "VIP":
        ticket_price = 118.90
elif time_of_the_championship == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    elif ticket_type == "VIP":
        ticket_price = 300.40
elif time_of_the_championship == "Final":
    if ticket_type == "Standard":
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    elif ticket_type == "VIP":
        ticket_price = 400

total_price = ticket_price * quantity

if total_price > 4000:
    total_price *= 0.75
    if photo == "Y" or photo == "N":
        total_price = total_price
elif total_price > 2500:
    total_price *= 0.9
    if photo == "Y":
        total_price = total_price + (40 * quantity)
    else:
        total_price = total_price

print(f"{total_price:.2f}")
