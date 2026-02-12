class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1
        visited = set()
        visited.add(startGene)
        queue = deque()
        queue.append((startGene, 0))
        var = ['A', 'C', 'G', 'T']


        while queue:
            gen, step = queue.popleft()


            for i in range(8):
                prot = gen[i]
                for j in var:
                    if j == prot:
                        continue
                    gen_mut = gen[:i]+j+gen[i+1:]
                    if gen_mut in visited:
                        continue
                    if gen_mut == endGene:
                        return step+1
                    if gen_mut in bank:
                        queue.append((gen_mut, step+1))
                    visited.add(gen_mut)
        return -1


        