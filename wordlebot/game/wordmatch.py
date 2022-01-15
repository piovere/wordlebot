import numpy as np
import string
import logging

LOG = logging.getLogger(__name__)

def yellows(guess: str, target: str):
    """Find the yellow letters in the guess
    
    Examples
    --------
    >>> g = 'abcde'
    >>> t = 'edcba'
    >>> yellows(g, t)
    [('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4)]
    >>> g = 'efghi'
    >>> yellows(g, t)
    [('e', 0)]
    >>> g = 'sassy'
    >>> t = 'sears'
    >>> yellows(g, t)
    [('s', 0), ('a', 1), ('s', 2)]
    """
    out = []
    for i, g in enumerate(guess):
        if g in target:
            out.append((g, i))
            target = target.replace(g, '', 1)
    return out

def greens(guess: str, target: str):
    """Find the green letters in the guess
    
    Examples
    --------
    >>> g = 'abcde'
    >>> t = 'fgcdh'
    >>> greens(g, t)
    [('c', 2), ('d', 3)]
    >>> g = 'sassy'
    >>> t = 'sears'
    >>> greens(g, t)
    [('s', 0)]
    """
    greens = [(g, i) for i, (g, t) in enumerate(zip(guess, target)) if g == t]
    return greens
    
def grade(guess: str, target: str) -> np.ndarray:
    """Evaluate a guess against the true word
    
    Examples
    --------
    >>> g = 'sassy'
    >>> t = 'sears'
    >>> grade(g, t).astype(int)
    array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])
    """
    LOG.debug(f"Real word was {target}, guess was {guess}")
    out = np.zeros((5, 26+26+26+1), dtype=bool)
    cd = {c: i+1 for i, c in enumerate(string.ascii_lowercase)}
    
    gs = greens(guess, target)
    ys = yellows(guess, target)
    
    # disambiguate yellows that are also green
    # It may be more efficient to use sets to do this
    for g in gs:
        try:
            yind = ys.index(g)
            del(ys[yind])
        except ValueError:
            # No match
            continue
    
    # Loop through each position
    for i, (lg, lt) in enumerate(zip(guess, target)):
        if (lg, i) in gs:
            LOG.debug(f"{lg} in position {i} is a green")
            offset = 0
        elif lg in [yi[0] for yi in ys]:
            LOG.debug(f"{lg} in position {i} is a yellow")
            LOG.debug(f"Removing {lg} from yellow list")
            yind = [yi[0] for yi in ys].index(lg)
            del(ys[yind])
            LOG.debug(ys)
            offset = 26
        else:  # character is gray
            LOG.debug(f"{lg} in position {i} is a gray")
            offset = 52
        
        LOG.debug(f"Setting character {i} (guess: {lg}, real: {lt}) to {offset+cd[lg]}")
        out[i, cd[lg]+offset] = True
    
    # Dummy check
    assert out[:, 0].sum() == 0
    
    return out
    
if __name__ == "__main__":
    LOG.setLevel(logging.DEBUG)
    LOG.addHandler(logging.StreamHandler())

    g = 'sassy'
    t = 'sears'
    grade(g, t)
