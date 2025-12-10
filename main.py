import arcade
from config import config

class MyFirstArcadeGame(arcade.Window):
    def __init__(self, width, height, title, isfullscreen, background_color):
        super().__init__(width, height, title, isfullscreen)
        self.background_color = background_color
        
    def setup(self):
        pass

    def on_draw(self):
        self.clear()


def main():
    screen_width = config["screenwidth"]
    screen_height = config["screenheight"]
    window_title = config["windowtitle"]
    bool_isfullscreen = config["isfullscreen"]
    background_color = config["rgb_background_color"]

    game = MyFirstArcadeGame(
        width=screen_width,
        height=screen_height,
        title=window_title,
        isfullscreen=bool_isfullscreen,
        background_color=background_color
    )

    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()