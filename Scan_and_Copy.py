import os
import shutil
import time
import pyudev

# Define the directory to copy files to
destination_folder = "files"

def copy_files_from_usb(usb_device):
    # Get the mount point of the USB device
    mount_point = usb_device.get('DEVNAME')

    # Check if the mount point exists and is a directory
    if os.path.isdir(mount_point):
        print(f"USB device mounted at: {mount_point}")

        # List all files in the USB device
        files = os.listdir(mount_point)

        # Copy files to the destination folder
        for file_name in files:
            source_path = os.path.join(mount_point, file_name)
            destination_path = os.path.join(destination_folder, file_name)
            shutil.copy(source_path, destination_path)
            print(f"Copied {file_name} to {destination_path}")

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Create a context for monitoring devices
context = pyudev.Context()

# Create a monitor for USB devices
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='block', device_type='disk')

print("USB device monitor started...")

# Monitor USB devices
for action, device in monitor:
    if action == 'add':
        print("USB device inserted...")
        copy_files_from_usb(device)
    elif action == 'remove':
        print("USB device removed...")
