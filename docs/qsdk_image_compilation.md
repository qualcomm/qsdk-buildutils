## To Compile QSDK Image 

Using the script build_qsdk.py mentioned in [single_image_compilation](single_image_compilation), the QSDK (NHSS) image can be built

- To repo sync:

```bash

python build_qsdk.py -w <workspace_name> -t <target_name> -a <architecture bit 32|64> -g {<AU tag> <Qartificatory version>} 


```

Example
```bash

python build_qsdk.py -w qsdk_image_wk -t ipq54xx -a 32 -g AU_LINUX_QSDK_NHSS.QSDK.13.0.5_TARGET_ALL.13.05.638.431.628 r13.0_00005.0


```
Note: The repo is already synced if single image was built.

- To Build and compile:
```bash


python build_qsdk.py -w <workspace_name> -t <target_name> -a <architecture bit 32|64> -b


```
Example
```bash

python build_qsdk.py -w qsdk_image_wk -t ipq54xx -a 32 -b

```
The NHSS build files would be available in qsdk_image_wk/qsdk/ipq folder.

- To Install the NHSS built image 
```bash

python build_qsdk.py -w <workspace_name> -t <target_name> -a <architecture bit 32|64> -i

```

Example
```bash

python build_qsdk.py -w qsdk_image_wk -t ipq54xx -a 32 -i

```