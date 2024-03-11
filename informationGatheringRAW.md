# Information Gathering

The goal of a penetration test (or pentest) is to detect security gaps to improve the defenses of the company being tested. Because the network, devices, and software within the company's environment change over time, penetration testing is a cyclic activity. A company's attack surface changes periodically due to newly discovered software vulnerabilities, configuration mistakes from internal activities, or IT restructuring that might expose new segments for targeting.

In this Learning Module, we'll learn how to methodically map such an attack surface using both passive and active means, and understand how to leverage this information during the entire penetration test lifecycle.

# The Penetration Testing lifecycle

This Learning Unit covers the following Learning Objectives:

 - Understand the stages of a Penetration Test
 - Learn the role of Information Gathering inside each stage
 - Understand the differences between Active and Passive Information Gathering

To keep a company's security posture as tightly controlled as possible, we should conduct penetration testing on a regular cadence and after every time there's a significant shift in the target's IT architecture.

A typical penetration test comprises the following stages:

- Defining the Scope
- Information Gathering
- Vulnerability Detection
- Initial Foothold
- Privilege Escalation
- Lateral Movement
- Reporting/Analysis
- Lessons Learned/Remediation

In this Module, we'll briefly cover scoping before turning our focus to the main objective, Information Gathering. We will learn more about the other stages during the rest of the course.

The scope of a penetration test engagement defines which IP ranges, hosts, and applications should be test subjects during the engagement, as compared to out-of-scope items that should not be tested.

Once we have agreed with the client on the engagement's scope and time frame, we can proceed to the second step, information gathering. During this step, we aim to collect as much data about the target as possible.

To begin information gathering, we typically perform reconnaissance to retrieve details about the target organization's infrastructure, assets, and personnel. This can be done either passively or actively. While the former technique aims to retrieve the target's information with almost no direct interaction, the latter probes the infrastructure directly. Active information gathering reveals a bigger footprint, so it is often preferred to avoid exposure by gathering information passively.

It's important to note that information gathering (also known as enumeration) does not end after our initial reconnaissance. We'll need to continue collecting data as the penetration test progresses, building our knowledge of the target's attack surface as we discover new information by gaining a foothold or moving laterally.

In this Module, we'll first learn about passive reconnaissance, then explore how to actively interact with a target for enumeration purposes.

# Passive Information Gathering

Passive Information Gathering

This Learning Unit covers the following Learning Objectives:

- Understand the two different Passive Information Gathering approaches
- Learn about Open Source Intelligence (OSINT)
- Understand Web Server and DNS passive information gathering

Passive Information Gathering, also known as Open-source Intelligence (OSINT), is the process of collecting openly-available information about a target, generally without any direct interaction with that target.

Before we begin, we need examine the two different schools of thought about what constitutes "passive" in this context.

In the strictest interpretation, we never communicate with the target directly. For example, we could rely on third parties for information, but we wouldn't access any of the target's systems or servers. Using this approach maintains a high level of secrecy about our actions and intentions, but can also be cumbersome and may limit our results.

In a looser interpretation, we might interact with the target, but only as a normal internet user would. For example, if the target's website allows us to register for an account, we could do that. However, we would not test the website for vulnerabilities during this phase.

Both approaches can be useful, depending on the objectives of the test we are conducting. For this reason, we need to consider the scope and rules of engagement for our penetration test before deciding which to use.

In this Module, we will adopt this latter, less rigid interpretation for our approach.

There are a variety of resources and tools we can use to gather information, and the process is cyclical rather than linear. In other words, the "next step" of any stage of the process depends on what we find during the previous steps, creating "cycles" of processes. Since each tool or resource can generate any number of varied results, it can be hard to define a standardized process. The ultimate goal of passive information gathering is to obtain information that clarifies or expands an attack surface, helps us conduct a successful phishing campaign, or supplements other penetration testing steps such as password guessing, which can ultimately lead to account compromise.

Instead of demonstrating linked scenarios, we will simply cover various resources and tools, explain how they work, and arm you with the basic techniques required to build a passive information gathering campaign.

Before we begin discussing resources and tools, let's share a personal example of a penetration test that involved successful elements of a passive information gathering campaign.

**A Note From the Authors**

Several years ago, the team at OffSec was tasked with performing a penetration test for a small company. This company had virtually no internet presence and very few externally-exposed services, all of which proved to be secure. There was practically no attack surface to be found. After a focused passive information gathering campaign that leveraged various Google search operators, connected bits of information "piped" into other online tools, and a bit of creative and logical thinking, we found a forum post made by one of the target's employees in a stamp-collecting forum:

    Hi!
    I'm looking for rare stamps from the 1950's - for sale or trade.
    Please contact me at david@company-address.com
    Cell: 999-999-9999

  Listing 1 - A forum post as a lure

We used this information to launch a semi-sophisticated client-side attack. We quickly registered a stamps-related domain name and designed a landing page that displayed various rare stamps from the 1950's, which we found using Google Images. The domain name and design of the site definitely increased the perceived reliability of our stamp trading website.

Next, we embedded some nasty client-side attack exploit code in the site's web pages, and called "David" during the workday. During the call, we posed as a stamp collector that had inherited their Grandfather's huge stamp collection.

David was overjoyed to receive our call and visited the malicious website to review the "stamp collection" without hesitation. While browsing the site, the exploit code executed on his local machine and sent us a reverse shell.

This is a good example of how some innocuous passively-gathered information, such as an employee engaging in personal business with his corporate email, can lead to a foothold during a penetration test. Sometimes the smallest details can be the most important.

> While "David" wasn't following best practices, it was the company's policy and lack of a security awareness program that set the stage for this breach. Because of this, we avoid casting blame on an individual in a written report. Our goal as penetration testers is to improve the security of our client's resources, not to target a single employee. Simply removing "David" wouldn't have solved the problem.

Let's review some of the most popular tools and techniques that can help us conduct a successful information gathering campaign. We will use MegaCorp One, a fictional company created by OffSec, as the subject of our campaign.

## Whois Enumeration

Whois is a TCP service, tool, and type of database that can provide information about a domain name, such as the name server and registrar. This information is often public, since registrars charge a fee for private registration.

We can gather basic information about a domain name by executing a standard forward search and passing the domain name, megacorpone.com, into whois, providing the IP address of our Ubuntu WHOIS server as an argument of the host (-h) parameter.

    kali@kali:~$ whois megacorpone.com -h 192.168.50.251
    Domain Name: MEGACORPONE.COM
    Registry Domain ID: 1775445745_DOMAIN_COM-VRSN
    Registrar WHOIS Server: whois.gandi.net
    Registrar URL: http://www.gandi.net
    Updated Date: 2019-01-01T09:45:03Z
    Creation Date: 2013-01-22T23:01:00Z
    Registry Expiry Date: 2023-01-22T23:01:00Z
    ...
    Registry Registrant ID: 
    Registrant Name: Alan Grofield
    Registrant Organization: MegaCorpOne
    Registrant Street: 2 Old Mill St
    Registrant City: Rachel
    Registrant State/Province: Nevada
    Registrant Postal Code: 89001
    Registrant Country: US
    Registrant Phone: +1.9038836342
    ...
    Registry Admin ID: 
    Admin Name: Alan Grofield
    Admin Organization: MegaCorpOne
    Admin Street: 2 Old Mill St
    Admin City: Rachel
    Admin State/Province: Nevada
    Admin Postal Code: 89001
    Admin Country: US
    Admin Phone: +1.9038836342
    ...
    Registry Tech ID: 
    Tech Name: Alan Grofield
    Tech Organization: MegaCorpOne
    Tech Street: 2 Old Mill St
    Tech City: Rachel
    Tech State/Province: Nevada
    Tech Postal Code: 89001
    Tech Country: US
    Tech Phone: +1.9038836342
    ...
    Name Server: NS1.MEGACORPONE.COM
    Name Server: NS2.MEGACORPONE.COM
    Name Server: NS3.MEGACORPONE.COM
    ...

Listing 2 - Using whois on megacorpone.com

Not all of this data is useful, but we did discover some valuable information. First, the output reveals that Alan Grofield registered the domain name. According to the Megacorp One Contact page, Alan is the "IT and Security Director".

We also found the name servers for MegaCorp One. Name servers are a component of DNS that we won't be examining now, but we should nevertheless add these servers to our notes.

