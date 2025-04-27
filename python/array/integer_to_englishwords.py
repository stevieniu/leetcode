"""
273. Integer to English Words
Convert a non-negative integer num to its English words representation.



Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


Constraints:

0 <= num <= 231 - 1

"""
class Solution:
    # Arrays to store words for numbers less than 10, 20, and 100
    below_ten = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    below_twenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    below_hundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    # Main function to convert a number to English words
    def numberToWords(self, num: int) -> str:
        # Handle the special case where the number is zero
        if num == 0:
            return "Zero"
        # Call the helper function to start the conversion
        return self._convert_to_words(num)

    # Recursive function to convert numbers to words
    # Handles numbers based on their ranges: <10, <20, <100, <1000, <1000000, <1000000000, and >=1000000000
    def _convert_to_words(self, num: int) -> str:
        if num < 10:
            return self.below_ten[num]
        if num < 20:
            return self.below_twenty[num - 10]
        if num < 100:
            return self.below_hundred[num // 10] + (" " + self._convert_to_words(num % 10) if num % 10 != 0 else "")
        if num < 1000:
            return self._convert_to_words(num // 100) + " Hundred" + (" " + self._convert_to_words(num % 100) if num % 100 != 0 else "")
        if num < 1000000:
            return self._convert_to_words(num // 1000) + " Thousand" + (" " + self._convert_to_words(num % 1000) if num % 1000 != 0 else "")
        if num < 1000000000:
            return self._convert_to_words(num // 1000000) + " Million" + (" " + self._convert_to_words(num % 1000000) if num % 1000000 != 0 else "")
        return self._convert_to_words(num // 1000000000) + " Billion" + (" " + self._convert_to_words(num % 1000000000) if num % 1000000000 != 0 else "")