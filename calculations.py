from lcoe.lcoe import lcoe
import numpy as np
from numpy_financial import irr
import matplotlib.pyplot as plt

operating_cost = 200  # $million/year
capital_cost = [5000, 10000, 20000, 40000]  # $million
discount_rate = 0.02  # %
lifetime = 25
annual_output = 25000  # kWh
list_lcoe = []
list_irr = []

for n in capital_cost:

    lcoe_value = lcoe(annual_output, n, operating_cost, discount_rate, lifetime)
    print("lcoe is:", lcoe_value)
    if lcoe_value < 0.5:
        print("profits per kWh:", 0.5 - lcoe_value)
    else:
        print("lcoe is above market price")
    lcoe_profit: float = (0.5 - lcoe_value) * annual_output
    y = 1 + discount_rate
    print("annual revenue is:", lcoe_profit)

    irr_input = np.zeros(25)
    irr_input[0] = - n

    for j in range(1, 25):
        irr_input[j] = lcoe_profit / y ** j

    irr_output = irr(irr_input)

    print("irr is:", irr_output)

    list_lcoe.append(lcoe_value)
    list_irr.append(irr_output)

print(list_lcoe)
print(list_irr)
plot = plt.figure()
plt.subplot(1, 2, 1)
plt.plot(capital_cost, list_lcoe)
plt.ylabel('lcoe')
plt.xlabel('Capital Cost')
plt.subplot(1, 2, 2)
plt.plot(capital_cost, list_irr)
plt.ylabel('irr')
plt.xlabel('Capital Cost')
plt.show()

operating_cost = [100, 200, 400, 800]  # $million/year
capital_cost = 5000  # $million
discount_rate = 0.02  # %
lifetime = 25
annual_output = 25000  # kWh

list_lcoe = []
list_irr = []

for n in operating_cost:

    lcoe_value = lcoe(annual_output, capital_cost, n, discount_rate, lifetime)
    print("lcoe is:", lcoe_value)
    if lcoe_value < 0.5:
        print("profits per kWh:", 0.5 - lcoe_value)
    else:
        print("lcoe is above market price")
    lcoe_profit: float = (0.5 - lcoe_value) * annual_output
    y = 1 + discount_rate
    print("annual revenue is:", lcoe_profit)

    irr_input = np.zeros(25)
    irr_input[0] = - capital_cost

    for j in range(1, 25):
        irr_input[j] = lcoe_profit / y ** j

    irr_output = irr(irr_input)

    print("irr is:", irr_output)

    list_lcoe.append(lcoe_value)
    list_irr.append(irr_output)

print(list_lcoe)
print(list_irr)
plot = plt.figure()
plt.subplot(1, 2, 1)
plt.plot(operating_cost, list_lcoe)
plt.ylabel('lcoe')
plt.xlabel('Operating Cost')
plt.subplot(1, 2, 2)
plt.plot(operating_cost, list_irr)
plt.ylabel('irr')
plt.xlabel('Operating Cost')
plt.show()

operating_cost = 100  # $million/year
capital_cost = 5000  # $million
discount_rate = [0.02, 0.03, 0.04, 0.05]  # %
lifetime = 25
annual_output = 25000  # kWh

list_lcoe = []
list_irr = []

for n in discount_rate:

    lcoe_value = lcoe(annual_output, capital_cost, operating_cost, n, lifetime)
    print("lcoe is:", lcoe_value)
    if lcoe_value < 0.5:
        print("profits per kWh:", 0.5 - lcoe_value)
    else:
        print("lcoe is above market price")
    lcoe_profit: float = (0.5 - lcoe_value) * annual_output
    y = 1 + n
    print("annual revenue is:", lcoe_profit)

    irr_input = np.zeros(25)
    irr_input[0] = - capital_cost

    for j in range(1, 25):
        irr_input[j] = lcoe_profit / y ** j

    irr_output = irr(irr_input)

    print("irr is:", irr_output)

    list_lcoe.append(lcoe_value)
    list_irr.append(irr_output)

print(list_lcoe)
print(list_irr)
plot = plt.figure()
plt.subplot(1, 2, 1)
plt.plot(discount_rate, list_lcoe)
plt.ylabel('lcoe')
plt.xlabel('discount rate')
plt.subplot(1, 2, 2)
plt.plot(discount_rate, list_irr)
plt.ylabel('irr')
plt.xlabel('discount rate')
plt.show()

operating_cost = 100  # $million/year
capital_cost = 5000  # $million
discount_rate = 0.02  # %
lifetime = [20, 25, 30, 35]
annual_output = 25000  # kWh

list_lcoe = []
list_irr = []

for n in lifetime:

    lcoe_value = lcoe(annual_output, capital_cost, operating_cost, discount_rate, n)
    print("lcoe is:", lcoe_value)
    if lcoe_value < 0.5:
        print("profits per kWh:", 0.5 - lcoe_value)
    else:
        print("lcoe is above market price")
    lcoe_profit: float = (0.5 - lcoe_value) * annual_output
    y = 1 + discount_rate
    print("annual revenue is:", lcoe_profit)

    irr_input = np.zeros(25)
    irr_input[0] = - capital_cost

    for j in range(1, 25):
        irr_input[j] = lcoe_profit / y ** j

    irr_output = irr(irr_input)

    print("irr is:", irr_output)

    list_lcoe.append(lcoe_value)
    list_irr.append(irr_output)

print(list_lcoe)
print(list_irr)
plot = plt.figure()
plt.subplot(1, 2, 1)
plt.plot(lifetime, list_lcoe)
plt.ylabel('lcoe')
plt.xlabel('lifetime')
plt.subplot(1, 2, 2)
plt.plot(lifetime, list_irr)
plt.ylabel('irr')
plt.xlabel('lifetime')
plt.show()

operating_cost = 100  # $million/year
capital_cost = 5000  # $million
discount_rate = 0.02  # %
lifetime = 25
annual_output = [25000, 30000, 35000, 40000]  # kWh

list_lcoe = []
list_irr = []

for n in annual_output:

    lcoe_value = lcoe(n, capital_cost, operating_cost, discount_rate, lifetime)
    print("lcoe is:", lcoe_value)
    if lcoe_value < 0.5:
        print("profits per kWh:", 0.5 - lcoe_value)
    else:
        print("lcoe is above market price")
    lcoe_profit: float = (0.5 - lcoe_value) * n
    y = 1 + discount_rate
    print("annual revenue is:", lcoe_profit)

    irr_input = np.zeros(25)
    irr_input[0] = - capital_cost

    for j in range(1, 25):
        irr_input[j] = lcoe_profit / y ** j

    irr_output = irr(irr_input)

    print("irr is:", irr_output)

    list_lcoe.append(lcoe_value)
    list_irr.append(irr_output)

print(list_lcoe)
print(list_irr)
plot = plt.figure()
plt.subplot(1, 2, 1)
plt.plot(annual_output, list_lcoe)
plt.ylabel('lcoe')
plt.xlabel('annual output')
plt.subplot(1, 2, 2)
plt.plot(annual_output, list_irr)
plt.ylabel('irr')
plt.xlabel('annual output')
plt.show()