# Mizika: Python Müzik Yönetim Kütüphanesi / Music Management Library

## Proje Açıklaması / Project Description
Mizika, Python için geliştirilmiş bir müzik yönetim kütüphanesidir. Müzik dosyalarını yönetmek, çalma listeleri oluşturmak ve müzik içeriğini işlemek için kullanışlı araçlar sağlar.

Mizika is a music management library developed for Python. It provides useful tools for managing music files, creating playlists, and processing music content.

## Özellikler / Features
- Müzik dosyalarını yönetme / Managing music files
- Çalma listesi oluşturma ve düzenleme / Creating and editing playlists
- Müzik dosyaları için temel işlemler / Basic operations for music files
- Esnek ve genişletilebilir mimari / Flexible and extensible architecture

## Kurulum / Installation
Projeyi yerel olarak kurmak için aşağıdaki komutu kullanabilirsiniz:
To install the project locally, use the following command:

```bash
pip install .
```

## Kullanım Örnekleri / Usage Examples

### Müzik Dosyası Oluşturma / Creating a Music File
```python
from mizika.core.song import Song

# Müzik dosyası oluşturma / Creating a music file
song = Song("müzik_dosyası_yolu.mp3")
```

### Çalma Listesi Yönetimi / Playlist Management
```python
from mizika.managing.playlist import Playlist

# Yeni çalma listesi oluşturma / Creating a new playlist
playlist = Playlist("Favoriler / Favorites")
playlist.add_song(song)
```

## Dizin Yapısı / Directory Structure
- `mizika/`: Ana kütüphane modülü / Main library module
  - `core/`: Temel sınıflar ve sabitler / Core classes and constants
  - `managing/`: Çalma listesi ve müzik yönetimi sınıfları / Playlist and music management classes
- `tester/`: Test ve örnek kullanım kodları / Test and example usage codes

## Geliştirme / Development
Projeye katkıda bulunmak isterseniz, lütfen bir issue açın veya pull request gönderin.
To contribute to the project, please open an issue or send a pull request.

## Lisans / License
Bu proje [LICENSE](LICENSE) dosyasında belirtilen lisans altında dağıtılmaktadır.
This project is distributed under the license specified in the [LICENSE](LICENSE) file.
