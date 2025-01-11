def _squares(n):
    """
    Arguments:
        n (int): arbitray integer
        
    Returns:
        a list of squares up to the value of ``n``.
    """

    return [ 
        i*i 
        for i in range(1, n+1) 
        if i*i < n 
    ]

def primes(n):
    """
    Arguments:
        n (int): arbitrary integer
    Returns:
        A list of primes up to the values of ``n``
    """
    
    sqs = _squares(n)
    sieve = {
        x: True
        for x in range(2,n+1)
    }

    # NOTE: len(sqs) + 2 gives the next closest root of a perfect square
    for i in range(2, len(sqs) + 2):
        if sieve[i]:
            for j in range(1+1, n // i + 1):
                sieve[i*j] = False

    return [ k for k,v in sieve.items() if v ]

if __name__== "__main__":
    print(primes(300))