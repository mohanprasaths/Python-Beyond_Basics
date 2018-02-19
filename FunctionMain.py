from Resolver.resolver import Resolver
from timeit import timeit

resolver = Resolver()
resolver("pluralsight.com")

timeit(setup='check cache working', stmt="resolver('pluralsight.com')", number=1)


