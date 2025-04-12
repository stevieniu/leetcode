/**
 * 547. Number of Provinces
 * https://leetcode.com/problems/number-of-provinces/description/
 *
 * There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
 *
 * A province is a group of directly or indirectly connected cities and no other cities outside of the group.
 *
 * You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
 *
 * Return the total number of provinces.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
 * Output: 2
 * Example 2:
 *
 *
 * Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
 * Output: 3
 *
 *
 * Constraints:
 *
 * 1 <= n <= 200
 * n == isConnected.length
 * n == isConnected[i].length
 * isConnected[i][j] is 1 or 0.
 * isConnected[i][i] == 1
 * isConnected[i][j] == isConnected[j][i]
 */

/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function(isConnected) {
    const n = isConnected.length;
    const visit = Array(n);
    visit.fill(0);
    let cnt = 0;
    for(let city = 0; city < n; city++) {
        if(visit[city] == 0) {
            bfs(visit, isConnected, city);
            cnt++;
        }
    }
    return cnt;


};

var bfs = function(visit, isConnected, city) {
    const q = [];
    q.push(city);
    visit[city] = 1;
    while (q.length > 0) {
        const node = q.shift();
        for(let nei = 0; nei < isConnected[node].length; nei++) {
            if (visit[nei] == 0 && isConnected[node][nei]) {
                q.push(nei);
                visit[nei] = 1;
            }
        }
    }
};

var dfs = function(visit, isConnected, city) {
    visit[city] = 1;
    for(let nei = 0; nei < isConnected[city].length; nei++) {
        if (visit[nei] == 0 && isConnected[city][nei])
            dfs(visit, isConnected, nei);
    }
}


var findCircleNum_unionfind = function(isConnected) {
    const uf = new UnionFind(isConnected);
    let cnt = isConnected.length;
    for(let city = 0; city < isConnected.length; city++) {
        for(let nei = city + 1; nei < isConnected.length; nei++) {
            if(isConnected[city][nei] && uf.find(city) != uf.find(nei)) {
                uf.union(city, nei);
                cnt--;
            }
        }
    }
    return cnt;
};
class UnionFind {

    constructor(isConnected) {
        this.roots = Array(isConnected.length);
        for (let i = 0; i < isConnected.length; i++) {
            this.roots[i] = i;
        }
        this.ranks = Array(isConnected.length);
        this.ranks.fill(1);
    }

    find(x) {
        if (x != this.roots[x])
            this.roots[x] = this.find(this.roots[x]);
        return this.roots[x];
    }

    union(x, y) {
        let rx = this.find(x);
        let ry = this.find(y);
        if (rx == ry) return false;
        if (this.ranks[rx] > this.ranks[ry]) {
            this.roots[ry] = rx;
            this.ranks[rx] += this.ranks[ry];
        } else {
            this.roots[rx] = ry;
            this.ranks[ry] += this.ranks[rx];
        }
        return true;
    }
}