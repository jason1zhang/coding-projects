package com.algs4.ds;

import com.algs4.io.StdIn;
import com.algs4.io.StdOut;

public class WeightedQuickUnionUF {
    private final int[] parent;     // parent[i] = parent of i
    private final int[] size;       // size[i] = number of elements in subtree rooted at i
    private int count;              // number of components

    /**
     * Initializes an empty union-find data structure with
     * {@code n} elements {@code 0} through {@code n-1}.
     * Initially, each element is in its own set.
     *
     * @param n the number of elements
     * @throws IllegalArgumentException if {@code n < 0}
     */
    public WeightedQuickUnionUF(int n) {
        this.count = n;
        this.parent = new int[n];
        this.size = new int[n];
        for (int i = 0; i < n; i++) {
            this.parent[i] = i;
            this.size[i] = 1;
        }
    }

    /**
     * Returns the number of sets.
     *
     * @return the number of sets (between {@code 1} and {@code n}
     */
    public int count() {
        return this.count;
    }

    /**
     * Returns the canonical element of the set containing element {@code p}.
     *
     * @param p an element
     * @return the canonical element of the set containing {@code p}
     * @throws IllegalArgumentException unless {@code 0 <= p < n}
     */
    public int find(int p) {
        validate(p);
        while (p != this.parent[p]) {
            p = this.parent[p];
        }

        return p;
    }

    // validate that p is a valid index
    private void validate(int p) {
        int n = this.parent.length;
        if (p < 0 || p >= n) {
            throw new IllegalArgumentException("index " + p + " is not between 0 and " + (n-1));
        }
    }

    /**
     * Merges the set containing element {@code p} with
     * the set containing element {@code q}.
     *
     * @param p one element
     * @param q the other element
     * @throws IllegalArgumentException unless
     *          both {@code 0 <= p < n} and {@code 0 <= q < n}
     */
    public void union(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        if (rootP == rootQ) {
            return;
        }

        // make smaller root point to larger one
        if (this.size[rootP] < this.size[rootQ]) {
            this.parent[rootP] = rootQ;
            this.size[rootQ] += this.size[rootP];
        } else {
            this.parent[rootQ] = rootP;
            this.size[rootP] += this.size[rootQ];
        }

        this.count--;
    }

    /**
     * Reads an integer {@code n} and a sequence of pairs of integers
     * (between {@code 0} and {@code n-1} from standard input, where each integer
     * in the pair represents some element;
     * if the elements are in different sets, merge the two sets
     * and print the pair to standard output.
     *
     * @param args the command-line arguments
     */
    public static void main(String[] args) {
        int n = StdIn.readInt();
        WeightedQuickUnionUF uf = new WeightedQuickUnionUF(n);
        while (!StdIn.isEmpty()) {
            int p = StdIn.readInt();
            int q = StdIn.readInt();
            if (uf.find(p) == uf.find(q)) {
                continue;
            }
            uf.union(p, q);
            StdOut.println(p + " " + q);
        }
        StdOut.println(uf.count() + " components");
    }
}
