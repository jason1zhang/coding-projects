import javax.swing.*;
import java.awt.*;

public class PathFinder extends JFrame {
    private final static int WIDTH = 800;
    private final static int HEIGHT = 800;

    private final static int COLS = 15;   // number of cells in the col
    private final static int ROWS = 15;   // number of cells in the row

    private final static int PAD = 20;

    private final Board maze;

    public static void main(String[] args) {
        SwingUtilities.invokeLater(PathFinder::new);
    }

    public PathFinder() {
        super("Path Finder");
        setSize(WIDTH, HEIGHT);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout(5, 5));
        setResizable(false);
        setBackground(Color.BLACK);
        setVisible(true);

        int PAD = 20;   // pad size to the border
        int size = (WIDTH - 4 * PAD) / COLS;

        this.maze = new Board(COLS, ROWS, size);
        this.maze.setSize(new Dimension(getWidth() - PAD, getHeight() - PAD));
        add(this.maze, BorderLayout.CENTER);
        this.maze.repaint();
    }
}
