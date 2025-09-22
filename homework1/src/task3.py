def check_sign(num):
    if (num > 0):
        return 1
    elif(num < 0):
        return -1
    else:
        return 0

def get_ten_primes():
    primeNums = []
    eval = 2

    while len(primeNums) < 10:
        prime = True
        for i in range(2, eval):
            if eval % i == 0:
                prime = False

        if prime:
            primeNums.append(eval)

        eval += 1

    return primeNums

def sum_1_to_100():
    sum = 0

    for i in range(1, 101):
        sum += i

    return sum


if __name__ == '__main__':
    get_ten_primes()