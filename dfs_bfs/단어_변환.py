from collections import defaultdict, deque


def connected(word1, word2):
    word_diff_count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            word_diff_count += 1
            if word_diff_count > 1:
                return False
    return word_diff_count == 1


def solution(begin, target, words):
    n = len(words)
    graph = defaultdict(set)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if connected(words[i], words[j]):
                graph[words[i]].add(words[j])
                graph[words[j]].add(words[i])

    queue = []
    visited = set()

    for word in words:
        if connected(begin, word):
            queue.append((word, 1))

    while queue:
        word, count = queue.pop()
        if word == target:
            return count

        for w in graph[word]:
            if w not in visited:
                visited.add(w)
                queue.append((w, count + 1))

    return 0