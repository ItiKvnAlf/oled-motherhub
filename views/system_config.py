from display.icons import set_icon_center
import display.config as config
from utils.center_text import center_text
from display.config import draw, width, font

def system_config_view(options: list):
    """
    Display the system configuration view.

    Args:
        options (list): List of options to display.
    """
    num_options = len(options)

    # Check if selected_digit_index is within bounds
    if config.data['selected_digit_index'] < num_options:
        selected_option = options[config.data['selected_button']]
    else:
        selected_option = options[0]  # Default to the first option

    # Draw icons and selected option text
    if config.data['selected_digit_index'] == 0:
        set_icon_center('right')  # Draw right icon for active selection

        # Draw the selected option only
        option_text = selected_option

        # Draw selected option with a white background and black text
        width_option = (width // 2 - draw.textlength(option_text)) // 2
        draw.rectangle((width_option - 2, 10, width_option + draw.textlength(option_text), 20), fill=255)
        draw.text((width_option, 10), option_text, font=font, fill=0)

        # Draw "BACK" button
        text4 = "BACK"
        width4 = (width - draw.textlength(text4) - 10)
        draw.text((width4, 10), text4, font=font, fill=255)

        # Draw up and down icons for navigation
        set_icon_center('up')
        set_icon_center('down')

    else:
        # If the first button is not selected, draw all buttons with transparent background
        set_icon_center('left')

        # Transparent background for all options when none are selected
        option_text = selected_option

        # Draw selected option with a white background and black text
        width_option = (width // 2 - draw.textlength(option_text)) // 2
        draw.text((width_option, 10), option_text, font=font, fill=255)

        # "BACK" remains in the same position
        text4 = "BACK"
        width4 = (width - draw.textlength(text4) - 10)
        draw.rectangle((width4 - 2, 10, width4 + draw.textlength(text4), 20), fill=255)
        draw.text((width4, 10), text4, font=font, fill=0)

def confirm_system_reboot_view():
    """
    Display the confirm system reboot view.
    """
    text1 = "REBOOT this device?"
    draw.text((center_text(text1), 5), text1, font=font, fill=255)

def confirm_system_shutdown_view():
    """
    Display the confirm system shutdown view.
    """
    text1 = "Confirm SHUTDOWN?"
    draw.text((center_text(text1), 5), text1, font=font, fill=255)

def system_change_mode_view():
    """
    Display the confirm system change mode view.
    """
    text1 = "Change MODE to"
    text2 = "DAUGHTER BOX?"
    draw.text((center_text(text1), 0), text1, font=font, fill=255)
    draw.text((center_text(text2), 10), text2, font=font, fill=255)

def confirm_system_change_mode_view():
    """
    Display the confirm system change mode view.
    """
    text1 = "The system will"
    text2 = "REBOOT. Proceed?"
    draw.text((center_text(text1), 0), text1, font=font, fill=255)
    draw.text((center_text(text2), 10), text2, font=font, fill=255)