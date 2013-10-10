Diceware
========

This is a Python implementation of the [Diceware](http://world.std.com/~reinhold/diceware.html) pasword-generating algorithm.

How to use
----------

1. You may need to set some permissions first.

        $ chmod u+x diceware

2. Run the program:

        $ ./diceware -w n

    where `n` is the number of words you want in your passphrase. The passphrase is printed to the terminal.

Caveats
-------

I'm not an expert in security or cryptography. If you want this to be more secure, use physical dice (or some other offline method of random number generation) to generate your passphrase the old-skool [_sic_] way.
