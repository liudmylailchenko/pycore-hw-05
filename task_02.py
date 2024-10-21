from typing import Generator
import re

def generator_numbers(text: str) -> Generator[int, None, None]:
  list = text.split()
  
  for i in list:
    if re.match(r'\d+\.\d+|\d+', i):
         yield float(i)
    else:
        continue

def sum_profit (text: str, generator: Generator[int, None, None]) -> float:
    gen = generator(text)
    sum = 0
    while True:
        try:
            sum += next(gen)
        except StopIteration:
            break
    return sum
