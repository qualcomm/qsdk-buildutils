# Single Image Flash

## Prerequisite

- Ensure that the device boots up to a valid U-Boot prompt.
- Ensure that the device is connected to the server or host machine through Ethernet.
- Ensure that the server or host machine has a TFTP server running.

## Procedure

1. Open the U-Boot console on the host machine:
   - Start PuTTY.
   - Select the serial connection type.
   - Choose the COM port (COM x) by checking the Device Manager for the port number.
   - Set the baud rate to 115200.

2. From the U-Boot console prompt, set the device IP address and the server IP address:
   ```bash
   setenv ipaddr <device IP address>
   setenv serverip <server IP address>
   saveenv
   ```

3. Check the server status; if the server is alive, a response is printed:
   ```bash
   ping $serverip
   ```

4. Flash a single image and perform a hard reboot after the flashing completes:
   ```bash
   tftpb <Single Image Name> && imgaddr=$fileaddr && source $imgaddr:script
   ```

## Image Selection 

### Image selection for IPQ54xx

| Flash type                   | Single image (32 bits)                    | Single image (64 bits)                         |
|-----------------------------|-------------------------------------------|-----------------------------------------------|
| NAND                        | nand-ipq5424-single.img                   | nand-ipq5424_64-single.img                     |
| NAND (4K)                   | nand-4k-ipq5424-single.img                | nand-4k-ipq5424_64-single.img                  |
| eMMC                        | emmc-ipq5424-single.img                   | emmc-ipq5424_64-single.img                     |
| eMMC Vendor Layout          | emmc-ipq5424-single-vendor.img            | emmc-ipq5424_64-single-vendor.img              |
| NOR plus NAND [GPT]         | norplusnand-ipq5424-single.img            | norplusnand-ipq5424_64-single.img              |
| NOR plus NAND (4K) [GPT]    | norplusnand-4k-ipq5424-single.img         | norplusnand-4k-ipq5424_64-single.img           |
| NORplus eMMC [GPT]          | norplusemmc-ipq5424-single.img            | norplusemmc-ipq5424_64-single.img              |
| NOR plus NAND [MIBIB]       | norplusnand-mibib-ipq5424-single.img      | norplusnand-mibib-ipq5424_64-single.img        |
| NOR plus NAND (4K) [MIBIB]  | norplusnand-4k-mibib-ipq5424-single.img   | norplusnand-4k-mibib-ipq5424_64-single.img     |
| NORplus eMMC [MIBIB]        | norplusemmc-mibib-ipq5424-single.img      | norplusemmc-mibib-ipq5424_64-single.img        |

### Image selection for IPQ53xx

| Flash type           | Single image (32 bits)                 | Single image (64 bits)                 |
|----------------------|----------------------------------------|----------------------------------------|
| NAND                 | nand-ipq5332-single.img                | nand-ipq_64-single.img                 |
| NAND (4K)            | nand-4k-ipq5332-single.img             | nand-4k-ipq5332_64-5332single.img      |
| eMMC                 | emmc-ipq5332-single.img                | emmc-ipq5332_64-single.img             |
| NORplus NAND         | norplusnand-ipq5332-single.img         | norplusnand-ipq5332_64-single.img      |
| NORplus NAND (4K)    | norplusnand-4k-ipq5332-single.img      | norplusnand-4k-ipq5332_64-single.img   |
| NORplus eMMC         | norplusemmc-ipq5332-single.img         | norplusemmc-ipq5332_64-single.img      |
| NAND64M              | nand-ipq5332-single-64M.img            | -                                      |
| TinyNOR 16M          | tiny-nor-ipq5332-single.img            | -                                      |
| TinyNOR Debug 16M    | tiny-nor-debug-ipq5332-single.img      | -                                      |

### Image selection for IPQ95xx

| Flash type            | Single image (32 bits)               | Single image (64 bits)               |
|-----------------------|--------------------------------------|--------------------------------------|
| NAND                  | nand-ipq9574-single.img              | nand-ipq9574_64-single.img           |
| NAND (4K)             | nand-4k-ipq9574-single.img           | nand-4k-ipq9574_64-single.img        |
| eMMC                  | emmc-ipq9574-single.img              | emmc-ipq9574_64-single.img           |
| NORplus NAND          | norplusnand-ipq9574-single.img       | norplusnand-ipq9574_64-single.img    |
| NORplus NAND (4K)     | norplusnand-4k-ipq9574-single.img    | norplusnand-4k-ipq9574_64-single.img |
| NORplus eMMC          | norplusemmc-ipq9574-single.img       | norplusemmc-ipq9574_64-single.img    |

