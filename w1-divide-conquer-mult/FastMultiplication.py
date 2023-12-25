def FastMultiplication (num1, num2):
    
    # base-case
    n  = len(num1)
    if n == 1:
        return (int(num1) * int(num2))    
    else:
        num1Right = num1[n//2:]
        num1Left = num1[:n//2]

        num2Right = num2[n//2:]
        num2Left =  num2[:n//2]

        firstTerm = FastMultiplication(num1Left, num2Left)
        thridTerm = FastMultiplication(num1Right, num2Right)

        secondTerm = (int(num1Left) + int(num1Right)) * ( int(num2Left) + int(num2Right)) \
                        - int(firstTerm) - int(thridTerm)
    
        return (10**n) * int(firstTerm) + (10**(n//2)) * int(secondTerm) + int(thridTerm)


if __name__ == "__main__":


    a = '3141592653589793238462643383279502884197169399375105820974944592'

    b = '2718281828459045235360287471352662497757247093699959574966967627'

    print("Output: ", FastMultiplication(a, b))

