==================================
AWS Command line interface (CLI)
==================================

|

The AWS Command Line Interface (CLI) is a unified tool to manage your
AWS services. With just one tool to download and configure, you can
control multiple AWS services from the command line and automate them
through scripts.

Documentation and links
----------------------------

AWS provides a `getting started guide
<http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html>`_
and this guide is really just a shortened version of that document.

Install
-----------------

.. code-block:: bash

  ~$ pip install awscli --upgrade 

For more info check out the `aws install docs <http://docs.aws.amazon.com/cli/latest/userguide/installing.html>`_
  
Setting up IAM
----------------

AWS Identity and Access Management (IAM) allows you to
configure what permissions users have in your account. But why
does IAM matter if you are the only one using your account?

This matters because anyone that has access to your root account
(e.g. through AWS Access Keys) also has access to your billing
information which includes CC info. Thus we should set up a Admin
user account that sandboxed from accessing billing information.

1. go too *My Account* --> AWS management console
2. click on IAM
3. customize your signin link e.g.

   https://frodob.signin.aws.amazon.com/console 

4. create a new user:
   * click on *Users*
   * Create a user name and select Programmatic access and AWS Management Console access
   * create a password for this user

5. create a group with role "AdministrationAccess" -- call it say 'vanilla'
6. setup security
   * [optional] For extra security you can enable multi-factor auth
   * click on 'create access key'
   * download the csv

7. configure you aws envrionment
   .. code-block:: bash
		   
      ~$ aws configure

   It will look something like this...

   .. code-block:: None
		   
      AWS Access Key ID [None]: SOOOOOOOMMEEEIIIIDDD        
      AWS Secret Access Key [None]: somekeyyyyyyyyyThatIIsLong
      Default region name [None]: us-west-2
      Default output format [None]: json

That just created did two things:
  1. Creates default profile in ~/.aws/config
  2. Stores credentials in ~/.aws/credentials
   
More info and the updated docs can be found here   
http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html

As an aside you can create multiple profiles via

.. code-block:: bash
		
   ~$ aws configure --profile fancy_profile

Test it
^^^^^^^^^^^

.. code-block:: bash

   ~$ aws s3 ls

It should return some s3 buckets or return nothing.  If some error occurs you can try running the following command to debug

.. code-block:: bash

   ~$ aws configure list

Setup ssh keys
----------------

Generate a public and private key pair

  * ~$ ssh-keygen -t rsa -C "SOMENAME" -f ~/.ssh/id_aws
  * ~$ mv ~/.ssh/id_aws ~/.ssh/id_aws.pem
  * ~$ sudo chmod 600 ~/.ssh/id_aws.pem
  * ~$ ssh-add ~/.ssh/id_aws.pem

From the IAM manager click on "upload SSH public access key"

There are other ways to create key pairs.

* https://docs.aws.amazon.com/cli/latest/userguide/cli-ec2-keypairs.html


Test it
^^^^^^^^^

1. go to  https://console.aws.amazon.com/ec2/
2. From the navigation bar, select the region in which you created the key pair.
3. In the navigation pane, under NETWORK & SECURITY, choose Key Pairs
4. Go to the *import key pairs tab*
