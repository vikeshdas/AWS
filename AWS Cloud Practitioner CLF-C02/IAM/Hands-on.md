## created a IAM user and attached polycies to ReadOnlyAcccess of s3.

#### Go to console  Then search for IAM service
<img src="images/3.png" width="80%" align="top-left" alt="" title="CNN" />

#### Go to "Access management"->"Users"
<img src="images/4.png" width="80%" align="top-left" alt="" title="CNN" />

#### Click on create user
<img src="images/5.png" width="80%" align="top-left" alt="" title="CNN" />

#### Fill user information and password etc.
<img src="images/6.png" width="80%" align="top-left" alt="" title="CNN" />
<img src="images/7.png" width="80%" align="top-left" alt="" title="CNN" />

#### Set permission 
<img src="images/8.png" width="80%" align="top-left" alt="" title="CNN" />

#### Create a group

<img src="images/9.png" width="80%" align="top-left" alt="" title="CNN" />

#### Enter name of group and select policies 
<img src="images/10.png" width="80%" align="top-left" alt="" title="CNN" />

#### Now add that user to above created group
<img src="images/11.png" width="80%" align="top-left" alt="" title="CNN" />


## remove AmazoneS3ReadOnlyAccess from above created user

### Go to ->IAM -> User  and chose user . then got to permission and select polycies you want to delete
<img src="images/practice1.png" width="80%" align="top-left" alt="" title="CNN" />

###  Click on Remove

<img src="images/practice2.png" width="80%" align="top-left" alt="" title="CNN" />


### Then click on remove policy
<img src="images/practice3.png" width="80%" align="top-left" alt="" title="CNN" />


## create group and attached  policy to the group and later add above created user to the group

### Create a group

<img src="images/9.png" width="80%" align="top-left" alt="" title="CNN" />

#### Enter name of group and select policies 
<img src="images/10.png" width="80%" align="top-left" alt="" title="CNN" />

#### Now add that user to above created group
<img src="images/11.png" width="80%" align="top-left" alt="" title="CNN" />

## IAM policies structure
<img src="images/12.png" width="80%" align="top-left" alt="" title="CNN" />

## create custom managed polycies and attached that to a user

### Go to IAM->Policies

<img src="images/practice4.png" width="80%" align="top-left" alt="" title="CNN" />

### Create Policies
<img src="images/practice5.png" width="80%" align="top-left" alt="" title="CNN" />

### select service on which permissions will be applied
<img src="images/practice5.png" width="80%" align="top-left" alt="" title="CNN" />

### click on write dropdown. Because we want to give write permision to that policy

<img src="images/practice6.png" width="80%" align="top-left" alt="" title="CNN" />

### Select puObject permision checkbox becuase we want to allow upload object in a bucket

<img src="images/practice7.png" width="80%" align="top-left" alt="" title="CNN" />

### Then specify ARN of a bucket on whcih you want to apply this policy

<img src="images/practice9.png" width="80%" align="top-left" alt="" title="CNN" />

### specify policy Name

<img src="images/practice10.png" width="80%" align="top-left" alt="" title="CNN" />

### Click on Create Policy


## created custome policy for s3 (to upload object) becuase ther is no managed policy for upload object. and then added that polycies to the group.

### GO to IAM -> User Groups and then click on a  Group and then go to permission and search selected policy

<img src="images/practice12.png" width="80%" align="top-left" alt="" title="CNN" />


## Create Role to access s3 from EC2

### Go to IAM -> Role  and Create Role

<img src="images/practice13.png" width="80%" align="top-left" alt="" title="CNN" />

### Slect trusted Entity (our trusted entity is EC2)

<img src="images/practice14.png" width="80%" align="top-left" alt="" title="CNN" />

### Select Service
<img src="images/practice15.png" width="80%" align="top-left" alt="" title="CNN" />


### Attach Policies to Role and click on Next
<img src="images/practice16.png" width="80%" align="top-left" alt="" title="CNN" />

### Give Name to the Role
<img src="images/practice17.png" width="80%" align="top-left" alt="" title="CNN" />

### we can see json representation policies
<img src="images/practice18.png" width="80%" align="top-left" alt="" title="CNN" />


### Click on Create
<img src="images/practice19.png" width="80%" align="top-left" alt="" title="CNN" />
