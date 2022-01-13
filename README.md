# WordleBot

Sounds vaguely like "Mandelbrot", right?

This is a project to teach myself to make a game-playing robot using reinforcement learning (RL) and TensorFlow (tf). The game itself seems simple enough to simulate.

To be clear, I'm going to focus on the RL here. To that end, I'm going to present the state to the robot in the form of correct/incorrect guesses (so a [6, 5, 27, 4] world state, I guess?). I will likely reevaluate that as I go along.

## TODO
- [ ] Simulate a wordle game by choosing a 5-letter word, accepting guesses, and grading them
- [ ] Write an ML agent that receives world state and produces a guess vector ([5, 27] output)
- [ ] Train that agent until it's way better than I am at Wordle
- [ ] Go back to averaging a 5.3 guess rate on my own

## Dumb notes
- There's a tests folder. That's mostly so I can keep myself honest/optimize the game step (since that'll likely be slow)
