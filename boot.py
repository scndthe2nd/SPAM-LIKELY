'''
# boot.py
import board
import digitalio
import storage
import usb_cdc
import usb_hid
import matrix

# This is only one example of a gamepad descriptor.
# It may not suit your needs, or be supported on your host computer.

GAMEPAD_REPORT_DESCRIPTOR = bytes((
    0x05, 0x01,  # Usage Page (Generic Desktop Ctrls)
    0x09, 0x05,  # Usage (Game Pad)
    0xA1, 0x01,  # Collection (Application)
    0x85, 0x04,  #   Report ID (4)
    0x05, 0x09,  #   Usage Page (Button)
    0x19, 0x01,  #   Usage Minimum (Button 1)
    0x29, 0x10,  #   Usage Maximum (Button 16)
    0x15, 0x00,  #   Logical Minimum (0)
    0x25, 0x01,  #   Logical Maximum (1)
    0x75, 0x01,  #   Report Size (1)
    0x95, 0x10,  #   Report Count (16)
    0x81, 0x02,  #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    0x05, 0x01,  #   Usage Page (Generic Desktop Ctrls)
    0x15, 0x81,  #   Logical Minimum (-127)
    0x25, 0x7F,  #   Logical Maximum (127)
    0x09, 0x30,  #   Usage (X)
    0x09, 0x31,  #   Usage (Y)
    0x09, 0x32,  #   Usage (Z)
    0x09, 0x35,  #   Usage (Rz)
    0x75, 0x08,  #   Report Size (8)
    0x95, 0x04,  #   Report Count (4)
    0x81, 0x02,  #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    0xC0,        # End Collection
))

bitmap_keyboard = usb_hid.Device(
    report_descriptor = (
        b'\x05\x01\t\x06\xa1\x01\x85\x04u\x01\x95\x08\x05\x07\x19\xe0)\xe7\x15'
        b'\x00%\x01\x81\x02\x95\x05u\x01\x05\x08\x19\x01)\x05\x91\x02\x95\x01u'
        b'\x03\x91\x03\x95xu\x01\x15\x00%\x01\x05\x07\x19\x00)w\x81\x02\xc0'
    ),
    usage_page = 0x1,
    usage = 0x6,
    in_report_lengths = (8,),
    out_report_lengths = (1,),
    report_ids=(4,),
)

gamepad = usb_hid.Device(
    report_descriptor=GAMEPAD_REPORT_DESCRIPTOR,
    usage_page=0x01,           # Generic Desktop Control
    usage=0x05,                # Gamepad
    report_ids=(4,),           # Descriptor uses report ID 4.
    in_report_lengths=(6,),    # This gamepad sends 6 bytes in its report.
    out_report_lengths=(0,),   # It does not receive any reports.
)

usb_hid.enable((usb_hid.Device.KEYBOARD), boot_device=1)
'''
import supervisor

supervisor.set_next_stack_limit(4096 + 4096)
