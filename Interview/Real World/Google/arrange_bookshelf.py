def sort_bookshelf(bookshelf):
    # Use the left arm to pick up the first book
    left_arm_book = bookshelf[0]

    # Use the right arm to pick up the second book
    right_arm_book = bookshelf[1]

    # Compare the two books and determine which one comes first in alphabetical order
    if left_arm_book > right_arm_book:
        # If the left arm book comes after the right arm book in alphabetical order,
        # then swap the two books
        bookshelf[0] = right_arm_book
        bookshelf[1] = left_arm_book

    # Repeat the process for the rest of the books on the shelf
    for i in range(2, len(bookshelf)):
        # Pick up the next book with the left arm
        left_arm_book = bookshelf[i]

        # Use the right arm to find the correct position for the left arm book
        for j in range(i - 1, -1, -1):
            right_arm_book = bookshelf[j]
            if left_arm_book < right_arm_book:
                # Shift the right arm book one position to the right to make room for the left arm book
                bookshelf[j + 1] = right_arm_book
                bookshelf[j] = left_arm_book
            else:
                # The left arm book belongs after the right arm book, so we can stop searching
                break

    # Return the sorted bookshelf
    return bookshelf


# Test the function
bookshelf = ["cat", "apple", "dog", "banana"]
print(sort_bookshelf(bookshelf))  # should print ['apple', 'banana', 'cat', 'dog']


# This code uses two "arms" represented by variables left_arm_book and right_arm_book to pick up and compare books on the bookshelf. The left arm starts at the beginning of the shelf and moves forward, while the right arm starts at the position just before the left arm and moves backwards. The two arms work together to insert the left arm book into its correct position in the sorted portion of the shelf.
