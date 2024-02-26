# Alternate exams included in the course
Oooh, more titles
## KLCP
Kali Linux Certified Professional 
80 question multiple choice in 
90 minutes - 
browser based and proctored
alternate material: https://kali.training/
## OSWP (PEN-210) 
Foundational Wireless Network Attacks
Skills needed to audit and secure wireless devices (network security)
vulns in: 802.11 networks and executing organized techniques
Exam simulates a "live wireless network" some scenarios contain traffic to the internet and similar AP's client behavior in a real network
Takes: 3 hours and 45 minutes
Once finished: 24 hours to upload documenation
resource: https://help.offsec.com/hc/en-us/articles/360059125211-KLCP-Exam-Guide
### Exam requirements
three secenarios available to attack
Only one scenario works at a time 
goal: obtain wireless key
then: connect to target AP and gain proof file from: 192.168.1.1/proof.txt
resource: https://help.offsec.com/hc/en-us/articles/360046904731-OSWP-Exam-Guide

# Challenge labs
## Labs 1-3
Important note: 
  All machines in the challenge labs will have either a 'local.txt' or a 'proof.txt', or both.
The contents of these files are randomized hashes that can be submitted to the OLP to log each compromise, just like the exercise flags. They are like checkpoints.
## Labs 4-6 
These are OSCP machines. Mock-exams. Serious business.
Though these are technically not with point values on the exam the standalone machines would be 20 points each - 60 points total and the ActiveDirectory set is 40 points.

All attack vectors for the machines are taught in the modules (and the training) and/or are leveraged in the first three Challenge Labs. However, the specific requirements to trigger the vulns may differ from the exact scenario's.

# exam
Won't be able to select a start time if the exam labs are full for that time period, so schedule exam ASAP.

# Modules

Alle modules, denk ik:

## Active Directory
De meest complexe, maar waarschijnlijk ook de meest belangrijke. It's ubiquitous in the enterprise environment.
Drie modules about the AD are:
### Active Directory Introduction and Enumeration
Is the first.
Paints a picture of how to think specifically about Windows machines in the context of an AD domain.
- Info gathering and setup
### Attacking Active Directory Authentication
Techniques to increase our presence withing the network by bypassing authentication protocols
### Lateral Movement in Active Directory
Apply pivoting concepts we've learned in complex AD environments

## Introduction to Cybersecurity (optional)
Broad survey on the world of cyber

## Effective Learning Strategies (Optional)
how to learn, how it happens and then construction of maaterials

## Report Writing for Penetration Testers (optional)
Framework and advice on writing notes as you progress through a test.  Also covers how to write a test report. The exam requires a report, so it is recommended.

## Enumeration and information gathering

### Information gathering / Enumeration
how to approach a network at the very outset of an engagement
Takes the most time and is usually one of, if not the most important part of a succesful pentest.

### Vulnerability Scanning
Techniques to narrow scope within a particular network 
- identify machines that are vulnerable

### Low-hanging fruit
As expected

## Web Application and Client Side Attacks

### Perimeter Attacks
methods of infiltration that can be reliably done from the internet
- initiated without access to internal network
Important because they are the most common

### Introduction to Web applications
Covering a methodology, toolset and an enumeration framework related to web applications

### Cross-Site Scripting (XSS)
very often seen vuln, good one to start with because it targets the _user_ of a web app as opposed to the server running it.
XSS is often weirdly intuitive.
Fun fact: XSS, since it targets users, is both a Web App attack and a Client-Side Attacks

### Common Web Application Attacks

### Directory traversal
obtain access to info we're not supposed tool 

### File inclusions
Advantage of ability to upload our own files to a web server 

### File Upload Vulnerabilities
Upload own files to a server > Exploit it 

### Command injection
Run code of choice

### SQL injection 
too common not to include 

### Client side Attacks 
very common external class of attacks. Take advantage of the human. Exploid common programs like Microsoft Office and Library Files 

## Other perimeter attacks

### Locating Public Exploits
How to use Kali and find exploits _on the internet_
(exploit-db.com)

### Fixing Exploits
Don't patch, lemme change the exploit 

### Anti Virus Evasion
Not a perimeter attack, but it will be helpful

### Password attacks 
Also includes cryptography

## Privilege escalation and Lateral Movement
Important because it gives more access
We always want to ask ourselves what the biggest impact our attacks can have on the network to provide the most value for our clients.

### Privileges

### Windows Privilege escalation

### Linux Privilege escalation
Repeats the last one and adds a dash of Linux

### Port Redirection and SSH tunneling

#### pivoting
Move into another machine on the network

#### tunneling
Move to another subnet

#### Tunneling through Deep Packet Inspection
particular technique that can be used to evade a common network-layer defense

### The Metasploit Framework (MSF)
MSF is a powerful set of tools that help us automate many of the enumeration and exploitation steps already covered

## Challenge Lab Preparation
After already doing 300 excercises, exploiting over 25 machines, it's time to put it together

### Assembling the Pieces
Walk the learner through a simulated pentest of five machines 
Everything from _Information gathering_ to _Lateral Movement in Active Directory_ are needed

### Trying Harder: The Challenge Labs


























































