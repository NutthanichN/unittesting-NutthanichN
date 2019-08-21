## Unit Testing Assignment

by Nutthanich Narphromar.


## Test Cases for unique

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| 3 items, no duplicate | list with 3 items
| one item many times    |  list with 1 item   |
| 2 items, many times, many orders | 2 items list, items in same order  |
| 7 items, many types, many times, many orders | 7 items list in same order |
| argument is a set | raise ValueError |
| argument is a tuple | raise ValueError |
| argument is a dict | raise ValueError |


## Test Cases for Fraction

Test of constructor

| Test case                                   |  Expected Result    |
|---------------------------------------------|---------------------|
| numerator and denominator with common factor| fraction in standard form (numerator and denominator have no common factor|
| both positive numerator and denominator |  positive fraction in standard form with both positive numerator and denominator |
| both negative numerator and denominator | positive fraction in standard form with both positive numerator and denominator |
| negative numerator and positive denominator | negative fraction in standard form with negative numerator and positive denominator |
| positive numerator and negative denominator | negative fraction in standard form with negative numerator and positive denominator |
| positive numerator | positive numerator and default denominator (= 1) |
| negative numerator | negative numerator and default denominator (= 1) |
| numerator is 0 | that numerator and default denominator (= 1) |
| numerator is 1 and denominator is 0 (positive infinity) | positive fraction with numerator = 1 and denominator = 0 |
| numerator is -1 and denominator is 0 (negative infinity) | negative fraction with numerator = -1 and denominator = 0 |
| numerator is greater than 1 and denominator is 0 (positive infinity) | positive fraction with numerator = 1 and denominator = 0 |
| numerator is less than 1 and denominator is 0 (positive infinity) | negaitive fraction with numerator = -1 and denominator = 0 |
| numerator is 0 and denominator is 0 | raise ValueError |

Test of string representation method

| Test case                                   |  Expected Result    |
|---------------------------------------------|---------------------|
| both positive numerator and denominator | the string of positive fraction in form "numerator/denominator" |
| positive numerator and negative denominator | the string of negative fraction in form "-numerator/denominator" |
| negaitive numerator and positive denominator | the string of negative fraction in form "-numerator/denominator" |
| both negaitive numerator and denominator | the string of positive fraction in form "numerator/denominator" |
| positive numerator (and denominator = 1) | the string of integer in form "integer" |
| positive numerator and denominator is -1 | the string of negative integer in form "-integer" |
| numerator is 0 and any denominator | the string of zero in form "0" |
| numerator is 1 and denominator is 0 (positive infinity) | the string of positive fraction in form "1/0" |
| numerator is -1 and denominator is 0 (negative infinity) | the string of negative fraction in form "-1/0" |
| numerator is greater than 1 and denominator is 0 (positive infinity) | the string of positive fraction in form "1/0" |
| numerator is less than 1 and denominator is 0 (positive infinity) | the string of positive fraction in form "-1/0" |


Test of addition operator (+) method

| Test case                                |  Expected Result  |
|------------------------------------------|-------------------|
| positive fraction plus positive fraction | positive fraction |
| negative fraction plus negative fraction | negative fraction |
| positive fraction plus zero | that positive fraction |
| any fraction that less than infinity plus positive infinity (1/0) | positive infinity (1/0) |
| any fraction that less than infinity plus negative infinity (-1/0) | negative infinity (-1/0) |
| positive infinity (1/0) plus positive infinity (1/0) | positive infinity (1/0) |
| negaitive infinity (-1/0) plus negative infinity (-1/0) | negative infinity (-1/0) |
| positive infinity (1/0) plus negative infinity (-1/0) | raise ValueError |


Test of multiplication operator (*) method

| Test case                                    |  Expected Result  |
|----------------------------------------------|-------------------|
| positive fraction multiplied by positive fraction | positive fraction |
| positive fraction multiplied by negative fraction | negative fraction |
| negative fraction multiplied by negative fraction | positive fraction |
| positive fraction multiplied by zero | zero |
| negative fraction multiplied by zero | zero |
| any fraction multiplied by one | that fraction |
| positive infinity (1/0) multiplied by positive fraction | positive infinity (1/0) |
| negative infinity (-1/0) multiplied by positive fraction | negative infinity (-1/0) |
| negative infinity (1/0) multiplied by negative fraction | positive infinity (1/0) |
| positive infinity (1/0) multiplied by positive infinity (1/0) | positive infinity (1/0) |
| negative infinity (-1/0) multiplied by negative infinity (-1/0) | positive infinity (1/0) |
| positive infinity (1/0) multiplied by negative infinity (1/0) | negative infinity (-1/0) |
| positive infinity (1/0) multiplied by zero | raise ValueError |
| negative infinity (-1/0) multiplied by zero | raise ValueError |

Test of equality operator (==) method

| Test case                              |  Expected Result  |
|----------------------------------------|-------------------|
| positive fraction == negative fraction | False             |
| any fraction == a standard form of that fraction | True    |
| positive infinity (1/0) == negative infinity (-1/0) | False |
