I need to handle duplicate letters.
If >1 occurrence of a letter, need to add its `original index + 1` as the starting location for the list `index` method.
But must use `0` the first time to ensure the whole list is searched.

Now to handle duplicates in the guess when they are absent from the word!
This is a royal pain.
Need to track presence of these and adjust somehow - but needs to be separate from other adjustment in reverse (already implemented to handle repeat letters in the word rather than guess) otherwise will mess this up.
Trying times recurred variable at present, it's clunky but I think it has promise.
