class Hanoi:

    @staticmethod
    def hanoi(disks: int, source: str, helper: str, destination: str) -> None:
        """
        Recursive function for Tower of Hanoi
        """
        # Base condition
        if disks == 1:
            print("Disk {} moves from tower {} to tower {}.".format(disks, source, destination))
            return

        # Recursive calls in which function calls itself
        Hanoi.hanoi(disks - 1, source, destination, helper)
        print("Disk {} moves from tower {} to tower {}.".format(disks, source, destination))
        Hanoi.hanoi(disks - 1, helper, source, destination)
