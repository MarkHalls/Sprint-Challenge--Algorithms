"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


def count_th(word):
    def counter(word, count=0):
        # split word into an array so we can check the characters
        arr = list(word)

        # base case, we want to return the count if our arr is empty
        if len(arr) == 0:
            return count

        # if our arr is greater than 1 and begins with the letter t
        if arr[0] == "t" and len(arr) > 1:

            # check if the second letter is h
            if arr[1] == "h":
                # we found h so let's increment counter and remove the first
                # 2 items from the array
                count += 1
                arr.pop(0)
                arr.pop(0)
            else:
                # we didn't find h so let's just remove the t
                arr.pop(0)
        else:
            # we didn't find t so remove the first item
            arr.pop(0)

        # merge the word into a new string so we can start over
        new_word = "".join(arr)

        return counter(new_word, count)

    return counter(word)
