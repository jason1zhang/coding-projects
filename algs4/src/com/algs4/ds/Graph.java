package com.algs4.ds;

import com.algs4.io.In;
import com.algs4.io.StdOut;

import java.util.NoSuchElementException;

public class Graph {
    private static final String NEWLINE = System.getProperty("line.separator");

    private final int V;
    private int E;
    private Bag<Integer>[] adj;

    /**
     * Initializes an empty graph with {@code V} vertices and 0 edges.
     *
     * @param V number of vertices
     * @throws IllegalArgumentException if {@code V < 0}
     */
    public Graph(int V) {
        if (V < 0) {
            throw new IllegalArgumentException("Number of vertices must be non-negative");
        }
        this.V = V;
        this.E = 0;
        this.adj = (Bag<Integer>[]) new Bag[V];
        for (int v = 0; v < this.V; v++) {
            adj[v] = new Bag<Integer>();
        }
    }

    /**
     * Initializes a graph from the specified input stream.
     * The format is the number of vertices <em>V</em>,
     * followed by the number of edges <em>E</em>,
     * followed by <em>E</em> pairs of vertices, with each entry separated by whitespace.
     *
     * @param in the input stream
     * @throws IllegalArgumentException if {@code in} is {@code null}
     * @throws IllegalArgumentException if the endpoints of any edge are not in prescribed range
     * @throws IllegalArgumentException if the number of vertices or edges is negative
     * @throws IllegalArgumentException if the input stream is in the wrong format
     */
    public Graph(In in) {
        if (in == null) {
            throw new IllegalArgumentException("argument is null");
        }

        try {
            this.V = in.readInt();
            if (this.V < 0) {
                throw new IllegalArgumentException("number of vertices in a Graph must be non-negative");
            }
            this.adj = (Bag<Integer>[]) new Bag[this.V];
            for (int v = 0; v < this.V; v++) {
                this.adj[v] = new Bag<Integer>();
            }

            int E = in.readInt();
            if (E < 0) {
                throw new IllegalArgumentException("number of edges in a Graph must be non-negative");
            }
            for (int i = 0; i < E; i++) {
                int v = in.readInt();
                int w = in.readInt();
                validateVertex(v);
                validateVertex(w);
                addEdge(v, w);
            }
        } catch (NoSuchElementException e) {
            throw new IllegalArgumentException("invalid input format in Graph constructor", e);
        }
    }

    /**
     * Initializes a new graph that is a deep copy of {@code G}.
     *
     * @param G the graph to copy
     * @throws IllegalArgumentException if {@code G} is {@code null}
     */
    public Graph(Graph G) {
        this.V = G.V();
        this.E = G.E();
        if (V < 0) {
            throw new IllegalArgumentException("Number of vertices must be non-negative");
        }

        // update adjacent lists
        this.adj = (Bag<Integer>[]) new Bag[this.V];
        for (int v = 0; v < this.V; v++) {
            this.adj[v] = new Bag<>();
        }

        for (int v = 0; v <this.V; v++) {
            // reverse so that adjacency list is the same order as original
            Stack<Integer> reverse = new Stack<>();
            for (int w : G.adj[v]) {
                reverse.push(w);
            }
            for (int w : reverse) {
                this.adj[v].add(w);
            }
        }
    }

    /**
     * Returns the number of vertices in this graph.
     *
     * @return the number of vertices in this graph
     */
    public int V() {
        return this.V;
    }

    /**
     * Returns the number of edges in this graph.
     *
     * @return the number of edges in this graph
     */
    public int E() {
        return this.E;
    }

    private void validateVertex(int v) {
        if (v < 0 || v >= this.V) {
            throw new IllegalArgumentException("vertex " + v + " is not between 0 and " + (this.V - 1));
        }
    }

    /**
     * Adds the undirected edge v-w to this graph.
     *
     * @param v one vertex in the edge
     * @param w the other vertex in the edge
     * @throws IllegalArgumentException unless both {@code 0 <= v < V} and {@code 0 <= w < V}
     */
    public void addEdge(int v, int w) {
        validateVertex(v);
        validateVertex(w);
        this.E++;
        this.adj[v].add(w);
        this.adj[w].add(v);
    }

    /**
     * Returns the vertices adjacent to vertex {@code v}.
     *
     * @param v the vertex
     * @return the vertices adjacent to vertex {@code v}, as an iterable
     * @throws IllegalArgumentException unless {@code 0 <= v < V}
     */
    public Iterable<Integer> adj(int v) {
        validateVertex(v);
        return this.adj[v];
    }

    /**
     * Returns the degree of vertex {@code v}.
     *
     * @param v the vertex
     * @return the degree of vertex {@code v}
     * @throws IllegalArgumentException unless {@code 0 <= v < V}
     */
    public int degree(int v) {
        validateVertex(v);
        return this.adj[v].size();
    }

    public String toString() {
        StringBuilder s = new StringBuilder();
        s.append(this.V + " vertices, " + this.E + " edges" + NEWLINE);
        for (int v = 0; v < this.V; v++) {
            s.append(v + ": ");
            for (int w : this.adj[v]) {
                s.append(w + " ");
            }
            s.append(NEWLINE);
        }

        return s.toString();
    }

    /**
     * Unit tests the {@code Grapph} data type.
     *
     * @param args the commmand-line arguemtns
     */
    public static void main(String[] args) {
        In in = new In(args[0]);
        Graph G = new Graph(in);
        StdOut.println(G);
    }
}

