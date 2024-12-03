import display.config as config
from utils.center_text import center_text
from display.config import draw, font

def daughters_info_view():
    item = config.data['dbs']
    daughters_detected = len(item)

    if daughters_detected < 10:
        daughters_detected = f"0{daughters_detected}"

    text1 = f"DAUGHTERS DETECTED:{daughters_detected}"
    text2 = "Push to refresh"
    draw.text((0, 0), text1, font=font, fill=255)
    draw.text((0, 20), text2, font=font, fill=255)
    
def daughters_detected_view():
    item = config.data['dbs'][config.data['current_index']]
    ip = item["ip"]
    page = f"({config.data['current_index']+1}/{len(config.data['dbs'])})"

    draw.text((0, 5), f"IP {page}: ", font=font, fill=255)
    draw.text((10, 15), ip, font=font, fill=255)

def no_daughters_view():
    text1 = "NO DAUGHTERS"
    text2 = "DETECTED"
    text3 = "Push to refresh"
    draw.text((center_text(text1), 0), text1, font=font, fill=255)
    draw.text((center_text(text2), 10), text2, font=font, fill=255)
    draw.text((center_text(text3), 20), text3, font=font, fill=255)