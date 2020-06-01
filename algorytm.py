
    # Create a grid of whatever size and a list of words.
    # Shuffle the word list, and then sort the words by longest to shortest.
    # Place the first and longest word at the upper left most position, 1,1 (vertical or horizontal).
    # Move onto next word, loop over each letter in the word and each cell in the grid looking for letter to letter matches.
    # When a match is found, simply add that position to a suggested coordinate list for that word.
    # Loop over the suggested coordinate list and "score" the word placement based on how many other words it crosses. Scores of 0 indicate either bad placement (adjacent to existing words) or that there were no word crosses.
    # Back to step #4 until word list is exhausted. Optional second pass.
    # We should now have a crossword, but the quality can be hit or miss due to some of the random placements. So, we buffer this crossword and go back to step #2. If the next crossword has more words placed on the board, it replaces the crossword in the buffer. This is time limited (find the best crossword in x seconds).


# horizontal/vertical zdecyduje czy +1 czy +13 do dlugosci (przez wymiary tablicy)
#DUZO słów naraz