# from generators.genetators import rand_int_array, nearly_sorted, reverse_sorted, rand_float_array, many_duplicates
from src import bubble_sort, quick_sort, heap_sort, counting_sort, radix_sort, bucket_sort, Stack, Queue, \
    fibo, fibo_recursive, factorial, factorial_recursive


# GENERATORS = [rand_int_array, rand_float_array, nearly_sorted, reverse_sorted, many_duplicates]
ALL_SORTS = [bubble_sort, quick_sort, heap_sort, counting_sort, radix_sort, bucket_sort]
FLOAT_SORTS = [bubble_sort, quick_sort, heap_sort, bucket_sort]

# TEST_GENERATORS = {
#     'randint': rand_int_array,
#     'nearly': nearly_sorted,
#     'reverse': reverse_sorted,
#     'randfloat': rand_float_array,
#     'duplicates': many_duplicates
# }

ALGORITHMS = {
    'bubble': bubble_sort,
    'quick': quick_sort,
    'heap': heap_sort,
    'counting': counting_sort,
    'radix': radix_sort,
    'bucket': bucket_sort
}

STRUCTURS = {
    'stack': Stack,
    'queue': Queue
}

MATH_FUNCS = {
    'fib': fibo,
    'fib_r': fibo_recursive,
    'fact': factorial,
    'fact_r': factorial_recursive
}
