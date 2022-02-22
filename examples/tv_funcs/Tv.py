class Tv:
    def __init__(self, volume, channel, size, on):
        self.__volume = volume
        self.__channel = channel
        self.__size = size
        self.__on = on
        self.__volume = 50
        self.__channel = 1
        self.__on = False

    
    def volume_up(self, volume):
        if self.__volume + volume < 100:
            self.__volume += volume
        else:
            print('Volume is at its maximum')


    def volume_down(self, volume):
        if self.__volume - volume > 0:
            self.__volume -= volume
        else:
            print('Volume is at its minimum')



volDown = Tv(50, 1, '32"', True)
# volDown.volume_down(100)
print(volDown.volume_down(100))