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
