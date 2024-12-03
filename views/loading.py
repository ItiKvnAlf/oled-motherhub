from utils.screen import blank_screen, display_screen
from utils.center_text import center_text
from display.config import draw, font

# LOADING VIEWS
def initial_screen_view():
    """Display the initial screen."""
    # Draw initial screen logo
    logo_pixels = [
        (28,2), (29,2),
        (29,3), (30,3), (31,3), (32,3), (33,3), (97,3), (98,3), (99,3), (100,3),
        (31,4), (32,4), (34,4), (34,4), (92,4), (93,4), (94,4), (95,4), (96,4), (97,4), (98,4), (99,4),
        (33,5), (34,5), (35,5), (36,5), (40,5), (41,5), (42,5), (43,5), (44,5), (45,5), (46,5), (47,5), (48,5), (49,5), (87,5), (88,5), (89,5), (90,5), (91,5), (92,5), (93,5), (94,5), (95,5), (96,5), (97,5), (98,5),
        (34,6), (35,6), (36,6), (37,6), (38,6), (39,6), (40,6), (41,6), (42,6), (43,6), (44,6), (45,6), (46,6), (47,6), (48,6), (49,6), (50,6), (51,6), (52,6), (53,6), (85,6), (86,6), (87,6), (88,6), (89,6), (90,6), (91,6), (92,6), (93,6), (94,6), (95,6), (96,6), (97,6),
        (35,7), (36,7), (37,7), (38,7), (39,7), (40,7), (41,7), (42,7), (43,7), (44,7), (45,7), (46,7), (47,7), (48,7), (49,7), (50,7), (51,7), (52,7), (53,7), (54,7), (55,7), (83,7), (84,7), (85,7), (86,7), (87,7), (88,7), (89,7), (90,7), (91,7), (92,7), (93,7), (94,7), (95,7), 
        (34,8), (35,8), (36,8), (37,8), (38,8), (39,8), (40,8), (41,8), (42,8), (43,8), (44,8), (45,8), (46,8), (47,8), (48,8), (49,8), (50,8), (51,8), (52,8), (53,8), (54,8), (55,8), (56,8), (57,8), (58,8), (81,8), (82,8), (83,8), (84,8), (85,8), (86,8), (87,8), (88,8), (89,8), (90,8), (91,8), (92,8), (93,8),
        (33,9), (34,9), (35,9), (36,9), (37,9), (38,9), (39,9), (40,9), (41,9), (42,9), (43,9), (44,9), (45,9), (46,9), (47,9), (48,9), (49,9), (50,9), (51,9), (52,9), (53,9), (54,9), (55,9), (56,9), (57,9), (58,9), (59,9), (60,9), (61,9), (62,9), (78,9), (79,9), (80,9), (81,9), (82,9), (83,9), (84,9), (85,9), (86,9), (87,9), (88,9), (89,9), (90,9), (91,9),
        (33,10), (34,10), (35,10), (36,10), (37,10), (38,10), (39,10), (40,10), (41,10), (42,10), (43,10), (44,10), (45,10), (46,10), (47,10), (48,10), (49,10), (50,10), (51,10), (52,10), (53,10), (54,10), (55,10), (56,10), (57,10), (58,10), (59,10), (60,10), (61,10), (62,10), (63,10), (64,10), (65,10), (66,10), (67,10), (68,10), (69,10), (70,10), (71,10), (72,10), (73,10), (74,10), (75,10), (76,10), (77,10), (78,10), (79,10), (80,10), (81,10), (82,10), (83,10), (84,10), (85,10), (86,10), (87,10), (88,10), (89,10),
        (33,11), (34,11), (35,11), (36,11), (37,11), (38,11), (39,11), (40,11), (41,11), (42,11), (43,11), (44,11), (45,11), (46,11), (47,11), (48,11), (49,11), (50,11), (51,11), (52,11), (53,11), (54,11), (55,11), (56,11), (57,11), (58,11), (59,11), (60,11), (61,11), (62,11), (63,11), (64,11), (65,11), (66,11), (67,11), (68,11), (69,11), (70,11), (71,11), (72,11), (73,11), (74,11), (75,11), (76,11), (77,11), (78,11), (79,11), (80,11), (81,11), (82,11), (83,11), (84,11), (85,11), (86,11), (87,11),
        (34,12), (35,12), (36,12), (37,12), (38,12), (39,12), (40,12), (41,12), (42,12), (43,12), (44,12), (45,12), (46,12), (47,12), (48,12), (49,12), (50,12), (51,12), (52,12), (53,12), (54,12), (55,12), (56,12), (57,12), (58,12), (59,12), (60,12), (61,12), (62,12), (63,12), (64,12), (65,12), (66,12), (67,12), (68,12), (69,12), (70,12), (71,12), (72,12), (73,12), (74,12), (75,12), (76,12), (77,12), (78,12), (79,12), (80,12), (81,12), (82,12), (83,12), (84,12), (85,12),
        (35,13), (36,13), (37,13), (38,13), (39,13), (40,13), (41,13), (42,13), (43,13), (44,13), (45,13), (46,13), (47,13), (48,13), (49,13), (50,13), (51,13), (52,13), (53,13), (54,13), (55,13), (56,13), (57,13), (58,13), (59,13), (60,13), (61,13), (62,13), (63,13), (64,13), (65,13), (66,13), (67,13), (68,13), (69,13), (70,13), (71,13), (72,13), (73,13), (74,13), (75,13), (76,13), (77,13), (78,13), (79,13), (80,13), (81,13), (82,13), (83,13),
        (36,14), (37,14), (38,14), (39,14), (40,14), (41,14), (42,14), (43,14), (44,14), (45,14), (46,14), (47,14), (48,14), (49,14), (50,14), (51,14), (52,14), (53,14), (54,14), (55,14), (56,14), (57,14), (58,14), (59,14), (60,14), (61,14), (62,14), (63,14), (64,14), (65,14), (66,14), (67,14), (68,14), (69,14), (70,14), (71,14), (72,14), (73,14), (74,14), (75,14), (76,14), (77,14), (78,14), (79,14), (80,14), (81,14),
        (38,15), (39,15), (40,15), (41,15), (42,15), (43,15), (44,15), (45,15), (46,15), (47,15), (48,15), (49,15), (50,15), (51,15), (52,15), (53,15), (54,15), (55,15), (56,15), (57,15), (58,15), (59,15), (60,15), (61,15), (62,15), (63,15), (64,15), (65,15), (66,15), (67,15), (68,15), (69,15), (70,15), (71,15), (72,15), (73,15), (74,15), (75,15), (76,15), (77,15), (78,15), (79,15),
        (40,16), (41,16), (42,16), (43,16), (44,16), (45,16), (46,16), (47,16), (48,16), (49,16), (50,16), (51,16), (52,16), (53,16), (54,16), (55,16), (56,16), (57,16), (58,16), (59,16), (60,16), (61,16), (62,16), (63,16), (64,16), (65,16), (66,16), (67,16), (68,16), (69,16), (70,16), (71,16), (72,16), (73,16), (74,16), (75,16), (76,16),
        (42,17), (43,17), (44,17), (45,17), (46,17), (47,17), (48,17), (49,17), (50,17), (51,17), (52,17), (53,17), (54,17), (55,17), (56,17), (57,17), (58,17), (59,17), (60,17), (61,17), (62,17), (63,17), (64,17), (65,17), (66,17), (67,17), (68,17), (69,17), (70,17), (71,17), (72,17), (73,17), (74,17),
    ]

    blank_screen()

    # Draw the logo pixel by pixel
    for pixel in logo_pixels:
        draw.point(pixel, fill=255)

    text = "CHILIPEPPERLABS"
    draw.text((center_text(text), 20), text, font=font, fill=255)
    display_screen()

def scanning_daughters_view():
    """Display the scanning daughters view."""
    text1 = "SCANNING FOR"
    text2 = "DAUGHTERS..."
    blank_screen()
    draw.text((center_text(text1), 5), text1, font=font, fill=255)
    draw.text((center_text(text2), 15), text2, font=font, fill=255)
    display_screen()