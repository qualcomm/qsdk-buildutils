# ===========================================================================
# Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
# SPDX-License-Identifier: ISC
# ===========================================================================


import os
import sys
import subprocess
import argparse
import json
import re

def main():
	if len(sys.argv) != 4:
		print("Usage: python prepare_binaries.py <target_soc> <version_string>")
		sys.exit(1)

	target_soc = sys.argv[1]
	version_string = sys.argv[2]
	soc_folder_name = sys.argv[3]

	# Extract base version from QART tag (e.g., r13.1.r1_00001.0 → 13.1)
	match = re.match(r"r(\d+\.\d+)", version_string)
	if not match:
		print(f"Invalid version string format: {version_string}")
		sys.exit(1)

	version_key = match.group(1)

	with open("download_links.json", "r") as f:
		data = json.load(f)

	if version_key not in data:
		print(f"Unsupported version: {version_key}")
		sys.exit(1)

	version_data = data[version_key]
	base_url = version_data["base_url"]
	download_links = version_data["links"]

	if target_soc not in download_links:
		print(f"Unsupported SoC: {target_soc}")
		sys.exit(1)

	script_dir = os.path.dirname(os.path.abspath(__file__))
	base_path = os.path.abspath(os.path.join(script_dir, "..", "qsdkwkspace"))
	full_base_path = os.path.join(base_path, soc_folder_name)
	target_dir = os.path.join(full_base_path, "qsdk", "ipq")
	os.makedirs(target_dir, exist_ok=True)
	os.chdir(target_dir)

	print(f"Downloading binaries for {target_soc} into {target_dir}...\n")

	for url_template in download_links[target_soc]:
		url = base_url + url_template.format(version=version_string)
		filename = url.split("/")[-1]
		try:
			subprocess.run(["wget", url], check=True)
			if os.path.exists(filename):
				with open(filename, 'rb') as f:
					if b"<html" in f.read(1024).lower():
						print(f"Warning: {filename} appears to be an HTML page. Check authentication or URL.")
		except subprocess.CalledProcessError:
			print(f"Failed to download: {url}")

	print("\nDownload complete.")

if __name__ == "__main__":
	main()
