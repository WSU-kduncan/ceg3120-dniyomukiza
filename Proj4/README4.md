
### Connecting via SSH Config file
1. I used **cd .ssh** command and created a config file there
+  Description on how file is configured
     + Create the name of your host
     + For HostName variable set your instance private IP as value
     + For User you can name it any how
     + 22 will be port value
     + IdentityFile key must have the path of the ssh key as value
  
2. ![](Screenshot%202022-10-30%20at%206.56.25%20PM.png)

Here is how my config file looks like: 

            Host form 
                HostName 10.0.1.10
                User ubuntu
                Port 22
                IdentityFile ~/pkey.pem
            
            Host quiz 
            HostName 10.0.1.20
            User ubuntu
            Port 22
            IdentityFile  ~/pkey.pem
            Need more? https://betterprogramming.pub/use-ssh-config-file-to-boost-your-productivity-b3867ce8cbfe
~                            3. INSTALL & CONFIGURE HAPROXY
+  First run apt-get update on ubuntu system
+   apt-get install -y haproxy
+    Haproxy -V: confirms if service is installed
+    Run systemctl status haproxy to check if haproxy is up and running
+    cd /etc/ haproxy: takes you into haproxy configuration directory
+    sudo touch filename.cfg
+   use sudo to get permission to create a file with cgf extention and use any text editor(I used vim) to edit this file
+    https://www.youtube.com/watch?v=L6U0PcESQ4Y&t=734s
+    https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration
+    /etc/ haproxy is the locartion of config file bacause in Linux systems configuration files will be in /etc folder
+    global and default settings were there
+    Modified my frontend to determine client IPs to send request to the load balancer
+    For backend:
balance type, I used roundrobin as balance type,
mode is http
then I mapped each server name with corresponding private IP.
+ sudo service haproxy reload or sudo systemctl restart haproxy will restar service after configuration change.

4. WEBSERVER CONFIGURATION &DOCUMENTATION 
   + **sudo apt-get install apache2** to install apache2
   + **apache2.config** located at **/etc/apache2** is located in this folder as all configuration files apache will need during start up reside here. I left it as is. It contains global configurations,pid file,timeout settings,maxkeepAliveRequests,etc 
   + I modified **index.html** file located at **/var/www/html**
   + This is the default root folder for apache. 
   + It has index page for apache(the homepage you see as a proof that apache is running)
   + sudo systemctl reload apache2 helps to restart the service after a configuration change.
  
  https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04


5. CONTENT BALANCING
![](Screen%20Shot%202022-10-26%20at%202.52.45%20PM.png)


![](Screen%20Shot%202022-10-26%20at%202.54.25%20PM.png)



  