# Define parameters associated with settings
# Created by Will Xu on July 16th, 2017


class Settings:

    def __init__(self):

        # Define screen parameters and values;
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Define ship speed factor and value;
        self.ship_speed_factor = 1.5

        # Define bullet parameters and values;
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_ammunition = 5
