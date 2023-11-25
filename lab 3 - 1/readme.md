# LAB 3-1: File Management in HDFS and S3

## Course Details

| Information |  |
| --- | --- |
| Course name | Tópicos especiales en Telemática |
| Course ID | ST0263 |
| Name | Juan David Echeverri Villada (jdecheverv@eafit.edu.co) |
| Teacher | Edwin Nelson Montoya Munera (emontoya@eafit.edu.co) |


## Steps followed:
Manage available files from datasets in HDFS (temporary storage) and S3 (permanent storage) services.

### Create s3 bucket

1. Go to S3 service and create a new bucket
2. Assign a name
3. Go to Object Ownership >> ACLs enabled and check the box 'Object writer'
4. go to 'Block Public Access settings for this bucket section', remove the default check and select the warning checkbox as acknowledged’
5. Create bucket
<img width="1657" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/e9c7c805-3524-400b-ad03-56bf2d51a6fb">
6. Select the id of the created bucket and go to 'Select the Permissions'  >> 'Access control list (ACL)'. Then edit
7. Grant access to everyone for list and read
8. Go back to the list of buckets, select the id and upload the [example file](https://github.com/st0263eafit/st0263-232/blob/main/bigdata/datasets/airlines.csv)
9. Select the name of the previously uploaded file >> Properties and copy the 'Object URL'.
<img width="1321" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/efc3b6d1-480f-4997-b131-862c9beda972">
---
### File management in HDFS with terminal

1. Follow lab-0 to create a cluster at EMR services
2. Connect to the cluster through SSH
3. create a folder called 'gutenberg-small' inside the path '/user/hadoop/datasets':
```cmd
mkdir -p hdfs dfs /user/hadoop/datasets/gutenberg-small
```
4. Now you can use list an put operations over the dfs, as follow:
```cmd
hdfs dfs -ls /user/hadoop/datasets
```
```cmd
hdfs dfs -put <YOUR_LOCAL_FOLDER> /user/hadoop/datasets/gutenberg-small/
```
---
### File management in HDFS using HUE
1. Go to EMR services >> EMR on EC2 >> clusters >> your cluster id >> applications and open Hue
2. Select the files section, where you should find the previous folder created (datasets). Otherwise create it
<img width="1792" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/e92acd0d-a3c5-45fc-a317-13f2fe4ab22d">
3. Now you can upload and list the files in the dfs

---
### File management in S3 using HUE
1. Follow the previous steps to initialize Hue. Then, go to s3 section
<img width="1791" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/e12b48c1-bbfe-4146-8f29-ecfce3c9455c">
You should be able to see all your buckets
2. Now you can manage all your files in your bucket (upload - list)
<img width="1361" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/3dedfc29-0869-4ade-81b5-5b1d323dc6fb">


