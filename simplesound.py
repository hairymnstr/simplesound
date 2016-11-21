import pygame, numpy

class Tone:
    def __init__(self):
        """ Create a new tone generator """
        # only initialise pygame if it hasn't been already.  Should make this
        # play well with other pygame stuff
        if pygame.mixer.get_init() == None:
            pygame.init()
        # load the parameters of the sound card
        self.sample_rate, self.format, self.channels = pygame.mixer.get_init()
    
    def play(self, freq, period_ms):
        """ Play a tone of specified frequency for a period of time.
            freq = frequency in Hz
            period_ms = time to play for in millisecods """
        
        # 2 * pi * freq / sample_rate is the step between samples in radians
        omega = numpy.pi * 2 * freq / self.sample_rate

        # arange returns a vector of values we can multiply by our step value
        # in one step using some of numpys mathematical optimisations
        xvalues = numpy.arange(int(self.sample_rate)) * omega

        # the values are scaled -1 to 1 as floating point, but we need to 
        # scale them based on the sample format of the sound card
        if self.format < 0:
            smp = (2 ** (abs(self.format)-1)) * numpy.sin(xvalues)
        else:
            smp = (2 ** (abs(self.format)-1)) * (numpy.sin(xvalues) + 1)

        # if the mixer is configured in stereo we need to copy the sine wave to
        # both left and right channels
        if self.channels == 2:
            smp = numpy.array(zip(smp, smp))

        # the sound driver requires the numpy array to be presented in the same
        # format.  This is because underneath the python there's a bunch of 
        # C optimisations for speed.  Currently only support 8 or 16 bit samples
        # in signed or unsigned format.  Could do more but I don't know what
        # pygame supports.
        if self.format == -16:
            smp = smp.astype(numpy.int16)
        elif self.format == 16:
            smp = smp.astype(numpy.uint16)
        elif self.format == -8:
            smp = smp.astype(numpy.int8)
        elif self.format == 8:
            smp = smp.astype(numpy.uint8)
        else:
            raise Exception("Unhandled sample format")

        # call this pygame function to convert the numpy array to a sound object
        snd = pygame.sndarray.make_sound(smp)

        # the sinewave we created is 1 second long, so if the period requested
        # is longer than that we need to loop.
        loops = period_ms / 1000
        if period_ms % 1000:
            loops += 1

        # the loops parameter is odd in that it always plays once then does loops
        # repeats, so 0 means play once, 1 means play twice etc.
        loops -= 1
        
        # play the sine wave looping until the requested period is reached
        snd.play(loops, period_ms)

        # play is an asynchronous call, that means it queues the sound up to be
        # played and then returns immediately.  If we don't wait for it to play
        # here you could end up playing all your notes at once and then quitting
        # before any have actually played!
        pygame.time.delay(period_ms)

if __name__ == "__main__":
    import time
    
    """ demo tune, courtesy of:
        http://processors.wiki.ti.com/index.php/Playing_The_Imperial_March
    """
    c = 261
    d = 294
    e = 329
    f = 349
    g = 391
    gS = 415
    a = 440
    aS = 455
    b = 466
    cH = 523
    cSH = 554
    dH = 587
    dSH = 622
    eH = 659
    fH = 698
    fSH = 740
    gH = 784
    gSH = 830
    aH = 880

    t = Tone()
    
    t.play(a, 500);
    t.play(a, 500);
    t.play(a, 500);
    t.play(f, 350);
    t.play(cH, 150);
    t.play(a, 500);
    t.play(f, 350);
    t.play(cH, 150);
    t.play(a, 650);
 
    time.sleep(0.150)
    #end of first bit
 
    t.play(eH, 500);
    t.play(eH, 500);
    t.play(eH, 500);
    t.play(fH, 350);
    t.play(cH, 150);
    t.play(gS, 500);
    t.play(f, 350);
    t.play(cH, 150);
    t.play(a, 650);
 
    time.sleep(0.150)
    #end of second bit...
 
    t.play(aH, 500);
    t.play(a, 300);
    t.play(a, 150);
    t.play(aH, 400);
    t.play(gSH, 200);
    t.play(gH, 200);
    t.play(fSH, 125);
    t.play(fH, 125);
    t.play(fSH, 250);
 
    time.sleep(0.250)
 
    t.play(aS, 250);
    t.play(dSH, 400);
    t.play(dH, 200);
    t.play(cSH, 200);
    t.play(cH, 125);
    t.play(b, 125);
    t.play(cH, 250);
 
    time.sleep(0.250)
 
    t.play(f, 125);
    t.play(gS, 500);
    t.play(f, 375);
    t.play(a, 125);
    t.play(cH, 500);
    t.play(a, 375);
    t.play(cH, 125);
    t.play(eH, 650);
 
    #end of third bit... (Though it doesn't play well)
    #let's repeat it
 
    t.play(aH, 500);
    t.play(a, 300);
    t.play(a, 150);
    t.play(aH, 400);
    t.play(gSH, 200);
    t.play(gH, 200);
    t.play(fSH, 125);
    t.play(fH, 125);
    t.play(fSH, 250);
 
    time.sleep(0.250)
 
    t.play(aS, 250);
    t.play(dSH, 400);
    t.play(dH, 200);
    t.play(cSH, 200);
    t.play(cH, 125);
    t.play(b, 125);
    t.play(cH, 250);
 
    time.sleep(0.250)
 
    t.play(f, 250);
    t.play(gS, 500);
    t.play(f, 375);
    t.play(cH, 125);
    t.play(a, 500);
    t.play(f, 375);
    t.play(cH, 125);
    t.play(a, 650);
