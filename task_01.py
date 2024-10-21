def caching_fibonacci():
    cache = {}

    def fibonacci(n: int) -> int:
        if not isinstance(n, int):
            return 'n must be an integer'
        
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci