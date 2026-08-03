class Solution(object):
    def minimumPushes(self, word):
        word_length = len(word)
        total_pushes = 0
        push_multiple = 1  # No.pushes needed for current group of 8 letters
      
        # Process complete grp 8 letters
        complete_groups = word_length // 8
        for i in range(complete_groups):
            total_pushes += push_multiple * 8  # Each of 8 letters needs push_multiplier pushes
            push_multiple += 1  # Next group needs one more push per letter
      
        # Process remaining letters (less than 8)
        remaining_letters = word_length % 8
        total_pushes += push_multiple * remaining_letters
      
        return total_pushes

        