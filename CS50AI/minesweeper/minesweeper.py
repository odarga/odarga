import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        # If count equals to number of cells, all is mines
        if self.count == len(self.cells) and self.count != 0:
            return self.cells

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        # If count equals to zero, all is safe
        if self.count == 0:
            return self.cells

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        # Removing cell marked as mine and decreasing count by one
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        # Removing cell marked as safe
        if cell in self.cells:
            self.cells.remove(cell)

class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # Marking cell as one of the moves made
        self.moves_made.add(cell)
        # Marking cell as a safe
        self.mark_safe(cell)
        neighbour_cells = set()
        count_mines = 0
        # Finding neighbours
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                # Ignore the cell itself
                if (i, j) == cell:
                    continue
                # Ignore out of bounds
                if 0 <= i < self.height and 0 <= j < self.width:
                    # Ignore already determined cells
                    if (i, j) in self.mines or (i, j) in self.safes:
                        if (i ,j) in self.mines:
                            count_mines += 1
                        continue
                    else:
                        neighbour_cells.add((i, j))
        # Creating new sentence
        new_sentence = Sentence(neighbour_cells, count - count_mines)
        # Adding sentence to knowledge base
        self.knowledge.append(new_sentence)
        # Finding new cells can be marked
        known_mines = set()
        known_safes = set()
        if self.knowledge:
            for sentence in self.knowledge:
                known_mines = sentence.known_mines()
                known_safes = sentence.known_safes()
                if known_mines:
                    for i in known_mines.copy():
                        if i not in self.mines:
                            # Marking new mine
                            self.mark_mine(i)
                if known_safes:
                    for j in known_safes.copy():
                        if j not in self.safes:
                            # Marking new safe
                            self.mark_safe(j)
        cells_new = set()
        # Checking for subsets to infer new sentences
        for i in range(len(self.knowledge) - 1):
            for j in range(i + 1, len(self.knowledge)):
                # Checking if subset
                if self.knowledge[i].cells and self.knowledge[i].cells.issubset(self.knowledge[j].cells) and self.knowledge[i].cells != self.knowledge[j].cells:
                    # Calculating new count
                    count_new = self.knowledge[j].count - self.knowledge[i].count
                    # Removing subset cells
                    for k in self.knowledge[j].cells:
                        if k not in self.knowledge[i].cells:
                            cells_new.add(k)
                    # Creating inferred sentence
                    inferred_sentence = Sentence(cells_new, count_new)
                    # Adding inferred sentence to knowledge base
                    self.knowledge.append(inferred_sentence)
                    cells_new.clear()
                # Checking if subset
                elif self.knowledge[j].cells and self.knowledge[j].cells.issubset(self.knowledge[i].cells) and self.knowledge[i].cells != self.knowledge[j].cells:
                    # Calculating new count
                    count_new = self.knowledge[i].count - self.knowledge[j].count
                    # Removing subset cells
                    for k in self.knowledge[i].cells:
                        if k not in self.knowledge[j].cells:
                            cells_new.add(k)
                    # Creating inferred sentence
                    inferred_sentence = Sentence(cells_new, count_new)
                    # Adding inferred sentence to knowledge base
                    self.knowledge.append(inferred_sentence)
                    cells_new.clear()
        # Finding new cells can be marked
        known_mines = set()
        known_safes = set()
        if self.knowledge:
            for sentence in self.knowledge:
                known_mines = sentence.known_mines()
                known_safes = sentence.known_safes()
                if known_mines:
                    for i in known_mines.copy():
                        if i not in self.mines:
                            # Marking new mine
                            self.mark_mine(i)
                if known_safes:
                    for j in known_safes.copy():
                        if j not in self.safes:
                            # Marking new safe
                            self.mark_safe(j)

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        for i in range(0, self.height):
            for j in range(0, self.width):
                # Return first found move that is safe and not already made
                if (i, j) not in self.moves_made and (i, j) in self.safes:
                    return (i, j)
        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        for i in range(0, self.height):
            for j in range(0, self.width):
                # Return first found move that is not mine and not already made
                if (i, j) not in self.moves_made and (i, j) not in self.mines:
                    return (i, j)
        return None
