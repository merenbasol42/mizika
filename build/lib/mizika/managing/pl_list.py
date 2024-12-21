'''
PLList, Playlist nesnelerini oluşturma, yoketme ve yönetmek için kullanılır.

PLList, tüm mevcut playlistleri dosya yolları olarak tutar. İhtiyaç halinde
PLaylist nesnesi yaratır. 
'''

import os
import json
from typing import Union
from .playlist import Playlist

class PLList:
    def __init__(self, path: str):
        self.path: str = path  # Kendisinin dosya yolu. Playlistlerin bilgilerinin tutulduğu json dosyalarının bulunduğu klasörün dosya yolu
        self.path_list: list[str] = []  # Playlistlerin json dosyalarının dosya yolları
        self.load()

    def load(self):
        '''
        "self.path" yolundaki klasördeki tüm json dosyalarının
        yollarını "self.path_list" listesine ekler
        '''
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        
        self.path_list = [
            os.path.join(self.path, f) 
            for f in os.listdir(self.path) 
            if f.endswith('.json')
        ]

    def get(self, name_or_index: Union[str, int]) -> Playlist:
        '''
        "self.path_list" e bulunan bir listeyi "Playlist" nesnesine
        çevirir ve döndürür.
        '''
        if isinstance(name_or_index, int):
            if 0 <= name_or_index < len(self.path_list):
                return Playlist(self.path_list[name_or_index])
            raise IndexError("Playlist index out of range")
        
        for path in self.path_list:
            if os.path.splitext(os.path.basename(path))[0] == name_or_index:
                return Playlist(path)
        
        raise ValueError(f"Playlist '{name_or_index}' not found")

    def create(self, name: str):
        '''
        "name" isminde yeni bir playlist oluşturur.
        Bu oluşturma "Playlist" nesnesi !yaratmaz!.
        JSON dosyasını oluşturur ve "self.path_list" e kaydeder.
        '''
        playlist_path = os.path.join(self.path, f"{name}.json")
        
        if os.path.exists(playlist_path):
            raise FileExistsError(f"Playlist '{name}' already exists")
        
        with open(playlist_path, 'w') as f:
            json.dump({"songs": []}, f, indent=2)
        
        self.path_list.append(playlist_path)

    def update(self, name_or_index: Union[str, int], new_name: str):
        '''
        Bir playlist'in ismini değiştirir
        Hem "path_list"teki varlığını hemde json dosyasını
        '''
        old_path = self.get(name_or_index).path
        new_path = os.path.join(self.path, f"{new_name}.json")
        
        if os.path.exists(new_path):
            raise FileExistsError(f"Playlist '{new_name}' already exists")
        
        os.rename(old_path, new_path)
        self.path_list[self.path_list.index(old_path)] = new_path

    def delete(self, name_or_index: Union[str, int]):
        '''
        Bir playlisti siler. 
        Hem "path_list"teki varlığını hemde json dosyasını
        '''
        path_to_delete = self.get(name_or_index).path
        self.path_list.remove(path_to_delete)
        os.remove(path_to_delete)
