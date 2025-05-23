# AWS

# IAM service
* It is used to control the access to AWS resources.We can manage permission which controls which resource can use a user.
* A user or group of users can be assigned json documents called policy.
<img src="images/1.png" width="80%" align="top-left" alt="" title="CNN" />
* Above policies define permissions for a user of a group.
* In AWS we provide the least privilege principle; it means don’t give more permission to a user then needs.

## what is policies
Policies is cobinatino of many permision.form example AdministrativeAccess policy is set of below permisions.
<img src="images/18.png" width="80%" align="top-left" alt="" title="CNN" />
```
"Action": * (allow all action)
"Resource": * (on all resource)
```
#### Below are permission of IAMReadOnlyAccess Policy

<img src="images/19.png" width="80%" align="top-left" alt="" title="CNN" />

## Create a IAM User 
It is global service when we create an IAM user or group you will notice that there is no region selected unlike other service
<img src="images/2.png" width="80%" align="top-left" alt="" title="CNN" />

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

## IAM policies structure
<img src="images/12.png" width="80%" align="top-left" alt="" title="CNN" />

* IAM polices start with version number
* Id : identifier for a policy
* Statement: Statement contains one or more statements
* Sid: is a statement id which identifies a statement.
* Effect: whether a statement allow or deny access to an api
* Principle : which account or user the policies applied to in above case this policy is for root user
* Action :list of resources to which action applied to .
* Resource : list of resources on which action will be applied to ,in this case resource is buckets on which action will be applied.

## Assign permission to a user
* Go to IAM->User
 <img src="images/13.png" width="80%" align="top-left" alt="" title="CNN" />

* Click on user to which you want to assign permission

<img src="images/14.png" width="80%" align="top-left" alt="" title="CNN" />

* Click on add permission

<img src="images/15.png" width="80%" align="top-left" alt="" title="CNN" />

* Click on attached policy

  <img src="images/16.png" width="80%" align="top-left" alt="" title="CNN" />

  * And attached policies :in my case I am attaching IamReadOnlyAccess Permission.so this user can not create IAM role or group user can only read.

      <img src="images/17.png" width="80%" align="top-left" alt="" title="CNN" />

## Create own policy
#### Go to IAM -> policies -> create policies
<img src="images/20.png" width="80%" align="top-left" alt="" title="CNN" />

#### Go To visual editor 
<img src="images/21.png" width="80%" align="top-left" alt="" title="CNN" />

#### Search IAM because we are going to Create plicies for IAM
<img src="images/22.png" width="80%" align="top-left" alt="" title="CNN" />

#### Filter action

#### Give Name to the policy
<img src="images/23.png" width="80%" align="top-left" alt="" title="CNN" />

## How can we access AWS
### we have three options 
* Console
* Command line interface
* SDK: Software development kit

## Access key
### It is a secreate same as user password.It is generated throut aws console. It contains Access Key ID just like username and Secrete Access Key just like passwrod.Access key is used to interact with AWS services using CLI.

### How to create access key
* Go to IAM -> Users: and click on currect logedin user
    <img src="images/secrete_key1.png" width="80%" align="top-left" alt="" title="CNN" />
* Click on security credentials
     <img src="images/secrete_key2.png" width="80%" align="top-left" alt="" title="CNN" />
* Scroll down and click on Create Access Key
         <img src="images/secrete_key3.png" width="80%" align="top-left" alt="" title="CNN" />
* select use case
         <img src="images/secrete_key4.png" width="80%" align="top-left" alt="" title="CNN" />
* click on create secrete key
         <img src="images/secrete_key5.png" width="80%" align="top-left" alt="" title="CNN" />
* Download csf file which contains secrete keys
         <img src="images/secrete_key6.png" width="80%" align="top-left" alt="" title="CNN" />


## AWS CLI
### A tool that enable you to intract with AWS services from local machine using commands in you command line cell

