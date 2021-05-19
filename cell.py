class Cell:
    """
    Basic cell in the matrix which tracks True/False and color.
    """

    color_map = {True: "BLACK", False: "WHITE"}

    def __init__(self, color="WHITE", val=False) -> None:
        self.color = color
        self.val = val

    def __repr__(self):
        if self.val:
            return "  X  "
        else:
            return "  _  "
