Reflection: OOP Fundamentals
Phase 1: Conceptual Check & Code Diagnosis

1. Conceptual Distinction
Encapsulation vs. Abstraction. Encapsulation involves grouping of data and the methods that manipulate such data and restricting access to such data in order to ensure the safety of the internal state of the object from any modification. Abstraction involves hiding of complex details while only the required information is presented to the caller.

An Analogy (pharmacy). The locked drug cabinet located behind the counter is an example of encapsulation; customers cannot help themselves with the drugs, and the pharmacist is responsible for the alteration of the stock. The prescription counter represents abstraction; the patient gives a prescription and gets drugs back without knowing how dosage is checked, stocks replenished, and insurance handled.

Why _attribute is called "convention-based non-public" and not really private. A leading underscore is just an indication to other coders that "this is an internal implementation detail; do not depend on this". This is not enforced by Python. It is always possible to access or modify obj._attribute, as well as use from module import *. Python uses a "let's pretend we are all consenting adults" approach; thus, there is no private keyword enforced by the compiler.
Name mangling of __attribute. In the class body, an identifier starting with double underscores but not ending with double underscores is mangled into _ClassName__attribute. For instance, self.__pin in class ATM becomes _ATM__pin. An attempt to use atm.__pin outside of the class fails, but atm._ATM__pin succeeds. Name mangling is done for the sake of avoiding accidental name collision in subclasses.

2. Code Diagnosis

Flaws in DigitalWallet:
First parameter name incorrect. The __init__(wallet,...) method (and other methods) uses wallet instead of self. This is technically okay in the __init__ method, but doesn't follow convention and may confuse readers. In fact, the add_funds(amount) method does not even have a self parameter (receives the instance as amount), and wallet is not defined within the method.

2) Inconsistent naming scheme / improper use of encapsulation. The wallet.Owner attribute is in camel case (attributes in Python should be in snake_case such as owner). The __balance attribute is name-mangled when there isn’t any need for that. 

3) Lack of property/balance.setter decorators and no proper validation. get_balance() is a getter written like it’s a Java code snippet. Also, the balance(self, new_balance) function is supposed to be a setter but there are no decorators for that function. In addition, the validation in this function simply prints a warning and then sets the value regardless.


Phase 4: Final Reflection Questions

1. What mistake was made when trying to access atm.__pin? Why? AttributeError: 'ATM' object has no attribute '__pin'. Since the attribute was defined within the class using self.__pin, Python name-mangled it to _ATM__pin at compile-time. Since the name is now gone, an external attempt to access it will fail. (But the name atm._ATM__pin still works – this demonstrates that this is merely an impediment to access, not a security feature.)

2. How does @property allow me to modify implementation details or add validation without changing the public interface? Callers can use account.balance and account.balance = x just as they would use an ordinary attribute. Since the attribute is actually a property, I am able to do any validation (like checking for negative values and raising a ValueError if needed) and storing it as _balance. This way, even if I choose to change the storage method (for example, as cents in int or as Decimal), I only have to change the property accessors.

3. What abstraction principles were applied in the ATM class? The ATM class provides users with four basic functionalities which include authentication, balance inquiry, deposit/withdraw, and mini statement. In the background, it provides functions that include validation of amounts, validation of insufficient funds, transaction logging and ValueError exception for BankAccount class. The caller has no knowledge of _balance and _transactions and any errors appear as friendlier messages.
