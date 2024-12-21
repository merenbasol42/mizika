'''
Mizika tüm özelliklerin birleştirildiği, kullanıcının giriş
noktasıdır.

Kullanıcı sadece bu sınıftan türettiği örnek ile müzika paketinin
sunduğu özellikleri kullanabilmelidir.
'''

from .managing.manager import MManager
from .core import MCore, Song 

class Mizika(MCore, MManager):
    def __init__(self, pls_dir_path: str):
        '''pls_dir_path: Playlistlerin json dosyalarının bulunduğu klasörün dosya yolu'''
        MCore.__init__(self)
        MManager.__init__(self, pls_dir_path)

    def load_song(self, index_or_song: int | Song):
        song = index_or_song
        if not isinstance(song, Song):
            # Eğer indeks verilirse, playlist'ten şarkıyı al
            song = self.play_pl.get_a_song(index_or_song)
        
        # Şarkıyı yükle
        super().load_song(song)
    
    def forward(self):
        self.load_song(
            super().forward()  
        )

    def backward(self):
        self.load_song(
            super().backward()
        )
