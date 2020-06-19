#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

Starting from inner, you do that inner operation once per n The while operation also checks once for the condition a = 0 is one

Those are three constants, which we drop, so I think it's O(n) is correct


b)O(n log n)

Because J is multiplied by 2 each time you are basically going to ever run half of n meaning the while loop is logarithmic and the while loop will be repeated N times by the for loop


c)O(n)

The recursive function returns once per n, so I believe this one is also O(n)



## Exercise II

We'd drop the egg at the middle story of the building If the egg doesn't break at that height, we go half-way from the middle to the top floor and drop.

If the egg does break at that height, we go half way from the middle to the bottom floor and drop

We keep doing this, cutting the number of floors to check in half until we divide the floors up so there's only one possible answer.

This is O(log(n)) since with each pass, the number of possibilities(n) is cut in half
