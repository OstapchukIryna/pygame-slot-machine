import sys
import pygame
from machine import Machine

from settings import WIDTH, HEIGHT, BG_IMAGE_PATH, FPS, GAME_WIDTH, GAME_HEIGHT, UI_HEIGHT


class Game:
    def __init__(self):

        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # noqa: F405
        pygame.display.set_caption("Slot Machine Demo")
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load(BG_IMAGE_PATH).convert()
        self.bg_image = pygame.transform.smoothscale(
            self.bg_image, (GAME_WIDTH, GAME_HEIGHT))

        self.machine = Machine()
        self.delta_time = 0

        # Sound
        # main_sound = pygame.mixer.Sound('audio/audio_track.mp3')
        # if track is done playing just play again
        # main_sound.play(loops=-1)

    def run(self) -> None:

        # Tell when the game starts

        while True:
            # Handle quit operation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.machine.spin_all()

            # Time variables
            self.delta_time = self.clock.tick(FPS) / 1000

            # Draw background
            self.screen.blit(self.bg_image, (0, 0))
            pygame.draw.rect(self.screen, (20, 20, 20),
                             (0, GAME_HEIGHT, WIDTH, UI_HEIGHT))
            self.machine.update(self.delta_time)
            self.machine.draw(self.screen)
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    # Continuously run
    game.run()
