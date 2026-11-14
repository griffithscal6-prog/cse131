# 1. Name:
#      Calvin Griffiths
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      This program asks the user to enter integers, finds groups of numbers that are already in ascending order, and
#      repeatedly merges those groups until all the numbers are sorted. It uses two fixed-size lists: a source list and
#      a destination list.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was keeping track of the indexes for the two sorted sub-lists while merging them into the
#      destination list. The program also needs to handle a pass with an odd number of sub-lists. In that case, the last
#      sub-list must be copied to the destination unchanged.
#     I added print statements to display the sub-lists being merged and the result of the merge. This helped me debug the
#     program and understand how the merge function works throughout each pass.
# 5. How long did it take for you to complete the assignment?
#      It took me about 2 hours to complete the assignment. I spent a lot of time debugging the merge function and
#      making sure that the indexes were being updated correctly. I also had to test the program with different inputs
#      to make sure it was working as expected. Overall, it was a challenging but rewarding experience.


def read_numbers() -> list[int]:
    """Read all integers from one space-separated line of user input."""
    while True:
        try:
            number_strings = input(
                "Enter the integers you want to sort, separated by spaces: "
            ).split()

            numbers = [0] * len(number_strings)

            for index in range(len(number_strings)):
                numbers[index] = int(number_strings[index])

            return numbers
        except ValueError:
            print("Please enter only whole numbers separated by spaces.")


def find_run_end(source: list[int], start: int) -> int:
    """Return the index immediately after an ascending run."""
    end = start + 1

    while end < len(source) and source[end - 1] <= source[end]:
        end += 1

    return end


def display_run(numbers: list[int], start: int, end: int) -> None:
    """Display the values between start and end, without changing the list."""
    output = "["

    for index in range(start, end):
        if index > start:
            output += ", "
        output += str(numbers[index])

    output += "]"
    print(output)


def merge_runs(
    source: list[int],
    destination: list[int],
    left_start: int,
    left_end: int,
    right_start: int,
    right_end: int,
    destination_start: int,
) -> int:
    """Merge two ascending runs and return the next destination index."""
    left_index = left_start
    right_index = right_start
    destination_index = destination_start

    # Compare the next unused value in each run and copy the smaller one.
    while left_index < left_end and right_index < right_end:
        if source[left_index] <= source[right_index]:
            destination[destination_index] = source[left_index]
            left_index += 1
        else:
            destination[destination_index] = source[right_index]
            right_index += 1

        destination_index += 1

    # Copy any values left in the left run.
    while left_index < left_end:
        destination[destination_index] = source[left_index]
        left_index += 1
        destination_index += 1

    # Copy any values left in the right run.
    while right_index < right_end:
        destination[destination_index] = source[right_index]
        right_index += 1
        destination_index += 1

    return destination_index


def copy_run(
    source: list[int],
    destination: list[int],
    source_start: int,
    source_end: int,
    destination_start: int,
) -> int:
    """Copy an unpaired ascending run and return the next destination index."""
    source_index = source_start
    destination_index = destination_start

    while source_index < source_end:
        destination[destination_index] = source[source_index]
        source_index += 1
        destination_index += 1

    return destination_index


def sub_list_sort(numbers: list[int]) -> list[int]:
    """Sort the numbers by repeatedly merging adjacent ascending runs."""
    source = numbers
    destination = [0] * len(source)
    size = len(source)

    if size < 2:
        return source

    pass_number = 1
    run_count = 0

    # Continue until a pass produces only one sorted run.
    while run_count != 1:
        source_index = 0
        destination_index = 0
        run_count = 0
        merge_number = 1

        print(f"\nPass {pass_number}")
        print("----------------------------------------")

        while source_index < size:
            left_start = source_index
            left_end = find_run_end(source, left_start)
            source_index = left_end

            if source_index < size:
                right_start = source_index
                right_end = find_run_end(source, right_start)
                source_index = right_end

                merge_start = destination_index

                print(f"Merge {merge_number}:")
                print("  Left run:  ", end="")
                display_run(source, left_start, left_end)
                print("  Right run: ", end="")
                display_run(source, right_start, right_end)

                destination_index = merge_runs(
                    source,
                    destination,
                    left_start,
                    left_end,
                    right_start,
                    right_end,
                    destination_index,
                )

                print("  Merged:    ", end="")
                display_run(destination, merge_start, destination_index)
                print()
                merge_number += 1
            else:
                # Copy an unpaired run without changing its order.
                print("Unpaired run copied without merging: ", end="")
                display_run(source, left_start, left_end)
                destination_index = copy_run(
                    source,
                    destination,
                    left_start,
                    left_end,
                    destination_index,
                )

            run_count += 1

        print("Array after this pass: ", end="")
        display_run(destination, 0, size)

        # Switch which list is the source and which is the destination.
        temporary = source
        source = destination
        destination = temporary
        pass_number += 1

    return source


def main() -> None:
    numbers = read_numbers()

    print("\nOriginal numbers: ", end="")
    display_run(numbers, 0, len(numbers))

    sorted_numbers = sub_list_sort(numbers)

    print("\nSorted numbers: ", end="")
    display_run(sorted_numbers, 0, len(sorted_numbers))


main()
