Reflection: OOP Fundamentals
Phase 1: Conceptual Check & Code Diagnosis

1. Conceptual Distinction

Encapsulation vs. Abstraction.**
Encapsulation is about *bundling data with the methods that operate on it and controlling access to that data*, so the object's internal state can only change in safe, intended ways. Abstraction is about *hiding complexity and exposing only what a user needs*, so the caller works with a simple interface instead of the implementation details.

Analogy (a pharmacy). The locked medicine cabinet behind the counter is encapsulation: customers can't grab drugs directly, and only the pharmacist changes the stock. The prescription window is abstraction: you hand over a prescription and receive medicine, without knowing how dosage checks, inventory, and insurance are processed.

Why `_attribute` is "convention-based non-public" and not truly private.
A single underscore is only a signal to other programmers: "this is internal, don't rely on it." Python does not enforce it. Anyone can still read or write `obj._attribute`, and tools like `from module import *` merely skip such names. Python follows a "we're all consenting adults" philosophy, so there is no compiler-enforced `private` keyword.

Name mangling with `__attribute`.
Inside a class body, Python rewrites an identifier that starts with two underscores (and doesn't end with two) to `_ClassName__attribute`. For example, `self.__pin` inside class `ATM` is stored as `_ATM__pin`. From the outside, `atm.__pin` fails, but `atm._ATM__pin` still works. Mangling exists mainly to avoid accidental name clashes in subclasses, not to provide real security.

2. Code Diagnosis

Flaws in `DigitalWallet`:

1. Wrong first parameter name. `__init__(wallet, ...)` (and later methods) don't use `self`. It technically works for `__init__` but breaks convention and confuses readers. Worse, `add_funds(amount)` has no `self` parameter at all, so it can't be called on an instance (it receives the instance as `amount`) and `wallet` is undefined inside it.
2. Naming convention violation / inconsistent encapsulation.** `wallet.Owner` uses a capitalized attribute (Python attributes should be `snake_case`, i.e. `owner`), while `__balance` is name-mangled without a good reason. A single-underscore `_balance` is the idiomatic non-public choice.
3. Missing `@property` / `@balance.setter` decorators and no real validation.** `get_balance()` is a Java-style getter, and the method `balance(self, new_balance)` is meant to be a setter but has no decorators. Also, its validation only *prints* a message and then still assigns the negative value. It should `raise ValueError` and not set the value.


Phase 4: Final Reflection Questions

1. What error occurred when accessing `atm.__pin` directly? Why?
`AttributeError: 'ATM' object has no attribute '__pin'`. Because the attribute was defined inside the class as `self.__pin`, Python name-mangled it to `_ATM__pin` at compile time. The name `__pin` no longer exists on the instance, so an outside lookup fails. (The mangled name `atm._ATM__pin` still works, which shows this is a deterrent against accidental access, not true security.)

2. How did `@property` let me change internals or add validation without altering the public API?
Callers use `account.balance` and `account.balance = x` exactly as they would with a plain attribute. Because `balance` is a property, I could put validation in the setter (rejecting negatives with `ValueError`) and store the value in `_balance`. If I later changed how the balance is stored (for example, in cents as an integer, or with a `Decimal`), I'd only edit the getter/setter, and no calling code would need to change.

3. How did the `ATM` class demonstrate abstraction?
The ATM gives users four simple operations: authenticate, check balance, deposit/withdraw, and mini statement. Behind them, it hides amount validation, insufficient-funds checks, transaction logging, and `ValueError` handling from `BankAccount`. The caller never touches `_balance` or `_transactions`, and errors are turned into friendly messages. `BankAccount` could change internally and the ATM's interface would stay the same.