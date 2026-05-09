define function LCS(text1, text2):
    # If either string is empty there, can be no common subsequence.
    if length of text1 or text2 is 0:
        return 0

    letter1 = the first letter in text1
    firstOccurence = first position of letter1 in text2

    # The case where the line *is not* part of the optimal solution
    case1 = LCS(text1.substring(1), text2)

    # The case where the line *is* part of the optimal solution
    case2 = 1 + LCS(text1.substring(1), text2.substring(firstOccurence + 1))
   
    return maximum of case1 and case2