# https://www.quora.com/What-is-an-intuitive-explanation-of-reservoir-sampling
# http://www.geeksforgeeks.org/reservoir-sampling/
# https://www.youtube.com/watch?v=A1iwzSew5QY&list=PLZxB91HFa5ASQG-Fs5i3qPaf4VsHFMyEI&index=19
"""
first explained:
Randomized algorithms are very useful, particularly data science. The main benefit is that it allows us to be both time and space efficient. One such algorithm is called Reservoir Sampling, or otherwise known as Algorithm R by Jeffrey Vitter in his paper on the subject. His goal was the address the following question.

Given a data set of unknown size N, uniformly select k elements from the set such that each element has a 1/N probability of being chosen.

Reservoir Sampling requires only O(n) time and only O(k) space.

Some examples

If k=1,N=2k=1,N=2. We place the first element in the reservoir. Since we know that the second / last element must have an acceptance probability of P=1/2P=1/2 When the stream ends after 22, it is clear that both elements had a 1/21/2 probability of being in the reservoir.

If k=1,N=3.k=1,N=3. We know that the third element must have an acceptance probability of 1/31/3. This also means that the element in the reservoir has a 2/32/3 chance of staying in the reservoir. Note that at n=2n=2 it had a 1/21/2 chance of being replaced. The probabilities telescope inwards when we calculate the probability of the first and second elements being in the reservoir.

P=1⋅12⋅23=13P=1⋅12⋅23=13

If we define the acceptance probability f(n,k)=1/nf(n,k)=1/n we will obtain any item with a final probability of 1/N1/N

P=12⋅23⋅34⋯n−2n−1⋅n−1n=1nP=12⋅23⋅34⋯n−2n−1⋅n−1n=1n

Generalizing for other values of k
It turns out that to generalize this for the case where k=kk=k, all we need to do is put the first k items into your reservoir first, this is to say that the first k elements have an acceptance probability of p=1=k/k. Afterwards, we sample each element with:

P(accept)=knP(accept)=kn

Once the new value from the stream is accepted, all we need to do is remove one element from the reservoir (with uniform probability) and fill in the new spot.
In this case, we will see the following telescoping effect with the probabilities.

P(kept)=1⋅kk+1⋅k+1k+2⋅k+2k+3⋯k+n−k−1n=kn

Second explained:
Imagine the following "dating" game show.  The contestant, a bachelorette, is seated at a table with an empty chair.  The host introduces the first suitor; the bachelorette has to invite him to sit with her and be her current "date".  Next, the host introduces the second suitor.  Now the girl gets the choice of whether she will keep her current "date" or replace him with the new suitor.  She can use a variety of means to make her decision, such as asking questions, or making the two suitors compete in some way.  After that, the host introduces the third suitor, and again the girl can choose to either keep or replace her current "date." After showing n suitors this way, the game show ends, and the girl goes on  a real date with the suitor she kept at the end, the "winner" of the show.

Imagine one contestant who simply flips a coin to decide whether or not to swap her current "date".  Is this "fair" to the suitors, i.e., is the probability distribution of the winner uniform over all the suitors?  The answer is no, because it is much more likely for the last few suitors to win than the first few suitors.  The very first suitor is most unfortunate of all, since if he wants to go on a date with the girl, he has to survive n-1 coin flips.  The last suitor has the best chances--he only needs to win a single coin flip.

So, what kind of procedure should the girl use if she wants to give all the suitors an equal chance, 1/n?  First of all, she has to swap to the last suitor with probability 1/n, since the last suitor wins if and only if she decides to swap on the last step.  Now what about the second-to-last suitor?  In order for him to win, she has to decide to swap on the (n-1)th step, and then also decide to not swap on the nth step.  This happens with probability pn−1pn−1(n-1)/n, where pn−1pn−1 is the probability that she swaps on the (n-1)th step and (n-1)/n is the probability she does not swap on the nth step.  Solving for 

pn−1pn−1(n-1)/n = 1/n

we get pn−1pn−1 = 1/(n-1).  Continuing the pattern, we see that her swap probability on the kth step is 1/k.

That is the algorithm for reservoir sampling.
"""

import numpy as np
from collections import deque, defaultdict
import random

def reservoirSampling(k, stream):
    """
    This implementation is not Ok and against the basic that
    number of stream should be unkown, always increase...
    """
    resevoir = deque()
    for i in range(k):
        resevoir.append(stream[i])
    for i in range(k, len(stream)):
        j = random.randrange(0, i)  # np.random.randint(0,  9)

        if j < k:
            resevoir[j] = stream[i]
    return resevoir

# https://stackoverflow.com/questions/2612648/reservoir-sampling
def reservoirSampling2(k, stream):
    resevoir = deque()
    for i, item in enumerate(stream): # generator start from 0
        if i < k:
            resevoir.append(item)
        else:
            j = np.random.randint(i)
            if j < k:
                resevoir[j] = stream[i]
    return resevoir


if __name__=='__main__':
    stream = '0123456789'*100
    totalTest = 5000
    k = 5

    mem = defaultdict()
    test = 0
    while test < totalTest:
        resK = reservoirSampling2(k, stream)
        for num in resK:
            if num in mem:
                mem[num] += 1
            else:
                mem[num] = 1
        print 'test {} counting finished'.format(test)
        test += 1
    print mem
    total = sum(mem.values())
    for num in mem:
        print '[{}]: {:2f}'.format(num, float(mem[num])/total)
