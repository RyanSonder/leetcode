# https://leetcode.com/problems/circular-sentence/

class circular_sentence:

    def solution(sentence: str) -> bool:
        first_letter = sentence[0]
        
        words = sentence.split()
        
        last_letter = words[0][-1:]
        
        for word in words[1:]:
            if word[0] != last_letter:
                return False
            last_letter = word[-1:]    
        
        return words[-1:][0].endswith(first_letter)
