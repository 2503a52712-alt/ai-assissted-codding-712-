## C++
#include <iostream>
#include <stdexcept>
from numpy import std


using namespace std;

long long factorial(int n) {
    if (n < 0) {
        throw invalid_argument("Factorial is not defined for negative numbers.");
    }
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int main() {
    cout << factorial(5) << endl;
    return 0;
}

### Python

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))