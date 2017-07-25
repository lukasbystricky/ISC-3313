class Television:
    
    def __init__(self):
        """
        Initialization routine. You may have decided to take in arguments
        as parameters to your constructor. I decided against that. This
        creates a TV that is turned off, unmuted with volume 10 and set
        to channel 2.
        """
        
        self._powerOn = False
        self._muted = False
        self._volume = 10
        self._channel = 2
        
    def togglePower(self):
        """
        Turns TV off if it is on and on if it is off.
        """
        
        self._powerOn = not self._powerOn
        
    def toggleMute(self):
        """
        Mutes the TV if it is unmuted and sets the volume to 0, otherwise
        unmutes the TV. I set this to work only if the TV is turned on.
        """
        
        if self._powerOn:            
            self._muted = not self._muted
        
            if self._muted:
                self._volume = 0
            
    def volumeUp(self):
        """
        Increments the volume by 1. Again I set this to work only if the
        TV is turned on.
        """
        
        if self._powerOn:   
            self._volume += 1
        
    def volumeDown(self):
        """
        Decrements the volume by 1. Only works if the TV is turned on and
        the volume is not 0.
        """
        
        if self._powerOn:   
            if self._volume > 0:
                self._volume -= 1
            
    def changeChannel(self, channel):
        """
        Changes the channel to a specified channel. Works only if the 
        TV is turned on.
        """
        
        if self._powerOn:   
            self._channel = channel
        
