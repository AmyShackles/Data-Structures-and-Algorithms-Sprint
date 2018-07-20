Exercise I:

a) I would say that this is O(n) as it's directly proportional to n input
b) I would say this is probably O(log n) because you're effectively halving the size of the data every iteration
c) This looks like it's going to be log(n^2) because it has nested for loops BUT when you run it with wildly different inputs, you get the same result and the same number of iterations, so I guess this is actually O(1). Oh! Because you're not ADDING to i, j, k when you do the comparisons. XD Always 63. XD
d) I would say probably O(n^2) because you have to interact with 'n' \* 2 because of the nested for loop
e) O(n^3) because of the nesting? Really kind of guessing here, if I'm honest.
f) This is recursive, but from testing it, it looks like it only runs as many many times as whatever's given for 'n', so I'm going to go with O(n) for this one.
g) This is also recursive and again from testing it, it looks like it only runs as many times as whatever the input is for 'n', so I'd go with O(n)

Exercise II:

a) for i, j in arr:
if j >= i:
return max(arr[j] - arr[i])

b) Can't. Prompt isn't giving a ratio of dropped eggs, just broken eggs. The solution for not having broken eggs is stop going to f floors and higher when you're a clumsy egg carrier.
Really, this could be computed by trying a floor right around the middle of all the floors. If the egg breaks, go down the number of floors / 2. If the egg doesn't break, go up the number of floors / 2. Keep dividing by 2 until you find the optimal floor of egg breakage. I'm unable to put that into code in a short amount of time, but that's the heuristic I'd use.

Exercise III:
a) Running time of a quicksort where the pivot is the first element and it's an already sorted list is O(n^2) because it has to check literally every item in the array and change the pivot every time in order to check that it's sorted.

b) The average running time for a quicksort is O(n log n) but the best case is O(n) because best case in an equally distributed array is that it's always going to choose a pivot where it can do the operation needed to be done.

Example code:
Exercise I:
a)
Assume input 10!
a = 0
while (0 < 10 _ 10 _ 10)
0 = 0 + 10 \* 10

    a = 100
    while (100 < 1000)
        100 = 100 + 10 * 10

    a = 1100 (suddenly regret trying this with 10)

    Assume input 4:
    a = 0
    while (0 < 4 * 4 * 4)
        0 = 0 + 4 * 4

    a = 16
    while (16 < 64)
        16 = 16 + 4 * 4

    a = 32
    while (32 < 64)
        32 = 32 + 16

    a = 48
    while (48 < 64)
        48 = 48 + 16
        end while

b)
i = array.length - 1;
so n would be i + 1
Let's go with...
i = 5
n = 6
x = 10
array = [5, 4, 8, 7, 2, 12]

    while array[i] > x and i >= 0
        i = i/2

    while array[5] > 10 and 5 >= 0
        5 = 5/2

    while 12 > 10 and 5 >= 0
        i = 5/2 (2.5)

    while ... this is poorly constructed, why isn't there rounding?
    Anyway, 2, 2.5, and 3 are not greater than 5

c) sum = 0
Okay, so say n is 2
for (i = 0; i < Math.sqrt(2) / 2; i++)
for (j = i; j < 8 + i; j++)
for (k = j; k < 8 + j; k++)
sum++

    Never mind, I'm just going to start testing in repl.it.
    sum = 0;

d) for (i = 1; i < n; i \*= 2)
for (j = 0; j < n; j++)
sum++;

e) sum = 0;
for (i = 0; i < n; i++)
for (j = i + 1; j < n; j++)
for (k = j + 1; k < n; k++)
for (l = k + 1; l < 10 + k; l++)
sum++

f) bunnyEars = function (bunnies) {
if (bunnies === 0) return 0;
return 2 + bunnyEars(bunnies - 1)
}

g) search = function (array, arraySize, target) {
if (arraySize > 0) {
if (array[arraySize - 1] === target) return true
else return search(array, arraySize-1, target)
}
return false;
}
