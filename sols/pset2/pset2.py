# ================================================================
# Problem Set 2 (Parts a, b, c)
# Students: Only edit the code in the indicated "solution_*" functions.
# Do NOT change the function signatures. Do NOT modify any code below
# the sentinel lines that say "DON'T WRITE ANYTHING BELOW THIS LINE".
# ================================================================

# ----------------------------------------------------------------
# Part (a)
# ----------------------------------------------------------------
def solution_a(balance, annualInterestRate, monthlyPaymentRate):
    """
    Compute the remaining credit card balance after 12 months if only the
    *minimum required monthly payment* is made each month.

    Parameters
    ----------
    balance : float
        Outstanding balance on the credit card at the start of month 1.
    annualInterestRate : float
        Annual interest rate as a decimal (e.g., 0.2 for 20% APR).
    monthlyPaymentRate : float
        Minimum monthly payment rate as a decimal (e.g., 0.04 for 4% of balance).

    Returns
    -------
    float
        Remaining balance after 12 months, **rounded to two decimal places**.

    Monthly Update Formulas
    -----------------------
    monthlyInterestRate = annualInterestRate / 12.0
    minimumPayment = monthlyPaymentRate * previousBalance
    monthlyUnpaidBalance = previousBalance - minimumPayment
    updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

    Implementation Rules
    --------------------
    * Start from the initial `balance` passed in.
    * Repeat the update process exactly 12 times (once per month).
    * Do NOT print inside this function.
    * Round only once at the end: `round(final_balance, 2)`.
    """
    # Replace the placeholder return below once you've written your code.

    monthly_interest_rate = annualInterestRate / 12.0
    for month in range(12):
        minimum_payment = monthlyPaymentRate * balance
        monthly_unpaid_balance = balance - minimum_payment
        balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)

    return round(balance, 2)  # placeholder

""" DON'T WRITE ANYTHING BELOW THIS LINE (Part a tests) """
def _test_part_a():
    # (balance, annualInterestRate, monthlyPaymentRate, expected_remaining_balance)
    test_cases = [
        (42, 0.2, 0.04, 31.38),   # from problem description
        (484, 0.2, 0.04, 361.61), # from problem description
    ]

    tolerance = 0.05  # acceptable diff due to rounding variation

    print("=== Testing Part (a): Minimum Monthly Payment Rate ===")
    for i, (bal, air, mpr, expected) in enumerate(test_cases, start=1):
        result = solution_a(bal, air, mpr)
        diff = abs(result - expected)
        assert diff <= tolerance, (
            f"Part (a) Test {i} failed: expected about {expected}, got {result} "
            f"(difference {diff:.2f} > {tolerance})"
        )
        print(
            f'Part (a) Test {i} passed: '
            f'balance={bal}, annualInterestRate={air}, monthlyPaymentRate={mpr} '
            f'-> Remaining balance: {result}'
        )
    print()

# ----------------------------------------------------------------
# Part (b)
# ----------------------------------------------------------------

def fixed_payment_12_months(balance, annual_interest_rate, fixed_payment):
    """
    Given a fixed payment per month, compute the balance after 12 months
    """
    monthly_interest_rate = annual_interest_rate / 12.0
    for month in range(12):
        monthly_unpaid_balance = balance - fixed_payment
        balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
    return balance

def solution_b(balance, annualInterestRate):
    """
    Compute the *lowest fixed monthly payment* (multiple of $10) needed to pay off
    a credit card balance within 12 months.

    Parameters
    ----------
    balance : float
        Outstanding balance on the credit card at the start of month 1.
    annualInterestRate : float
        Annual interest rate as a decimal (e.g., 0.2 for 20% APR).

    Returns
    -------
    int
        The lowest *fixed* monthly payment (in dollars) that will pay off the debt
        in 12 months or less. Must be a multiple of 10. You may return an `int`
        (recommended) or a `float` that is effectively an integer multiple of 10.

    Monthly Update Formulas
    -----------------------
    monthlyInterestRate  = annualInterestRate / 12.0
    monthlyUnpaidBalance = previousBalance - fixedPayment
    updatedBalance       = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

    Implementation Hints
    --------------------
    * Start `fixedPayment` at 10.
    * Simulate 12 months. If balance > 0, increase `fixedPayment` by 10 and try again.
    * Stop when the 12-month simulated balance is <= 0.
    * Do NOT print inside this function; just return the payment.
    """
    # TODO: Implement the incremental search (step by $10) described above.
    # Replace the placeholder return below once you've written your code.

    fixed_payment = 10
    while fixed_payment_12_months(balance, annualInterestRate, fixed_payment) > 0.0:
        fixed_payment += 10

    return fixed_payment # placeholder

