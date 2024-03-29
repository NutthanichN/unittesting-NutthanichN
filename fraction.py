import math


class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        # check arguments type
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError("Numerator and denominator should be integer.")
        # set infinity case to standard form (1/0), (-1/0)
        if denominator == 0:
            if numerator > 0:
                numerator = 1
            elif numerator < 0:
                numerator = -1
        # normal case, move minus to numerator
        elif denominator < 0:
            if numerator > 0:
                numerator = - numerator
            elif numerator < 0:
                numerator = abs(numerator)
            denominator = abs(denominator)

        # set numerator and denominator values
        if numerator == 0 and denominator == 0:
            self.numerator = 0
            self.denominator = 0
        else:
            gcd = math.gcd(numerator, denominator)
            self.numerator = int(numerator / gcd)
            self.denominator = int(denominator / gcd)

    def is_nan(self):
        """Check if the fraction is NaN or not."""
        if self.numerator == 0 and self.denominator == 0:
            return True
        return False

    def __str__(self):
        """Return fraction as a string."""
        if self.is_nan():
            return "0/0"
        elif self.numerator == 0 or self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        new_numerator = 1
        new_denominator = 1
        # NaN + any fraction = NaN
        if self.is_nan() or frac.is_nan():
            return Fraction(0, 0)
        # infinity plus each other
        elif self.denominator == 0 and frac.denominator == 0:
            if self.numerator + frac.numerator > 0:
                new_numerator = 1
            elif self.numerator + frac.numerator < 0:
                new_numerator = -1
            else:
                new_numerator = 0
            new_denominator = 0
        # normal case and any number + (+/-)infinity
        else:
            new_numerator = (self.numerator * frac.denominator) + (self.denominator * frac.numerator)
            new_denominator = self.denominator * frac.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, frac):
        """Return the product of two fractions as a new fraction."""
        # NaN * any fraction = NaN
        if self.is_nan() or frac.is_nan():
            return Fraction(0, 0)
        # 0 * (*/-)infinity = NaN
        elif self.denominator == 0:
            if frac.numerator == 0:
                return Fraction(0, 0)
        # normal cases
        new_numerator = self.numerator * frac.numerator
        new_denominator = self.denominator * frac.denominator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator
