"""List Practice

Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.

    For example::

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """
    for item in items:
        print item
        
    


def long_words(words):
    """Return words in input list that longer than 4 characters.

    For example::

        >>> long_words(["hello", "a", "b", "hi", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

    (If there are duplicates, show both --- notice "bacon" appears
    twice in output)

    If no words are longer than 4 characters, return an empty list::

        >>> long_words(["all", "are", "tiny"])
        []
    """
    new_list = [word for word in words if len(word) > 4]
    return new_list

        

def n_long_words(words, n):
    """Return words in list longer than `n` characters.

    For example::

        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "bacon", "bacon"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'bacon', 'bacon']

        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """
    new_list = [word for word in words if len(word) > n]
    return new_list


def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `min()`!

    For example::

        >>> smallest_int([-5, 2, -5, 7])
        -5

        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return `None`::

        >>> smallest_int([]) is None
        True
    """
    # if the list is empty return None
    if len(numbers) == 0:
        return None 
    
    #setting the smallest int as the first item in numbers:
    int_smallest = numbers[0]
    #iterating over the numbers list
    for number in numbers:
        #if the list is not empty check if any number is smaller than int_smallest, if yes, rebinding that value to int_smallest
        if int_smallest > number:
            int_smallest = number
    return int_smallest
            


def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `max()`!

    For example::

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None::

        >>> largest_int([]) is None
        True
    """
    # if the list is empty return None
    if len(numbers) == 0:
        return None 
    
    #setting the largest int as the first item in numbers:
    int_largest = numbers[0]
    #iterating over the numbers list
    for number in numbers:
        #if the list is not empty check if any number is larger than int_largest, if yes, rebinding that value to int_largest
        if int_largest < number:
            int_largest = number
    return int_largest
    


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.

    For example::

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off
    the half::

        >>> halvesies([1, 5])
        [0.5, 2.5]
    """
    halvsies_list = [(float(number)/2) for number in numbers]
    return halvsies_list


def word_lengths(words):
    """Return the length of words in the input list.

    For example::

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """
    word_length_list = []
    #iterating over the words list
    for word in words:
        #initializing a counter to count letters in each word
        count = 0
        #iterating over letter in each word
        for letter in word:
            count +=1
        word_length_list.append(count)
    return word_length_list


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.

    For example::

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero::

        >>> sum_numbers([])
        0
    """
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers += number
    return sum_of_numbers



def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.

    For example::

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in input, the product is zero::

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::

        >>> mult_numbers([])
        1
    """
    product = 1
    for number in numbers:
        product *= number
    return product


def join_strings(words):
    """Return a string of all input strings joined together.

    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.

    For example::

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string::

        >>> join_strings([])
        ''
    """
    new_string = ''
    for word in words:
        new_string += word
    return new_string



def average(numbers):
    """Return the average (mean) of the list of numbers given.

    For example::

        >>> average([2, 4])
        3.0

    This should handle cases where the result isn't an integer::

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.

    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
    """
    sum_of_numbers = 0
    average_of_numbers = 0
    for number in numbers:
        sum_of_numbers += float(number) 
        average_of_numbers = float(sum_of_numbers)/len(numbers)
    return average_of_numbers


def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".

    For example::

        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course::

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """
    return ', '.join(words)
       


def reverse_list(items):
    """Return the input list, reversed.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    You should do this without changing the original list::

        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """
    reversed_list = []
    #initializing last index 
    index_last = len(items)-1
    #Looping over the list items until we reach the first item
    while index_last >= 0:
        #appending the last item in each loop to the reversed_list
        reversed_list.append(items[index_last])
        index_last -= 1

    return reversed_list

def reverse_list_in_place(items):
    """Reverse the input list `in place`.

    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]

        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """
    #initializing first index and last index
    index_first = 0
    index_last = len(items) - 1
    # Looping over the list until first index equals last (in case of odd number of items) or first index is less than last (in case of even items)
    while index_first <= index_last:
        #storing the item at first index in a temporary variable before rebinding first and last items
        temp_first = items[index_first]
        items[index_first] = items[index_last]
        items[index_last] = temp_first
        #moving the first index forward by one and last index back by one to rebind the next set of items
        index_first += 1
        index_last -=1
    return 




def duplicates(items):
    """Return list of words from input list which were duplicates.

    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.

    For example::

        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']

        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]

    You should do this without changing the original list::

        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']

        >>> orig
        ['apple', 'apple', 'berry']
    """
    duplicates_list = []
    #iterating over the items in the items list by index
    for idx in range(len(items)):
        #iterating over the remaining items in the items list by index
        for inner_index in range(idx+1,len(items)):
            #if item at idx is present at a later index
            if items[idx] == items[inner_index]:
                #if the item is not already present in the duplicates list, add it to the duplicates list
                if items[idx] not in duplicates_list:
                    duplicates_list.append(items[idx])
    #return the sorted list of duplicates
    return sorted(duplicates_list)                    

def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word.

    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.

    **DO NOT** use the `list.index()` method.

    For example::

        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]

    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")

    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::

        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]

    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """

    

    list_of_indices = []
    # iterating over the list of words 
    for word in words:
        #iterating over each letter of each word by index
        for idx in range(len(word)):
            #checking to see if the letter at any index matches the argument letter and adding only the first index to the list of indices or adding None
            if word[idx] == letter:
                list_of_indices.append(idx)
                break
            elif letter not in word:
                list_of_indices.append(None)
                break
    return list_of_indices

    
  



#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")
