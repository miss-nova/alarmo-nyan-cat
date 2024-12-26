# Alarmo Nyan Cat Animation Payload
This is a simple payload, which can be booted over USB (or other methods of your choosing), displaying an animation of nyan cat.

## Usage
- Download the latest release or build from source.
- Hold down the confirm, back and notification button on the Alarmo at the same time.
- While holding all three buttons down, plug in the USB cable to your PC.  
  The dial button on top of the Alarmo should light up red and a drive should appear on the PC.
- Copy the `a.bin` to the newly appeared drive.
- Copy the `MarkFile` to the drive.

The Alarmo should disconnect from the PC and a picture of a cat is displayed on the screen.  
You can turn the dial to fade through different colors, press the back button to display a QR code with [AES key data](../key_bruteforcer/README.md), or press down on the dial to make the cat return. Hold down the dial to keep running the animation, if you're building from source or are using the standard release.

## Building
- Clone https://github.com/GaryOderNichts/alarmo with all submodules.
- Enter the AES key and IV in the `key.py` file (as a hex string between the quotes).
- Delete the `data` folder or delete the `cat.png` inside of it. Either way works.
- Download this repo's files and extract it to inside the `usb_payload` folder, wherever you cloned the `alarmo` folder.
- Make sure you overwrite files in the `usb_payload` directory when extracting.
- Run `make`.

## Modifying
### If desired, you can replace the Nyan Cat frames with whatever custom frames you want!
- Unfortunately, there are limitations to this, so take note of three things:
  - First of all, the max number of frames you can add are up to 11 frames. This is in order to be able to fit the payload when compiled to fit the Alarmo's USB debug storage.
  - Second, you can ONLY have 11 frames, unless you modify the source files to reduce the amount.
  - Third, you must be sure to use images that are small in file size, so again, it can fit into the Alarmo's USB debug storage when compiled and used.
- That aside though, start by deleting all the nyan cat frames from the `data` folder.
- For each custom frame you wish to add and to set the order of the frames, you must name the first frame `cat20.png`.
- Every time you add a new frame, you must add the previous frame's number + 1.
- All the files should be named `cat20.png` - `cat30.png` in that order.
- Continue with the building instructions above this section.

## Credits
- This repo is based off of the USB payload by GaryOderNichts: https://github.com/GaryOderNichts/alarmo.
- https://github.com/nayuki/QR-Code-generator for QR Code generation.
