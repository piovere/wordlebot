# Diary

Making notes to myself as I screw things up

## 14 January 2022

I wrote the test to extract the green and yellow guesses per yesterday's note, and that was fine. But when I circled back to combine them (and return an evaluation of the guess, with green, yellow, and gray letters), I had a harder time than I wanted. Some of it was regular programmer brain (referring to the actual word, not the guess), and some of it was not cleaning up behind myself (deleting letters from the yellow list as they were used so they didn't get reported twice). I think it's right now, but I should probably add more tests to be sure (maybe I'll just start taking my guesses from the actual Wordle game!).

Next step will be to take the evaluation result and incorporate it into the world state that I described yesterday, then writing the logic that handles turns and assigns rewards for the various guesses. I'm thinking that each yellow is `+1`, each green is `+10`, and a correct guess is something like `+100 * (6 - guess_number)`. I do want the network to learn not to guess fake words, so I'll also add an evaluation loop to check if the word is not in the word list and assign a very negative score (`-1000`?) in response. That would also have the effect of pushing up the guess number without changing the world state. Is it fair to make the "game is over" logic just check the sum of the last part of the world vector? I.e. verify that `world[-5:, 1:].sum() > 0`? I think that would mean that the last 5 letters are not blank. I suppose I could also verify that the number of blank letters is zero with a while loop `while world[:, 0].sum() > 0: # DO STUFF`.

## 13 January 2022

My dog was apparently excited for me to come back to this project on day 2. At least that's why I assume she woke me up at 3am.

I am designing the world state. I think this is best represented by 30 one-hot vectors, each of length 26 + 26 + 26 + 1. That's each of the 26 english letters on each of a gray, yellow, and green backgrounds, plus a blank character for squares that haven't been guessed yet. The Wordle UI has a few other elements (which letters have already been guessed are highlighted on the keyboard as well and there's a small banner that tells you when you've tried to guess a word that's not in the game's dictionary), but I think some of this is redundant and some of it is going to be encapsulated in the score that the game iterator returns (along with the next iteration of the world).

I built out the functions to return the green letters (correct guess, correct location) and yellow letters (correct letter, wrong location). I should maybe have a function that also returns the gray letters (letters in guess that do not appear in the word)? It'd have a nice symmetry. I still need to deconflict letters that are both yellow and green (any green letter should also be a yellow letter). I probably also need to write the test case for multiple matches (e.g. a guess of "sassy" with a correct word of "sears" should have a green "s", yellow "a", yellow "s", gray "s", and gray "y").

## 12 Junuary 2022

I started the project today. I think that if I can get the game going in about a week of spare time I'll be pretty happy (it helps that this month has a big old deadline at the jobby-job). Still, the simplified version of the game shouldn't be *too* wild [^1].

While I'm focused on the one-hot vectors here (because that's what needs to go to the character-level ML agent), I'm going to write the translation layer to make the output human readable.

I wanted this to work with pipenv but wasn't able to do so. The python on my path was 3.9 (miniforge) when I initialized/installed pipenv. When I remembered that `tensorflow-macos` required python 3.8, I first tried to downgrade using conda, which made pipenv sad. Then I installed asdf (yay!) but apparently there's some kind of bug when asdf tries to build python 3.8. In the end, I've tabled pipenv for another day. I do want to move to that eventually, but I'm not there yet.

[^1]: Last words