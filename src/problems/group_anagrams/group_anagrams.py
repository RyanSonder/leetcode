# https://leetcode.com/problems/group-anagrams/

class group_anagrams:

    def solution(strs):
        
        # Base case
        if len(strs) == 1:
            return [[strs[0]]]
        

        
        anagrams = [[strs[0]]]
        while strs[1:]:
            s = strs[1]
            outer_flag = False

            for i in range(len(anagrams)):
                t = anagrams[i][0]

                inner_flag = False

                if len(s) != len(t): 
                    continue

                d = {} 
                for j in range(len(s)): 
                    cs = s[j]
                    ct = t[j]

                    d[cs] = d.get(cs, 0) + 1
                    d[ct] = d.get(ct, 0) - 1

                for n in d.values(): 
                    if n != 0 : 
                        inner_flag = True
                        continue

                if inner_flag:
                    continue

                anagrams[i].append(s)
                outer_flag = True
                break

            if not outer_flag:
                anagrams.append([s])
            strs.pop(1)
        
        return anagrams
