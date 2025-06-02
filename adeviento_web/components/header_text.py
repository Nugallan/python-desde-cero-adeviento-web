import reflex as rx
from adeviento_web.styles.styles import Size, TextColor

def header_text(icon: str, text: str, dark=True) -> rx.Component:
    return rx.hstack(
        rx.box(
            class_name=f"nes-icon is-medium {icon}"
        ),
        rx.heading(
            text,
            size="5",
            color=TextColor.ACCENT.value if dark else TextColor.SECONDARY.value
        ),
        spacing="5",
        padding_bottom=Size.BUTTON.value,
        align="center"
    )