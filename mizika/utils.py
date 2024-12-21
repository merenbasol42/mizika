"""
"mizika" paketine ait tüm utility öğelerinin tanımlandığı betik.

Örneğin pakete özel exception sınıfları ve ortak yardımcı fonksiyonlar.
"""

from typing import Any, Callable, Optional, TypeVar, Union
import os
import logging
import functools

#
# Paket Özel Exception Sınıfları
#
class MizikaException(Exception):
    """Mizika paketi için temel exception sınıfı"""
    pass

class ConfigurationError(MizikaException):
    """Konfigürasyon hatalarında kullanılacak exception"""
    pass

class ResourceNotFoundError(MizikaException):
    """Kaynak bulunamadığında kullanılacak exception"""
    pass

#
# Ortak Utils
#
def safe_call(default_return: Any = None) -> Callable:
    """
    Fonksiyon çağrımlarında hata yakalama decorator'ı
    
    Args:
        default_return: Hata durumunda döndürülecek varsayılan değer
    
    Returns:
        Decorator fonksiyonu
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.error(f"Hata oluştu: {e}")
                return default_return
        return wrapper
    return decorator

def ensure_type(expected_type: type, error_message: Optional[str] = None) -> Callable:
    """
    Fonksiyon parametrelerinin tipini kontrol eden decorator
    
    Args:
        expected_type: Beklenen parametre tipi
        error_message: Özel hata mesajı
    
    Returns:
        Decorator fonksiyonu
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(arg: Any, *args: Any, **kwargs: Any) -> Any:
            if not isinstance(arg, expected_type):
                msg = error_message or f"Parametre {expected_type.__name__} tipinde olmalı"
                raise TypeError(msg)
            return func(arg, *args, **kwargs)
        return wrapper
    return decorator

#
# MShell Utils
#
def parse_shell_command(command: str) -> dict:
    """
    Shell komutlarını ayrıştırır
    
    Args:
        command: İşlenecek komut dizesi
    
    Returns:
        Komut bilgilerini içeren sözlük
    """
    parts = command.split()
    return {
        'command': parts[0] if parts else None,
        'args': parts[1:] if len(parts) > 1 else []
    }

#
# Diğer Paket Utility'leri
#
from .core.utils import *
from .managing.utils import *

__all__ = [
    # Exception Sınıfları
    'MizikaException',
    'ConfigurationError', 
    'ResourceNotFoundError',
    
    # Utility Fonksiyonları
    'safe_call',
    'ensure_type',
    'parse_shell_command'
]
