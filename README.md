# Web-App-recon-automation
Project name: Web application Recon Automation using python
Created under: VIEH Group
Created by: Soumya Mohanty, Pramod v gurlhosur, Danish Eqbal, Mahestarun p, Saravana Dandu

What is Automation?
IT automation is the use of instructions to create a repeated process that replaces an IT professional's manual work in data centers and cloud deployments. Software tools, frameworks and appliances conduct the tasks with minimum administrator intervention.

Why Python is best for automation?
Python is an object-oriented programming language, which allows the large size code to be modularity and also helps in easy to read the code and maintain it. And also Command line can drive the entire test automation workflow.

How we can use python automation for bug hunting?
The most important things is that we have packages already built-in in python, which helps automating our workflow easily. We can modules like OS module which is pre-built and pre-installed in the python modules section , which helps us to use os command in the system. For example let’s suppose there is a pre-defined tool in Kali linux, which is nmap, used for scanning for open ports in a host, so let’s use python’s OS module which helps using to execute the multiple nmap commands or we can do multiple scans  using a  python script, for n’s number of target or ip’s. 
Automating your bug bounty stuffs is easy and also easy to maintain it.

The phases if bug hunting what we will automate using automation :>

1. Subdomain Enumeration
2. URL Fuzzing
3. Directory Brute-Forcing
4. Parameter Fuzzing

Description
1. Subdomain Enumeration
Subdomain enumeration is the process of finding valid subdomain for domain. We will explore three different subdomain enumeration methods:

a) Brute Force: The brute forcing is to try the possible combination of words, alphabets, and numbers before the main domain in order to get a subdoomain that is resloved to IP address.
b) OSINT (Open Source Intelligence): To speed up the process of OSINT subdomain discovery, we can automate the above mehtods with the help of tools like dubfiner
c) Virtual Host: Some subdomains aren't always hosted in publically accessible DNS results, such as development versions of a web application or administration portals. Instead, the DNS record could be kept on a private DNS server or recorded on the developer's machines in their /etc/hosts file (or c:\windows\system32\drivers\etc\hosts file for Windows users) which maps domain names to IP addresses.

In this we are using passive as well as virtual host discovery to look for subdomains.

Tool used: Assetfinder, subfinder, httpx, Ffuf.

2. URL Fuzzing: We can user URL Fuzzer to find hidden files and directories on a web server by fuzzing. this is a discovery activity which allows you to discover resources that were not meant to be publically accessible (eg. /backups, /index.php)

In the we are gathering urls from waybackurls.

Tools used: Waybackurls, gau.

3) Directory Brute-Forcing: Directory fuzzing (a.k.a. directory bruteforcing) is a technique that can find some of those "hidden" paths. Dictionaries of common paths are used to request the web app for each path until exhaustion of the list. This technique relies on the attacker using a dictionnary/wordlist.
 In this we are using a tool named Dirsearch for directory brute-Forcing. 

Tool used: FFUF.

4: Parameter Fuzzing: An invalid character submitted in a URL parameter causes an error in the database query or script execution. This indicates that the application has not fully validated user-supplied input. These errors can lead to HTML injection, SQL injection, or arbitrary code execution.

In this, We are using a tool named FFUF for Parameter Fuzzing.

