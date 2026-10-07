using System;
using System.Collections.Generic;
using System.Text;
public class Solution {
    public IList<string> RemoveInvalidParentheses(string s) {
        IList<string> result = new List<string>();
        if (string.IsNullOrEmpty(s)) {
            result.Add("");
            return result;
        }
        HashSet<string> visited = new HashSet<string>();
        Queue<string> queue = new Queue<string>();
        queue.Enqueue(s);
        visited.Add(s);
        bool found = false;
        while (queue.Count > 0) {
            int count = queue.Count;
            HashSet<string> currentLevel = new HashSet<string>();
            for (int i = 0; i < count; i++) {
                string curr = queue.Dequeue();
                if (IsValid(curr)) {
                    result.Add(curr);
                    found = true;
                }
                if (found) continue;
                for (int j = 0; j < curr.Length; j++) {
                    if (curr[j] != '(' && curr[j] != ')') continue;
                    string next = curr.Substring(0, j) + curr.Substring(j + 1);
                    if (!visited.Contains(next)) {
                        visited.Add(next);
                        queue.Enqueue(next);
                    }
                }
            }
            if (found) break;
        }
        return result;
    }
    private bool IsValid(string s) {
        int count = 0;
        foreach (char c in s) {
            if (c == '(') {
                count++;
            } else if (c == ')') {
                count--;
                if (count < 0) return false;
            }
        }
        return count == 0;
    }
}