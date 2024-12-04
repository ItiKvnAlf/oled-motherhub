import display.config as config
from views.system_config import confirm_system_change_mode_view, confirm_system_reboot_view, confirm_system_shutdown_view, system_change_mode_view
from display.config import draw, font

def confirm_view():
    """Display the confirm view."""

    # Get confirm view based on the current state
    if config.data['current_state'] == "system_reboot":
        confirm_system_reboot_view()
    elif config.data['current_state'] == "system_shutdown":
        confirm_system_shutdown_view()
    elif config.data['current_state'] == "system_change_mode":
        system_change_mode_view()
    elif config.data['current_state'] == "confirm_change_mode":
        confirm_system_change_mode_view()

    # Buttons for confirmation

    # Check if "NO" button is selected
    if config.data['selected_confirm_button'] == 0:
        # Draw "NO" button as selected (white background, black text)
        draw.rectangle((39, 20, 55, 30), fill=255)
        draw.text((41, 20), "NO", font=font, fill=0)
    else:
        # Draw "NO" button as normal (black background, white text)
        draw.text((41, 20), "NO", font=font, fill=255)
    
    # Check if "YES" button is selected
    if config.data['selected_confirm_button'] == 1:
        # Draw "YES" button as selected (white background, black text)
        draw.rectangle((68, 20, 90, 30), fill=255)
        draw.text((70, 20), "YES", font=font, fill=0)
    else:
        # Draw "YES" button as normal (black background, white text)
        draw.text((70, 20), "YES", font=font, fill=255)