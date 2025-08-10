import toga
from settings import *


class Milo(toga.App):
    def startup(self) -> None:
        # self.main_window = toga.MainWindow(size=(500, 700))
        self.main_window = toga.MainWindow()
        # card_front = toga.Image("resources/images/card_front.png")
        card_front = Image.open("resources/images/card_front.png")
        card_back = Image.open("resources/images/card_back.png")
        # card_back = toga.Image("resources/images/card_back.png")
        right = toga.Image("resources/images/right.png")
        wrong = toga.Image("resources/images/wrong.png")
        title_font = ImageFont.truetype("resources/fonts/Roboto-Italic.ttf", 40)
        word_font = ImageFont.truetype("resources/fonts/Roboto-Bold.ttf", 60)
        # toga.Font.register("Roboto", "resources/Roboto-Regular.ttf")

        self.wrapper = toga.Column(
            style=Pack(
                background_color=RED,
                align_items=CENTER,
                justify_content=CENTER,
            ),
        )
        self.page = toga.Column(
            style=Pack(
                flex=1,
                background_color=BLUE,
                # gap=10,
                padding=10,
                align_items=CENTER,
                justify_content=CENTER,
            )
        )
        # self.header = toga.Row(style=Pack(flex=1, background_color=BURLYWOOD))
        # self.body = toga.Row(style=Pack(flex=1, background_color=GREEN))
        self.body = toga.Row(style=Pack(background_color=GREEN))
        self.footer = toga.Row(
            # style=Pack(background_color=YELLOW, width=300, height=100, gap=10)
            style=Pack(background_color=YELLOW, gap=250)
        )

        self.card_front = toga.ImageView(card_front)
        cfront_size = (800, 526)
        val = cfront_size[1] / 4
        crd_pos = cfront_size[1] / val

        if pil_present:
            img_canvas = ImageDraw.Draw(card_front)
            img_canvas.text(
                (cfront_size[0] / 2, cfront_size[1] / 3),
                "Title - Pillow image",
                fill="red",
                anchor="mm",
                font=title_font,
            )
            img_canvas.text(
                (cfront_size[0] / 2, cfront_size[1] / 1.5),
                "Word - Pillow image",
                fill="green",
                anchor="mm",
                font=word_font,
            )
            print(crd_pos)
            self.card_front = toga.ImageView(
                card_front,
            )

        self.card_back = toga.ImageView(card_front)
        self.right = toga.ImageView(right)
        self.wrong = toga.ImageView(wrong)

        #
        self.body.add(self.card_front)
        self.footer.add(self.right, self.wrong)

        # Add nodes
        self.page.add(self.body, self.footer)
        self.wrapper.add(self.page)

        # # Add the content on the main window
        self.main_window.content = self.wrapper

        # Show the main window
        self.main_window.show()


def main():
    return Milo("Milo", "com.tnkvie.milo")


if __name__ == "__main__":
    main().main_loop()
