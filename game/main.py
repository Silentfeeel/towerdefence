import arcade
from config import (SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, BOOL_ISFULLSCREEN, 
                    BACKGROUND_COLOR, MUSIC_VOLUME, GITHUB_REPO_PAGE)
import os
import webbrowser


class Game(arcade.Window):
    def __init__(self, width, height, title, isfullscreen, background_color):
        super().__init__(width, height, title, isfullscreen)
        self.background_color = background_color

        self.is_main_menu = True

        self.main_menu_buttons = arcade.SpriteList()
        self.always_visible_sprites = arcade.SpriteList()

        self.set_mouse_visible(False)
        
        
    def setup(self):
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        ASSETS_PATH = os.path.join(BASE_PATH, "..", "assets")

        self.medival_cursor = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "medival_cursor.png"),
            scale=1.0
        )

        self.bg_img = arcade.load_texture(
            os.path.join(ASSETS_PATH, "pngs", "main_menu_bg.png")
        )

        self.main_menu_title = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "main_menu_game_title.png"),
            scale=1.0
        )
        
        self.start_btn = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "start_game_btn.png"),
            scale=0.8
        )

        self.exit_game_btn = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "exit_game_btn.png"),
            scale=0.8
        )

        self.github_logo = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "github-mark.png"),
            scale=0.4
        )

        self.start_btn.center_x = self.width // 2
        self.start_btn.center_y = self.height // 2 - 120

        self.exit_game_btn.center_x = (self.width // 2)
        self.exit_game_btn.center_y = (self.height // 2) - 400

        self.main_menu_title.center_x = self.width // 2
        self.main_menu_title.center_y = self.height - 280

        self.github_logo.center_x = 50
        self.github_logo.center_y = 50
        
        self.medival_cursor.center_x = 0
        self.medival_cursor.center_y = 0

        self.main_menu_buttons.append(self.start_btn)
        self.main_menu_buttons.append(self.exit_game_btn)
        self.main_menu_buttons.append(self.main_menu_title)
        self.main_menu_buttons.append(self.github_logo)
        self.always_visible_sprites.append(self.medival_cursor)

        self.main_theme_music = arcade.load_sound(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            ASSETS_PATH,
            "music",
            "main_theme.mp3"
        ))
        arcade.play_sound(self.main_theme_music, volume=MUSIC_VOLUME, loop=True)

    def on_mouse_press(self, x, y, button, modifiers):
        clicked_sprites = arcade.get_sprites_at_point((x, y), self.main_menu_buttons)

        for sprite in clicked_sprites:
            if sprite == self.exit_game_btn:
                self.exit_game()
            elif sprite == self.github_logo:
                self.open_github_page()
            elif sprite == self.start_btn:
                pass
        return super().on_mouse_press(x, y, button, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        self.medival_cursor.center_x = x
        self.medival_cursor.center_y = y
        return super().on_mouse_motion(x, y, dx, dy)

    def on_draw(self):
        self.clear()

        if self.is_main_menu: 
            arcade.draw_texture_rect(self.bg_img, arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))
            self.main_menu_buttons.draw()

        self.always_visible_sprites.draw()

    def exit_game(self):
        arcade.exit()
        return

    def open_github_page(self):
        webbrowser.open(GITHUB_REPO_PAGE)
        return
        

def main():
    game = Game(
        width=SCREEN_WIDTH,
        height=SCREEN_HEIGHT,
        title=WINDOW_TITLE,
        isfullscreen=BOOL_ISFULLSCREEN,
        background_color=BACKGROUND_COLOR
    )

    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
