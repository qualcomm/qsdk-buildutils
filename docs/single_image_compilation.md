## To Compile and Generate a Single Image

Download the build_qsdk.py script from CLO into the linux build machine.


The following command can be used to download the file:
```bash

wget https://git.codelinaro.org/clo/qsdk/oss/system/tools/meta/-/raw/win.platform_tools.1.0.r29/scripts/build_qsdk.py`

```
This script supports the following activities:
-	Repo sync from CLO based on the AU tag. 
-	Pull the binaries from Qartifactory.
-	Compile and Build the NHSS image.
-	Prepare for single image by installing the required binaries 
-	Create a single image which can be used for flashing. 

The following command does all the above activities:
```bash

`python build_qsdk.py -w <workspace_name> -t <target_name> -a <architecture bit 32|64> -g {<AU tag> <Qartificatory version> -b -p`

```


Sample command:
```bash


`python build_qsdk.py -w qsdk_image_wk -t ipq54xx -a 32 -g AU_LINUX_QSDK_NHSS.QSDK.13.0.5_TARGET_ALL.13.05.638.431.628 r13.0_00005.0 -b -p`


```

The single image would be created in <workspace_name>/qsdk/ipq/bin. 
