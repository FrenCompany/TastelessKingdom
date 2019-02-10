from src.control.Driver import Driver
from src.utils import init_screen


def main():
    screen = init_screen()
    driver = Driver(screen)

    while True:
        driver.tick()


if __name__ == "__main__":
    main()
