######
#day2#
######

It is really hard!

----------creat package----------

/home/guoxi/project/02.course/day2-bestpractices-1

###create python package

/home/guoxi/project/02.course/day2-bestpractices-1/animals

###test code####
 import animals

harmless_birds = animals.harmless.Birds()
harmless_birds.printMembers()

dangerous_fish = animals.dangerous.Fish()
dangerous_fish.printMembers()

###test code finish###

I forget record the process!!! But whatever, I have done it.

----------debug--------------
use pdb to find the bug

but i found the bug without debugger

I do not know how to describe it. but i finished it.


---------profiling-------

###using cProfile 

python -m cProfile matmult.py

optimize matmult.py  at line 9 and 14 !!!

###using line_profiler

###install line_profiler:
    pip install --user line_profiler
###test:
    /home/guoxi/.local/bin/kernprof work!

kernprof -l -v euler72.py
'''
/home/guoxi/.local/bin/kernprof -l -v euler72.py
30397485.0
Wrote profile results to euler72.py.lprof
Timer unit: 1e-06 s

Total time: 0.00714121 s
File: euler72.py
Function: gen_primes at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     4                                           @profile
     5                                           def gen_primes(n):
     6         1          2.6      2.6      0.0      l = range(2,n)
     7         1          0.6      0.6      0.0      primes = []
     8       999        474.3      0.5      6.6      for j in range(0,len(l)):
     9       998        317.3      0.3      4.4          p = True
    10      2968       1246.0      0.4     17.4          for d in primes:
    11      2967       2230.0      0.8     31.2              if(d > sqrt(l[j])):
    12       167         63.1      0.4      0.9                  break
    13      2800       1687.2      0.6     23.6              if(l[j] % d == 0):
    14       830        290.4      0.3      4.1                  p = False
    15       830        303.9      0.4      4.3                  break;
    16       998        425.1      0.4      6.0          if(p):
    17       168         94.7      0.6      1.3              primes.append(l[j])
    18                                           
    19         1          6.1      6.1      0.1      return primes

Total time: 0.202952 s
File: euler72.py
Function: factorize at line 21

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    21                                           @profile
    22                                           def factorize(n,primes):
    23      9999       3841.7      0.4      1.9      factors = []
    24      9999       3404.1      0.3      1.7      init_n = n
    25     96347      39335.8      0.4     19.4      for p in primes:
    26    118736      63768.8      0.5     31.4          while(n%p == 0):
    27     22389       9800.6      0.4      4.8              n = n/p
    28     22389       8709.3      0.4      4.3              factors.append(p)
    29     96347      54009.9      0.6     26.6          if(p > sqrt(n)):
    30      9999       4005.7      0.4      2.0              break
    31      9999       4933.5      0.5      2.4      if(n > 1):
    32      9596       3999.9      0.4      2.0          factors.append(n)
    33      9999       7142.6      0.7      3.5      return factors

Total time: 0.566468 s
File: euler72.py
Function: fast_phi at line 50

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    50                                           @profile
    51                                           def fast_phi(n,primes):
    52      9999     516029.9     51.6     91.1      factors = factorize(n,primes)
    53      9999       4003.1      0.4      0.7      phi = factors[0]-1
    54     31985      17361.6      0.5      3.1      for i in range(1,len(factors)):
    55     21986      10448.2      0.5      1.8          if(factors[i] == factors[i-1]):
    56      7685       4126.3      0.5      0.7              phi *= (factors[i]-1)*(factors[i])/(factors[i]-1)
    57                                                   else:
    58     14301       6999.1      0.5      1.2              phi *= (factors[i]-1)
    59      9999       7500.2      0.8      1.3      return phi
'''

this is the output
ok, line_profile is more easy to ready

So, euler72.py optimise speed at line 52

how to optimise matmult.py? maybe later i can do it

