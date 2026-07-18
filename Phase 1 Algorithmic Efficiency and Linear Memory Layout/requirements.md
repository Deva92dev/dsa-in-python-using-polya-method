# Put Zero at end of an array 10/07/26

- If there is only one element in the array, process will not start and there will not no pointers to run.

- First Pointer will start from 0th index of the array and second pointer will start 1st index of the array.

- If both pointers are not pointing to "0", they will keep increasing their place by 1 and the process will stop if second pointer reached at the end of the array without any swapping at all.

- If first pointer points to non zero number and second pointer points to 0, then again both pointers will increase its place by 1

- If both the pointers point to "0", then only second pointer will increase its place by 1 and first pointer will remain at its place.

- Swapping will happen only if first pointer points to "0", and second pointer points to non zero number, meaning value of second pointer must not be equal to value of first pointer. And swapping will be done by using temporary variable. And values of pointer will be swapped and after swapping both pointers will increase its place by 1 respectively. and then that temporary variable will be ready to re-assign for next swap

- System rules
  - In python you can only swap the references not the pointers
  - To check your rules, you look at the data inside the box
  - To move to the next box, you increment the box number
  - values swap not the pointers itself

# Summing two distinct numbers to target, 11/07/26

- First Pointer will start at 0th index and move right and Second pointer will start at last index(arr.length - 1) and move left.

- If the sum of the values which are both pointers pointing at is less than the target, first pointer will increase its place by 1(move right)

- If the sum of the values which are both pointers pointing at is greater than the target, second pointer will decrease its place by 1(move left)

- If the sum of the values which are both pointers pointing at is equal to the target, we will return the indices of both pointers

- Both pointer must never access the same index because problem requires two distinct numbers

# Summing three distinct numbers to target, 14/07/26

- Solve Three dimensional problem in O(N^2) time requires freezing one dimension and then try to solve it for other two dimension. and also eliminate of dead space which is already covered by one dimension(means do not include that in further calculation).

- I took Three pointers and fixed first pointer at 0th index of array. And Then put second pointer and 1st index of array and third pointer at last index of array(arr.length - 1).

- So, after fixing the position of first pointer, we move second pointer one place right if sum of three is less than the target and if sum is more than the target, third pointer will move one place left.

- and if i did not get the required result, first pointer will move one place right and in that condition second pointer will be on next index of first pointer and third pointer at last index of array(arr.length - 1) and will do the same operation again till we get sum of three equal to target.

- condition will be for first pointer will traverse till the last index of array.
- second pointer traverse in right direction and third pointer traverse in left direction.

- range(len(my_array)) creates an iterable of indices starting from 0 up to len(my_array) - 1
- first pointer must stop 2 places before the end of array because it need space for other two pointers(think of an array have only 3 items)

# Maximum mathematical sum of contiguous sub-array of size k in an array, 18/07/26

- Will have two variables named, highest and current and one more window for tracking
- we will get the sum of first k elements of array and put the value in highest and current both.

- sum(islice(my_list, k)) calculates the sum of the first k elements of an iterable my_list. This approach is preferred over slicing (sum(my_list[:k])) when memory efficiency is critical, as islice (from the itertools module) extracts elements without creating an intermediate list copy

- And the loop will start from index k and traverse to end of array

- Now when sliding window moves right one place we will add last current value to new incoming element and subtract the leaving element and at this point we will compare which is bigger, current or highest.

- If current is bigger, we will update the value of highest with that current value and then sliding window will move right one place.
- If current is less than the highest, then no need to update value of highest and sliding window will move one place right.

- sliding window will run till the last element of array.
