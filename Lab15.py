# Eva Deans
# Program from Dr. Ferner
# CSC344 Lab 15

import random

def main():
    numHosts = 2
    additive = 2
    reductionRate = .2

    transmission_rates = []
    for i in range(numHosts):
        transmission_rates.append(random.randint(0,100))

    iteration = 0
    while (iteration < 200):
        print("\nIteration" + str(iteration))
        sum = 0
        for i in range(len(transmission_rates)):
            print("Host " + str(i) + ": " + format(transmission_rates[i], ".4f"))
            sum += transmission_rates[i]
        print("Total transmission rate = " + format(sum, ".4f"))

        if sum > 100:
            for i in range(len(transmission_rates)):
                transmission_rates[i] *= reductionRate
        else:
            for i in range(len(transmission_rates)):
                transmission_rates[i] += additive

        iteration += 1

if __name__ == '__main__':
    main()