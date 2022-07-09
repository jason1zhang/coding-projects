package com.algs4.app;

import com.algs4.ds.Graph;
import com.algs4.io.In;
import com.algs4.io.StdOut;

public class DepthFirstSearch {
    private boolean[] marked;       // marked[v] = is there an s-v path?
    private int count;              // number of vertices connected to s

    /**
     * Computes the vertices in graph {@code G} that are
     * connected to the source vertex {@code s}.
     *
     * @param G the graph
     * @param s the source vertex
     * @throws IllegalArgumentException unless {@code 0 <= s < V}
     */
    public DepthFirstSearch(Graph G, int s) {
        this.marked = new boolean[G.V()];
        validateVertex(s);
        dfs(G, s);
    }

    // depth first search from v
    private void dfs(Graph G, int v) {
        this.count++;
        this.marked[v] = true;
        for (int w : G.adj(v)) {
            if (!this.marked[w]) {
                dfs(G, w);
            }
        }
    }

    /**
     * Is there a path between the source vertex {@code s} and vertex {@code v}?
     *
     * @param v the vertex
     * @return {@code true} if there is a path, {@code false} otherwise
     * @throws IllegalArgumentException unless {@code 0 <= v < V}
     */
    public boolean marked(int v) {
        validateVertex(v);
        return this.marked[v];
    }

    /**
     * Returns the number of vertices connected to the source vertex {@code s}.
     *
     * @return the number of vertices connected to the source vertex {@code s}.
     */
    public int count() {
        return this.count;
    }

    // throw an IllegalArgumentException unless {@code 0 <= v < V}
    private void validateVertex(int v) {
        int V = this.marked.length;
        if (v < 0 || v >= V) {
            throw new IllegalArgumentException("vertex " + v + " is not between 0 and " + (V - 1));
        }
    }

    /**
     * Unit tests the {@code DepthFirstSearch} data type.
     *
     * @param args the command-line arguments
     */
    public static void main(String[] args) {
        In in = new In(args[0]);
        Graph G = new Graph(in);
        int s = Integer.parseInt(args[1]);
        DepthFirstSearch search = new DepthFirstSearch(G, s);
        for (int v = 0; v < G.V(); v++) {
            if (search.marked(v)) {
                StdOut.print(v + " ");
            }
        }
        StdOut.println();
        if (search.count() != G.V()) {
            StdOut.println("Not connected");
        } else {
            StdOut.println("connected");
        }
    }
}
