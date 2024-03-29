### Sorting Parameters
**1. Stability:-**
```
A sorting algorithm is stable if it preserves the relative order of equal elements after
sorting.
```
**2. In place:-**
```
A sorting algorithm is in-place if it sorts using only O(1) auxiliary memory (not counting
the array that needs to be sorted).
```
**3. Best case complexity:-**
```
A sorting algorithm has a best case time complexity of O(T(n)) if its running time is at
least T(n) for all possible inputs.
```
**4. Average case complexity:-**
```
A sorting algorithm has an average case time complexity of O(T(n)) if its running time,
averaged over all possible inputs, is T(n).
```
**5. Worst case complexity:-**
```
A sorting algorithm has a worst case time complexity of O(T(n)) if its running time is at
most T(n).
```

## Stability in sorting
Stability in sorting means whether a sort algorithm maintains the relative order of the equals keys of the original
input in the result output.
So a sorting algorithm is said to be stable if two objects with equal keys appear in the same order in sorted output
as they appear in the input unsorted array.

```
Consider a list of pairs:
(1, 2) (9, 7) (3, 4) (8, 6) (9, 3)
Now we will sort the list using the first element of each pair.
A stable sorting of this list will output the below list:
(1, 2) (3, 4) (8, 6) (9, 7) (9, 3)
Because (9, 3) appears after (9, 7) in the original list as well.
An unstable sorting will output the below list:
(1, 2) (3, 4) (8, 6) (9, 3) (9, 7)
Unstable sort may generate the same output as the stable sort but not always.
```
Well-known stable sorts:
- Merge sort
- Insertion sort
- Radix sort
- Tim sort
- Bubble Sor

Well-known unstable sorts
- Heap sort
- Quick sort

## Bubble Sort Parameters
- Stable: Yes
- In place: Yes
- Best case complexity: O(n)
- Average case complexity: O(n^2)
- Worst case complexity: O(n^2)
- Space complexity: O(1)


The BubbleSort compares each successive pair of elements in an unordered list and inverts the elements if they
are not in order.The bubble sort uses a straightforward logic that works by repeating swapping the adjacent elements if they are not in the right order. It compares one pair at a time and swaps if the first element is greater than the second element; otherwise, move further to the next pair of elements for comparison.

The following example illustrates the bubble sort on the list {6,5,3,1,8,7,2,4} 
(pairs that were compared in each step are encapsulated in '**'):

```
{6,5,3,1,8,7,2,4}
{**5,6**,3,1,8,7,2,4} -- 5 < 6 -> swap
{5,**3,6**,1,8,7,2,4} -- 3 < 6 -> swap
{5,3,**1,6**,8,7,2,4} -- 1 < 6 -> swap
{5,3,1,**6,8**,7,2,4} -- 8 > 6 -> no swap
{5,3,1,6,**7,8**,2,4} -- 7 < 8 -> swap
{5,3,1,6,7,**2,8**,4} -- 2 < 8 -> swap
{5,3,1,6,7,2,**4,8**} -- 4 < 8 -> swap
```
After one iteration through the list, we have {5,3,1,6,7,2,4,8}. Note that the greatest unsorted value in the array
(8 in this case) will always reach its final position. Thus, to be sure the list is sorted we must iterate n-1 times for lists
of length n.
