## Build Machine Requirements
TODO

## Build Environment setup

For building either the single image or the QSDK image, a Linux environment is required.

- Install the following packages:
  ```bash
  apt-get install -y python3 python3-pip python3-venv python3-yam
  ```

- Install pip for python:
  ```bash
  RUN pip install --no-cache-dir requests formatter2
  ```

- Download the setup_qsdk.sh script from CLO into the Linux build machine:
  ```bash
  wget https://git.codelinaro.org/clo/qsdk/oss/system/openwrt/ipq-scripts/-/raw/win.platform_tools.1.0/setup_qsdk.sh
  ```

- Run this script to install the rest of the required packages.

- Install Repo and set the environment path to identify the `repo` command:
  ```bash
  git clone https://git.codelinaro.org/clo/tools/repo.git -b aosp/stable /root/bin/repo
  ENV PATH="/root/bin/repo-src:${PATH}"
  ```
