class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + ":" + s
        return encoded

    def decode(self, encoded: str) -> List[str]:
        result = [] #empty list for decoded strings storage
        i = 0 #pointer for traversing the encoded string

        while i < len(encoded): #continue until entire encoded string processed
            j = i # secondary pointer to check for delimiter

            while encoded[j] != ":": #traverse secondary pointer until delimiter
                j += 1

            length = int(encoded[i:j]) #when we hit delimiter find length from i to j (length of string from substring)

            result.append(encoded[j+1:j+1+length]) #extract string of given length after :


            i = j+1+length #move pointer i to start of next encoded segment

        return result #return list of decoded strings