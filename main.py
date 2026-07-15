import sys
import pygame
from machine import Machine


from settings import WIDTH, HEIGHT, BG_IMAGE_PATH, FPS


class Game:
    def __init__(self):

        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # noqa: F405
        pygame.display.set_caption("Slot Machine Demo")
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load(BG_IMAGE_PATH)  # noqa: F405

        # TODO:Create Machine class
        self.machine = Machine()
        self.delta_time = 0

        # Sound
        main_sound = pygame.mixer.Sound('audio/')
        # if track is done playing just play again
        main_sound.play(loops=-1)

    def run(self) -> None:

        # Tell when the game starts

        while True:
            # Handle quit operation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Time variables
            # Every time while is True
            self.start_time = pygame.time.get_ticks()
            self.delta_time = (pygame.time.get_ticks() -
                               self.start_time) / 1000

            # Update display with every tick
            pygame.display.update()
            # Draw background
            self.screen.blit(self.bg_image, (0, 0))
            self.machine.update(self.delta_time)
            self.clock.tick(FPS)


if "__name__" == "__main__":
    game = Game()
    # Continuously run
    game.run()
