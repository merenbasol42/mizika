"""
Mizika müzik yönetim paketi.

Bu paket, müzik çalma, yönetme ve kontrol etme özellikleri sağlar.
"""

__version__ = "0.1.0"
__author__ = "Muzika Geliştirme Ekibi"

# Dış dünyaya açılacak temel sınıflar ve fonksiyonlar
from .mizika import Mizika
from .utils import (
    # Exception Sınıfları
    MizikaException,
    ConfigurationError,
    ResourceNotFoundError,
    
    # Utility Fonksiyonları
    safe_call,
    ensure_type,
    parse_shell_command
)

# Paket seviyesinde kullanılabilir tüm bileşenler
__all__ = [
    # Temel Sınıflar
    'Mizika',
    'Song',
    'MCore',
    'MManager',
    'Playlist',
    
    # Test Fonksiyonu
    'test',
    
    # Exception Sınıfları
    'MizikaException',
    'ConfigurationError',
    'ResourceNotFoundError',
    
    # Utility Fonksiyonları
    'safe_call',
    'ensure_type',
    'parse_shell_command'
]
