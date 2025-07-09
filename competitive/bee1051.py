salary = float(input())

tax = 0.0

if salary <= 2000.00:
    print("Isento")
elif salary <= 3000.00:
    tax = (salary - 2000.00) * 0.08
    print(f"R$ {tax:.2f}")
elif salary <= 4500.00:
    tax = (1000.00 * 0.08) + ((salary - 3000.00) * 0.18)
    print(f"R$ {tax:.2f}")
else:
    tax = (1000.00 * 0.08) + (1500.00 * 0.18) + ((salary - 4500.00) * 0.28)
    print(f"R$ {tax:.2f}")
