# Lowering the File Size of Collected Media
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/0050a936217ec4b5b9cf44a66826778898ed29d5/source/lower_file_size.md" class="reference">31 Oct 2025</a>


When your form collects more than one image or you are collecting tens of
thousands of records, you could face difficulties generating the Media
Attachments ZIP if you do not adjust the image quality settings before starting
data collection.

Open Camera is a 3rd party open-source application that can help you do this.

## Instructions

[Install Open Camera](https://play.google.com/store/apps/details?id=net.sourceforge.opencamera&hl=en_US)
from the Android Play Store.

![image](/images/lower_file_size/open_cam.png)

## KoboCollect

In KoboCollect, when you take a photo, you will now be asked which app should be
used by default: Choose Open Camera and select 'Always' so you are not asked
again.

## Open Camera

In the Open Camera settings, go to Photo Settings, then:

1. Open Camera Resolution and choose the smallest acceptable resolution.
2. Open image quality and choose a percentage: 90% will look almost perfect,
   below 50% the image will become harder to recognize. Start with 70% and test
   some images at different quality levels to find the lowest acceptable size.

This website provides an overview of
[how to estimate](http://fotoforensics.com/tutorial-estq.php) the optimal JPEG
quality level.
