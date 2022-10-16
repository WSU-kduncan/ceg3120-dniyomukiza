### PROVISIONING AWS INFRASTRUCTURE USING SCRIPTS 
  There are so many ways to create resources using templates. The one I like most is aws cloudformation. In a nutshell, this template will be comprised of parameters, mappings,resources, output,etc. We will breakdown this template skeleton later. This link has all information you need for any aws that are supported by cloudformation: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html

+ PARAMETERS

These are pretty much like variables in programming languages. They will hold values and you can refer to them down the road. Exampe is KeyName which will contain the the key that you will need for your instance to run. InstanceType is another example of what a variable can be. Let's say you wanna create an ec2 instance t1.micro. You can give this value to instance type variable and later using defining properties of your instances. Here is an example:

      Parameters:
        InstanceTypeParameter:
           Type: String
           Default: t2.micro
           AllowedValues:
              - t2.micro
              - m1.small
              - m1.large
            Description: Enter t2.micro, m1.small, or m1.large. Default is t2.micro.
+ VPC
  
  You need to determine your CIDR block range for your VPC. Tags are one of other VPC properties you can have where you name your resource. You can have one or many tages with key value pair each.

       Resources:
              VPC:
                Type: 'AWS::EC2::VPC'
                Properties:
                     CidrBlock: 10.0.0.0/24
                     Tags:
                         - Key: Name
                         Value: myVPC
    Also you can have more properties such as:

    InstanceTenancy: values will be default to say that your VPC runs on shared hardware, otherwise that will be dedicated hardware.This options cost more money though!
    
    enableDnsHostnames: Determines whether the VPC supports assigning public DNS hostnames to instances with public IP addresses. Default is false

    enableDnsSupport: Determines whether the VPC supports DNS resolution through the Amazon provided DNS server.If both attributes are set to true, instances with public IP addresses receive corresponding public DNS hostnames.
    For more abut VCP visit https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html

+ SUBNET
  When you create each subnet, you provide the VPC ID and IPv4 CIDR block for the subnet.The size of the subnet's IPv4 CIDR block can be the same as a VPC's or a subset of it. The smallest IPv4 subnet (and VPC) you can create uses a /28 netmask (16 IPv4 addresses), and the largest uses a /16 netmask (65,536 IPv4 addresses)
    
      Subnet:
         Type: 'AWS::EC2::Subnet'
          Properties:
             VpcId: !Ref VPC
             CidrBlock: 10.0.0.0/28
             Tags:
               - Key: Application
                 Value: !Ref 'AWS::StackId'
                - Key: Name
                  Value: Niyomukiza-CF-Subnet
    If you need more about subnet, this is a link https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html

+ INTERNET GATEWAY
   Allocates an internet gateway for use with a VPC. After creating the Internet gateway, you should attach it to a VPC.

    __Type__: 'AWS::EC2::InternetGateway' 
     
     __Properties:__
       
       Tags : optional
+ ATTACH GATEWAY
   
       Type: 'AWS::EC2::VPCGatewayAttachment'
          Properties:
              VpcId: !Ref VPC
               InternetGatewayId: !Ref InternetGateway

       Properties breakdown:
           InternetGatewayId: You must specify either InternetGatewayId or VpnGatewayId, but not both.

           VpcId:  The ID of your VPC
           VpnGatewayId: The ID of the virtual private gateway.


+ ROUTE TABLE :
    Specifies a route table for a specified VPC. After you create a route table, you can add routes and associate the table with a subnet.

    Main route table: The route table that automatically comes with your VPC. It controls the routing for all subnets that are not explicitly associated with any other route table.

    Each subnet in your VPC must be associated with a route table, which controls the routing for the subnet (subnet route table). If your subnet is not explicitly associated with a particular route table, it will take the main route table

    Custom route table: A route table that you create for your VPC.
     
           Type: 'AWS::EC2::RouteTable'
           Properties:
               VpcId: !Ref VPC
               Tags: - Key: Application
                       Value: !Ref 'AWS::StackId'
                     - Key: Name
                       Value: Niyomukiza-CF-RouteTable
    You should associate a route table with subnet, and both must be in same VPC
+ ROUTE
  Specifies a route in a route table within a VPC. You must specify either DestinationCidrBlock or plus the ID of one of the target resources(route table).

       
  

