"""
721. Accounts Merge
https://leetcode.com/problems/accounts-merge/description/?envType=company&envId=linkedin&favoriteSlug=linkedin-thirty-days

Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.



Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]


Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
"""

import collections
from typing import List
class Solution:

    # dfs
    # def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    #     graph = collections.defaultdict(set)
    #     emailToname = {}

    #     for account in accounts:
    #         name = account[0]
    #         for email in account[1:]:
    #             graph[email].add(account[1])
    #             graph[account[1]].add(email)
    #             emailToname[email] = name

    #     visit = set()
    #     res = []
    #     def dfs(email, emailList):
    #         if email not in visit:
    #             visit.add(email)
    #             emailList.append(email)

    #         for nei in graph[email]:
    #             if nei in visit:
    #                 continue
    #             dfs(nei, emailList)

    #     for email in graph:
    #         emailList = []
    #         dfs(email, emailList)
    #         if emailList:
    #             res.append([emailToname[email]] + sorted(emailList))
    #     return res

    # union find
    # def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    #     uf = UnionFind(len(accounts))
    #     emailToAcc = {}

    #     for i, a in enumerate(accounts):
    #         for e in a[1:]:
    #             if e in emailToAcc:  # if e already in emailToAcc, i and  emailToAcc[e] belong to the same person, should merge
    #                 uf.union(i, emailToAcc[e])
    #             else:
    #                 emailToAcc[e] = i

    #     emailGroup = collections.defaultdict(list) # index of account -> list of email
    #     for e, i in emailToAcc.items():
    #         leader = uf.find(i)
    #         emailGroup[leader].append(e)

    #     res = []
    #     for i, emails in emailGroup.items():
    #         name = accounts[i][0]
    #         res.append([name] + sorted(emailGroup[i]))
    #     return res

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        par = [i for i in range(n)]  # initially x == par[x]
        rank = [1] * n

        def find(x):
            while x != par[x]:
                par[x] = par[par[x]]
                x = par[x]
            return x

        def union(x1, x2):
            p1, p2 = find(x1), find(x2)
            if p1 == p2:  # x1 and x2 have the same parent, already being unioned
                return False
            elif rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        emailToAcc = {}
        for i, emails in enumerate(accounts):
            for e in emails[1:]:
                if e in emailToAcc:
                    union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i

        emailGroup = collections.defaultdict(list)
        for e, i in emailToAcc.items():
            root = find(i)
            emailGroup[root].append(e)
        print(emailGroup)
        res = []
        for a, e in emailGroup.items():
            res.append([accounts[a][0]] + sorted(e))
        return res


class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]  # parent, intially, each node is the parent of itself
        self.rank = [1] * n  # the size of each element, initally set to 1 for each disjoint set

    # find x's parent
    def find(self, x):
        while x != self.par[
            x]:  # if the x's parent is not itself, then looking for the parent, otherwise, it is the root
            self.par[x] = self.par[self.par[x]]  # path compression, i.e. make parent point to its parent
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:  # if p1 and p2 are equal, do nothing
            return False
        elif self.rank[p1] > self.rank[
            p2]:  # merge small size set to large size set, so if rank of p1 > p2, then merge p2 to p1, vice versa
            self.par[p2] = p1  # merge p2 to p1, make parent of p2 to p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True