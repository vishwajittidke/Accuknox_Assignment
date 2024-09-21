Answers to the Questions given:  

Question 1:

1. In this example, So I have made a Signal Handler which sleeps for 5 seconds and hence that the signals are synchronously executed.
2. After calling the MyModel.objects.create(), the handler will delay the program for 5 seconds, proving that signals are synchronously executed.
3. Then after you will see "Model instance created" printed after the signal finishes its processing, confirming synchronous execution.


Question 2:

1. By default, the Django signals do run in the same thread as the caller. I have used python'S threading library to print the current thread.
2. Both the main thread and the signal handler print the current thread name.
3. You will see that the thread name will be printed in both places is the same, proving that signals run in the same thread as the caller by default.


Question 3:

1. Yes, Django signals run in the same database transaction as the caller by default. To demonstrate this, we can raise 2.an exception in the signal handler to see if it rolls back the transaction.
2. When MyModel.objects.create() is called, the signal handler raises an exception, which should cause the entire transaction to roll back.
3. After the exception, the count of MyModel objects will be 0, showing that the signal runs in the same transaction and causes a rollback when an exception occurs.


Topic: Custom classes in Python:

1. The __init__() method initializes the rectangle with length and width.
2. The __iter__() method defines the behavior when the object is iterated over, first yielding the length and then the width.