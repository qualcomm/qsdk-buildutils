# qsdk-buildutils

This project contains helper scripts that is used for build and single image creation of qsdk for DragonWing Wireless LAN Access Point software 

## Branches

**main**: Primary development branch. Contributors should develop submissions based on this branch, and submit pull requests to this branch.

## Requirements

The build environment is linux based.
*	Install the following packages with the following command:
    	apt-get install -y python3 python3-pip python3-venv python3-yam
*	Install pip for python
	    RUN pip install --no-cache-dir requests formatter2
*	Download the setup_qsdk.sh script from CLO into the linux build machine. The following command can be used to download the file:
        wget https://git.codelinaro.org/clo/qsdk/oss/system/openwrt/ipq-scripts/-/raw/win.platform_tools.1.0.r26/setup_qsdk.sh
*	Run this script to install the rest of the required packages.


## Installation Instructions

Download the python scripts from this repo to your build machine.

## Usage

Invoke the build_qsdk.py script.

This script supports the following activities:
•	Repo sync from CLO based on the AU tag. 
•	Pull the binaries from Qartifactory.
•	Compile and Build the NHSS image.
•	Prepare for single image by installing the required binaries 
•	Create a single image which can be used for flashing. 

The following command does all the above activities:

python build_qsdk.py -w <workspace_name> -t <target_name> -a <architecture bit 32|64> -g {<AU tag> <Qartificatory version> -b -p


## Development

To develop new features/fixes for the software, refer to the [CONTRIBUTING.md file](CONTRIBUTING.md).

## Getting in Contact

How to contact maintainers. E.g. GitHub Issues, GitHub Discussions could be indicated for many cases. However a mail list or list of Maintainer e-mails could be shared for other types of discussions. E.g.

* [Report an Issue on GitHub](../../issues)
* [Open a Discussion on GitHub](../../discussions)
* [E-mail us](mailto:shivapri@qti.qualcomm.com) for general questions

## License

*meta_qsdk* is licensed under the [BSD-3-Clause Clear License](https://spdx.org/licenses/BSD-3-Clause-Clear.html). See [LICENSE.txt](LICENSE.txt) for the full license text.
