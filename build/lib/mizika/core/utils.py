'''
Core paketinin yardımcı fonksiyonlarını içerir.
Müzik dosyaları ve işlemleri ile ilgili genel utility fonksiyonları.
'''
import os
import mimetypes
from typing import List, Optional

def is_music_file(file_path: str) -> bool:
    '''
    Verilen dosyanın müzik dosyası olup olmadığını kontrol eder.
    
    Args:
        file_path (str): Kontrol edilecek dosyanın yolu
    
    Returns:
        bool: Dosya müzik dosyası ise True, değilse False
    '''
    # Desteklenen müzik dosya uzantıları
    music_extensions = [
        '.mp3', '.wav', '.flac', '.ogg', 
        '.m4a', '.aac', '.wma', '.opus'
    ]
    
    # Dosya uzantısını kontrol et
    file_ext = os.path.splitext(file_path)[1].lower()
    if file_ext in music_extensions:
        return True
    
    # MIME tipini kontrol et
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type is not None and mime_type.startswith('audio/')

def list_music_files(directory: str) -> List[str]:
    '''
    Belirli bir dizindeki tüm müzik dosyalarını listeler.
    
    Args:
        directory (str): Taranacak dizinin yolu
    
    Returns:
        List[str]: Bulunan müzik dosyalarının tam yolları
    '''
    music_files = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            if is_music_file(full_path):
                music_files.append(full_path)
    
    return music_files

def format_duration(seconds: Optional[float]) -> str:
    '''
    Saniye cinsinden verilen süreyi dakika:saniye formatına çevirir.
    
    Args:
        seconds (Optional[float]): Saniye cinsinden süre
    
    Returns:
        str: Dakika:saniye formatında süre
    '''
    if seconds is None or seconds < 0:
        return "00:00"
    
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    
    return f"{minutes:02d}:{secs:02d}"
