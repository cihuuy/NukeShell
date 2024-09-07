# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=['.', './Core'],  # Sesuaikan jalur jika ada perubahan
    binaries=[],
    datas=[],
    hiddenimports=['Crypto', 'pyscreenshot', 'Pillow'],  # Pastikan impor ini ada di Linux
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],  # Tambahkan modul yang ingin dikecualikan jika diperlukan
    noarchive=False,
    optimize=0,  # Jika ingin optimasi, gunakan level 1 atau 2
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,  # Ubah ke True jika ingin melihat informasi debug
    bootloader_ignore_signals=False,
    strip=True,  # Aktifkan strip untuk mengurangi ukuran binary di Linux
    upx=True,  # Pastikan UPX terinstal di sistem Linux, atau ubah ke False jika tidak diperlukan
    upx_exclude=[],  # Jika ada library yang tidak kompatibel dengan UPX, tambahkan di sini
    runtime_tmpdir=None,
    console=True,  # Ubah ke False jika ingin menjalankan aplikasi tanpa konsol
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,  # Opsi ini relevan hanya untuk macOS, tidak diperlukan di Linux
    entitlements_file=None,  # Hanya relevan untuk macOS
)
