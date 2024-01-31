def solution(strings, n):
  
  return sorted(strings, key=lambda s: (s[n], s))

assert solution(["sun", "bed", "car"], 1) == ["car", "bed", "sun"]
assert solution(["abce", "abcd", "cdx"], 2) == ["abcd", "abce", "cdx"]