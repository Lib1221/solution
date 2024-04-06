class Solution:
    def interpret(self, command: str) -> str:
        w = ""
        for i in range(len(command)):
            if command[i] == "G":
                w = w + "G"
            elif command[i] == chr(40) and command[i+1] == chr(41):
                w = w + "o"
                i = i + 1

            elif command[i] == chr(40) and command[i+3] == chr(41):
                w = w + "al"
                i = i + 3
        return w
        