""" DON'T WRITE ANYTHING BELOW THIS LINE (Part b tests) """
def _test_part_b():
    # (balance, annualInterestRate, expected_payment)
    test_cases = [
        (3329, 0.2, 310), # from problem description
        (4773, 0.2, 440), # from problem description
        (3926, 0.2, 360), # from problem description
    ]

    print("=== Testing Part (b): Fixed Monthly Payment (Multiple of $10) ===")
    for i, (bal, air, expected) in enumerate(test_cases, start=1):
        result = solution_b(bal, air)
        # ensure it's a multiple of 10
        assert result % 10 == 0, f"Part (b) Test {i} failed: result {result} is not a multiple of 10."
        assert result == expected, (
            f"Part (b) Test {i} failed: expected {expected}, got {result}"
        )
        print(
            f'Part (b) Test {i} passed: '
            f'balance={bal}, annualInterestRate={air} -> Lowest Payment: {result}'
        )
    print()

# ----------------------------------------------------------------
# Part (c)
# ----------------------------------------------------------------
def solution_c(balance, annualInterestRate, epsilon=0.01):
    """
    Use *bisection search* to compute the smallest fixed monthly payment (to the cent)
    needed to pay off a credit card balance within 12 months.

    Parameters
    ----------
    balance : float
        Outstanding balance on the credit card at the start of month 1.
    annualInterestRate : float
        Annual interest rate as a decimal (e.g., 0.2 for 20% APR).
    epsilon : float, optional
        Acceptable error in the bisection convergence (default 0.01 == 1 cent).

    Returns
    -------
    float
        The lowest fixed monthly payment (rounded to two decimals) that will pay
        off the debt in 12 months or less.

    Bounds for Bisection
    --------------------
    monthlyInterestRate = annualInterestRate / 12.0
    lowerBound = balance / 12.0
        # (what you'd pay if there were no interest)
    upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
        # (what you'd pay if you waited and paid interest on full balance all year)

    Implementation Outline
    ----------------------
    * While the difference between bounds is greater than `epsilon`, bisect.
    * Simulate 12 months given the mid-point guess.
    * If balance after 12 months is > 0, payment too low -> move lower bound up.
    * Else move upper bound down.
    * At the end, round the final payment guess to two decimals and return.
    * Do NOT print inside this function.
    """

    lower = epsilon
    upper = epsilon
    # set upper
    while fixed_payment_12_months(balance, annualInterestRate, upper) >= 0:
        upper *= 10

    while upper - lower > epsilon:
        print(lower, upper)
        midpoint = (upper + lower) / 2.0
        if fixed_payment_12_months(balance, annualInterestRate, midpoint) < 0:
            upper = midpoint
        else:
            lower = midpoint

    return round(upper, 2)

""" DON'T WRITE ANYTHING BELOW THIS LINE (Part c tests) """
def _test_part_c():
    # (balance, annualInterestRate, expected_payment)
    test_cases = [
        (320000, 0.2, 29157.09),  # from problem description
        (999999, 0.18, 90325.03), # from problem description
    ]

    tolerance = 0.05  # lenient tolerance per problem statement

    print("=== Testing Part (c): Fixed Monthly Payment via Bisection (to the cent) ===")
    for i, (bal, air, expected) in enumerate(test_cases, start=1):
        result = solution_c(bal, air)
        diff = abs(result - expected)
        assert diff <= tolerance, (
            f"Part (c) Test {i} failed: expected about {expected}, got {result} "
            f"(difference {diff:.2f} > {tolerance})"
        )
        print(
            f'Part (c) Test {i} passed: '
            f'balance={bal}, annualInterestRate={air} -> Lowest Payment: {result:.2f}'
        )
    print()

# ----------------------------------------------------------------
# Master test runner
# ----------------------------------------------------------------
def main():
    _test_part_a()
    _test_part_b()
    _test_part_c()

if __name__ == "__main__":
    main()
# ================================================================
