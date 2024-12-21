'''
MCore, temel çalma işlevlerinin kolay bir erişim ile sunulduğu bir sınıftır.
MCore sınıfı, "mizika" paketinin çekirdeğidir.

MCore sınıfı müzik çalma işlevi için python-vlc kullanır.
'''
from typing import Optional

import vlc
from .song import Song
from .consts import *

class MCore:
    __instance: 'MCore' = None
    def __init__(self):
        if MCore.__instance is not None: return MCore.__instance
        else: MCore.__instance = self
        self.__vlc_ins = vlc.Instance()
        self.__player = self.__vlc_ins.media_player_new()

        self.state: bool = False  # is playing or paused
        self.volume: float = 50.0  # default volume at 50%
        self.curr_song: Optional[Song] = None  # current playing song

    def load_song(self, song: Song):
        '''Şarkıyı oynatıcıya yükler'''
        media = self.__vlc_ins.media_new(song.path)
        self.__player.set_media(media)
        self.curr_song = song
        self.__player.audio_set_volume(int(self.volume))

    #
    # State
    #

    def play(self):
        '''
        "state"i true olarak ayarlar. Müziği başlatır veya
        devam ettirir. Zaten çalıyorsa birşeye ellemez
        '''
        if not self.state and self.curr_song:
            self.__player.play()
            self.state = True

    def pause(self):
        '''Müzik çalmayı duraklatır'''
        if self.state:
            self.__player.pause()
            self.state = False

    #
    # Position
    #
    
    def get_pos(self):
        return self.__player.get_time() / S_TO_MS

    def set_pos(self, new_pos: float):
        '''Şarkının pozisyonunu "new_pos" olarak ayarlar'''
        if self.curr_song: 
            self.__player.set_time(new_pos * S_TO_MS)

    def rewind(self, val: float = DEFAULT_WIND):
        '''Şarkının pozisyonunu "val" kadar geriye sarar'''
        self.set_pos(
            max(0.0, self.get_pos() - val)
        )

    def towind(self, val: float = DEFAULT_WIND):
        '''Şarkının pozisyonunu "val" kadar ileriye sarar'''
        self.set_pos(
            min(
                self.curr_song.length,
                self.get_pos() + val
            )
        )

    #
    # Volume
    #

    def set_vol(self, percent: float):
        '''
        Ses düzeyini "percent" olarak ayarlar
        Dikkat edilmesi gereken husus "percent" 0 ila 100 arasına getirilir
        '''
        if percent < 0: percent = 0
        elif percent > 100: percent = 100
        
        self.player.audio_set_volume(int(percent))
        self.volume = percent

    def inc_vol(self, percent: float):
        '''
        Ses düzeyini "percent" kadar artırır
        Dikkat edilmesi gereken husus "percent" 0 ila 100 arası olmalıdır
        '''
        self.set_vol(self.volume + percent)

    def desc_vol(self, percent: float):
        '''
        Ses düzeyini "percent" kadar azaltır
        Dikkat edilmesi gereken husus "percent" 0 ila 100 arası olmalıdır
        '''
        self.set_vol(self.volume - percent)
