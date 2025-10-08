# Steps To Flash Individual Images

## Prerequisite

- Ensure that the device boots up to a valid U-Boot prompt.

## 3.2.1 Procedure

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

4. Print the list of partitions using the following command:
   - In case of NAND or NORplusNAND flash type:
     ```bash
     smem
     ```
   - In case of eMMC or NORplus eMMC flash type:
     ```bash
     mmc part
     ```

5. Flash the image based on the partition name from the listing:
   ```bash
   tftpb <Image Name> && flash <Partition Name>
   ```

Example


This example uses the ipq9574 norplusnand device and shows the kernel and rootfs image flashing separately.

```bash
IPQ9574# smem
ubi0: attaching mtd2
ubi0: scanning is finished
ubi0: attached mtd2 (name "fs", size 60 MiB)
ubi0: PEB size: 131072 bytes (128 KiB), LEB size: 126976 bytes ubi0: min./max. I/O unit sizes: 2048/2048, sub-page size 2048

ubi0: VID header offset: 2048 (aligned 2048), data offset: 4096 ubi0: good PEBs: 480, bad PEBs: 0, corrupted PEBs: 0
ubi0: user volume: 4, internal volumes: 1, max. volumes count: 128 ubi0: max/mean erase counter: 8/2, WL threshold: 4096, image sequence number: 1953157655
ubi0: available PEBs: 0, total reserved PEBs: 480, PEBs reserved for bad PEB handling: 40
flash_type:	0x6
flash_index:	0x0
flash_chip_select:	0x0
flash_block_size:	0x10000
flash_density:	0x1000000 partition table offset 0x0
No.: Name	Attributes	Start		Size 0: 0:SBL1	0x0000ffff		0x0	0xc0000
1: 0:MIBIB	0x001040ff	0xc0000	0x10000
2: 0:BOOTCONFIG	0x001040ff	0xd0000	0x20000
3: 0:BOOTCONFIG1	0x001040ff	0xf0000	0x20000
4: 0:QSEE	0x0000ffff	0x110000	0x180000
5: 0:QSEE_1	0x0000ffff	0x290000	0x180000
6: 0:DEVCFG	0x0000ffff	0x410000	0x10000
7: 0:DEVCFG_1	0x0000ffff	0x420000	0x10000
8: 0:APDP	0x0000ffff	0x430000	0x10000
9: 0:APDP_1	0x0000ffff	0x440000	0x10000
10: 0:TME	0x0000ffff	0x450000	0x40000
11: 0:TME_1	0x0000ffff	0x490000	0x40000
12: 0:RPM	0x0000ffff	0x4d0000	0x20000
13: 0:RPM_1	0x0000ffff	0x4f0000	0x20000
14: 0:CDT	0x0000ffff	0x510000	0x10000
15: 0:CDT_1	0x0000ffff	0x520000	0x10000
16: 0:APPSBLENV	0x0000ffff	0x530000	0x10000
17: 0:APPSBL	0x0000ffff	0x540000	0xa0000
18: 0:APPSBL_1	0x0000ffff	0x5e0000	0xa0000
19: 0:ART	0x0000ffff	0x680000	0x70000
20: 0:ETHPHYFW	0x0000ffff	0x6f0000	0x80000
21: 0:TRAINING	0x0100ffff	0x0	0x80000
22: rootfs	0x0100ffff	0x80000	0x3c00000
	ubi	vol	0	wifi_fw	
	ubi	vol	1	kernel	
	ubi	vol	2	ubi_rootfs	
ubi vol	3	rootfs_data
23:	rootfs_1	0x0100ffff	0x3c80000	 0x3c00000
24:	NVRAM	0x0100ffff	0x7880000	0x300000

IPQ9574#
IPQ9574# tftpb openwrt-ipq95xx-ipq95xx_32-qcom_alxx-fit-uImage.itb && flash kernel
IPQ9574#
IPQ9574# tftpb openwrt-ipq95xx-ipq95xx_32-squashfs-root.img && flash ubi_rootfs
```


With this command, the partition memory address is updated with the new image.
