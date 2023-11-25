# LAB 3-0: EMR Cluster

## Course Details

| Information |  |
| --- | --- |
| Course name | Tópicos especiales en Telemática |
| Course ID | ST0263 |
| Name | Juan David Echeverri Villada (jdecheverv@eafit.edu.co) |
| Teacher | Edwin Nelson Montoya Munera (emontoya@eafit.edu.co) |


## Steps followed:
The following guide will provide the steps to follow for a correct creation of the AWS EMR Cluster.

### Create s3 bucket

In AWS, go to s3, set up and create a new bucket (all default configs)
<img width="902" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/10f31225-5261-41fc-b854-72e5339d455c">

---
### EMR cluster creation
1. Go to EMR service, and select create new cluster. Version should be 6.14.0, and the application bundle should be custom, with the following options
<img width="794" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/1544420b-1f3c-4754-bc64-3ed9eae2ac48">

2. Configurate cluster termination configuration to finish cluster after 3 hours idle time
<img width="772" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/db621a87-912c-4810-b89a-f8a76d3dae0f">

3. Go to software settings >> enter configuration. And paste the following config:
```json
   [
    {
      "Classification": "jupyter-s3-conf",
      "Properties": {
        "s3.persistence.enabled": "true",
        "s3.persistence.bucket": "<YOUR_BUCKET_NAME>"
      }
    }
  ]
```
4. Go to  Security configuration and EC2 key pair and set the vockey used for other labs (or a custom one)
<img width="784" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/69e5a3db-8168-4a32-8682-016e03e29391">

5. In the section 'Identity and Access Management (IAM) roles select the next options:

- Amazon EMR Service Role: EMR_DefaultRole
- EC2 Instance Profile for Amazon EMR: EMR_EC2_DefaultRole
- Custom Auto Scaling Role: LabRole (or custom)

6. Create cluster
---
### Modify security groups
1. Go to EMR service >> EMR on EC2 >> block public access.
2. Edit >> turn off >> save
3. Then, go to Amazon EMR menu >> EMR on EC2 >> Clusters and select the Cluster ID that has the status 'Waiting'. Then Applications option.
4. Open TCP ports for the application bundle as follows, in addition open TCP ports 22, 14000 and 9878.
<img width="976" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/11144a04-0eee-4c22-8031-957b911957e3">
5. Go to EC2 service >> security grpups and select the following security group
<img width="1511" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/aec3fc64-664c-4809-8324-77117a56b542">
6. Select edit inbound rules and then for each port from the step 4 do: add rule >> Custom tcp and add port number. When you're done, click save

---
### Access primary node
1. Go to EMR service >> EMR on EC2 >> cluster and then click on the id of the created cluster
2. Click on Connect to the Primary node using SSM and follow procedure
3. Edit 'hue.init' file
```cmd
sudo nano /etc/hue/conf/hue.ini
```
4. Find the line containing 'webhdfs_url' and change the port. You should put the HDFS Name Node port found in the Applications section over your cluster (selected port in this case is 9870).
<img width="775" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/45e67ef6-4b7d-4dfe-b9d3-89c6ee1e3b38">

6. Save content and restart using
```cmd
sudo systemctl restart hue.service
```
---
### Use Hue
1. Go to EMR service >> EMR on EC2 >> and select the cluster Id, then applications
2. Select the url of 'hue', and then enter using 'hadoop' as user and any password 
<img width="1781" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/dccc0d7d-0dc1-4608-bc6a-be2177e96743">

### Use JupyterHub
1. Follow the same procedure for hue, but use user 'jovyan' and password 'jupyter'.
2. Now you can create your own jupyter server
<img width="1104" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/89b9007b-996a-4985-8b70-83dcbd8abd93">
