from display.config import draw, font, width

def menu_view():
    """Display the main menu."""
    text1 = f"[MH]"
    draw.text((0, 0), " PUSH: Config ", font=font, fill=255)
    draw.text((0, 10), "RIGHT: Info ", font=font, fill=255)
    draw.text((0, 20), " DOWN: Daughters ", font=font, fill=255)
    draw.text((width - draw.textlength(text1), 0), text1, font=font, fill=255)