# Introduction to Cybersecurity

Definiton: cyber is different from other technical fields because it involves _malicious_ and _intelligent_ actors. (e.g. opponents)

## On emulating the minds of our opponent

It's worth pausing to consider the particular attention that we will give to the offensive side of security, even in many of our defensive courses and Modules. One might wonder why a cybersecurity professional whose primary interest and goal is defending a network, organization, or government should also learn the offensive side.

Let's take the analogy of a medieval monarch building a castle. If the monarch learns that their enemy has catapults capable of hurling large boulders, they might design their castle to have thicker walls. Similarly, if their enemy is equipped with ladders, the monarch might give their troops tools to push the ladders off the walls.

The more this monarch knows about their would-be attacker and the more they can think like an attacker, the better defense they can build. The monarch might engage in "offensive" types of activities or audits to understand the gaps in their own defenses. For example, they could conduct "war games" where they direct their own soldiers to mock-battle each other, helping them fully understand the capabilities and destructive potential of a real attacker.

In cybersecurity, enterprises might hire an individual or a firm to perform a penetration test, also known as a pentest. A penetration tester takes on the role of an attacker to better understand the system's vulnerabilities and exposed weaknesses.

Leveraging the skill-sets and mindsets of an attacker allows us to better answer questions like:

    "How might an attacker gain access?"
    "What can they do with that access?" -" What are the worst possible outcomes from an attack?"

While learning hacking skills is (of course) essential for aspiring penetration testers, we also believe that defenders, system administrators, and developers will greatly benefit from at least a cursory education in offensive techniques and technologies as well.

Conversely, it's been our experience that many of the best penetration testers and web application hackers are those who have had extensive exposure to defending networks, building web applications, or administrating systems.

## Principles 

The principle of least privilege - only grant each part within a system the lowest possible privileges needed to achieve it's task.

Zero trust - ultimate conclusion of least privilege.

Open security - Security is not dependend on _secrecy_. "Even if an attacker knows exactly how the security is implemented, the attacker should still be thwarted." This isn't to say that nothing should be secret. Credentials are a clear case where the security of a password depends on its secrecy. However, we'd want our system to be secure even if the attacker knows there is a password, and even if they know the cryptographic algorithm behind it.

Defense in Depth - add defenses to as many layers of a system as possible, so if one is bypassed another may prevent full infiltration.

Threat modeling - Threat modeling describes taking data from real-world adversaries and evaluating those attack patterns and techniques against our people, processes, systems, and software. It is important to consider how the compromise of one system in our network might impact others.

Threat Intelligence -  data that has been refined in the context of the organization: actionable information that an organization has gathered via threat modeling about a valid threat to that organization's success. **Information isn't considered threat intelligence unless it results in an action item for the organization. The existence of an exploit is not threat intelligence;**  however, it is potentially useful information that might lead to threat intelligence.

# Extra sources

David Wheeler's [website](https://dwheeler.com/secure-programs/Secure-Programs-HOWTO/follow-good-principles.html)
[OWASP cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Product_Design_Cheat_Sheet.html#security-principles)
[OWASP whitepaper](https://secure-it-is.nl/whitepaper/)

