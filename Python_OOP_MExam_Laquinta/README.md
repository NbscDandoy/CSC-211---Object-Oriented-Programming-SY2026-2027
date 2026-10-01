Submission Create a Grit repository Python_OOP_MExam_YourSurname. Add five runnable files named exercise_26.py through exercise_30.py and a README.md with Python 3 run instructions. Email your instructor the repository URL. if the repository is private, grant your instructor access before sending the link.

implement the required classes in each file. the code blocks give the variables and calls your program must suport; they are not thee class solutions. Run each file and comfirm its output matches the block shown. Equivalent working implementations earn credit. Each Exercise is worth 15 points.

#26 classes instances and methods 15 points.
implement Player with _init_(name, score=0), independent name and score instance attributes, and add_points(points), which updates and returns that player's score.

#27 classes attributes and shadowing 15 points.
implement Device with a class attribute room initially set to "Lab 1" and an initializer storing each assest_tag. The given calls change the class attribute, then shadow it on one instance.

#28 encapsulation with methods 15 points.
implement BankAccount with _balance, _init_(initial_balance=0), get_balance(), deposit(amount), and withdraw(amount). Raise ValueError for a negative initial balance, nonpositive deposits or withdrawals, and withdrawals exceeding the balance.

#29 properties and validation 15 points.
implement Product with name, a validating price property backed by_price, and total(quantity). Reject any initial or assigned price of 0 or less with ValueError.

#30 abstractiong and independent instance state 15 points.
implement ReadingList with a seperate_books list per instance, add_book(title), count() and titles(). Reject blank or whitespace-only titles with ValueError. Return a copy from titles() so callers cannot modify the internal list.
