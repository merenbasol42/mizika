'''
Song, herhangi bir şarkıyı temsil etmek için kullanılan bir sınıftır.
'''
import os
import vlc
from typing import Optional

class Song:
    def __init__(self, path: str):
        self.path: str = path
        self.length: Optional[float] = None
    
    def check(self) -> bool:
        '''Şarkının herhangi bir sorunun olup olmadığını test eder'''
        return self.__path_check() and self.__length_check()

    def __path_check(self) -> bool:
        '''Şarkının, verilen konumda olup olmadığını kontrol eder'''
        return os.path.exists(self.path) and os.path.isfile(self.path)

    def __length_check(self) -> bool:
        '''Şarkının uzunluğunu bulmaya çalışır'''
        try:
            instance = vlc.Instance()
            media = instance.media_new(self.path)
            media.parse()
            
            # Uzunluğu milisaniye cinsinden al
            duration = media.get_duration()
            
            # Eğer uzunluk 0 veya negatifse geçersiz kabul et
            if duration <= 0:
                return False
            
            # Uzunluğu saniye cinsinden kaydet
            self.length = duration / 1000.0
            return True
        except Exception:
            return False
