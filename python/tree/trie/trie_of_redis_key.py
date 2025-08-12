class TrieNode:
    def __init__(self):
        self.children = {} # word: [TrieNode, cnt of chidlren, memory usage]
        # self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, key):
        word_lst = key.split(':')
        cur = self.root
        m_usage = memory_usage_cache[key] if key in memory_usage_cache else 0

        for word in word_lst:
            if word not in cur.children:
                cur.children[word] = [TrieNode(), 1, m_usage]
            else:
                cur.children[word][1] += 1
                cur.children[word][2] += m_usage
            cur = cur.children[word][0]



    def print(self, lvl_limit):
        cur = self.root
        def dfs(node, result, lvl):
            if not node:
                return
            if result and lvl <= lvl_limit:
                res_lst = result.split(':')
                line = f'|{res_lst[0]:<{cols_width[0] - 1}}|{res_lst[1]:<{cols_width[1] - 1}}|{res_lst[2]:<{cols_width[2] - 1}}|'
                print(line)
            keys = node.children.keys()
            for key in keys:
                dfs(node.children[key][0], '  ' * lvl + key + ':' + str(node.children[key][2]) + ':' + str( node.children[key][1]), lvl + 1)
        cols_width = [80, 20, 20]
        print('-' * sum(cols_width))
        header_key_word = ['KEY', 'KB', 'KEYS COUNT']
        print(f'|{header_key_word[0]:<{cols_width[0] - 1}}|{header_key_word[1]:<{cols_width[1] - 1}}|{header_key_word[2]:<{cols_width[2] - 1}}|')
        print('-' * sum(cols_width))
        dfs(cur, "", 0)



key1 = 'avro:search:tst1'
key2 = 'avro:search:abs2'
key3 = 'avro:time:2342'
key4 = 'avro:time:333'

memory_usage_cache = {key1: 100, key2: 200, key3: 300, key4: 400}

trie = Trie()
trie.add(key1)
trie.add(key2)
trie.add(key3)
trie.add(key4)
trie.print(3)


