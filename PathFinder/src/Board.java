import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;

public class Board extends JPanel {
    private final int numOfCols;
    private final int numOfRows;

    private final Cell[] grid;
    private final ArrayList<Cell> stack;

    private final Cell start;
    private final Cell end;
    private Cell current;

    /**
     * Creates a new <code>JPanel</code> with a double buffer
     * and a flow layout.
     */
    public Board(int numOfCols, int numOfRows, int cellSize) {
        this.numOfCols = numOfCols;
        this.numOfRows = numOfRows;

        grid = new Cell[this.numOfCols * this.numOfRows];
        for (int j = 0; j < this.numOfRows; j++) {
            for (int i = 0; i < this.numOfCols; i++) {
                this.grid[i + j * this.numOfCols] = new Cell(i, j, cellSize);
            }
        }

        this.start = this.grid[0];
        this.start.getWalls()[3] = false;
        this.end = this.grid[grid.length - 1];
        this.end.getWalls()[1] = false;
        this.current = this.start;
        stack = new ArrayList<>();

        this.setBackground(Color.WHITE);

    }

    public int getIndex(int i, int j) {
        if (i < 0 || j < 0 || i >= this.numOfCols || j >= this.numOfRows) {
            return -1;
        }

        return i + j * this.numOfCols;
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);

        drawGrid(g);
        startMoving(g);
    }

    public void drawGrid(Graphics g) {
        for (int j = 0; j < this.numOfRows; j++) {
            for (int i = 0; i < this.numOfCols; i++) {
                this.grid[i + j * this.numOfCols].draw(g);
            }
        }
    }

    public void startMoving(Graphics g) {
        while (this.current != null) {
            this.current.setVisited(true);

            Cell next = this.current.findNeighbor(this);
            if (next != null) {
                stack.add(this.current);
                removeWalls(this.current, next);
                next.setVisited(true);
                this.current = next;
            } else if (!stack.isEmpty()){
                this.current = stack.remove(stack.size() - 1);
            } else {
                return;
            }
        }
    }

    private void removeWalls(Cell cellA, Cell cellB) {
        int diffX = cellA.getX() - cellB.getX();
        if (diffX == 1) {
            cellA.getWalls()[3] = false;
            cellB.getWalls()[1] = false;
        } else if (diffX == -1) {
            cellA.getWalls()[1] = false;
            cellB.getWalls()[3] = false;
        }

        int diffY = cellA.getY() - cellB.getY();
        if (diffY == 1) {
            cellA.getWalls()[0] = false;
            cellB.getWalls()[2] = false;
        } else if (diffY == -1) {
            cellA.getWalls()[2] = false;
            cellB.getWalls()[0] = false;
        }
    }

    public Cell[] getGrid() {
        return grid;
    }
}
