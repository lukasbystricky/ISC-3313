from Television import Television

# initialize TV object
tv = Television()

# turn on TV
tv.togglePower()

# increment volume by 1
tv.volumeUp()

# change to channel 15
tv.changeChannel(15)

print("Channel:", tv._channel)
print("Volume:", tv._volume)

# Mute TV
tv.toggleMute()
print("Volume:", tv._volume)

# Try to turn volume down
tv.volumeDown()
print("Volume:", tv._volume)
        
