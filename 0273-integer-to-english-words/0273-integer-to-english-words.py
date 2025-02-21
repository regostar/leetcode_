class Solution:
    def __init__(self):
        self.sequences_3 = ['Hundred', 'Thousand', 'Million', 'Billion', 'Trillion']
        self.below_10 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"] # for 30 we don't say thirty zero hence empty string
        self.below_20 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.below_100 = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def _convert_to_words(self, num: int) -> str:
        # recursive soln
        if num < 10:
            return self.below_10[num]
        if num < 20:
            return self.below_20[num - 10]
            # indexes is 19-10
        if num < 100:
            # 86 or 8, can never be below 20
            tens = self.below_100[num // 10]  
            ones = " " + self._convert_to_words(num % 10) if num % 10 != 0 else ""
            return tens + ones
        if num < 1000:
            return self._convert_to_words(num // 100) + " Hundred" + (" " + self._convert_to_words(num % 100) if num % 100 != 0 else "")
        if num < 1000000:
            return self._convert_to_words(num // 1000) + " Thousand" + (" " + self._convert_to_words(num % 1000) if num % 1000 != 0 else "")
        if num < 1000000000:
            return self._convert_to_words(num // 1000000) + " Million" + (" " + self._convert_to_words(num % 1000000) if num % 1000000 != 0 else "")
        return self._convert_to_words(num // 1000000000) + " Billion" + (" " + self._convert_to_words(num % 1000000000) if num % 1000000000 != 0 else "")
        # no_digits = len(str(num)) # 4 7
        # no_of_3s = no_digits // 3 # 1  2
        # category_3s = (10 ** (no_of_3s + 1))
        # segment = " " +  self.sequences_3[no_of_3s-1] if num % category_3s != 0 else ""
        # return self._convert_to_words(num //category_3s) + segment
        


    def numberToWords(self, num: int) -> str:
        # middle chunk 0 
        # 0 hundred we don't
        if num == 0:
            return "Zero"
        
        return self._convert_to_words(num)


        
        