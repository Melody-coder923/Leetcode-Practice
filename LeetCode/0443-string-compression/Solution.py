class Solution:
    def compress(self, chars: List[str]) -> int:
        write=0
        i=0
        while i< len(chars):
            current_char=chars[i]
            count=1
            while i+1< len(chars) and chars[i+1]==current_char:
                count+=1
                i+=1
            chars[write]=current_char
            write+=1
            if count>1:
                for num in str(count):
                    chars[write]=num
                    write+=1
            i+=1
        return write
        
                