from linked import *



def isPalindrome(head):
    if head is None or head.next is None:
        return True

    temp = head
    reverseHead = reverseLL(head)  # Reverse a copy, not the original

    while temp and reverseHead:
        if temp.data != reverseHead.data:
            print("Entered the non-palindrom block")
            return False
        print(f"Value Equal: Head: {temp.data} = Reversed: {reverseHead.data}")
        temp = temp.next
        reverseHead = reverseHead.next

    return True

# Test
head = createLlFromList([1, 2, 1, 1])
print_ll(head)
isPal = isPalindrome(head)
print("Is Palindrome:", isPal)
