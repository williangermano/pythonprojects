print("Bem vindo a calculadora de gorjeta?")
bill = float(input("Qual foi o valor do seu pedido?"))
tip = int(input("Qual a porcentagem que você pretende dar de gorjeta?"))
people = int(input("Quantas pessoas irão pagar?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Cada pessoa deve pagar o valor de R$ {final_amount}")