# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "httpx",
#     "toga",
#     "toga-web",
# ]
# ///

"""
Draw the mandelbrot set in a Beeware Toga app
"""

import httpx
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


def greeting(name):
    name = name.strip() or "stranger"
    return f"Hello, {name}"


class TogaMandelbrot(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            "Your name: ",
            style=Pack(padding=(0, 5)),
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            "Say Hello!",
            on_press=self.say_hello,
            style=Pack(padding=5),
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def older_say_hello(self, widget):
        print(f"Hello, {self.name_input.value}")

    async def old_say_hello(self, widget):
        await self.main_window.dialog(
            toga.InfoDialog(
                greeting(self.name_input.value),
                "Hi there!",
            )
        )

    async def say_hello(self, widget):
        async with httpx.AsyncClient() as client:
            response = await client.get("https://jsonplaceholder.typicode.com/posts/42")

        payload = response.json()
        # print(payload["body"])

        await self.main_window.dialog(
            toga.InfoDialog(
                greeting(self.name_input.value),
                payload["body"],
            )
        )


def main() -> toga.App:
    return TogaMandelbrot()
