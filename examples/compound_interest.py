# Python3 program to find compound
# interest for given values.
# www.geeksforgeeks.org

# Compound interest is interest calculated on both the 
# initial principal and the accumulated interest from previous periods.


def compound_interest(principal, rate, time):
 
    # Calculates compound interest
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)
 
 
# Driver Code
compound_interest(10000, 10.25, 5)
