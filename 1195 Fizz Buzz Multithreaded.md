## Description

Write a program that outputs the string representation of numbers from 1 to n, however:
```
If the number is divisible by 3, output "fizz".
If the number is divisible by 5, output "buzz".
If the number is divisible by both 3 and 5, output "fizzbuzz".
```
For example, for ```n = 15```, we output: ```1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz.```

Suppose you are given the following code:
```
class FizzBuzz {
  public FizzBuzz(int n) { ... }               // constructor
  public void fizz(printFizz) { ... }          // only output "fizz"
  public void buzz(printBuzz) { ... }          // only output "buzz"
  public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
  public void number(printNumber) { ... }      // only output the numbers
}
```
Implement a multithreaded version of ```FizzBuzz``` with four threads. The same instance of ```FizzBuzz``` will be passed to four different threads:

1.Thread A will call  ```fizz()``` to check for divisibility of 3 and outputs ```fizz```.
2.Thread B will call ```buzz()``` to check for divisibility of 5 and outputs ```buzz```.
3.Thread C will call ```fizzbuzz()``` to check for divisibility of 3 and 5 and outputs ```fizzbuzz```.
4.Thread D will call ```number()``` which should only output the numbers.

## Solution

```java
class FizzBuzz {
    private int n;
    private Lock mainLock;
    private Condition three;
    private Condition five;
    private Condition threeFive;
    private Condition number;
    private volatile int cur = 1;

    public FizzBuzz(int n) {
        this.n = n;
        this.mainLock = new ReentrantLock();
        three = mainLock.newCondition();
        five = mainLock.newCondition();
        threeFive = mainLock.newCondition();
        number = mainLock.newCondition();
    }

    // printFizz.run() outputs "fizz".
    public void fizz(Runnable printFizz) throws InterruptedException {
        mainLock.lock();
        while (cur <= n) {
            while ((cur % 3 != 0 || cur % 15 == 0) && cur <=n ) {
                three.await();
            }
            doPrint(printFizz);
        }
        mainLock.unlock();
    }

    // printBuzz.run() outputs "buzz".
    public void buzz(Runnable printBuzz) throws InterruptedException {
        mainLock.lock();
        while (cur <= n) {
            while ((cur % 5 != 0 || cur % 15 == 0) && cur <= n) {
                five.await();
            }
            doPrint(printBuzz);
        }
        mainLock.unlock();
    }

    // printFizzBuzz.run() outputs "fizzbuzz".
    public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        mainLock.lock();
        while (cur <= n) {
            while (cur % 15 != 0 && cur <= n) {
                threeFive.await();
            }

            doPrint(printFizzBuzz);
        }
        mainLock.unlock();
    }

    private void doPrint(Runnable printFizzBuzz) {
        if (cur > n) {
            sigAll();
        } else {
            printFizzBuzz.run();
            cur++;
            sig();
        }
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void number(IntConsumer printNumber) throws InterruptedException {
        mainLock.lock();
        while (cur <= n) {
            while ((cur % 3 == 0 || cur % 5 == 0) && cur <= n) {
                number.await();
            }

            while (cur <= n && cur % 3 != 0 && cur % 5 != 0) {
                printNumber.accept(cur);
                cur++;
            }
            if (cur > n) {
                sigAll();
            } else {
                sig();
            }
        }
        mainLock.unlock();
    }

    private void sigAll() {
        three.signal();
        five.signal();
        threeFive.signal();
        number.signal();
    }

    private void sig() {
        if (cur % 3 == 0 && cur % 5 == 0) {
            threeFive.signal();
        } else if (cur % 3 == 0) {
            three.signal();
        } else if (cur % 5 == 0) {
            five.signal();
        } else {
            number.signal();
        }
    }
}
```
