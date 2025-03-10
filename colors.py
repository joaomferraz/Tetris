class Colors:
        dark_grey = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        dark_blue = (44, 44, 127)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)

        @classmethod
        def get_cell_colors(cls):
            return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.dark_blue, cls.cyan, cls.blue]
        