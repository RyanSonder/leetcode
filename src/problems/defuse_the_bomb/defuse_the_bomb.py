# Defuse The Bomb


class DefuseTheBomb:

    def solution(self, code: [int], k: int):
        if k == 0:
            return [0] * len(code)

        elif k < 0:
            decryption = []
            for i in range(len(code)):
                decryption.append(sum(code[k:]))
                # Rotate the list
                first = code.pop(0)
                code.append(first)

            return decryption

        else: # k > 0
            decryption = []
            extended = code + code
            for i in range(len(code)):
                decryption.append(sum(extended[i+1:i+k+1]))
            return decryption