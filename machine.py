import pygame
from settings import START_X, START_Y, SYMBOL_SIZE, OFFSET_X, NUM_REELS, SYMBOLS, GAME_WIDTH, GAME_HEIGHT
from reel import Reel

BASE_SPIN_DURATION = 1.5
STAGGER_SECONDS = 0.3


class Machine:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.spawn_reels()

    def spawn_reels(self) -> None:
        self.reels: list[Reel] = [
            Reel(
                pygame.Vector2(
                    START_X + i * (SYMBOL_SIZE + OFFSET_X), START_Y),
                SYMBOLS,
            )
            for i in range(NUM_REELS)
        ]
        for reel in self.reels:
            reel.spin()

    def spin_all(self) -> None:
        if any(reel.is_spinning for reel in self.reels):
            return   # не даём стартовать новый спин, пока предыдущий не закончился
        for i, reel in enumerate(self.reels):
            reel.start_spin(BASE_SPIN_DURATION + i * STAGGER_SECONDS)

    def update(self, dt: float) -> None:
        for reel in self.reels:
            reel.update(dt)

    def draw(self, surface: pygame.Surface) -> None:
        game_area = pygame.Rect(0, 0, GAME_WIDTH, GAME_HEIGHT)
        previous_clip = surface.get_clip()
        surface.set_clip(game_area)

        for reel in self.reels:
            reel.draw(surface)

        surface.set_clip(previous_clip)
