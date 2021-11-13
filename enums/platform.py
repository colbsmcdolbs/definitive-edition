from enum import Enum


class Platform(Enum):
    # PC
    PC = 'PC'

    # Nintendo
    NES = 'Nintendo Entertainment System'
    SNES = 'Super Nintendo Entertainment System'
    N64 = 'Nintendo 64'
    GC = 'Nintendo GameCube'
    WII = 'Nintendo Wii'
    WIIU = 'Nintendo Wii U'
    NSW = 'Nintendo Switch'
    GB = 'Nintendo GameBoy'
    GBC = 'Nintendo GameBoy Color'
    GBA = 'Nintendo GameBoy Advance'
    NDS = 'Nintendo DS'
    N3DS = 'Nintendo 3DS'

    # Sony
    PS1 = 'Sony PlayStation'
    PS2 = 'Sony PlayStation 2'
    PS3 = 'Sony PlayStation 3'
    PS4 = 'Sony PlayStation 4'
    PS5 = 'Sony PlayStation 5'
    PSP = 'Sony PlayStation Portable'
    PSV = 'Sony PlayStation Vita'

    # Sega
    SMS = 'Sega Master System'
    SG = 'Sega Genesis'
    SCD = 'Sega CD'
    S32X = 'Sega 32x'
    SS = 'Sega Saturn'
    SD = 'Sega Dreamcast'

    # Microsoft
    XB = 'Microsoft Xbox'
    XB360 = 'Microsoft Xbox 360'
    XB1 = 'Microsoft Xbox One'
    XBS = 'Microsoft Xbox Series S/X'

    # Misc
    ARC = 'Arcade'
    MOB = 'Mobile'
