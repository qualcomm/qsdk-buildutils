## To Compile and Generate a Single Image

This step is useful to build the Qualcomm deliverable as it is and generate a single image for flashing.

Download the build_qsdk.py script from Code Linaro into the linux build machine.

The following command can be used to download the file:
```bash

wget https://git.codelinaro.org/clo/qsdk/oss/system/tools/meta/-/raw/win.platform_tools.1.0.r29/scripts/build_qsdk.py`

```
This script performs the following steps:
-	Repo sync from code linaro based on the relase tag. 
-	Compile and Build the NHSS (Linux/Filesystem) image.
-	Download the Pre-built binaries from Qualcomm artifcatory site (Qartificatory).
-	Assemble individual images for creating the single image. 
-	Create a single image using the individual images. This single imagew can be used for flashing. 

The following command performs all the above steps:
```bash
`python build_qsdk.py -w <workspace_name> -t <target_name> -a <architecture bit 32|64> -g {<tag> <Qartificatory version> -b -p`
```
TODO : explain what is worksapce name, target name etc

Example command:
```bash
`python build_qsdk.py -w qsdk_image_wk -t ipq54xx -a 32 -g AU_LINUX_QSDK_NHSS.QSDK.13.0.5_TARGET_ALL.13.05.638.431.628 r13.0_00005.0 -b -p`
```
The above command will build for IPQ54xx ARM32 target.

The single image would be created in <workspace_name>/qsdk/ipq/bin. 
