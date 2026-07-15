from dataclasses import dataclass

# Display settings
ORIGINAL_GAME_WIDTH = 1600
ORIGINAL_GAME_HEIGHT = 900       # именно фон/игровая зона, без UI
ORIGINAL_UI_HEIGHT = 100

SCALE = 0.8

GAME_WIDTH = int(ORIGINAL_GAME_WIDTH * SCALE)      # 1280
GAME_HEIGHT = int(ORIGINAL_GAME_HEIGHT * SCALE)     # 720
UI_HEIGHT = int(ORIGINAL_UI_HEIGHT * SCALE)          # 80

WIDTH = GAME_WIDTH                        # 1280
HEIGHT = GAME_HEIGHT + UI_HEIGHT           # 800
FPS = 120

# Images
BG_IMAGE_PATH = "graphics/bg.png"
SYMBOL_PATH = "graphics/symbols/0_{}.png"


@dataclass(frozen=True)
class SymbolConfig:
    name: str
    image_path: str
    weight: int


# 5 symbols for demo, random weights
SYMBOLS: dict[str, SymbolConfig] = {
    cfg.name: cfg
    for cfg in [
        SymbolConfig("diamond", SYMBOL_PATH.format("diamond"), weight=5),
        SymbolConfig("floppy", SYMBOL_PATH.format("floppy"), weight=15),
        SymbolConfig("hourglass", SYMBOL_PATH.format("hourglass"), weight=15),
        SymbolConfig("seven", SYMBOL_PATH.format("seven"), weight=5),
        SymbolConfig("telephone", SYMBOL_PATH.format("telephone"), weight=20),
    ]
}

GAME_INDICES = range(1, 4)   # 0 and 4 are outside of visible game area
NUM_REELS = 5
SYMBOL_SIZE = min(GAME_WIDTH // NUM_REELS, GAME_HEIGHT // 3)   # 240

_reels_total_width = NUM_REELS * SYMBOL_SIZE                    # 1200
_horizontal_margin = (GAME_WIDTH - _reels_total_width) // 2      # 40

START_X = _horizontal_margin
START_Y = -SYMBOL_SIZE

OFFSET_X = 0
OFFSET_Y = 0