####  Install CLI on windows
* Click on this link and it will download automatically and then install by clicking install and next next
https://awscli.amazonaws.com/AWSCLIV2.msi

* Go to serach bar and serach command prompt.
* Run below command to chekc isntalled or not
    ```
    aws --version
    ``` 
    <img src="images/cli1.png" width="80%" align="top-left" alt="" title="CNN" />
* if you find above result in cli it means every thing is fine till here.

#### Configure local command prompt to connect with aws 
* Open command prompt
* Type below command 
    ```
    aws configure
    ```
* Above command will ask for Access key ID , Secrete access key and region. chose region which is closer to you 
    <img src="images/cli_configure.png" width="80%" align="top-left" alt="" title="CNN" />


## Roles for Aws Services
A service need to perform some operation on other service in aws and for that service need to have permision to perform operation just like permision to user to perform operation.

example: EC2 instance roles: Grant EC2 instances permissions to access services (like S3, DynamoDB)

### Create role for EC2
* Got IAM -> Rol ->Create role
    <img src="images/24.png" width="80%" align="top-left" alt="" title="CNN" />
* select aws service : becuase we are creating role for serevice.
    <img src="images/25.png" width="80%" align="top-left" alt="" title="CNN" />
* in above image from in service and user dropdown select serivice for which role you are going to create.in ower case select EC2
    <img src="images/26.png" width="80%" align="top-left" alt="" title="CNN" />
* chose use case EC2 on same above page 
* click on next

* attache policies with role.
    <img src="images/27.png" width="80%" align="top-left" alt="" title="CNN" />
* Give role name
    <img src="images/28.png" width="80%" align="top-left" alt="" title="CNN" />

## EC2
Elastic compute cloud ,it is a infrastructure as a service.it is on-demand virtual machine.

### what can we chose while creating EC2
* we can chose operating system.
* How much computer power & core (CPU) 
* chose How much RAM
* chose storage space
    ```
    chose any one:
    - do you want storage that is going to be attached through the network(EBS & EFS)
    - Hardware 
    ```
* Network Card
* Firewall rulse: Security group
* Bootstrap script
    ```
    Well, bootstrapping means launching commands when the machine starts.So, that script is only run once and when it first starts,and then will never be run again.
    ```
## AWS SDK
### It AWS software development kit. It is set of libraries or language specific APIs for different programing languages. It allow you to access and mange aws services programatically

## IAM ROLE FOR SERVICES
#### An IAM role is an IAM identity that you can create in your account that has specific permissions. An IAM role is similar to an IAM user. It contains permission policies that determine what the identity can and cannot do in AWS. 

Since we are saying it is identity it must have user_id and password jsut like a user when we create a aws user.Yes it has user_id and password but it is temporary.

### Create Role
* Go to IAM -> User
    <img src="images/role1.png" width="80%" align="top-left" alt="" title="CNN" />
* Create role
    <img src="images/role2.png" width="80%" align="top-left" alt="" title="CNN" />
* Select service on which this role you are going to apply
    <img src="images/role3.png" width="80%" align="top-left" alt="" title="CNN" />
* Attach plicies to that role 
    <img src="images/role4.png" width="80%" align="top-left" alt="" title="CNN" />
* Give Role Name and click on create role
    <img src="images/role5.png" width="80%" align="top-left" alt="" title="CNN" />

* After creating role you can see role information it has ARN also this is identity of role.
    <img src="images/role6.png" width="80%" align="top-left" alt="" title="CNN" />
*You can see permision assigned to role
    <img src="images/role6.png" width="80%" align="top-left" alt="" title="CNN" />


## AWS BUCKET
#### Bucket must have globaly unique name across all regions all account.Bucket must defined in a specific level. S3 look like a global service but bucket are created in a region. It is used to store unstructure data in objec form.Object file have a key, the key is full path of object

Bucket can store max file upto 500gb. If you want to store larger then 500gb you shoudl use multipart upload.

### policies vs permision vs role

