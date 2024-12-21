'''
Playlist, MManager üstünden kullanılacak olan; oynatma listesini
temsil eden sınıftır.

Daha çok bir veri yapısıdır.
'''

import os
import json
from typing import Optional, Union
from ..core.song import Song

class Playlist:
    def __init__(self, path: str):
        self.path: str = path  # Kendisinin JSON dosya yolu. Playlistin bilgileri bir JSON dosyasında tutulur
        self.path_list: list[str] = []  # Şarkıların dosya yollarının bulunduğu liste
    
    def load(self):
        '''
        "self.path" dosya yolunda bulunan json dosyasındaki
        tüm şarkıların yollarını "self.path_list"e kaydeder
        '''
        if not os.path.exists(self.path):
            with open(self.path, 'w') as f:
                json.dump({"songs": []}, f, indent=2)
        
        with open(self.path, 'r') as f:
            data = json.load(f)
            self.path_list = data.get('songs', [])

    def get_a_song(self, index: int) -> Song:
        '''Bir şarkı nesnesi oluşturur ve döndürür'''
        if 0 <= index < len(self.path_list):
            return Song(self.path_list[index])
        raise IndexError("Song index out of range")

    def check(self, index: Optional[int] = None) -> bool:
        '''Eğer index == None ise tüm şarkıları kontrol eder'''
        if index is not None:
            return (0 <= index < len(self.path_list) and 
                    os.path.exists(self.path_list[index]))
        
        return all(os.path.exists(song_path) for song_path in self.path_list)

    def add_song(self, *paths: str):
        '''playlistin sonuna bir şarkı ekler'''
        for path in paths:
            if not os.path.exists(path): raise Exception("Böyle bir dosya yok")
            if self.path_list.count(path) > 0: raise Exception("Böyle bir müzik zaten kayıtlı")
            self.path_list.append(path)
        
        self._save_playlist()

    def remove_song(self, *indexs: int):
        '''verilen indexteki şarkıyı, listeden kaldırır'''
        sorted_indexs = sorted(indexs, reverse=True)
        for index in sorted_indexs:
            if 0 <= index < len(self.path_list):
                del self.path_list[index]
        
        self._save_playlist()

    def insert_song(self, up_down: bool, target: int, *indexs: int):
        '''
        Bir veya daha fazla şarıkının sırasını değiştirir
        "indexs"teki şarkıları target'a yerleştirir.
        "up_down" parametresine göre eskiden "target" indisinde
        olan eleman aşağı veya yukarıya itilir.
        '''
        if not (0 <= target < len(self.path_list)):
            raise IndexError("Target index out of range")
        
        # Validate all indexes
        if not all(0 <= idx < len(self.path_list) for idx in indexs):
            raise IndexError("One or more song indexes out of range")
        
        # Extract songs to move
        songs_to_move = [self.path_list[idx] for idx in indexs]
        
        # Remove songs from their original positions
        for idx in sorted(indexs, reverse=True):
            del self.path_list[idx]
        
        # Insert songs at the target position
        insert_pos = target + 1 if up_down else target
        for song in songs_to_move:
            self.path_list.insert(insert_pos, song)
        
        self._save_playlist()

    def _save_playlist(self):
        '''Playlist'i JSON dosyasına kaydeder'''
        with open(self.path, 'w') as f:
            json.dump({"songs": self.path_list}, f, indent=2)
