from src.funcs.fact import *
from src.funcs.fibonacci import *
from src.funcs.sorts.bubble import *
from src.funcs.sorts.counting import *
from src.funcs.sorts.radix import *
from src.funcs.sorts.quick import *
from src.funcs.sorts.bucket import *
from src.funcs.sorts.heap import *


def main() -> None:
    print(factorial(5))
    print(factorial_recursive(5), end='\n\n')

    print(fibo(10))
    print(fibo_recursive(10), end='\n\n')

    print(bubble_sort([5, 2, 8, 2, 1]), end='\n\n')

    print(counting_sort([4, 2, 2, 2, -3, -8, 3, 0, -3, 1, 3, 0]), end='\n\n')

    print(radix_sort([1371371051334257, 4745, 24399293, 4745, 4748, 5, 276, 42, 5, 19, 20]), end='\n\n')
    print(radix_sort([291, 34, 18], 16), end='\n\n')

    print(quick_sort([9, -3, 5, 21, 6, 18, -6, -3, 1, 3, 5, 32]))
    print(quick_sort([9.3, -3.6, -3.5, -3.6, 10, 12.1]), end='\n\n')

    print(bucket_sort([9.3, -3.6, -3.5, -3, 10, 12.1, -100]))

    print(heap_sort([3, 1.5, -2.9, -2.95, 0, 4.7, -1, 3, 2, 4.7]))
    print(heap_sort([0]))


if __name__ == '__main__':
    main()
