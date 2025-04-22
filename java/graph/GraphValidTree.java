/**
 * 261. Graph Valid Tree
 * https://leetcode.com/problems/graph-valid-tree/description/
 *
 * You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
 *
 * Return true if the edges of the given graph make up a valid tree, and false otherwise.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
 * Output: true
 * Example 2:
 *
 *
 * Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
 * Output: false
 *
 *
 * Constraints:
 *
 * 1 <= n <= 2000
 * 0 <= edges.length <= 5000
 * edges[i].length == 2
 * 0 <= ai, bi < n
 * ai != bi
 * There are no self-loops or repeated edges.
 *
 *
 */
package graph;

import java.util.Arrays;

public class GraphValidTree {
    public boolean validTree(int n, int[][] edges) {
        UnionFind uf = new UnionFind(n);
        int cnt = n;
        for(int i = 0; i < edges.length; i++) {
            if (uf.find(edges[i][0]) == uf.find(edges[i][1]))  return false;
            uf.union(edges[i][0], edges[i][1]);
            cnt--;
        }
        return cnt == 1;
    }
}
class UnionFind {
    int[] root;
    int[] rank;
    UnionFind(int n) {
        root = new int[n];
        for(int i = 0; i < n; i++)
            root[i] = i;
        rank = new int[n];
        Arrays.fill(rank, 1);
    }

    int find(int x) {
        if (root[x] != x)
            root[x] = find(root[x]);
        return root[x];
    }

    boolean union(int x, int y) {
        int rx = find(x);
        int ry = find(y);
        if (rx == ry) return false;
        if(rank[rx] > rank[ry]) {
            root[ry] = rx;
            rank[rx] += rank[ry];
        } else {
            root[rx] = ry;
            rank[ry] += rank[rx];
        }
        return true;
    }
}