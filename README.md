simplesound.py
==============

A really simple tone generator for Python.

I wrote this after realising how hard it was to do basic beep functionality
in Python on the Raspberry Pi.  It contains the knowledge that I gathered
debugging my demo using pygame.

It should play well with pygame based programs.  It requires Pygame and numpy to be installed but should run on the Raspberry Pi default.

Usage
-----

    from simplesound import Tone
    
    t = Tone()
    
    t.play(440, 1000) # play a concert pitch A for 1000ms
    
In this library play is a blocking call.

If you look in simplesound.py there's a demo of a short tune using a single Tone objectwith multiple calls to play()

License
-------

Use it for what you like.  CC-BY 4.0 Nathan Dumont 2016
