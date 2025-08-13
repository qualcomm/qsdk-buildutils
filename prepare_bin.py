# ===========================================================================
# Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
# SPDX-License-Identifier: ISC
# ===========================================================================


import os
import sys
import subprocess
import argparse
import json

def main():
	if len(sys.argv) != 3:
		print("Usage: python prepare_binaries.py <target_soc> <version_string>")
		sys.exit(1)

	target_soc = sys.argv[1]
	version_string = sys.argv[2]

	with open("download_links.json", "r") as f:
		data = json.load(f)

	base_url = data["base_url"]
	download_links = data["links"]

	if target_soc not in download_links:
		print(f"Unsupported SoC: {target_soc}")
		sys.exit(1)

	target_dir = os.path.abspath(os.path.join(os.getcwd(), "..", "..", "qsdk", "ipq"))
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
