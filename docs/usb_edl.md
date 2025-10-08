# Bring up Device using USB EDL

In the case where the device is blank or does not boot up to the uBOOT, it can be brought up to the uBOOT using the USB emergency download (EDL) mode. 
After this, Single image can be flashed using the steps in section 3.1 Flash a single image.

## Required Tools

Install the necessary tools and drivers from the Qualcomm website. This is a one-time setup.

1. Install the Qualcomm Package Manager 3 (QPM3):\
   <https://qpm.qualcomm.com/#/main/tools/details/QPM3>

2. Install the Qualcomm USB Driver (QUD):\
   <https://qpm.qualcomm.com/#/main/tools/details/QUD>

## EDL Recovery Setup and Bringup

1. Connect the USB Type-A cable between the USB 3.0 port on the device and the host machine.

   - NOTE: Ensure that the Vcc pin (Pin 1) is cut off in the USB A-to-A cable.

2. Note the COM port number on the Host machine.

- NOTE:	Port number is the COM port number detected on the Host computer. For more information, see the Device Manager application on Windows PC.

3.	Perform power cycle, and run the EDL Recovery script by providing the IPQ folder path, which contains the required binaries, target, port number, device type, and flash type.

The EDL recovery script is available either at synced repo path : meta-tools-oss/scripts/EDL_recovery.py
Or it can get downloaded from the below path:
https://git.codelinaro.org/clo/qsdk/oss/system/tools/meta/-/raw/win.platform_tools.1.0.r29/scripts/EDL_recovery.py

```bash 
Syntax:  python EDL_recovery.py -b <folderpath> -t <target_name> -d <boardtype> -f <flash type> -p <port_number>
```

Example
```bash
python EDL_recovery.py -b C:\qsdk_image_wk\ipq -t IPQ5424 -d RDP487 -f NAND -p 17 
```

