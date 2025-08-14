# ===========================================================================
# Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
# SPDX-License-Identifier: BSD-3-Clause
# ===========================================================================

import os
import shutil
import sys

# Define file lists for each SoC and variant
file_lists = {
	"ipq54xx": {
		"32": [
			"openwrt-ipq54xx-ipq54xx_32-qcom_maxx-fit-uImage.itb",
			"openwrt-ipq54xx-ipq54xx_32-squashfs-root.img",
			"openwrt-ipq5424-ipq54xx_32-mmc32-u-boot.elf",
			"openwrt-ipq5424-ipq54xx_32-nand32-u-boot.elf",
			"openwrt-ipq5424-ipq54xx_32-norplusmmc32-u-boot.elf",
			"openwrt-ipq5424-ipq54xx_32-norplusnand32-u-boot.elf"
		],
		"64": [
			"openwrt-ipq54xx-generic-qcom_maxx-fit-uImage.itb",
			"openwrt-ipq54xx-generic-squashfs-root.img",
			"openwrt-ipq5424-generic-mmc-u-boot.elf",
			"openwrt-ipq5424-generic-nand-u-boot.elf",
			"openwrt-ipq5424-generic-norplusmmc-u-boot.elf",
			"openwrt-ipq5424-generic-norplusnand-u-boot.elf"
		]
	},
	"ipq95xx": {
		"32": [
			"openwrt-ipq95xx-ipq95xx_32-qcom_alxx-fit-uImage.itb",
			"openwrt-ipq95xx-ipq95xx_32-squashfs-root.img",
			"openwrt-ipq9574-ipq95xx_32-mmc32-u-boot.elf",
			"openwrt-ipq9574-ipq95xx_32-nand32-u-boot.elf",
			"openwrt-ipq9574-ipq95xx_32-norplusmmc32-u-boot.elf",
			"openwrt-ipq9574-ipq95xx_32-norplusnand32-u-boot.elf"
		],
		"64": [
			"openwrt-ipq95xx-generic-qcom_alxx-fit-uImage.itb",
			"openwrt-ipq95xx-generic-squashfs-root.img",
			"openwrt-ipq9574-generic-mmc-u-boot.elf",
			"openwrt-ipq9574-generic-nand-u-boot.elf",
			"openwrt-ipq9574-generic-norplusmmc-u-boot.elf",
			"openwrt-ipq9574-generic-norplusnand-u-boot.elf"
		]
	},
	"ipq53xx": {
		"32": [
			"openwrt-ipq53xx-ipq53xx_32-qcom_mixx-fit-uImage.itb",
			"openwrt-ipq53xx-ipq53xx_32-squashfs-root.img",
			"openwrt-ipq5332-ipq53xx_32-mmc32-u-boot.elf",
			"openwrt-ipq5332-ipq53xx_32-nand32-u-boot.elf",
			"openwrt-ipq5332-ipq53xx_32-norplusmmc32-u-boot.elf",
			"openwrt-ipq5332-ipq53xx_32-norplusnand32-u-boot.elf"
		],
		"64": [
			"openwrt-ipq53xx-generic-qcom_mixx-fit-uImage.itb",
			"openwrt-ipq53xx-generic-squashfs-root.img",
			"openwrt-ipq5332-generic-mmc-u-boot.elf",
			"openwrt-ipq5332-generic-nand-u-boot.elf",
			"openwrt-ipq5332-generic-norplusmmc-u-boot.elf",
			"openwrt-ipq5332-generic-norplusnand-u-boot.elf"
		]
	}
}

def copy_files(base_path, soc, arch):
	source_dir = os.path.join(base_path, "qsdk", "bin", "targets", soc,
											"generic" if arch == "64" else f"{soc}_32")
	target_dir = os.path.join(base_path, "qsdk", "ipq")
	files = file_lists.get(soc, {}).get(arch, [])
	if not files:
		print(f"No files defined for SoC: {soc}, Architecture: {arch}")
		return
	os.makedirs(target_dir, exist_ok=True)
	for filename in files:
		src_path = os.path.join(source_dir, filename)
		if os.path.exists(src_path):
			shutil.copy(src_path, target_dir)
			print(f"Copied {filename} to qsdk/ipq/")
		else:
			print(f"File not found: {filename}")

def main():
	if len(sys.argv) != 3:
		print("Usage: python copy_binaries.py <target_soc> <architecture>")
		sys.exit(1)

	target_soc = sys.argv[1]
	architecture = sys.argv[2]

	script_dir = os.path.dirname(os.path.abspath(__file__))
	base_path = os.path.abspath(os.path.join(script_dir, "..", "qsdkwkspace"))
	soc_folder_name = next((d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))), None)


	if not soc_folder_name:
		print("Error: Could not determine SoC folder name.")
		sys.exit(1)

	full_base_path = os.path.join(base_path, soc_folder_name)

	qsdk_ipq_path = os.path.join(full_base_path, "qsdk", "ipq")
	os.makedirs(qsdk_ipq_path, exist_ok=True)

	try:
		tools_path = os.path.join(full_base_path, "qsdk", "staging_dir", "host", "bin")
		for tool in ["ubinize", "mkimage", "mksquashfs4"]:
			shutil.copy(os.path.join(tools_path, tool), qsdk_ipq_path)
		print("Copied ubinize, mkimage and mksquashfs4 to qsdk/ipq")
	except FileNotFoundError as e:
		print(f"Error copying tools: {e}")
		sys.exit(1)

	try:
		meta_tools_path = os.path.join(full_base_path, "meta-tools-oss"))
		shutil.copytree(os.path.join(meta_tools_path, "scripts"), os.path.join(qsdk_ipq_path, "scripts"), dirs_exist_ok=True)
		for script in ["pack.py", "pack_v3.py"]:
			shutil.copy(os.path.join(meta_tools_path, script), os.path.join(qsdk_ipq_path, "scripts"))
		shutil.copy(os.path.join(meta_tools_path, "prepareSingleImage.py"), qsdk_ipq_path)
		print("Copied scripts and tools from meta-tools-oss to qsdk/ipq")

		soc_folder_map = {
			"ipq54xx": "ipq5424",
			"ipq53xx": "ipq5332",
			"ipq95xx": "ipq9574"
		}
		folder_name = soc_folder_map.get(target_soc)
		if folder_name:
			shutil.copytree(os.path.join(meta_tools_path, folder_name),
							os.path.join(qsdk_ipq_path, folder_name), dirs_exist_ok=True)
			print(f"Copied {folder_name} folder from meta-tools-oss to qsdk/ipq")
	except FileNotFoundError:
		print("Error copying meta tools: {e}")
		sys.exit(1)

	copy_files(full_base_path, target_soc, architecture)

if __name__ == "__main__":
	main()