Assuming we have an IP address, we can also use the whois client to perform a reverse lookup and gather more information.

    kali@kali:~$ whois 38.100.193.70 -h 192.168.50.251
    ...
    NetRange:       38.0.0.0 - 38.255.255.255
    CIDR:           38.0.0.0/8
    NetName:        COGENT-A
    ...
    OrgName:        PSINet, Inc.
    OrgId:          PSI
    Address:        2450 N Street NW
    City:           Washington
    StateProv:      DC
    PostalCode:     20037
    Country:        US
    RegDate:        
    Updated:        2015-06-04
    ...

Listing 3 - Whois reverse lookup

The results of the reverse lookup give us information about who is hosting the IP address. This information could be useful later, and as with all the information we gather, we will add this to our notes.

## Google Hacking

The term "Google Hacking" was popularized by Johnny Long in 2001. Through several talks and an extremely popular book (Google Hacking for Penetration Testers, he outlined how search engines like Google could be used to uncover critical information, vulnerabilities, and misconfigured websites.

At the heart of this technique is using clever search strings and operators for the creative refinement of search queries, most of which work with a variety of search engines. The process is iterative, beginning with a broad search, which is narrowed using operators to sift out irrelevant or uninteresting results.

We'll start by introducing several of these operators to learn how they can be used.

The site operator limits searches to a single domain. We can use this operator to gather a rough idea of an organization's web presence.

![Searching_with_a_Site_Operator](Searching_with_a_Site_Operator.png)
Figure 1: Searching with a Site Operator

The image above shows how the site operator limited the search to the megacorpone.com domain we have specified.

We can then use further operators to narrow these results. For example, the filetype (or ext) operator limits search results to the specified file type.

In the example below, we combine operators to locate TXT files (filetype:txt) on www.megacorpone.com (site:megacorpone.com):

![FSearching_with_a_Filetype_Operator](Searching_with_a_Filetype_Operator.png)
Figure 2: Searching with a Filetype Operator

We receive an interesting result. Our query found the robots.txt file, containing following content.

    User-agent: *
    Allow: /
    Allow: /nanites.php

  Listing 4 - robots.txt file

The robots.txt file instructs web crawlers, such as Google's search engine crawler, to allow or disallow specific resources. In this case, it revealed a specific PHP page (/nanities.php) that was otherwise hidden from the regular search, despite being listed allowed by the policy.

The ext operator could also be helpful to discern which programming languages might be used on a web site. Searches like ext:php, ext:xml, and ext:py will find indexed PHP Pages, XML, and Python pages, respectively.

We can also modify an operator using - to exclude particular items from a search, narrowing the results.

For example, to find interesting non-HTML pages, we can use site:megacorpone.com to limit the search to megacorpone.com and subdomains, followed by -filetype:html to exclude HTML pages from the results.

![Searching_with_the_Exclude_Operator](Searching_with_the_Exclude_Operator.png)
Figure 3: Searching with the Exclude Operator

In this case, we found several interesting pages, including web directories indices.

In another example, we can use a search for intitle:"index of" "parent directory" to find pages that contain "index of" in the title and the words "parent directory" on the page.

![Using Google to Find Directory Listings](Using_Google_to_Find_Directory_Listings.png)
Figure 4: Using Google to Find Directory Listings

The output refers to directory listing pages that list the file contents of the directories without index pages. Misconfigurations like this can reveal interesting files and sensitive information.

These basic examples only scratch the surface of what we can do with search operators. The Google Hacking Database (GHDB) contains multitudes of creative searches that demonstrate the power of leveraging combined operators.

![The Google Hacking Database](The_Google_Hacking_Database.png)
Figure 5: The Google Hacking Database (GHDB)

Another way of experimenting with Google Dorks is through the DorkSearch portal, which provides a pre-built subset of queries and a builder tool to facilitate the search.

Mastery of these operators, combined with a keen sense of deduction, are key skills for effective search engine "hacking".


## Netcraft

Netcraft is an internet service company, based in England, offering a free web portal that performs various information gathering functions such as discovering which technologies are running on a given website and finding which other hosts share the same IP netblock.

Using services such as Netcraft is considered a passive technique, since we never directly interact with our target.

Let's review some of Netcraft's capabilities. For example, we can use Netcraft's DNS search page to gather information about the megacorpone.com domain:

![Netcraft Results for *.megacorpone.com](Netcraft_Results_for.png)
Figure 6: Netcraft Results for *.megacorpone.com Search

For each server found, we can view a "site report" that provides additional information and history about the server by clicking on the file icon next to each site URL.

![Netcraft Site report for www.megacorpone.com](Netcraft_Site_Report_for.png)
Figure 7: Netcraft Site Report for www.megacorpone.com

The start of the report covers registration information. However, if we scroll down, we discover various "site technology" entries.

![Site Technology for www.megacorpone.com](Site_Technology_for.png)
Figure 8: Site Technology for www.megacorpone.com

This list of subdomains and technologies will prove useful as we move on to active information gathering and exploitation. For now, we will add it to our notes.


## Open-Source Code

In the following sections, we'll explore various online tools and resources we can use to passively gather information. This includes open-source projects and online code repositories such as:

- GitHub
- GitHub Gist
- GitLab
- SourceForge

Code stored online can provide a glimpse into the programming languages and frameworks used by an organization. On a few rare occasions, developers have even accidentally committed sensitive data and credentials to public repos.

The search tools for some of these platforms will support the Google search operators that we discussed earlier in this Module.

GitHub's search for example, is very flexible. We can use GitHub to search a user's or organization's repos; however, we need an account if we want to search across all public repos.

To perform any Github search, we first need to register a basic account, which is free for individuals and organizations.

Once we've logged in to our Github account, we can perform multiple keyword-based searches by typing into the top-right search field.

![GitHub Search](GitHub_Search.png)
Figure 9: GitHub Search

Let's search MegaCorp One's repos for interesting information. We can use path:users to search for any files with the word "users" in the filename and press ENTER.

![File Operator in GitHub Search](File_Operator_in_GitHub_Search.png)
Figure 9: File Operator in GitHub Search

Our search only found one file - xampp.users. This is nevertheless interesting because XAMPP is a web application development environment. Let's check the contents of the file.

![xampp.users File Content](File_Content.png)
Figure 10: xampp.users File Content

This file appears to contain a username and password hash, which could be very useful when we begin our active attack phase. Let's add it to our notes.

This manual approach will work best on small repos. For larger repos, we can use several tools to help automate some of the searching, such as Gitrob and Gitleaks.. Most of these tools require an access token to use the source code-hosting provider's API.

The following screenshot shows an example of Gitleaks finding an AWS access key ID in a file.

![Example Gitleaks Output](Example_Gitleaks_Output.png)
Figure 11: Example Gitleaks Output

Obtaining these credentials allows us unlimited access to the same AWS account and could lead to a compromise of any cloud service managed by this identity.

> Tools that search through source code for secrets, like Gitrob or Gitleaks, generally rely on regular expressions or entropy-based detections to identify potentially useful information. Entropy-based detection attempts to find strings that are randomly generated. The idea is that a long string of random characters and numbers is probably a password. No matter how a tool searches for secrets, no tool is perfect and they will miss things that a manual inspection might find.

## Shodan


As we gather information on our target, it is important to remember that traditional websites are just one part of the internet.

Shodan is a search engine that crawls devices connected to the internet, including the servers that run websites, but also devices like routers and IoT devices.

To put it another way, Google and other search engines search for web server content, while Shodan searches for internet-connected devices, interacts with them, and displays information about them.

Although Shodan is not required to complete any material in this Module or the labs, it's worth exploring a bit. Before using Shodan we must register a free account, which provides limited access.

Let's start by using Shodan to search for hostname:megacorpone.com.

![Searching MegaCOrp One's domain with Shodan](Searching_MegaCorp_One_domain_with_Shodan.png)
Figure 12: Searching MegaCorp One's domain with Shodan

In this case, Shodan lists the IPs, services, and banner information. All of this is gathered passively, avoiding interacting with the client's web site.

This information gives us a snapshot of our target's internet footprint. For example, there are four servers running SSH. We can drill down to refine our results by clicking on SSH under Top Ports on the left pane.

![MegaCorp_One_servers_running_SSH](MegaCorp_One_servers_running_SSH.png)
Figure 13: MegaCorp One servers running SSH

Based on Shodan's results, we know exactly which version of OpenSSH is running on each server. If we click on an IP address, we can retrieve a summary of the host.

![Shodan Host Summary](Shodan_Host_Summary.png)
Figure 14: Shodan Host Summary

We can review the ports, services, and technologies used by the server on this page. Shodan will also reveal if there are any published vulnerabilities for any of the identified services or technologies running on the same host. This information is invaluable when determining where to start when we move to active testing.

## Security Headers and SSL/TLS

There are several other specialty websites that we can use to gather information about a website or domain's security posture. Some of these sites blur the line between passive and active information gathering, but the key point for our purposes is that a third-party is initiating any scans or checks.

One such site, Security Headers, will analyze HTTP response headers and provide basic analysis of the target site's security posture. We can use this to get an idea of an organization's coding and security practices based on the results.

Let's scan www.megacorpone.com and check the results.

![Scan Results for www.megacorpone.com](Scan_Results_for.png)
Figure 15: Scan results for www.megacorpone.com

The site is missing several defensive headers, such as Content-Security-Policy and X-Frame-Options. These missing headers are not necessarily vulnerabilities in and of themselves, but they could indicate web developers or server admins that are not familiar with server hardening.

> Server hardening is the overall process of securing a server via configuration. This includes processes such as disabling unneeded services, removing unused services or user accounts, rotating default passwords, setting appropriate server headers, and so forth. We don't need to know all the ins and outs of configuring every type of server, but understanding the concepts and what to search for can help us determine how best to approach a potential target.

Another scanning tool we can use is the SSL Server Test from Qualys SSL Labs. This tool analyzes a server's SSL/TLS configuration and compares it against current best practices. It will also identify some SSL/TLS related vulnerabilities, such as Poodle or Heartbleed. Let's scan www.megacorpone.com and check the results.

![SSL Server Test results for www.megacorpone.com](SSL_Server_Test_results_for.png)
Figure 16: SSL Server Test results for www.megacorpone.com

The results seem better than the Security Headers check. However, this shows that the server supports TLS versions such as 1.0 and 1.1, which are deemed legacy as they implement insecure [cipher suites](<https://www.ssllabs.com/ssltest/) - this ultimately suggests that our target is not applying current best practices for SSL/TLS hardening. Disabling the TLS_DHE_RSA_WITH_AES_256_CBC_SHA suite has been recommended for several years, for example, due to multiple vulnerabilities both on AES Cipher Block Chaining mode and the SHA1 algorithm. We can use these findings to gain insights about the security practices, or lack thereof, within the target organization.

# Active Information Gathering

This Learning Unit covers the following Learning Objectives:

- Learn to perform Netcat and Nmap port scanning
- Conduct DNS, SMB, SMTP, and SNMP Enumeration
- Understand Living off the Land techniques

In this Learning Unit, we will move beyond passive information gathering and explore techniques that involve direct interaction with target services. We should keep in mind that innumerable services can be targeted in the field, for example Active Directory, which we'll cover in more detail in a separate Module. We'll nevertheless review some of the more common active information gathering techniques in this Module including port scanning and DNS, SMB, SMTP, and SNMP enumeration.

We'll mainly showcase active information gathering techniques that we can execute using pre-installed tools on our local Kali machine. However, in some cases during a penetration test, we won't have the luxury of running our favorite Kali Linux tool. In an assumed breach scenario such as this, we are typically given a Windows-based workstation by the client and must use what's available on Windows.

When "Living off the Land", we can leverage several pre-installed and trusted Windows binaries to perform post-compromise analysis. These binaries are shortened as LOLBins or, more recently, LOLBAS to include Binaries, Scripts and Libraries.

> Strictly speaking, LOLBAS binaries are typically used in a way other than by design. In this case, we'll relax the definition to include using standard Windows binaries "as they are" to perform information gathering.

In the upcoming sections, we are going to showcase the most popular LOLBAS techniques along with common Kali tools used for active information gathering.

## DNS Enumaration

The Domain Name System (DNS) is a distributed database responsible for translating user-friendly domain names into IP addresses. It's one of the most critical systems on the internet. This is facilitated by a hierarchical structure that is divided into several zones, starting with the top-level root zone.

Each domain can use different types of DNS records. Some of the most common types of DNS records include:

-  NS: Nameserver records contain the name of the authoritative servers hosting the DNS records for a domain.
-   A: Also known as a host record, the "a record" contains the IPv4 address of a hostname (such as www.megacorpone.com).
-  AAAA: Also known as a quad A host record, the "aaaa record" contains the IPv6 address of a hostname (such as www.megacorpone.com).
-  MX: Mail Exchange records contain the names of the servers responsible for handling email for the domain. A domain can contain multiple MX records.
 - PTR: Pointer Records are used in reverse lookup zones and can find the records associated with an IP address.
- CNAME: Canonical Name Records are used to create aliases for other host records.
-  TXT: Text records can contain any arbitrary data and be used for various purposes, such as domain ownership verification.

Due to the wealth of information contained within DNS, it is often a lucrative target for active information gathering.

Let's demonstrate this by using the host command to find the IP address of www.megacorpone.com.

    kali@kali:~$ host www.megacorpone.com
    www.megacorpone.com has address 149.56.244.87

   Listing 5 - Using host to find the A host record for www.megacorpone.com

By default, the host command searches for an A record, but we can also query other fields, such as MX or TXT records, by specifying the record type in our query using the -t option.

    kali@kali:~$ host -t mx megacorpone.com
    megacorpone.com mail is handled by 10 fb.mail.gandi.net.
    megacorpone.com mail is handled by 20 spool.mail.gandi.net.
    megacorpone.com mail is handled by 50 mail.megacorpone.com.
    megacorpone.com mail is handled by 60 mail2.megacorpone.com.

  Listing 6 - Using host to find the MX records for megacorpone.com

In this case, we first ran the host command to fetch only megacorpone.com MX records, which returned four different mail server records. Each server has a different priority (10, 20, 50, 60) and the server with the lowest priority number will be used first to forward mail addressed to the megacorpone.com domain (fb.mail.gandi.net).

We then ran the host command again to retrieve only the megacorpone.com TXT records, which returned two entries.

    kali@kali:~$ host -t txt megacorpone.com
    megacorpone.com descriptive text "Try Harder"
    megacorpone.com descriptive text "google-site-verification=U7B_b0HNeBtY4qYGQZNsEYXfCJ32hMNV3GtC0wWq5pA"

  Listing 7 - Using host to find the TXT records for megacorpone.com

Now that we have collected some initial data from the megacorpone.com domain, we can continue to use additional DNS queries to discover more hostnames and IP addresses belonging to the same domain. For example, we know that the domain has a web server with the hostname "www.megacorpone.com".

Let's run host against this hostname.

    kali@kali:~$ host www.megacorpone.com
    www.megacorpone.com has address 149.56.244.87 

  Listing 8 - Using host to search for a valid host

Now, let's determine if megacorpone.com has a server with the hostname "idontexist". We'll observe the difference between the query outputs.

    kali@kali:~$ host idontexist.megacorpone.com
    Host idontexist.megacorpone.com not found: 3(NXDOMAIN)

  Listing 9 - Using host to search for an invalid host

In Listing 8, we queried a valid hostname and received an IP resolution response. By contrast, Listing 9 returned an error (NXDOMAIN) indicating a public DNS record does not exist for that hostname. Since we now understand how to search for valid hostnames, we can automate our efforts.

Having learned the basics of DNS enumeration, we can develop DNS brute-forcing techniques to speed up our research.

Brute forcing is a trial-and-error technique that seeks to find valid information such as directories on a web server, username and password combinations, or in this case, valid DNS records. By using a wordlist containing common hostnames, we can attempt to guess DNS records and check the response for valid hostnames.

In the examples so far, we used forward lookups, which request the IP address of a hostname to query both a valid and an invalid hostname. If host successfully resolves a name to an IP, this could be an indication of a functional server.

We can automate the forward DNS-lookup of common hostnames using the host command in a Bash one-liner.

First, let's build a list of possible hostnames.

    kali@kali:~$ cat list.txt
    www
    ftp
    mail
    owa
    proxy
    router

   Listing 10 - A small list of possible hostnames

Next, we can use a Bash one-liner to attempt to resolve each hostname.

    kali@kali:~$ for ip in $(cat list.txt); do host $ip.megacorpone.com; done
    www.megacorpone.com has address 149.56.244.87
    Host ftp.megacorpone.com not found: 3(NXDOMAIN)
    mail.megacorpone.com has address 51.222.169.212
    Host owa.megacorpone.com not found: 3(NXDOMAIN)
    Host proxy.megacorpone.com not found: 3(NXDOMAIN)
    router.megacorpone.com has address 51.222.169.214

   Listing 11 - Using Bash to brute force forward DNS name lookups

Using this simplified wordlist, we discovered entries for "www", "mail", and "router". The hostnames "ftp", "owa", and "proxy", however, were not found. Much more comprehensive wordlists are available as part of the SecLists project. These wordlists can be installed to the /usr/share/seclists directory using the sudo apt install seclists command.

With the exception of the www record, our DNS-forward brute force enumeration revealed a set of scattered IP addresses in the same approximate range (51.222.169.X). If the DNS administrator of megacorpone.com configured PTR records for the domain, we could scan the approximate range with reverse lookups to request the hostname for each IP.

Let's use a loop to scan IP addresses 51.222.169.200 through 51.222.169.254. We will filter out invalid results (using grep -v) by showing only entries that do not contain "not found".

    kali@kali:~$ for ip in $(seq 200 254); do host 51.222.169.$ip; done | grep -v "not found"
    ...
    208.169.222.51.in-addr.arpa domain name pointer admin.megacorpone.com.
    209.169.222.51.in-addr.arpa domain name pointer beta.megacorpone.com.
    210.169.222.51.in-addr.arpa domain name pointer fs1.megacorpone.com.
    211.169.222.51.in-addr.arpa domain name pointer intranet.megacorpone.com.
    212.169.222.51.in-addr.arpa domain name pointer mail.megacorpone.com.
    213.169.222.51.in-addr.arpa domain name pointer mail2.megacorpone.com.
    214.169.222.51.in-addr.arpa domain name pointer router.megacorpone.com.
    215.169.222.51.in-addr.arpa domain name pointer siem.megacorpone.com.
    216.169.222.51.in-addr.arpa domain name pointer snmp.megacorpone.com.
    217.169.222.51.in-addr.arpa domain name pointer syslog.megacorpone.com.
    218.169.222.51.in-addr.arpa domain name pointer support.megacorpone.com.
    219.169.222.51.in-addr.arpa domain name pointer test.megacorpone.com.
    220.169.222.51.in-addr.arpa domain name pointer vpn.megacorpone.com.
    ...

   Listing 12 - Using Bash to brute force reverse DNS names

We have successfully managed to resolve a number of IP addresses to valid hosts using reverse DNS lookups. If we were performing an assessment, we could further extrapolate these results, and might scan for "mail2", "router", etc., and reverse-lookup positive results. These types of scans are often cyclical; we expand our search based on any information we receive at every round.

Now that we have developed our foundational DNS enumeration skills, let's explore how we can automate the process using a few applications.

There are several tools in Kali Linux that can automate DNS enumeration. Two notable examples are DNSRecon and DNSenum; let's explore their capabilities.

DNSRecon is an advanced DNS enumeration script written in Python. Let's run dnsrecon against megacorpone.com, using the -d option to specify a domain name and -t to specify the type of enumeration to perform (in this case, a standard scan).

    kali@kali:~$ dnsrecon -d megacorpone.com -t std
    [*] std: Performing General Enumeration against: megacorpone.com...
    [-] DNSSEC is not configured for megacorpone.com
    [*] 	 SOA ns1.megacorpone.com 51.79.37.18
    [*] 	 NS ns1.megacorpone.com 51.79.37.18
    [*] 	 NS ns3.megacorpone.com 66.70.207.180
    [*] 	 NS ns2.megacorpone.com 51.222.39.63
    [*] 	 MX mail.megacorpone.com 51.222.169.212
    [*] 	 MX spool.mail.gandi.net 217.70.178.1
    [*] 	 MX fb.mail.gandi.net 217.70.178.217
    [*] 	 MX fb.mail.gandi.net 217.70.178.216
    [*] 	 MX fb.mail.gandi.net 217.70.178.215
    [*] 	 MX mail2.megacorpone.com 51.222.169.213
    [*] 	 TXT megacorpone.com Try Harder
    [*] 	 TXT megacorpone.com google-site-verification=U7B_b0HNeBtY4qYGQZNsEYXfCJ32hMNV3GtC0wWq5pA
    [*] Enumerating SRV Records
    [+] 0 Records Found

   Listing 13 - Using dnsrecon to perform a standard scan

Based on the output above, we have managed to perform a successful DNS scan on the main record types against the megacorpone.com domain.

Let's try to brute force additional hostnames using the list.txt file we created previously for forward lookups.

    kali@kali:~$ cat list.txt 
    www
    ftp
    mail
    owa
    proxy
    router

   Listing 14 - List to be used for subdomain brute forcing using dnsrecon

To perform our brute force attempt, we will use the -d option to specify a domain name, -D to specify a file name containing potential subdomain strings, and -t to specify the type of enumeration to perform, in this case brt for brute force.

    kali@kali:~$ dnsrecon -d megacorpone.com -D ~/list.txt -t brt
    [*] Using the dictionary file: /home/kali/list.txt (provided by user)
    [*] brt: Performing host and subdomain brute force against megacorpone.com...
    [+] 	 A www.megacorpone.com 149.56.244.87
    [+] 	 A mail.megacorpone.com 51.222.169.212
    [+] 	 A router.megacorpone.com 51.222.169.214
    [+] 3 Records Found

  Listing 15 - Brute forcing hostnames using dnsrecon

Our brute force attempt has finished, and we have managed to resolve a few hostnames.

DNSEnum is another popular DNS enumeration tool that can be used to further automate DNS enumeration of the megacorpone.com domain. We can pass the tool a few options, but for the sake of this example we'll only pass the target domain parameter:

    kali@kali:~$ dnsenum megacorpone.com
    ...
    dnsenum VERSION:1.2.6

    -----   megacorpone.com   -----

    ...

    Brute forcing with /usr/share/dnsenum/dns.txt:
    _______________________________________________
    
    admin.megacorpone.com.                   5        IN    A        51.222.169.208
    beta.megacorpone.com.                    5        IN    A        51.222.169.209
    fs1.megacorpone.com.                     5        IN    A        51.222.169.210
    intranet.megacorpone.com.                5        IN    A        51.222.169.211
    mail.megacorpone.com.                    5        IN    A        51.222.169.212
    mail2.megacorpone.com.                   5        IN    A        51.222.169.213
    ns1.megacorpone.com.                     5        IN    A        51.79.37.18
    ns2.megacorpone.com.                     5        IN    A        51.222.39.63
    ns3.megacorpone.com.                     5        IN    A        66.70.207.180
    router.megacorpone.com.                  5        IN    A        51.222.169.214
    siem.megacorpone.com.                    5        IN    A        51.222.169.215
    snmp.megacorpone.com.                    5        IN    A        51.222.169.216
    syslog.megacorpone.com.                  5        IN    A        51.222.169.217
    test.megacorpone.com.                    5        IN    A        51.222.169.219
    vpn.megacorpone.com.                     5        IN    A        51.222.169.220
    www.megacorpone.com.                     5        IN    A        149.56.244.87
    www2.megacorpone.com.                    5        IN    A        149.56.244.87


    megacorpone.com class C netranges:
    ___________________________________

    51.79.37.0/24
    51.222.39.0/24
    51.222.169.0/24
    66.70.207.0/24
    149.56.244.0/24


    Performing reverse lookup on 1280 ip addresses:
    ________________________________________________

    18.37.79.51.in-addr.arpa.                86400    IN    PTR      ns1.megacorpone.com.
    ...

   Listing 16 - Using dnsenum to automate DNS enumeration

We have now discovered several previously-unknown hosts as a result of our extensive DNS enumeration. As mentioned at the beginning of this Module, information gathering has a cyclic pattern, so we'll need to perform all the other passive and active enumeration tasks on this new subset of hosts to disclose any new potential details.

The enumeration tools covered are practical and straightforward, and we should familiarize ourselves with each before continuing.

Having covered Kali tools, let's explore what kind of DNS enumeration we can perform from a Windows perspective.

Although not in the LOLBAS listing, nslookup is another great utility for Windows DNS enumeration and still used during 'Living off the Land' scenarios.

> Applications that can provide unintended code execution are normally listed under the LOLBAS project

Now let's connect to our Windows 11 client. For this we can use the xfreerdp command. The syntax is /u: and the username, /p: and the password, and /v: and the ip address.

    kali@kali:~$ xfreerdp /u:student /p:lab /v:192.168.50.152

   Listing 17 - Connecting to the Windows 11 client

Once connected on the Windows 11 client, we can open a command prompt window and run a simple query to resolve the A record for the mail.megacorptwo.com host.

    C:\Users\student>nslookup mail.megacorptwo.com
    DNS request timed out.
    timeout was 2 seconds.
    Server:  UnKnown
    Address:  192.168.50.151

    Name:    mail.megacorptwo.com
    Address:  192.168.50.154

   Listing 18 - Using nslookup to perform a simple host enumeration

In the above output, we queried the default DNS server (192.168.50.151) to resolve the IP address of mail.megacorptwo.com, which the DNS server then answered with "192.168.50.154".

Similarly to the Linux host command, nslookup can perform more granular queries. For instance, we can query a given DNS about a TXT record that belongs to a specific host.

    C:\Users\student>nslookup -type=TXT info.megacorptwo.com 192.168.50.151
    Server:  UnKnown:
    Address:  192.168.50.151

    info.megacorptwo.com    text =

        "greetings from the TXT record body"

  Listing 19 - Using nslookup to perform a more specific query

In this example, we are specifically querying the 192.168.50.151 DNS server for any TXT record related to the info.megacorptwo.com host.

The nslookup utility is as versatile as the Linux host command and the queries can also be further automated through PowerShell or Batch scripting.


## TCP/UDP Port Scanning Theory

Port scanning is the process of inspecting TCP or UDP ports on a remote machine with the intention of detecting what services are running on the target and what potential attack vectors may exist.

> Please note that port scanning is not representative of traditional user activity and could be considered illegal in some jurisdictions. Therefore, it should not be performed outside the labs without direct, written permission from the target network owner.

It is essential to understand the implications of port scanning, as well as the impact that specific port scans can have. Due to the amount of traffic some scans can generate, along with their intrusive nature, running port scans blindly can have adverse effects on target systems or the client network such as overloading servers and network links or triggering an IDS/IPS. Running the wrong scan could result in downtime for the customer.

Using a proper port scanning methodology can significantly improve our efficiency as penetration testers while also limiting many of the risks. Depending on the scope of the engagement, instead of running a full port scan against the target network, we can start by only scanning for ports 80 and 443. With a list of possible web servers, we can run a full port scan against these servers in the background while performing other enumeration. Once the full port scan is complete, we can further narrow our scans to probe for more and more information with each subsequent scan. Port scanning should be understood as a dynamic process that is unique to each engagement. The results of one scan determine the type and scope of the next scan.

We'll begin our exploration of port scanning with a simple TCP and UDP port scan using Netcat. It should be noted that Netcat is not a port scanner, but it can be used as such in a rudimentary way to showcase how a typical port scanner works.

Since Netcat is already present on many systems, we can repurpose some of its functionality to mimic a basic port scan when we are not in need of a fully-featured port scanner. We will also explore better tools dedicated to port scanning in detail.

Let's start by covering TCP scanning techniques, focusing on UDP later. The simplest TCP port scanning technique, usually called CONNECT scanning, relies on the three-way TCP handshake mechanism. This mechanism is designed so that two hosts attempting to communicate can negotiate the parameters of the network TCP socket connection before transmitting any data.

In basic terms, a host sends a TCP SYN packet to a server on a destination port. If the destination port is open, the server responds with a SYN-ACK packet and the client host sends an ACK packet to complete the handshake. If the handshake completes successfully, the port is considered open.

We can demonstrate this by running a TCP Netcat port scan on ports 3388-3390. We'll use the -w option to specify the connection timeout in seconds, as well as -z to specify zero-I/O mode, which is used for scanning and sends no data.

    kali@kali:~$ nc -nvv -w 1 -z 192.168.50.152 3388-3390
    (UNKNOWN) [192.168.50.152] 3390 (?) : Connection refused
    (UNKNOWN) [192.168.50.152] 3389 (ms-wbt-server) open
    (UNKNOWN) [192.168.50.152] 3388 (?) : Connection refused
    sent 0, rcvd 0

   Listing 20 - Using netcat to perform a TCP port scan

Based on this output, we know that port 3389 is open, while connections on ports 3388 and 3390 have been refused. The screenshot below shows the Wireshark capture of this scan.

![Wireshark capture of a Netcat port scan](Wireshar_capture_of_a_Netcat_port_scan.png)
Figure 17: Wireshark capture of the Netcat port scan

In this capture (Figure 17), Netcat sent several TCP SYN packets to ports 3390, 3389, and 3388 on packets 1, 3, and 7, respectively. Due to a variety of factors, including timing issues, the packets may appear out of order in Wireshark. We'll observe that the server sent a TCP SYN-ACK packet from port 3389 on packet 4, indicating that the port is open. The other ports did not reply with a similar SYN-ACK packet, and actively rejected the connection attempt via a RST-ACK packet. Finally, on packet 6, Netcat closed this connection by sending a FIN-ACK packet.

Now that we have a good understanding of the TCP handshake and have examined how a TCP scan works behind the scenes, let's cover UDP scanning. Since UDP is stateless and does not involve a three-way handshake, the mechanism behind UDP port scanning is different from TCP.

Let's run a UDP Netcat port scan against ports 120-123 on a different target. We'll use the only nc option we have not covered yet, -u, which indicates a UDP scan.

    kali@kali:~$ nc -nv -u -z -w 1 192.168.50.149 120-123
    (UNKNOWN) [192.168.50.149] 123 (ntp) open

   Listing 21 - Using Netcat to perform a UDP port scan

From the Wireshark capture, we'll notice that the UDP scan uses a different mechanism than a TCP scan.

![WIreshark capture of a UDP Netcat port scan](Wireshark_capture_of_a_UDP_Netcat_port_scan.png)
Figure 18: Wireshark capture of a UDP Netcat port scan

As shown in Figure 18, an empty UDP packet is sent to a specific port (packets 2, 3, 4, 6, and 8). If the destination UDP port is open, the packet will be passed to the application layer. The response received will depend on how the application is programmed to respond to empty packets. In this example, the application sends no response. However, if the destination UDP port is closed, the target should respond with an ICMP port unreachable (as shown in packets 5, 7, and 9), sent by the UDP/IP stack of the target machine.

Most UDP scanners tend to use the standard "ICMP port unreachable" message to infer the status of a target port. However, this method can be completely unreliable when the target port is filtered by a firewall. In fact, in these cases the scanner will report the target port as open because of the absence of the ICMP message.

Now that we have covered both TCP and UDP scanning techniques, let's review a few common pitfalls that can occur when performing such scans.

UDP scanning can be problematic for several reasons. First, UDP scanning is often unreliable, as firewalls and routers may drop ICMP packets. This can lead to false positives and ports showing as open when they are, in fact, closed. Second, many port scanners do not scan all available ports, and usually have a pre-set list of "interesting ports" that are scanned. This means open UDP ports can go unnoticed. Using a protocol-specific UDP port scanner may help to obtain more accurate results. Finally, penetration testers often forget to scan for open UDP ports, instead focusing on the "more exciting" TCP ports. Although UDP scanning can be unreliable, there are plenty of attack vectors lurking behind open UDP ports. A TCP scan also generates much more traffic than a UDP scan, due to overhead and packet retransmissions.

## Port Scanning with Nmap

Having built a solid understanding of port scanning fundamentals, let's now learn about Nmap, the de-facto tool for port scanning.

Nmap (written by Gordon Lyon, aka Fyodor) is one of the most popular, versatile, and robust port scanners available. It has been actively developed for over two decades and offers numerous features beyond port scanning.

Some of the Nmap example scans we'll cover in this Module are run using sudo. This is because quite a few Nmap scanning options require access to raw sockets, which in turn require root privileges. Raw sockets allow for surgical manipulation of TCP and UDP packets. Without access to raw sockets, Nmap is limited as it falls back to crafting packets by using the standard [Berkeley socket API](https://networkprogrammingnotes.blogspot.com/p/berkeley-sockets.html_.

Before exploring some port scanning examples, we should understand the footprint that each Nmap scan leaves on the wire and the scanned hosts.

A default Nmap TCP scan will scan the 1000 most popular ports on a given machine. Before we start running scans blindly, let's examine the amount of traffic sent by this type of scan. We'll scan one of the lab machines while monitoring the amount of traffic sent to the target host using iptables.

We will use several iptables options. First, let's use the -I option to insert a new rule into a given chain, which in this case includes both the INPUT (Inbound) and OUTPUT (Outbound) chains, followed by the rule number. We can use -s to specify a source IP address, -d to specify a destination IP address, and -j to ACCEPT the traffic. Finally, we'll use the -Z option to zero the packet and byte counters in all chains.

    kali@kali:~$ sudo iptables -I INPUT 1 -s 192.168.50.149 -j ACCEPT

    kali@kali:~$ sudo iptables -I OUTPUT 1 -d 192.168.50.149 -j ACCEPT

    kali@kali:~$ sudo iptables -Z

  Listing 22 - Configuring our iptables rules for the scan

Next, let's generate some traffic using nmap:

    kali@kali:~$ nmap 192.168.50.149
    Starting Nmap 7.92 ( https://nmap.org ) at 2022-03-09 05:12 EST
    Nmap scan report for 192.168.50.149
    Host is up (0.10s latency).
    Not shown: 989 closed tcp ports (conn-refused)
    PORT     STATE SERVICE
    53/tcp   open  domain
    88/tcp   open  kerberos-sec
    135/tcp  open  msrpc
    139/tcp  open  netbios-ssn
    389/tcp  open  ldap
    445/tcp  open  microsoft-ds
    464/tcp  open  kpasswd5
    593/tcp  open  http-rpc-epmap
    636/tcp  open  ldapssl
    3268/tcp open  globalcatLDAP
    3269/tcp open  globalcatLDAPssl

    Nmap done: 1 IP address (1 host up) scanned in 10.95 seconds

  Listing 23 - Scanning an IP for the 1000 most popular TCP ports

The scan completed and revealed a few open ports.

Now let's review some iptables statistics to get a clearer idea of how much traffic our scan generated. We can use the -v option to add some verbosity to our output, -n to enable numeric output, and -L to list the rules present in all chains.

    kali@kali:~$ sudo iptables -vn -L
    Chain INPUT (policy ACCEPT 1270 packets, 115K bytes)
    pkts bytes target     prot opt in     out     source               destination
    1196 47972 ACCEPT     all  --  *      *       192.168.50.149      0.0.0.0/0

    Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
    pkts bytes target     prot opt in     out     source               destination

    Chain OUTPUT (policy ACCEPT 1264 packets, 143K bytes)
     pkts bytes target     prot opt in     out     source               destination
    1218 72640 ACCEPT     all  --  *      *       0.0.0.0/0            192.168.50.149

  Listing 24 - Using iptables to monitor nmap traffic for a top 1000 port scan

According to the output, this default 1000-port scan generated around 72 KB of traffic.

Let's use iptables -Z to zero the packet and byte counters in all chains again and run another nmap scan, this time using -p to specify all TCP ports.

    kali@kali:~$ sudo iptables -Z

    kali@kali:~$ nmap -p 1-65535 192.168.50.149
    Starting Nmap 7.92 ( https://nmap.org ) at 2022-03-09 05:23 EST
    Nmap scan report for 192.168.50.149
    Host is up (0.11s latency).
    Not shown: 65510 closed tcp ports (conn-refused)
    PORT      STATE SERVICE
    53/tcp    open  domain
    88/tcp    open  kerberos-sec
    135/tcp   open  msrpc
    139/tcp   open  netbios-ssn
    389/tcp   open  ldap
    445/tcp   open  microsoft-ds
    464/tcp   open  kpasswd5
    593/tcp   open  http-rpc-epmap
    636/tcp   open  ldapssl
    3268/tcp  open  globalcatLDAP
    3269/tcp  open  globalcatLDAPssl
    5985/tcp  open  wsman
    9389/tcp  open  adws
    47001/tcp open  winrm
    49664/tcp open  unknown
    ...

    Nmap done: 1 IP address (1 host up) scanned in 2141.22 seconds

    kali@kali:~$ sudo iptables -vn -L
    Chain INPUT (policy ACCEPT 67996 packets, 6253K bytes)
    pkts bytes target     prot opt in     out     source               destination
    68724 2749K ACCEPT     all  --  *      *       192.168.50.149      0.0.0.0/0

    Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
    pkts bytes target     prot opt in     out     source               destination

    Chain OUTPUT (policy ACCEPT 67923 packets, 7606K bytes)
    pkts bytes target     prot opt in     out     source               destination
    68807 4127K ACCEPT     all  --  *      *       0.0.0.0/0            192.168.50.149

   Listing 25 - Using iptables to monitor nmap traffic for a port scan on ALL TCP ports

A similar local port scan explicitly probing all 65535 ports generated about 4 MB of traffic - a significantly higher amount. However, this full port scan has discovered more ports than the default TCP scan found.

Our results imply that a full Nmap scan of a class C network (254 hosts) would result in sending over 1000 MB of traffic to the network. Ideally, a full TCP and UDP port scan of every single target machine would provide the most accurate information about exposed network services. However, we clearly need to balance any traffic restrictions (such as a slow uplink) with discovering additional open ports and services via a more exhaustive scan. This is especially true for larger networks, such as a class A or B network assessment.

> There are modern port scanners like MASSCAN and RustScan that, although faster than Nmap, generate a substantial amount of concurrent traffic. Nmap, on the other hand, imposes some traffic rate limiting that results in less bandwidth congestion and more covert behavior.

Having learned about Nmap's basic use, we'll now explore some of Nmap's various scanning techniques, beginning with Stealth / SYN Scanning.

The most popular Nmap scanning technique is SYN, or "stealth" scanning. There are many benefits to using a SYN scan and as such, it is the default scan option used when no scan option is specified in an nmap command and the user has the required raw socket privileges.

SYN scanning is a TCP port scanning method that involves sending SYN packets to various ports on a target machine without completing a TCP handshake. If a TCP port is open, a SYN-ACK should be sent back from the target machine, informing us that the port is open. At this point, the port scanner does not bother to send the final ACK to complete the three-way handshake.

    kali@kali:~$ sudo nmap -sS 192.168.50.149
    Starting Nmap 7.92 ( https://nmap.org ) at 2022-03-09 06:31 EST
    Nmap scan report for 192.168.50.149
    Host is up (0.11s latency).
    Not shown: 989 closed tcp ports (reset)
    PORT     STATE SERVICE
    53/tcp   open  domain
    88/tcp   open  kerberos-sec
    135/tcp  open  msrpc
    139/tcp  open  netbios-ssn
    389/tcp  open  ldap
    445/tcp  open  microsoft-ds
    464/tcp  open  kpasswd5
    593/tcp  open  http-rpc-epmap
    636/tcp  open  ldapssl
    3268/tcp open  globalcatLDAP
    3269/tcp open  globalcatLDAPssl
    ...

   Listing 26 - Using nmap to perform a SYN scan

Because the three-way handshake is never completed, the information is not passed to the application layer and as a result, will not appear in any application logs. A SYN scan is also faster and more efficient because fewer packets are sent and received.

> Please note that term "stealth" refers to the fact that, in the past, firewalls would fail to log incomplete TCP connections. This is no longer the case with modern firewalls and although the stealth moniker has stuck around, it could be misleading.

The next Nmap scanning method we'll explore is named TCP Connect Scanning, which, as the name suggests, performs a full TCP connection.

When a user running nmap does not have raw socket privileges, Nmap will default to the TCP connect scan technique. Since an Nmap TCP connect scan makes use of the Berkeley sockets API to perform the three-way handshake, it does not require elevated privileges. However, because Nmap has to wait for the connection to complete before the API will return the status of the connection, a TCP connect scan takes much longer to complete than a SYN scan.

We may occasionally need to perform a connect scan using nmap, such as when scanning via certain types of proxies. We can use the -sT option to start a connect scan.

    kali@kali:~$ nmap -sT 192.168.50.149
    Starting Nmap 7.92 ( https://nmap.org ) at 2022-03-09 06:44 EST
    Nmap scan report for 192.168.50.149
    Host is up (0.11s latency).
    Not shown: 989 closed tcp ports (conn-refused)
    PORT     STATE SERVICE
    53/tcp   open  domain
    88/tcp   open  kerberos-sec
    135/tcp  open  msrpc
    139/tcp  open  netbios-ssn
    389/tcp  open  ldap
    445/tcp  open  microsoft-ds
    464/tcp  open  kpasswd5
    593/tcp  open  http-rpc-epmap
    636/tcp  open  ldapssl
    3268/tcp open  globalcatLDAP
    3269/tcp open  globalcatLDAPssl
    ...

   Listing 27 - Using nmap to perform a TCP connect scan

The output shows that the connect scan resulted in a few open services that are only active on the Windows-based host, especially Domain Controllers, as we'll cover shortly. One major takeaway, even from this simple scan, is that we can already infer the underlying OS and role of the target host.

Having reviewed the most common Nmap TCP scanning techniques, let's learn about UDP Scanning.

When performing a UDP scan, Nmap will use a combination of two different methods to determine if a port is open or closed. For most ports, it will use the standard "ICMP port unreachable" method described earlier by sending an empty packet to a given port. However, for common ports, such as port 161, which is used by SNMP, it will send a protocol-specific SNMP packet in an attempt to get a response from an application bound to that port. To perform a UDP scan, we'll use the -sU option, with sudo required to access raw sockets.

    kali@kali:~$ sudo nmap -sU 192.168.50.149
    Starting Nmap 7.70 ( https://nmap.org ) at 2019-03-04 11:46 EST
    Nmap scan report for 192.168.131.149
    Host is up (0.11s latency).
    Not shown: 977 closed udp ports (port-unreach)
    PORT      STATE         SERVICE
    123/udp   open          ntp
    389/udp   open          ldap
    ...
    Nmap done: 1 IP address (1 host up) scanned in 22.49 seconds

  Listing 28 - Using nmap to perform a UDP scan

The UDP scan (-sU) can also be used in conjunction with a TCP SYN scan (-sS) to build a more complete picture of our target.

    kali@kali:~$ sudo nmap -sU -sS 192.168.50.149
    Starting Nmap 7.92 ( https://nmap.org ) at 2022-03-09 08:16 EST
    Nmap scan report for 192.168.50.149
    Host is up (0.10s latency).
    Not shown: 989 closed tcp ports (reset), 977 closed udp ports (port-unreach)
    PORT      STATE         SERVICE
    53/tcp    open          domain
    88/tcp    open          kerberos-sec
    135/tcp   open          msrpc
    139/tcp   open          netbios-ssn
    389/tcp   open          ldap
    445/tcp   open          microsoft-ds
    464/tcp   open          kpasswd5
    593/tcp   open          http-rpc-epmap
    636/tcp   open          ldapssl
    3268/tcp  open          globalcatLDAP
    3269/tcp  open          globalcatLDAPssl
    53/udp    open          domain
    123/udp   open          ntp
    389/udp   open          ldap
    ...

  Listing 29 - Using nmap to perform a combined UDP and SYN scan

Our joint TCP and UDP scan revealed additional open UDP ports, further disclosing which services are running on the target host.

We can now extend what we have learned from a single host and apply it to a full network range through Network Sweeping.

To deal with large volumes of hosts, or to otherwise try to conserve network traffic, we can attempt to probe targets using Network Sweeping techniques in which we begin with broad scans, then use more specific scans against hosts of interest.

When performing a network sweep with Nmap using the -sn option, the host discovery process consists of more than just sending an ICMP echo request. Nmap also sends a TCP SYN packet to port 443, a TCP ACK packet to port 80, and an ICMP timestamp request to verify whether a host is available.

    kali@kali:~$ nmap -sn 192.168.50.1-253
    Starting Nmap 7.92 ( https://nmap.org ) at 2022-03-10 03:19 EST
    Nmap scan report for 192.168.50.6
    Host is up (0.12s latency).
    Nmap scan report for 192.168.50.8
    Host is up (0.12s latency).
    ...
    Nmap done: 254 IP addresses (13 hosts up) scanned in 3.74 seconds

  Listing 30 - Using nmap to perform a network sweep

Searching for live machines using the grep command on a standard nmap output can be cumbersome. Instead, let's use Nmap's "greppable" output parameter, -oG, to save these results in a more manageable format.

    kali@kali:~$ nmap -v -sn 192.168.50.1-253 -oG ping-sweep.txt
    Starting Nmap 7.92 ( https://nmap.org ) at 2022-03-10 03:21 EST
    Initiating Ping Scan at 03:21
    ...
    Read data files from: /usr/bin/../share/nmap
    Nmap done: 254 IP addresses (13 hosts up) scanned in 3.74 seconds
    ...

    kali@kali:~$ grep Up ping-sweep.txt | cut -d " " -f 2
    192.168.50.6
    192.168.50.8
    192.168.50.9
    ...

  Listing 31 - Using nmap to perform a network sweep and then using grep to find live hosts

We can also sweep for specific TCP or UDP ports across the network, probing for common services and ports in an attempt to locate systems that may be useful or have known vulnerabilities. This scan tends to be more accurate than a ping sweep.

    kali@kali:~$ nmap -p 80 192.168.50.1-253 -oG web-sweep.txt
    Starting Nmap 7.92 ( https://nmap.org ) at 2022-03-10 03:50 EST
    Nmap scan report for 192.168.50.6
    Host is up (0.11s latency).

    PORT   STATE SERVICE
    80/tcp open  http

    Nmap scan report for 192.168.50.8
    Host is up (0.11s latency).

    PORT   STATE  SERVICE
    80/tcp closed http
    ...

    kali@kali:~$ grep open web-sweep.txt | cut -d" " -f2
    192.168.50.6
    192.168.50.20
    192.168.50.21

  Listing 32 - Using nmap to scan for web servers using port 80

To save time and network resources, we can also scan multiple IPs, probing for a short list of common ports. For example, let's conduct a TCP connect scan for the top 20 TCP ports with the --top-ports option and enable OS version detection, script scanning, and traceroute with -A.

    kali@kali:~$ nmap -sT -A --top-ports=20 192.168.50.1-253 -oG top-port-sweep.txt
    Starting Nmap 7.92 ( https://nmap.org ) at 2022-03-10 04:04 EST
    Nmap scan report for 192.168.50.6
    Host is up (0.12s latency).

    PORT     STATE  SERVICE       VERSION
    21/tcp   closed ftp
    22/tcp   open   ssh           OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey:
    |   3072 56:57:11:b5:dc:f1:13:d3:50:88:b8:ab:a9:83:e2:29 (RSA)
    |   256 4f:1d:f2:55:cb:40:e0:76:b4:36:90:19:a2:ba:f0:44 (ECDSA)
    |_  256 67:46:b3:97:26:a9:e3:a8:4d:eb:20:b3:9b:8d:7a:32 (ED25519)
    23/tcp   closed telnet
    25/tcp   closed smtp
    53/tcp   closed domain
    80/tcp   open   http          Apache httpd 2.4.41 ((Ubuntu))
    |_http-server-header: Apache/2.4.41 (Ubuntu)
    |_http-title: Under Construction
    110/tcp  closed pop3
    111/tcp  closed rpcbind
    ...

  Listing 33 - Using nmap to perform a top twenty port scan, saving the output in greppable format

The top 20 nmap ports are determined using the /usr/share/nmap/nmap-services file, which uses a simple format of three whitespace-separated columns. The first is the name of the service, the second contains the port number and protocol, and the third is the "port frequency". Everything after the third column is ignored, but is typically used for comments as shown by the use of the pound sign (#). The port frequency is based on how often the port was found open during periodic research scans of the internet.

    kali@kali:~$ cat /usr/share/nmap/nmap-services 
    ...
    finger    79/udp    0.000956
    http    80/sctp    0.000000    # www-http | www | World Wide Web HTTP
    http    80/tcp    0.484143    # World Wide Web HTTP
    http    80/udp    0.035767    # World Wide Web HTTP
    hosts2-ns    81/tcp    0.012056    # HOSTS2 Name Server
    hosts2-ns    81/udp    0.001005    # HOSTS2 Name Server
    ...

  Listing 34 - The nmap-services file showing the open frequency of TCP port 80

At this point, we could conduct a more exhaustive scan against individual machines that are service-rich or are otherwise interesting.

There are many different ways we can be creative with our scanning to conserve bandwidth or lower our profile, as well as interesting host discovery techniques that are worth further research.

We have now scanned hosts that revealed a few services, so we can guess the nature of the target's operating system. Luckily for us, Nmap is already shipped with an OS Fingerprinting option.

OS fingerprinting can be enabled with the -O option. This feature attempts to guess the target's operating system by inspecting returned packets. This works because operating systems often use slightly different implementations of the TCP/IP stack (such as varying default TTL values and TCP window sizes), and these slight variances create a fingerprint that Nmap can often identify.

Nmap will inspect the traffic received from the target machine and attempt to match the fingerprint to a known list. By default, Nmap will display the detected OS only if the retrieved fingerprint is very accurate. Since we want to get a rough idea of the target OS, we include the --osscan-guess option to force Nmap print the guessed result even if is not fully accurate.

For example, let's consider this simple nmap OS fingerprint scan.

    kali@kali:~$ sudo nmap -O 192.168.50.14 --osscan-guess
    ...
    Running (JUST GUESSING): Microsoft Windows 2008|2012|2016|7|Vista (88%)
    OS CPE: cpe:/o:microsoft:windows_server_2008::sp1 cpe:/o:microsoft:windows_server_2008:r2 cpe:/o:microsoft:windows_server_2012:r2 cpe:/o:microsoft:windows_server_2016 cpe:/o:microsoft:windows_7 cpe:/o:microsoft:windows_vista::sp1:home_premium
    Aggressive OS guesses: Microsoft Windows Server 2008 SP1 or Windows Server 2008 R2 (88%), Microsoft Windows Server 2012 or Windows Server 2012 R2 (88%), Microsoft Windows Server 2012 R2 (88%), Microsoft Windows Server 2012 (87%), Microsoft Windows Server 2016 (87%), Microsoft Windows 7 (86%), Microsoft Windows Vista Home Premium SP1 (85%), Microsoft Windows 7 Professional (85%)
    No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
    ...

  Listing 35 - Using nmap for OS fingerprinting

The response suggests that the underlying operating system of this target is either Windows 2008 R2, 2012, 2016, Vista, or Windows 7.

> Note that OS Fingerprinting is not always 100% accurate, often due to network devices like firewalls or proxies that rewrite packet headers in between the communication.

Once we have recognized the underlying operating system, we can go further and identify services running on specific ports by inspecting service banners with -A parameter which also runs various OS and service enumeration scripts against the target. .

    kali@kali:~$ nmap -sT -A 192.168.50.14
    Nmap scan report for 192.168.50.14
    Host is up (0.12s latency).
    Not shown: 996 closed tcp ports (conn-refused)
    PORT    STATE SERVICE       VERSION
    21/tcp  open  ftp?
    | fingerprint-strings:
    |   DNSStatusRequestTCP, DNSVersionBindReqTCP, GenericLines, NULL, RPCCheck, SSLSessionReq, TLSSessionReq, TerminalServerCookie:
    |     220-FileZilla Server 1.2.0
    |     Please visit https://filezilla-project.org/
    |   GetRequest:
    |     220-FileZilla Server 1.2.0
    |     Please visit https://filezilla-project.org/
    |     What are you trying to do? Go away.
    |   HTTPOptions, RTSPRequest:
    |     220-FileZilla Server 1.2.0
    |     Please visit https://filezilla-project.org/
    |     Wrong command.
    |   Help:
    |     220-FileZilla Server 1.2.0
    |     Please visit https://filezilla-project.org/
    |     214-The following commands are recognized.
    |     USER TYPE SYST SIZE RNTO RNFR RMD REST QUIT
    |     HELP XMKD MLST MKD EPSV XCWD NOOP AUTH OPTS DELE
    |     CDUP APPE STOR ALLO RETR PWD FEAT CLNT MFMT
    |     MODE XRMD PROT ADAT ABOR XPWD MDTM LIST MLSD PBSZ
    |     NLST EPRT PASS STRU PASV STAT PORT
    |_    Help ok.
    | ftp-syst:
    |_  SYST: UNIX emulated by FileZilla.
    | ssl-cert: Subject: commonName=filezilla-server self signed certificate
    | Not valid before: 2022-01-06T15:37:24
    |_Not valid after:  2023-01-07T15:42:24
    |_ssl-date: TLS randomness does not represent time
    135/tcp open  msrpc         Microsoft Windows RPC
    139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
    445/tcp open  microsoft-ds?
    Nmap done: 1 IP address (1 host up) scanned in 55.67 seconds

   Listing 36 - Using nmap for banner grabbing and/or service enumeration

In the above example we used the -A parameter to run a service scan with extra options. If we want to run a plain service nmap scan we can do it by providing only the -sV parameter.

Banner grabbing significantly impacts the amount of traffic used as well as the speed of our scan. We should always be mindful of the options we use with nmap and how they affect our scans.

> Banners can be modified by system administrators and intentionally set to fake service names to mislead potential attackers.

Now that we have covered Nmap's major features, we'll focus on specific Nmap scripts encompassed by the Nmap Scripting Engine (NSE).

We can use the NSE to launch user-created scripts in order to automate various scanning tasks. These scripts perform a broad range of functions including DNS enumeration, brute force attacks, and even vulnerability identification. NSE scripts are located in the /usr/share/nmap/scripts directory.

The http-headers script, for example, attempts to connect to the HTTP service on a target system and determine the supported headers.

    kali@kali:~$ nmap --script http-headers 192.168.50.6
    Starting Nmap 7.92 ( https://nmap.org ) at 2022-03-10 13:53 EST
    Nmap scan report for 192.168.50.6
    Host is up (0.14s latency).
    Not shown: 998 closed tcp ports (conn-refused)
    PORT   STATE SERVICE
    22/tcp open  ssh
    80/tcp open  http
    | http-headers:
    |   Date: Thu, 10 Mar 2022 18:53:29 GMT
    |   Server: Apache/2.4.41 (Ubuntu)
    |   Last-Modified: Thu, 10 Mar 2022 18:51:54 GMT
    |   ETag: "d1-5d9e1b5371420"
    |   Accept-Ranges: bytes
    |   Content-Length: 209
    |   Vary: Accept-Encoding
    |   Connection: close
    |   Content-Type: text/html
    |
    |_  (Request type: HEAD)

    Nmap done: 1 IP address (1 host up) scanned in 5.11 seconds

  Listing 37 - Using nmap's scripting engine (NSE) for OS fingerprinting

To view more information about a script, we can use the --script-help option, which displays a description of the script and a URL where we can find more in-depth information, such as the script arguments and usage examples.

    kali@kali:~$ nmap --script-help http-headers
    Starting Nmap 7.92 ( https://nmap.org ) at 2022-03-10 13:54 EST

    http-headers
    Categories: discovery safe
    https://nmap.org/nsedoc/scripts/http-headers.html
      Performs a HEAD request for the root folder ("/") of a web server and displays the HTTP headers returned.
    ...

  Listing 38 - Using the --script-help option to view more information about a script

When internet access is not available, much of this information can also be found in the NSE script file itself.

It's worth our time to explore the various NSE scripts, as many of them are helpful and time-saving.

Having learned how to perform port scanning from Kali, let's explore how can we apply the same concepts from a Windows host.

If we are conducting initial network enumeration from a Windows laptop with no internet access, we are prevented from installing any extra tools that might help us, like the Windows Nmap version. In such a limited scenario, we are forced to pursue the 'living off the land' strategy we discussed earlier. Luckily, there are a few helpful built-in PowerShell functions we can use.

The Test-NetConnection function checks if an IP responds to ICMP and whether a specified TCP port on the target host is open.

For instance, from the Windows 11 client, we can verify if the SMB port 445 is open on a domain controller as follows.

    PS C:\Users\student> Test-NetConnection -Port 445 192.168.50.151

    ComputerName     : 192.168.50.151
    RemoteAddress    : 192.168.50.151
    RemotePort       : 445
    InterfaceAlias   : Ethernet0
    SourceAddress    : 192.168.50.152
    TcpTestSucceeded : True

  Listing 39 - Port scanning SMB via PowerShell

The returned value in the TcpTestSucceeded parameter indicates that port 445 is open.

We can further script the whole process in order to scan the first 1024 ports on the Domain Controller with the PowerShell one-liner shown below. To do so we need to instantiate a TcpClient Socket object as Test-NetConnection send additional traffic that is non needed for our purposes.

    PS C:\Users\student> 1..1024 | % {echo ((New-Object Net.Sockets.TcpClient).Connect("192.168.50.151", $_)) "TCP port $_ is open"} 2>$null
    TCP port 88 is open
    ...

  Listing 40 - Automating the PowerShell portscanning

We start by piping the first 1024 integer into a for-loop which assigns the incremental integer value to the $_ variable. Then, we create a Net.Sockets.TcpClient object and perform a TCP connection against the target IP on that specific port, and if the connection is successful, it prompts a log message that includes the open TCP port.

We've covered just the starting point of PowerShell's abilities, which can be further extended to match the traditional Nmap features.


## SMB Enumeration 

## SMTP Enumeration 

## SNMP Enumeration



== END OF LINE ==
