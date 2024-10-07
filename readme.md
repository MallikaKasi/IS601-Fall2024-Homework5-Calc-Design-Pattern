## Welcome to Command-Plugin based Calculator Application 

This is the interactive Calculator that performs 
Addition

Subtraction

Multiplication

Division

### This Calclulatore can run in 2 modes

1) Interactive Mode which is implemneted using plugins

2) Implementation of command pattern and REPL

### Testing Commands:

pytest 

pytest --pylint

pytest --pylint --cov

pytest tests/test_main.py.


### Run the Applications:
To run the Interactive Calculator: python main.py I

To perfomr the calculation directly from Command Line:  python main.py 2 3 add


### Test Results:
## (venv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week5/Week5_Project$ pytest
======================================================================== test session starts =========================================================================

tests/test_main.py::test_calculate_and_print[5-3-add-The result of 5 add 3 is equal to 8] PASSED                                                               [ 55%]

tests/test_operations.py::test_operation[a3-b3-add-expected3] PASSED                                                                                           [ 95%]

tests/test_operations.py::test_operation[a4-b4-add-expected4] PASSED                                                                                           [ 97%]

tests/test_operations.py::test_divide_by_zero PASSED                                                                                                           [100%]

========================================================================= 40 passed in 0.21s =========================================================================
## (venv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week5/Week5_Project$ pytest --pylint 
======================================================================== test session starts =========================================================================

tests/test_operations.py::test_operation[a3-b3-subtract-expected3] PASSED                                                                                      [ 95%]

tests/test_operations.py::test_operation[a4-b4-add-expected4] PASSED                                                                                           [ 97%]

tests/test_operations.py::test_divide_by_zero PASSED                                                                                                           [100%]

=================================================================== 40 passed, 8 skipped in 1.24s ====================================================================
## (venv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week5/Week5_Project$ pytest --pylint --cov 
======================================================================== test session starts =========================================================================

---------- coverage: platform linux, python 3.10.12-final-0 ----------
Name                             Stmts   Miss  Cover
----------------------------------------------------

app/__init__.py                     83     71    14%

tests/test_main.py                  51      4    92%

tests/test_operations.py            11      0   100%
----------------------------------------------------

TOTAL                              418     92    78%
=================================================================== 40 passed, 8 skipped in 1.80s ====================================================================
## (venv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week5/Week5_Project$ pytest --num_records=10
======================================================================== test session starts =========================================================================


tests/test_operations.py::test_operation[a98-b98-multiply-expected98] PASSED                                                                                   [ 99%]

tests/test_operations.py::test_operation[a99-b99-divide-expected99] PASSED                                                                                     [ 99%]

tests/test_operations.py::test_divide_by_zero PASSED                                                                                                           [100%]

======================================================================== 230 passed in 0.81s =========================================================================
## (venv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week5/Week5_Project$ python main.py 
        Welcome to Command-Plugin based Calculator Application:    
           
Usage of this Calculator:

    To start the Interactive Calculator: python main.py I 

    To perform the calculation from Commamd Line Type Like below:

       python main.py <number1> <number2> add

       python main.py <number1> <number2> subtract

       python main.py <number1> <number2> multiply

       python main.py <number1> <number2> divide

## (venv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week5/Week5_Project$ python main.py I 

Option To Perform Interactive Calculation:
        

Type A. To Perform Add

Type S. To Perform Subtract

Type M. To Perform Multiply

Type D. To Perform Divide

Type E. To Exit

Choose an option : A

Enter the first number: 2

Enter the second number: 3

The result of adding 2.0 + 3.0 = 5.0

Type C : to Continue , Type E : to Exit  
C

Type A. To Perform Add

Type S. To Perform Subtract

Type M. To Perform Multiply

Type D. To Perform Divide

Type E. To Exit
Choose an option : M

Enter the first number: 3

Enter the second number: 4


The result of Multiplying 3.0 * 4.0 = 12.0

Type C : to Continue , Type E : to Exit  


E
Exiting.

## (venv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week5/Week5_Project$ python main.py 5 6 multiply

The result of 5 multiply 6 is equal to 30

