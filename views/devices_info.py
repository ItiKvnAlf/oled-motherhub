import display.config as config
from utils.center_text import center_text
from utils.scroll_text import start_scrolling_text
from display.config import draw, width, font

def mother_info_view():
    item = config.data['mh']
    ssid = item['ssid']
    ip = item['ip']
    linked = item['linked']

    if ssid == None:
        ssid = "N/A"

    if ip == None:
        ip = "N/A"

    if linked > 1:
        linked = f"{linked} DBs"
    elif linked == 0:
        linked = "N/A"
    else:
        linked = f"{linked} DB"

    draw.text((0, 0), f"SSID: ", font=font, fill=255)
    draw.text((0, 10), f"IP: {ip}", font=font, fill=255)
    draw.text((0, 20), f"LINKED TO: {linked}", font=font, fill=255)

    max_width = (width - (draw.textlength("SSID: ")))
    x_pos = (draw.textlength("SSID: "))
    start_scrolling_text(config.data['current_state'], config.data['current_index'], f"{ssid}", max_width, x_pos, 0)

def mother_info_password_view():
    item = config.data['mh']
    password = item['password']

    if config.data['reveal_password'] == True:
        text1 = f"PASS: {password}"
        text2 = "PUSH to hide"
        draw.text((center_text(text1) - 8, 5), text1, font=font, fill=255)
        draw.text((center_text(text2) - 8, 20), text2, font=font, fill=255)
    else:
        text1 = "PASS: ********"
        text2 = "PUSH to reveal"
        draw.text((center_text(text1), 5), text1, font=font, fill=255)
        draw.text((center_text(text2), 20), text2, font=font, fill=255)
