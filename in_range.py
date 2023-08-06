def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    # YOUR CODE HERE

    min_arr = min(nums)
    max_arr = max(nums)
    #lowest
    if min_arr > lowest:
        print(str(min_arr) + " " + "fits")
    else:
      print(str(lowest) + " " + "fits")

    #highest
    if max_arr > highest:
      print(str(highest) + " " + "fits")
    else:
      print(str(max_arr) + " " + "fits")



in_range([10, 20, 30, 40, 50], 15, 30)
