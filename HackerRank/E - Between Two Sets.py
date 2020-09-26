# https: // www.hackerrank.com / challenges / between - two - sets / problem


def getTotalX(a, b):
    # Write your code here
    x = 0
    for n in range(1, min(b) + 1):
        multiple_of_a = True

        for element_a in a:
            if n % element_a != 0:
                multiple_of_a = False
                break

        if multiple_of_a:
            factor_of_b = True
            for element_b in b:
                if element_b % n != 0:
                    factor_of_b = False
                    break

            if factor_of_b:
                x += 1

    return x
Solution 2
return len([i for i in range(1, min(b)+1) if all(i%ab==0 for ab in a) and all(bb%i==0 for bb in b)])
