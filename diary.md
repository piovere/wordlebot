# Diary

Making notes to myself as I screw things up

## 12 Junuary 2022

I started the project today. I think that if I can get the game going in about a week of spare time I'll be pretty happy (it helps that this month has a big old deadline at the jobby-job). Still, the simplified version of the game shouldn't be *too* wild [^1].

While I'm focused on the one-hot vectors here (because that's what needs to go to the character-level ML agent), I'm going to write the translation layer to make the output human readable.

I wanted this to work with pipenv but wasn't able to do so. The python on my path was 3.9 (miniforge) when I initialized/installed pipenv. When I remembered that `tensorflow-macos` required python 3.8, I first tried to downgrade using conda, which made pipenv sad. Then I installed asdf (yay!) but apparently there's some kind of bug when asdf tries to build python 3.8. In the end, I've tabled pipenv for another day. I do want to move to that eventually, but I'm not there yet.

[^1]: Last words