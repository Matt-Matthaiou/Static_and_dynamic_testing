### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # We are assigning the value to 1 instead of checking.
      return True
    else                # there is no : after else
      return False
   

  dif highest_card(self, card1 card2):  # We shoud start a function wit def and 
  if card1.value > card2.value:         # also  there is a missing coma between 
    return card                         # card1 and card2
  else:                                 # the if statement if not indented correctly
    return card2
  


def cards_total(self, cards):
total                                       # total is not a variable yet 
  for card in cards:
    total += card.value
    return "You have a total of" + total    # the plus operator is wrong.
                                            # the return statement should be on the same level as the for loop.
```
