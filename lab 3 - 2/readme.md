# LAB 3-2: Data Catalog with Glue and Athena

## Course Details

| Information |  |
| --- | --- |
| Course name | Tópicos especiales en Telemática |
| Course ID | ST0263 |
| Name | Juan David Echeverri Villada (jdecheverv@eafit.edu.co) |
| Teacher | Edwin Nelson Montoya Munera (emontoya@eafit.edu.co) |


## Steps followed:
Catalog data from the course dataset and send serverless queries

### Create bucket
1. Follow the lab 3-1 to create a s3 bucket
2. Upload the dataset of your choice
<img width="954" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/3f95e41a-aac6-42e0-9bb9-f98240a5a7e6">

---
### Catalog Data
1. Go to AWS >> Glue Service >> Data catalog >> Crawlers and create a new crawler
2. In Choose data sources and classifiers section, click on Add a data source
3. Search your bucket and find the folder you want to catalog.
<img width="1519" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/5684e3d5-1173-4949-8e2c-27fae1a1c912">
4. Select the IAM role created for the project
5. Target database should be default. set Frequency to 'on demand' to catalog the data manually.
6. Create the crawler
7. Start it by selecting the crawler and then run
8. When it is done, go to Data catalog >> Databases >> Table, Where the new tables with your data should be
<img width="1792" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/0eefbe49-f0a0-47ec-9957-bec82450fa4b">
---
### Query with Atena
1. Go to AWS >> Athena >> Query editor >> Settings >> click on Manage
2. Lets set a location to store the results.
<img width="1701" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/ac47feb0-bb59-4426-a613-0e4d1fbe597a">

3. Go back to Editor section. Select the table created with your crawler.
<img width="671" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/3f4a288d-e2c6-491e-b95f-c5d7da6be7e2">

4. Now you can query your data and it will be stored in the bucket defined before
<img width="1727" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/64bf4c0d-2c28-4f4a-b934-ea441ee1bea1">
example:

```sql
SELECT * FROM flights where distance < 26;
```


