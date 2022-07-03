import java.awt.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Cell {
    private final int x;    // column index
    private final int y;    // row index
    private boolean visited;

    private final int size;

    private final boolean[] walls = {true, true, true, true};

    public Cell(int x, int y, int size) {
        this.x = x;
        this.y = y;
        this.visited = false;
        this.size = size;
    }

    public Cell findNeighbor(Board board) {
        List<Cell> neighbors = new ArrayList<>();

        Cell[] grid = board.getGrid();

        int topIndex = board.getIndex(this.x, this.y - 1);
        if (topIndex != -1 && !grid[topIndex].isVisited()) {
            neighbors.add(grid[topIndex]);
        }

        int rightIndex = board.getIndex(this.x + 1, this.y);
        if (rightIndex != -1 && !grid[rightIndex].isVisited()) {
            neighbors.add(grid[rightIndex]);
        }

        int bottomIndex = board.getIndex(this.x, this.y + 1);
        if (bottomIndex != -1 && !grid[bottomIndex].isVisited()) {
            neighbors.add(grid[bottomIndex]);
        }

        int leftIndex = board.getIndex(this.x - 1, this.y);
        if (leftIndex != -1 && !grid[leftIndex].isVisited()) {
            neighbors.add(grid[leftIndex]);
        }

        if (neighbors.size() > 0) {
            Random rand = new Random();
            int index = rand.nextInt(neighbors.size());
            return neighbors.get(index);
        } else {
            return null;
        }
    }

    public boolean isVisited() {
        return this.visited;
    }

    public void setVisited(boolean visited) {
        this.visited = visited;
    }

    @Override
    public String toString() {
        return "Cell{" +
                "x=" + x +
                ", y=" + y +
                ", size=" + size +
                '}';
    }

    public void draw(Graphics g) {
        Graphics2D g2 = (Graphics2D) g;
        g2.setStroke(new BasicStroke(5.0f));
        g2.setColor(Color.DARK_GRAY);

        int PAD = 20;

        int x0 = this.x * this.size + PAD;
        int y0 = this.y * this.size + PAD;

        if (this.walls[0]) {
            g2.drawLine(x0, y0, x0 + this.size, y0);
        }

        if (this.walls[1]) {
            g2.drawLine(x0 + this.size, y0, x0 + this.size, y0 + this.size);
        }

        if (this.walls[2]) {
            g2.drawLine(x0 + this.size, y0 + this.size, x0, y0 + this.size);
        }

        if (this.walls[3]) {
            g2.drawLine(x0, y0 + this.size, x0, y0);
        }

        if (this.visited) {
            g2.setColor(Color.WHITE);
            g2.fillRect(x0, y0, this.size, this.size);
        }
    }

    public int getX() {
        return this.x;
    }

    public int getY() {
        return this.y;
    }

    public boolean[] getWalls() {
        return this.walls;
    }
}
