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

## Whois Enumeration

## Google Hacking

## Netcraft

## Open-Source Code

## Shodan

## Security Headers and SSL/TLS

== END OF LINE ==
