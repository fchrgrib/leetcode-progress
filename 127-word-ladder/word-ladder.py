class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        queue = deque()
        wl = len(beginWord)
        graph_w: Dict[str: List[str]] = {}

        for i in wordList:
            for j in range(wl):
                key = i[:j]+"*"+i[j+1:]
                
                if key not in graph_w:
                    graph_w[key] = [i]
                else:
                    graph_w[key].append(i)
        



        queue.append((beginWord, 1))

        while queue:
            word, count = queue.popleft()
            for i in range(wl):
                w_f = word[:i]+"*"+word[i+1:]
                if w_f in graph_w:
                    for j in graph_w[w_f]:
                        if j in visited:
                            continue
                        if j == endWord:
                            return count + 1
                        visited.add(j)
                        queue.append((j, count+1))
        return 0
        