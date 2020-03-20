class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l  # The list the robot is tasked with sorting
        self._item = None  # The item the robot is holding
        self._position = 0  # The list position the robot is at
        self._light = "OFF"  # The state of the robot's light
        self._time = 0  # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        """
        My initial thought is to use bubble sort for this since we can only hold one item at a time. 
        if we start at the beginning of the list and compare the held item to see if it's larger
        we can move the largest item to the end of the list and start over. 
        This is going to be pretty slow though because we'd have to start at the beginning each time. 

        The light indicates whether we've swapped something this pass

        move right swapping the largest numbers until you reach the end
        then move left swapping the smallest numbers until you reach the end. 

        if the light is on and you reach the left end, move right until you find None and swap the currently held item. 

        [1 3 4 5 6]
        1 is held
        [N 3 4] move right holding 1
        [N 1 4] 3 is bigger than 1 so swap it (turn on the light too)
        [N 1 4] 4 is bigger than 3 and we're at the end of the list so hold 3
        [N 1 4] move left holding 3
        [N 3 4] 1 is less than 3 so swap it
        [N 3 4] move left holding 1
        [1 3 4] we've reached the end so swap 1 with None
        [1 3 4] 1 is bigger than None so swap it
        [1 N 4] increment None and repeat

        rules: 

        Starting: None (cursor), None is always swapped
        move right, if held is bigger or equal, swap until you reach the end
        move left, if held is smaller or equal, swap until you reach None
        When you reach None, swap and move right one. 

        repeat until none is at the end of right

        improvement: if swapped number has been swapped with a number other than None, turn light on
            if the light stayed off when you reach the end of right, move left and swap with None, array is sorted
        
        """

        # start by swapping the first item with the held None
        self.swap_item()

        def sorter():
            # first base case, if we're at the end of the list, return
            if self.can_move_right() == False:
                return

            while self.can_move_right():
                self.move_right()
                # if we're holding the None item, swap it
                if self.compare_item() is None:
                    self.swap_item()
                elif self.compare_item() == -1:
                    self.swap_item()

            # second base case, the end of the list equals None.
            if self.compare_item() is None:
                self.swap_item()
                return
            # we aren't holding None at the end of the list so
            # check if held is bigger than end of list
            elif self.compare_item() >= 0:
                self.swap_item()

            # now we bubble sort the smallest items until we reach None
            # this will make sure the smallest item is put where None currently is
            while self.can_move_left() and self.compare_item() is not None:
                self.move_left()
                if self.compare_item() is None:
                    self.swap_item()
                elif self.compare_item() == 1:
                    self.swap_item()

            sorter()

        sorter()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [
        15,
        41,
        58,
        49,
        26,
        4,
        28,
        8,
        61,
        60,
        65,
        21,
        78,
        14,
        35,
        90,
        54,
        5,
        0,
        87,
        82,
        96,
        43,
        92,
        62,
        97,
        69,
        94,
        99,
        93,
        76,
        47,
        2,
        88,
        51,
        40,
        95,
        6,
        23,
        81,
        30,
        19,
        25,
        91,
        18,
        68,
        71,
        9,
        66,
        1,
        45,
        33,
        3,
        72,
        16,
        85,
        27,
        59,
        64,
        39,
        32,
        24,
        38,
        84,
        44,
        80,
        11,
        73,
        42,
        20,
        10,
        29,
        22,
        98,
        17,
        48,
        52,
        67,
        53,
        74,
        77,
        37,
        63,
        31,
        7,
        75,
        36,
        89,
        70,
        34,
        79,
        83,
        13,
        57,
        86,
        12,
        56,
        50,
        55,
        46,
    ]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
