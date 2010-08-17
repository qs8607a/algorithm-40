#!/usr/bin/python
# -*- coding: utf-8 -*-
# reference: http://en.wikipedia.org/wiki/Knapsack_problem
 
# 0-1 $B%J%C%W%5%C%/LdBj(B (2$B<!85F0E*7W2hK!(B)
# items = [{'w':weight, 'v':value}, {...}, {...}]
def knapsack_01(items, capacity):
  dp = [[0 for row in xrange(capacity+1)] for col in xrange(len(items)+1)]
  for c in xrange(1, capacity+1):
    print 'c = ', c, ' ////////////////////'
    for n in xrange(1, len(items)+1):
      cur = items[n-1]
      print 'cur = ', cur
      if cur['w'] <= c:
        left = dp[n-1][c - cur['w']] + cur['v']
        top  = dp[n-1][c]
        print 'left = ', left, ', top = ', top
        dp[n][c] = left if left > top else top
      else:
        dp[n][c] = dp[n][c-1]
      
      for i in xrange(len(dp)):
        print dp[i]
      print ''
  return dp[-1][-1]
 
# unbound $B%J%C%W%5%C%/LdBj(B (1$B<!85F0E*7W2hK!(B)
# items = [{'w':weight, 'v':value}, {...}, {...}]
def knapsack_123(items, capacity):
  dp = [0 for i in xrange(capacity+1)]
  for c in xrange(1, capacity+1):
    candidates = [item['v'] + dp[c-item['w']]
                  for item in items if item['w'] <= c]
    dp[c] = max(candidates) if candidates else 0
  return dp[-1]
 
if __name__ == '__main__':
  sample_data = [{'w':2, 'v':4},
                 {'w':2, 'v':5},
                 {'w':1, 'v':2},
                 {'w':3, 'v':8}]
 
  print knapsack_01(sample_data,  4)
  print knapsack_123(sample_data, 7)
