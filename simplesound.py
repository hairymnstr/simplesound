import pygame, numpy

class Tone:
    def __init__(self):
        """ Create a new tone generator """
        if pygame.mixer.get_init() == None:
            pygame.init()
        self.sample_rate, self.format, self.channels = pygame.mixer.get_init()
    
    def _make_sample(self, freq):
        if self.format < 0:
            peak = 2 ** (abs(self.format)-1)
        else:
            peak = 2 ** self.format
        omega = numpy.pi * 2 * freq / self.sample_rate
        xvalues = numpy.arange(int(self.sample_rate)) * omega
        return (peak * numpy.sin(xvalues))
    
    def play(self, freq, period_ms):
        """ Play a tone of specified frequency for a period of time.
            freq = frequency in Hz
            period_ms = time to play for in millisecods """
        smp = self._make_sample(freq)
        
        if self.channels == 2:
            smp = numpy.array(zip(smp, smp)).astype(numpy.int16)
        snd = pygame.sndarray.make_sound(smp)
        loops = period_ms / 1000
        if period_ms % 1000:
            loops += 1
        loops -= 1
        
        snd.play(loops, period_ms)
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