
import pygame
import random
from settings import *
from symbol_sprite import SymbolSprite
from easing import ease_out_cubic

SPIN_FILLER_STEPS = 20


class Reel:
    def __init__(self, pos: pygame.Vector2, symbols: dict[str, SymbolConfig]) -> None:
        self.pos = pos
        # {"cherry": {"weight": 10, "image_path": "..."}, ...}
        self.symbols = symbols
        self.symbol_sprites = pygame.sprite.Group()

        # Spinnig logic
        self._slot_sprites: list[SymbolSprite] = []
        self.is_spinning = False
        self.spin_elapsed = 0.0
        self.spin_duration = 0.0
        self.strip: list[str] = []

        self.spin()

    def _pick_random_symbols(self, count: int = 5) -> list[str]:
        names = list(self.symbols.keys())
        weights = [self.symbols[name].weight for name in names]
        return random.choices(names, weights=weights, k=count)

    def _set_slots(self, names: list[str]) -> None:
        """(Пере)создаёт 5 спрайтов под конкретный набор имён — используется и для мгновенного спина, и как стартовое состояние анимации."""
        self.symbol_sprites.empty()
        self._slot_sprites = []
        for i, name in enumerate(names):
            sprite = SymbolSprite(self.symbols[name], self.pos, i)
            self.symbol_sprites.add(sprite)
            self._slot_sprites.append(sprite)

    def spin(self) -> None:
        """Мгновенный (без анимации) спин — даёт финальный результат сразу."""
        self._set_slots(self._pick_random_symbols(5))

    def start_spin(self, duration: float) -> None:
        """Запускает анимированный спин: строит ленту (мелькание + финал), включает состояние SPINNING."""
        filler = self._pick_random_symbols(SPIN_FILLER_STEPS)
        final_symbols = self._pick_random_symbols(5)
        self.strip = filler + final_symbols

        self.is_spinning = True
        self.spin_elapsed = 0.0
        self.spin_duration = duration
        self._set_slots(self.strip[0:5])

    def update(self, dt: float) -> None:
        if not self.is_spinning:
            return

        self.spin_elapsed += dt
        progress = min(self.spin_elapsed / self.spin_duration, 1.0)
        eased = ease_out_cubic(progress)

        # сколько всего "шагов" пройдёт окно за весь спин
        max_scroll = len(self.strip) - 5
        scroll = eased * max_scroll
        strip_index = int(scroll)
        sub_offset = (scroll - strip_index) * SYMBOL_SIZE

        visible_names = self.strip[strip_index: strip_index + 5]
        for i, (sprite, name) in enumerate(zip(self._slot_sprites, visible_names)):
            if sprite.name != name:
                sprite.set_symbol(self.symbols[name])
            base_y = self.pos.y + i * (SYMBOL_SIZE + OFFSET_Y)
            sprite.rect.topleft = (self.pos.x, base_y - sub_offset)

        if progress >= 1.0:
            self.is_spinning = False

    def draw(self, surface: pygame.Surface) -> None:
        self.symbol_sprites.draw(surface)

        # TODO add sounds
        # self.stop_sound = pygame.mixer.Sound("audio/stop.mp3")
        # self.stop_sound.set_volume(0.5)
