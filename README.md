# AWS

## How can we access AWS
### we have three options 
* Console
* Command line interface
* SDK: Software development kit

## Access key
### It is a secreate same as user password.It is generated throut aws console. It contains Access Key ID just like username and Secrete Access Key just like passwrod.

### How to create access key
* Go to IAM -> Users: and click on currect logedin user
    <img src="images/secrete_key1.png" width="100%" align="top-left" alt="" title="CNN" />
* Click on security credentials
     <img src="images/secrete_key2.png" width="100%" align="top-left" alt="" title="CNN" />
* Scroll down and click on Create Access Key
         <img src="images/secrete_key3.png" width="100%" align="top-left" alt="" title="CNN" />
* select use case
         <img src="images/secrete_key4.png" width="100%" align="top-left" alt="" title="CNN" />
* click on create secrete key
         <img src="images/secrete_key5.png" width="100%" align="top-left" alt="" title="CNN" />
* Download csf file which contains secrete keys
         <img src="images/secrete_key6.png" width="100%" align="top-left" alt="" title="CNN" />


## AWS CLI
### A tool that enable you to intract with AWS services using commands in you command line cell

####  Install CLI on windows
* Click on this link and it will download automatically and then install by clicking install and next next
https://awscli.amazonaws.com/AWSCLIV2.msi

* Go to serach bar and serach command prompt.
* Run below command to chekc isntalled or not
    ```
    aws --version
    ``` 
    <img src="images/cli1.png" width="100%" align="top-left" alt="" title="CNN" />
* if you find above result in cli it means every thing is fine till here.

#### Configure local command prompt to connect with aws 
* Open command prompt
* Type below command 
    ```
    aws configure
    ```
* Above command will ask for Access key ID , Secrete access key and region. chose region which is closer to you 
    <img src="images/cli_configure.png" width="100%" align="top-left" alt="" title="CNN" />



## AWS SDK
### It AWS software development kit. It is set of libraries or language specific APIs for different programing languages. It allow you to access and mange aws services programatically

## IAM ROLE FOR SERVICES
#### An IAM role is an IAM identity that you can create in your account that has specific permissions. An IAM role is similar to an IAM user. It contains permission policies that determine what the identity can and cannot do in AWS. 

Since we are saying it is identity it must have user_id and password jsut like a user when we create a aws user.Yes it has user_id and password but it is temporary.

### Create Role
* Go to IAM -> User
    <img src="images/role1.png" width="100%" align="top-left" alt="" title="CNN" />
* Create role
    <img src="images/role2.png" width="100%" align="top-left" alt="" title="CNN" />
* Select service on which this role you are going to apply
    <img src="images/role3.png" width="100%" align="top-left" alt="" title="CNN" />
* Attach plicies to that role 
    <img src="images/role4.png" width="100%" align="top-left" alt="" title="CNN" />
* Give Role Name and click on create role
    <img src="images/role5.png" width="100%" align="top-left" alt="" title="CNN" />

* After creating role you can see role information it has ARN also this is identity of role.
    <img src="images/role6.png" width="100%" align="top-left" alt="" title="CNN" />
*You can see permision assigned to role
    <img src="images/role6.png" width="100%" align="top-left" alt="" title="CNN" />


## AWS BUCKET
#### Bucket must have globaly unique name across all regions all account.Bucket must defined in a specific level. S3 look like a global service but bucket are created in a region. It is used to store unstructure data in objec form.Object file have a key, the key is full path of object

Bucket can store max file upto 500gb. If you want to store larger then 500gb you shoudl use multipart upload.

### policies vs permision vs role

