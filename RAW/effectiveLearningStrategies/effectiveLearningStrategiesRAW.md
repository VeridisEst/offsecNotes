# Effective Learning Strategies

This Learning Module is intended to provide learners a better understanding of learning strategies as well as a preview of the OffSec instruction style and what to expect. After completing this Module, learners should be able to effectively plan how to best approach the coursework ahead.

Let's briefly review why this is an important Module. The information covered will not only help learners prepare to succeed in the training ahead, but will also be useful to cyber security professionals in the long term. Since both technology and the security landscape are constantly evolving and changing (we'll explore this more later), professionals must continually learn and grow. Finding success and satisfaction in this field is often tied to our ability to become efficient and comfortable learners.

We will cover the following Learning Units in this Learning Module:

    Learning Theory
    Unique Challenges to Learning Technical Skills
    The OffSec Training Methodology
    A Case Study Regarding Executable Permission
    Common Methods and Strategies
    Advice and Suggestions on Exams
    Practical Steps

# Learning Theory

Let's begin with a very basic discussion of Learning Theory. We'll make some general observations about this field of study and examine the current state of our (constantly-evolving) understanding of how learners learn.

In general, this Learning Unit and the next will illuminate some of the problems and difficulties that individuals face when learning new subjects.

This Learning Unit covers the following Learning Objectives:

    Understand the general state of our understanding about education and education theory
    Understand the basics of memory mechanisms and dual encoding
    Recognize some of the problems faced by learners, including "The Curve of Forgetting" and cognitive load

## What we know and what we don't

Although we humans have always taught, we have only recently (within the past 100 years) begun researching learning theory.1

Some of this research focuses on the structure and purpose of schools themselves. For example, a great deal of research ponders the ideal classroom size,2 whether or not activities in gym class can help a learner in science class,3 and so on. Although these studies may not initially seem relevant to our focus on cyber security, a few key aspects of this research are worth mentioning.

First, learning is not entirely dependent on the learner. The teacher, the material, the education format, and a variety of other factors affect success more than a learner's raw capability. In fact, a learner's past performance is a poor predictor of future success,4 and external events and circumstances can drastically affect a learner's performance.5

Second, as new educational studies are constantly released, it's clear there's still much to be discovered about the mechanics of our memory. This includes research suggesting that the notion of learning modes (or learning styles) is more of a myth than previously thought.6,7

With this in mind, OffSec designs our courses around current, established academic research regarding learning theory, and (partially because we aim to be perpetual learners) we're constantly seeking to improve our methods.

As instructors, our ultimate goal is to create a highly-effective learning environment that equips learners to excel in the ever-changing field of information security, regardless of past experience or performance in the field.

However, before we can discuss more practical strategies, let's explore some of the current research in the field of learning theory to understand how it's best applied.
1

(encyclopedia.com, 2022), https://www.encyclopedia.com/psychology/encyclopedias-almanacs-transcripts-and-maps/learning-theory-history ↩︎
2

(Kieschnick, 2018), https://www.hmhco.com/blog/class-size-matters ↩︎
3

(Chen, 2022), https://www.publicschoolreview.com/blog/the-pros-and-cons-of-mandatory-gym-class-in-public-schools ↩︎
4

(Carnevale, Fasules, Quinn, and Campbell, 2019), https://1gyhoq479ufd3yna29x7ubjn-wpengine.netdna-ssl.com/wp-content/uploads/FR-Born_to_win-schooled_to_lose.pdf ↩︎
5

(wbur, 2018), https://www.wbur.org/hereandnow/2018/08/27/public-private-school-family-income-study ↩︎
6

(Nancekivell, 2019), https://www.apa.org/news/press/releases/2019/05/learning-styles-myth ↩︎
7

(May, 2018), https://www.scientificamerican.com/article/the-problem-with-learning-styles/ ↩︎

## Memory Mechanisms and Dual Coding

It can be a bit overwhelming to think of education as a whole, so let's try to understand it in more simple terms first. One of the ways we can demonstrate that we've "learned" something is if we are able to create and retrieve a memory.

For example, we might learn a specific command to rename a file in Linux, mv oldfilename.txt newfilename.txt. Later, we might find ourselves at a computer, needing to rename a file. We hope that in that situation, away from our text book and any instructional material, we'll remember this particular command and syntax. Ideally, we can enter the command from memory and successfully rename the file.

A great deal of research has gone into how memory works and how we create strong memories and learn new skills.1 A full review of all of the details is out of scope for this Module, but in short, we might summarize by saying that we can improve memory by doing the following:

    Improve the quality of information we take in
    Improve the way or mode in which we receive information
    Improve our practice of retrieving information

We will explore all of these more, but for now, let's review them quickly:

    Improve the quality of information we take in: At a basic level, we expect our training material to be accurate. We might need explanatory paragraphs (like this one), written in a simple, easy-to-understand manner. This responsibility generally falls to the instructor or training provider.

    Improve the way or mode in which we receive information: This could include multiple approaches. Information might be more easily retained if presented in multiple formats, such as videos or images. This might also comprise, for example, a safe, distraction-free environment for the learner.

    Improve our practice of retrieving information: This may seem like merely exam practice at first, but there's more to it than that. A learner who reads a paragraph about how to create a file and then follows along to create a file independently is working on memory retrieval.

The more we work to improve in these three areas, the better we will be at remembering and learning. We also know that repeating information while changing the delivery mode can also be helpful.

Taking in the same information via a secondary method, for example, reading an explanation and then watching a video about the same Module, is called Dual Coding. The basic principle behind Dual Coding is that repeatedly studying the same information through different means improves retention.

Figure 1: Dual Coding
Figure 1: Dual Coding

The image shown above is more than just an illustration of Dual Coding; it's is actually an example of Dual Coding itself. By combining the text paragraph explaining the process of reading about a concept and combining it with explanatory visual aids, the information is better imprinted into our brains.

There is an increasing amount of research, including repeatable experiments and evidence from neuroimaging, that supports Dual Coding as an effective learning strategy.2
1

(Harvard, 2022), https://bokcenter.harvard.edu/how-memory-works ↩︎
2

(Cuevas, 2014), https://sciencebasedmedicine.org/brain-based-learning-myth-versus-reality-testing-learning-styles-and-dual-coding/ ↩︎

## The Forgetting Curve and Cognitive load

In a fictional tale by Jorge Luis Borges, a character named Funes the Memorious1 could remember in vivid detail every single thing he witnessed. Unfortunately, most of us aren't blessed with this gift. Two of the most common problems we encounter when trying to learn something (or create a memory) are "too long ago" or "too much information at once".

Let's start by examining the problem of forgetting. In 1885, learning scientist Hermann Ebbinghaus set out to memorize a few documents, then tested himself repeatedly on what he remembered. He was only able to remember all of the details if he tested himself immediately after memorizing. Ebbinghaus found he only remembered 100 percent of the information at the time of acquisition. After that, he started forgetting information very quickly. When he waited 20 minutes, he could only remember 58%. A day later, he could only remember 23%. He called this decline The Forgetting Curve.2

Figure 2: Ebbinghaus' Forgetting Curve
Figure 2: Ebbinghaus' Forgetting Curve

Thankfully, almost 150 years later, most of us have search engines and other tools available to us that Ebbinghaus did not.3 For example, if we forget the specific command to rename a file in Linux, such as mv oldfilename.txt newfilename.txt, we can quickly and easily Google it.

This is great news, since it means our learning approach doesn't need to be centered around memorizing facts. Instead, we can shift our focus to learning a method (in this case, our method might be to Google the command we need).

The second problem, which we've referred to as "too much information at once", is usually referred to as Cognitive Load.4

To better understand cognitive load, it may be helpful to imagine our brain as sort of a room, with pieces of information (that take up space) moving in and out. At some point, if more and more information keeps coming in, there simply isn't enough space for everything to stay organized. Pretty soon, the room is too full and there isn't enough space for more to come in through the door.

To remedy this, instructors may try reducing what is called "extraneous load." These are extra pieces of new information that aren't important or necessary. Let's go back to our example of renaming a file. Imagine that our instructor also explained that this command is exactly the same as the command we might use if we wanted to change the location of the file to the exact same directory and then giving it a new name. While technically true, it's possible that this bit of information would not improve our understanding of renaming files. Instead, trying to understand "relocating something to it's original location" might take up additional mental capacity, actually impeding our learning.

It's easy to imagine how disorganized instructional materials might increase cognitive load, but the same is also true for the classroom or environment where the learner is physically located. A noisy coffee shop is full of smells, conversations, people, and movement--all of which our brains are constantly taking in. In the case of online learning, learners may need to reduce extraneous load in the physical learning space itself. We'll explore this more later.
1

(Borges, 1962), http://vigeland.caltech.edu/ist4/lectures/funes borges.pdf ↩︎
2

(wikipedia, 2022), https://en.wikipedia.org/wiki/Forgetting_curve ↩︎
3

(Schaefer, 2015), https://www.inkling.com/blog/2015/08/why-google-changed-forgetting-curve/ ↩︎
4

(Loveless, 2022), https://www.educationcorner.com/cognitive-load-theory/ ↩︎

# Unique Challenges to Learning Technical Skills

Next, let's examine some of the other unique challenges that we will face when trying to learn technical skills.

This Learning Unit covers the following Learning Objectives:

    Recognize the differences and advantages of digital learning materials
    Understand the challenge of preparing for unknown scenarios
    Understand the potential challenges of remote or asynchronous learning


## Digital vs Print Materials

Let's consider the difference between learning in the Offensive Security Portal versus more traditional learning experiences like reading from a book. Technical skills such as coding are often taught using materials on the same medium where the practical work is done (a screen). This is the case with the OffSec Library.

Some studies have been done on the difference between learning on a screen or from a book,1 and researchers have even explored whether or not the size of the screen matters. Interestingly, the research shows relevant information.

Among the findings are that smaller screens may make learning more difficult and that individuals who read books tend to understand the information more fully. There are payoffs and drawbacks to both approaches. Sometimes screen reading can cause visual or sensory fatigue. learners learning in a digital context have easy access to a number of tools, including the ability to quickly and easily reference additional materials (for example, looking up the definition of a new vocabulary word). On the other hand, sometimes the act of reading forces one into a distraction-free environment that allows for deeper focus.2

The second, and perhaps the more important thing to note here, has to do with a concept known as Contextual Learning.3 Although we can't explore all of its details in this Module, this concept suggests that even on an intuitive level, we know that it's easier to learn how to build a house on a construction site.

In other words, when the training material is presented in the same context as the skill that we're trying to learn, our brain has to do less translation work and can accept the new information more readily. This doesn't mean that books about computers are worthless - it just means that our brains have to do more work to assimilate information from the page and think about it in the context of the computer screen.
1

(Szalavitz, 2012), https://healthland.time.com/2012/03/14/do-e-books-impair-memory/ ↩︎
2

(Oxford Learning, 2021), https://www.oxfordlearning.com/reading-online-vs-offline-whats-best-for-learning/ ↩︎
3

(Imel, 2000), https://files.eric.ed.gov/fulltext/ED448304.pdf ↩︎

## Expecting the Unexpected

There is another unique challenge that we will face in learning cyber security. This field is consistently focused on trying to prepare for situations we can't possibly predict.

Let's consider a couple of simple examples. We might learn about Enterprise Network Architecture, which examines the way a business organizes servers, workstations, and devices on a network. Unfortunately, as in-depth as that Module might go, it's unlikely to cover the exact network architecture that we'll encounter in some future scenario. In another Module, we might thoroughly and perfectly understand a specific attack vector, and we might even be able to execute it in the lab environment, but that doesn't mean we will encounter that exact vector in all future environments.

We also must take into account that the entire field of cyber security is constantly evolving. New vulnerabilities are discovered all the time. A network that is secure today may not be secure in six months. A learner needs to be able to exceed their initial training in order to remain effective in the field.

In this way, learning about cyber security is similar to learning transversal skills1 like leadership, communication, and teamwork. As with these skills, we cannot afford to focus on memorizing a series of steps to take. There is no simple, straightforward standard operating procedure for building better teamwork just as there is no simple, straightforward standard operating procedure for exploit development. Instead, we need to focus on understanding methods, techniques, and the purpose behind certain actions.

Let's return briefly to our example of learning how to secure a network. We mentioned that "A network that is secure today may not be secure in six months." The best approach to this problem is not to learn a series of steps we can follow to make that network secure today, then learn a new set of steps in six months. The solution is to learn the methodology and the purpose behind each security step. When new risks arise, we'll apply the same methodology, adapting and evolving along with the changing threat landscape.

Later in this Module we will discuss some potential approaches that can help us do this.
1

(Lopez and Rodriguez-Lopez, 2020), https://ervet-journal.springeropen.com/articles/10.1186/s40461-020-00100-0 ↩︎

## The Challenges of Remote and Asynchronous Learning

There is one more aspect of this particular type of learning that we will want to take into consideration--the fact that this is a remote learning environment. During the global COVID-19 pandemic, many schools adopted distance learning for the first time, and learners of all ages faced the new challenges1 presented by trying to learn via a computer monitor at home.

We must also consider that some online learning is asynchronous, meaning the instructor may not be present in a Zoom call or classroom to deliver a lecture, instruction, or to answer questions. Instead, the learner can participate in the class at whatever hour or pace works best for them. There are some definite advantages and disadvantages to this type of learning.

learners in a remote, asynchronous learning environment should be aware of two things:

    The advantages that come from the peer support, community, and camaraderie of other learners in a traditional classroom setting is no longer a guarantee.
    The pace and timing of the course is largely the learner's responsibility.

We will discuss some practical solutions to the second item shortly, but in order to connect with a wider community of learners, Offensive Security learners have a community of co-learners available on the OffSec Discord Server.2 There may also be local meetups or other communities available to a learner. Seeking out support and help (as well as helping and supporting others in turn) has benefits far beyond the classroom as well.
1

(Minnesota State, 2022), https://careerwise.minnstate.edu/education/successonline.html ↩︎
2

(OffSec, 2022), https://offs.ec/discord ↩︎

# OffSec Training Methodology

Now that we've examined some of the challenges we'll face as learners, let's explore how the structure and design of OffSec training materials will help us.

We won't be able to go into detail on everything that goes into creating meaningful and useful training.1 Instead, we'll focus on a few of the more noticeable strategies that we, as learners, will be able to take advantage of.

This Learning Unit covers the following Learning Objectives:

    Understand what is meant by a Demonstrative Methodology
    Understand the challenge of preparing for unknown scenarios
    Understand the potential challenges of remote or asynchronous learning

1

(Hackathorn, Solomon, Blankmeyer, et al., 2011), https://eric.ed.gov/?id=EJ1092139 ↩︎

## The Demonstration Method 

As one might infer from the name, using the Demonstration Method means showing (or acting out) what one hopes the learner will be able to accomplish. To illustrate this, let's return briefly to our example of learning to rename a file in Linux.

One way to provide this information is to be very direct.

`Use the "mv" command.`

    Listing 1 - Not using the demonstration method.

Although this is technically correct, a learner might still not fully understand how to use this information. An instructor using the demonstration method will follow the exact steps that a learner should follow, including the resulting output of running the command. The relevant information might be better presented with a code block.

Before showing the code block, we would first lay out our plan and detail any new or interesting commands we're planning on running. Here we might discuss that we'll use ls *.txt to list any .txt files in the directory. Next, we will run our renaming command, mv oldfilename.txt newfilename.txt. Finally, we'll use ls *.txt to check if our command worked.

`kali@kali:~$ ls *.txt
oldfilename.txt
kali@kali:~$ mv oldfilename.txt newfilename.txt 
kali@kali:~$ ls *.txt
newfilename.txt`

    Listing 2 - Renaming a file and checking our results.

After the code listing, we would explain our results. In this case, we listed the .txt files and only had one, named oldfilename.txt. We then ran our renaming command and received no output, as expected. Finally, we checked our results by running ls *.txt again. This time, the output shows the only .txt file in the directory is newfilename.txt. We could take further steps to ensure this file contains the same contents as earlier, and that only the filename has changed.

While it may seem unnecessary to include these extra items, this sort of demonstration and description begins to expose the thought process that a learner will need to learn. We verified our work in this case and checked that our command worked. Although that's not necessarily part of renaming a file, getting in the habit of checking our work is an excellent habit to adopt.

Sometimes the material will take what feels like a longer route in order to show both the new skill and a useful context. It may also actively expose and discuss the instructor's "mistakes" and redirections. Demonstrating a thought process in this manner is called modeling,1 and was developed as a way to teach critical thinking skills.2
1

(Wikipedia, 2023), https://en.wikipedia.org/wiki/Instructional_modeling ↩︎
2

(Daniel, Lafortune, Pallascio, et al., 2005), https://www.researchgate.net/profile/Marie-france_Daniel/publication/262849880_Modeling_the_Development_Process_of_Dialogical_Critical_Thinking_in_Pupils_Aged_10_to_12_Years/links/54ee0f110cf25238f93984dd.pdf ↩︎


## Learning by doing 

Doing something helps us learn it. There is an absolute wealth of research to support learning by doing as a method that increases memory retention and improves the overall educational experience of a learner.1,2,3,4

We know this method works well for learners, and OffSec has applied it in several ways.

    The Training Materials
    The Module Exercises
    The Challenge Labs
    Proving Grounds

The training materials themselves will always trend toward focusing on scenarios that we can follow along with. There are times when we need to discuss a bit of theory so that we have enough background to go deeper, but in general, if the material can demonstrate working through a problem, then the expectation is that the learner should be able to follow along. Often a virtual machine (VM) is specifically built in order to accommodate this.

The Module Exercises themselves will often involve working with a VM as well. This is the approach as often as is reasonably possible, but with some Modules (this one, for example) that are more theoretical, exercises are presented in a more standard question-and-answer format.

The OffSec Library also contains Challenge Labs, which take the exercises one step further. A Challenge Lab is, essentially, an environment of additional practice exercises specifically created to help learners prepare for an exam (which, perhaps as expected, is also hands-on). We highly recommend that learners take advantage of this additional opportunity.

Finally, we leverage assessments and exams. These are exercises and networked lab environments specifically for proving the skills we've learned. Since a real world environment will not give us a clear indication for which vulnerabilities might be present on a system, we don't create a 1:1 link between a course Module and an assessment (for example, we don't advertise whether or not a machine is vulnerable to privilege escalation).

With this in mind, the skills and methods learners will learn in the courses are directly applicable in the assessment and exam environments.
1

(Koedinger, McLaughlin, Kim, et al., 2015), http://pact.cs.cmu.edu/pubs/koedinger, Kim, Jia, McLaughlin, Bier 2015.pdf ↩︎
2

(Bates, 2015): https://opentextbc.ca/teachinginadigitalage/chapter/4-4-models-for-teaching-by-doing/ ↩︎
3

(Boser, 2020): https://www.the-learning-agency-lab.com/the-learning-curve/learning-by-doing/ ↩︎
4

(Djavad Mowafaghain Centre for Brain Health, 2018): https://www.centreforbrainhealth.ca/news/learning-doing-better-retention-learning-watching/ ↩︎


## Facing Difficulty

There is a common expression that "practice makes perfect". That may be true, but it begs the question, what makes for ideal practice?

Let's consider the following experiment that was performed in 1978.1 A group of 8-year-old children were divided into two groups to practice a simple task: toss a small bean bag into a target hole. After being introduced to the task with the target at a distance of three feet (about 90 cm), the groups spent the next three months practicing. One group kept practicing with the target at the same distance. The other aimed at a pair of targets - practicing with distances of both two feet (60 cm) and four feet (120 cm).

In the final test, the task was to toss the bean bags to a target three feet away. The group who had spent all of their practicing at that exact distance was in fact bested by the group who had practiced at two and four feet.

This and other studies demonstrate that struggle is not only important to the learning experience, but it's actually more important than mere repetition for creating the neural pathways that help us learn new skills.

This necessity for struggle means that we won't do much exact repetition in the OffSec learning materials. Since learning is self-directed, learners seeking more repetition can return to specific parts of the material as many times as they would like.

In lieu of this sort of repetition, we often choose to take an indirect route to the finish line. For example, we might try things that don't work so that we can experience the act of picking ourselves up and trying again. This is the metaphorical equivalent of moving the target around a bit.

Put simply, we feel that memorizing syntax is less important than being familiar with challenges and comfortable with a bit of struggle as a necessary character trait for someone in the field of information security.

Let's make one other note here while we're on the subject. We expect that just about every learner will get stuck at some point in their learning journey. We don't see this as a negative.

Getting stuck isn't fun, but we believe that being comfortable in a situation where we might not have all of the information and working through the problem is critical to success in the field of cyber security. To that end, we both sometimes take an indirect route to the finish line (in order to encounter "getting stuck") and provide technical exercises that ask learners to go beyond simply repeating covered material. Our goal is to help you practice getting stuck enough that you become quite comfortable with recovering.

To that end, we have written about this notion, which we call The Try Harder Mindset, in greater detail and with some specific strategies elsewhere.2
1

(Kerr and Booth, 1978), https://pubmed.ncbi.nlm.nih.gov/662537/ ↩︎
2

(OffSec, 2019), https://www.offsec.com/offsec/what-it-means-to-try-harder/ ↩︎


## Contextual Learning and Interleaving

Whenever possible, OffSec's learning materials will present a new skill as part of a realistic scenario. This can be difficult with more basic skills, like the command used to rename a file, but as we move deeper and deeper into the materials, we will find ourselves working through hands-on scenarios that are as representative of the real world as possible.

Teaching this way takes more time; however, learning new skills in a realistic context drastically improves a learner's retention and success.1

learners may also find that when information is presented in context, they are actually learning several things at once. For example, if we are learning about how an attack method might be both executed and detected at the same time, our brain can make more connections to help us learn effectively. This method is called interleaving.2
1

(Osika, MacMahon, Lodge, Carroll, 2022), https://www.timeshighereducation.com/campus/contextual-learning-linking-learning-real-world ↩︎
2

(University of Arizona, 2022), https://academicaffairs.arizona.edu/l2l-strategy-interleaving ↩︎

# Case Study: chmod -x chmod

It may be difficult to understand some of these ideas about teaching and learning completely out of context. In order to observe some of these ideas "in action", let's take a moment to learn about something called executable permissions.1 We'll use this as a sort of case study to better understand how the OffSec training materials are presented and how we might approach learning.

For this next section, please keep in mind that it is fine if the content is more technical than what you feel you are ready for or if you are not able to follow along. For example, we're going to start off by saying "Every file on a Linux machine has a number of properties associated with it." It is fine if, as a reader, you don't know what a Linux machine is yet, or what properties are, or even what files are.

We'll try and keep things pretty basic for a while, and then we'll go a little deeper. If you're a bit more experienced in Linux, you may enjoy the puzzle that we work through as we go on.

Again, the purpose here isn't actually to learn about the executable portion, but to have an example so that we can discuss how we might approach teaching such a subject.

This Learning Unit covers the following Learning Objectives:

    Review a sample of learning material about the executable permission, expand beyond the initial information set, and work through a problem
    Understand how OffSec's approach to teaching is reflected in the sample material

1

(Arora, 2013), https://www.thegeekstuff.com/2013/02/sticky-bit/ ↩︎

## What is executable permission

Every file on a Linux machine has a number of additional properties associated with it. These include when the file was created, what user created it, which users have permissions to read that file, and even the name of the file itself.

File permissions are particularly important. They indicate whether or not we are allowed to either read, write, or execute a particular file. We might think of the word write in this context as our ability to make certain changes to a file. This could, for example, be set to not allow us to write to a file, which might keep that file from being accidentally deleted. The permissions might also be set to not allow us to read a file that has information in it that we shouldn't be allowed to view.

These are called the file permissions1, and they pertain to a few different types of users who might be on this computer: the file owner, the user ownership group, and anyone else. These different classes of users can be given (or denied) permission for each of the three actions above: read, write, and execute. For the sake of this Module, we'll focus only on the owner of the file, ourselves in this case.

Let's open a terminal and review how this works in practice. We'll touch2 a file (newfilename.txt), which will create it and automatically make us the owner. Then we'll use the listing command ls3 to gather information about the file, providing the -l parameter that will produce a long listing including the file permissions.

`kali@kali:~$ touch newfilename.txt
kali@kali:~$ ls -l newfilename.txt
-rw-r--r-- 1 kali kali 0 Jun  6 12:31 newfilename.txt`

    Listing 3 - Checking file permissions

> In some situations, our touch command may fail because of directory permissions.4 Although this is beyond the scope of this introduction, for now it's worth knowing that directory permissions apply to all files and directories within a directory. If the directory permissions don't allow us to create files in this location, the touch command will obviously fail.

The touch command produced no output. This is normal. The output of the ls command includes information about the permissions as indicated by the letters rwx, where the "r" is for read, the "w" is for write, and the "x" is for execute. A dash (-) indicates that the user class doesn't have the corresponding permissions. In this case, we have permission to read and write to our new file, but there is no "x" character in the output, meaning no class has permission to execute.

As the owner of a particular file, we were granted read and write permissions by default when we created it, but we aren't granted executable permissions. In other words, if newfilename.txt was a program, we would not be able to execute it. This is a small but useful security feature that prevents us from accidentally running something we might not want to.

Let's keep going. In this scenario, let's say we have a simple program that will give us a complete list of employee names. This program is a Python script we've created named find_employee_names.py. Let's try to run the script.

`kali@kali:~$ ./find_employee_names.py
zsh: permission denied: ./find_employee_names.py
kali@kali:~$ ls -l find_employee_names.py
-rw-r--r-- 1 kali kali 206 Jun  7 12:31 find_employee_names.py`

    Listing 4 - First attempt at running our script.

We try running the script by simply entering the name of the file, find_employee_names.py, in the terminal. The ./ part of the command simply instructs the system where to find the file. This should work, but the output is not what we expected. The "zsh: permission denied" error message indicates that for some reason, we're not able to execute (or run) our script.

We also ran the same ls command as before. As with our newly created file, there's no "x" character in the output, which means that we don't have permission to execute. This explains the "permission denied" output.

Let's change the executable permission for this file and give ourselves permission to execute the file (put another way, to run it as a program). We can use chmod +x to add the executable permission to our script file. Let's do so and try running the script again.

`kali@kali:~$ chmod +x find_employee_names.py
kali@kali:~$ ls -l find_employee_names.py
-rwxr-xr-x 1 kali kali 206 Jun  7 12:31 find_employee_names.py
kali@kali:~$  ./find_employee_names.py
R. Jones
R. Diggs
G. Grice
C. Smith
C. Woods
D. Coles
J. Hunter
L. Hawkins
E. Turner
D. Hill`

    Listing 5 - Second attempt after chmod.

After we gave ourselves permission, we did a quick check with ls to find out if the output would change. It did! This time, the output contains the "x" character, indicating that executable permission is allowed for all three user classes.

Next, we ran our script again, and thankfully, we receive the expected output this time. The script provided us a list of the current employees.

Let's now change it back so that we no longer have permission to execute the file. To add the permission, we used chmod +x, so this time, we will use chmod -x.

`kali@kali:~$ chmod -x find_employee_names.py
kali@kali:~$ ./find_employee_names.py
zsh: permission denied: ./find_employee_names.py`

    Listing 6 - Putting things back the way they were

We're back where we started now with the same error message as before. From this small experiment, we should have a very basic understanding of the executable permission bit, the chmod tool, and the +x and -x options.
1

(Study Tonight, 2022), https://www.studytonight.com/linux-guide/understanding-file-permissions-in-linux-unix ↩︎
2

(Rani, 2021), https://www.geeksforgeeks.org/touch-command-in-linux-with-examples/ ↩︎
3

(Verma, 2021), https://www.geeksforgeeks.org/practical-applications-ls-command-linux/ ↩︎
4

(Linux Foundation, 2022), https://www.linuxfoundation.org/blog/blog/classic-sysadmin-understanding-linux-file-permissions ↩︎


## Going Deeper: Encountering a Strange Problem 

Let's take a moment to remind ourselves that it is fine if we are not following all of the technical steps we've been covering. Some of the following examples are specifically included to be interesting to learners who have a better understanding of Linux.

Let's continue to explore and push our learning further.

We'll consider the fact that the chmod command itself is just a file. It follows the same rules as other files on the system, including the same rules about permissions. It exists in a slightly different location (in the /usr/bin/ directory) as our script, but the only reason we are able to run the chmod +x find_employee_names.py command at all is because the chmod file has its permissions set to allow us to run it as a program.

Now, let's ask ourselves an interesting question: since chmod is the tool that allows us to set permissions, what would we do if we did not have permission to execute it?

Thankfully, it is not easy to accidentally remove our executable permission for this file. Despite this, we've done so on our system.

Let's explore how to fix our script again. We'll start with our script that worked previously.

`kali@kali:~$ ./find_employee_names.py
zsh: permission denied: ./find_employee_names.py
kali@kali:~$ chmod +x find_employee_names.py
zsh: permission denied: chmod`

    Listing 7 - Something isn't quite right here.

In this initial case, our simple script wouldn't run. This is the same problem we ran into previously. We tried the solution that worked before, but this time we got a new error message.

We could try running chmod on the chmod file, but we will run into the same problem. Let's run it on /usr/bin/chmod, since this is the specific location of the file.

`kali@kali:~$ chmod +x /usr/bin/chmod
zsh: permission denied: chmod`

    Listing 8 - Trying to chmod our chmod binary.

Once again our permission is denied, but we're not stuck yet.

> A particularly observant learner might reasonably ask why we needed to use "./" for our own Python script, but not for chmod. The answer, which is beyond the scope of this Module, has to do with the PATH environment variable. Interested or curious learners can learn more about this with external study.

For the most part, we've been checking for permission by simply attempting to execute the program. Let's recall the method we used earlier to check for this permission - using the ls command with the -l option. If we run ls -l without anything at the end, we'll be able to observe information for every file in the current directory. Since we are only interested in one file, we will follow our command with a specific file name.

Let's run this command for two different files.

`kali@kali:~$ ls -l find_employee_names.py
-rw-r--r-- 1 kali kali 206 Jun  7 12:31 find_employee_names.py`

`kali@kali:~$ ls -l /usr/bin/ls
-rwxr-xr-x 1 root root 147176 Sep 24  2020 /usr/bin/ls`

    Listing 9 - Running ls -l on different files.

In this example, we checked some of the information on two different files. We've run this on our Python script before and the output, missing the "x" character, is expected.

The second time, we ran ls on the ls file. This time we'll notice the output includes the "x" character. This explains why we can't run find_employee_names.py, but we can run ls.


## One Potential solution

There are a number of ways to fix our chmod problem. The simplest solutions involve finding a "clean" version of the chmod file and replacing it. The more complicated solutions include running one binary in the context of another binary that has the correct permissions. Let's explore one particularly interesting solution.

We need to do what our chmod file can do, but we also need permission to do it. To put this another way, our end goal is a file that can do what chmod can do, but that has the permissions of another file, such as ls.

We'll start by making a copy of a file that we know has the permission set we need. Since we checked the ls command earlier, let's copy that file into a new file named chmodfix.

`kali@kali:~$ cp /usr/bin/ls chmodfix
kali@kali:~$ ls -l chmodfix
-rwxr-xr-x 1 kali kali 147176 Jun  8 08:16 chmodfix`

    Listing 10 - Copying a file with cp.

Our new chmodfix file has the same permissions as the file we copied. This is a promising start.

The new chmodfix file is a perfect copy of ls. It can be run in the same way as ls, can use the same options, and so on. In other words, anywhere we would have used ls, we can use this instead. Let's try running it on itself.

`kali@kali:~$ ./chmodfix -l chmodfix
-rwxr-xr-x 1 kali kali 147176 Jun  8 08:16 chmodfix`

    Listing 11 - Anything ls can do, chmodfix can do.

The output is the same as before. This is progress!

Since the only thing that seems to be "broken" with our chmod file is the permissions (as far as we know, the contents of the file itself are fine), let's try to copy only the contents of the file and not the permissions. In other words, we only need the contents of the file - not the entire thing.

Since we know that cp will copy the entire file, we can't use that approach. The cat command1 is often used to show the contents of a file, so we will use that. Instead of just sending the contents of the file to display in the terminal window, we can use the ">" character to send them into our chmodfix file.

First, we'll run ls -l so that we can easily confirm whether or not the file contents change.

`kali@kali:~$ ls -l chmodfix
-rwxr-xr-x 1 kali kali 147176 Jun  8 08:20 chmodfix
kali@kali:~$ cat /usr/bin/chmod > chmodfix
kali@kali:~$ ls -l chmodfix
-rwxr-xr-x 1 kali kali 64448 Jun  8 08:21 chmodfix`

    Listing 12 - Sending the contents of chmod to chmodfix.

We previously examined the -rwxr-xr-x portion of the output. We'll also notice a number, "147176" in the case of the first command, in the output. This number indicates the size of the file. After we run the cat command, we'll observe that the file name and the permissions are still the same as before, but the file size is now "64448". This output indicates that the contents of the file have changed, but the permissions remained intact.

Let's return to the beginning and try to run chmodfix +x on our script.

`kali@kali:~$ ./chmodfix +x find_employee_names.py`

`kali@kali:~$ ./find_employee_names.py    
R. Jones
R. Diggs
G. Grice
C. Smith
C. Woods
D. Coles
J. Hunter
L. Hawkins
E. Turner
D. Hill`

    Listing 13 - Our fix worked!

Excellent! We were able to restore our permission to execute our script and run it. It's certainly a relief to receive our list of employees again.

Let's go one step further and restore our system so that we don't run into this problem again. Let's try and run the chmodfix command on the original chmod file to fix things.

kali@kali:~$ ./chmodfix +x /usr/bin/chmod
./chmodfix: changing permissions of '/usr/bin/chmod': Operation not permitted

    Listing 14 - Another obstacle.

We've hit another obstacle. We don't have permission to modify /usr/bin/chmod.

Whoever set up this system made it so the average user could not interrupt system files in /usr/bin/ (like chmod). Copying the file or the contents of the file was clearly allowed, but we're trying to write to a file in that folder, and we don't have permission to do that.

Right now we are trying to run this command as the kali user. Let's try running the command again, but this time as a Super User. To do this, we'll use the sudo command,2 followed by our original command. The system will prompt us for our password.

`kali@kali:~$ sudo ./chmodfix +x /usr/bin/chmod
[sudo] password for kali: `

    Listing 15 - Yo dawg, I heard you like chmod, so I chmod +x your chmod.

This worked.

It may be too early to call ourselves "hackers". However, finding unique ways to gain permissions unintended by a particular system is at the core of cyber security. This quick example offers a solid start.
1

(Linuxize, 2021), https://linuxize.com/post/linux-cat-command/ ↩︎
2

(Aruchamy, 2021), https://www.baeldung.com/linux/sudo-command ↩︎


## Analyzing this approach

If much of the preceding example was new to you, congratulations! You've survived your first bit of cyber security training. Remember, the actual solutions and commands aren't as important as understanding (for now) how this material was taught.

Although we covered an admittedly simple section from our written training, let's take a moment to examine how we taught this material. We'll highlight a few things in particular:

    Using the demonstration method
    Learning by doing
    The skill, not the tool
    Interleaving
    Expecting the unexpected

Let's quickly explore each of these.

The demonstration method is used specifically in the tone and voice of the example covered, but also in the series of actions that we follow. We don't skip steps, including verifying whether our solutions worked.

Notably, we encounter a "problem" (not being able to execute our script) almost immediately, which represents the real-world, day-to-day experience of learners after the course has ended. Research also supports problem solving as a very effective learning strategy both for engagement and retention.1

This problem-solving approach is used throughout Modules very intentionally. One way learners can take advantage of this is by trying to predict outcomes. We might, for example, try to guess what the next step will be in solving a problem. If we are surprised that the course material goes in another direction, and if we're curious, we can always try our solution!

This is a great way to follow the material, but let's consider something little more direct and practical. Learning by doing is an area where learners can take learning into their own hands and accelerate their own growth. The best way to do this is to follow along.

We can acknowledge that in the case presented in this Module, it would have been difficult to follow along manually. Normally, a Module will include at least one virtual machine that is specifically set up to allow learners to follow the accompanying text. In this case, we would have used a Linux machine with our find_employee_names.py script on it.

Let's discuss where and how to follow along by focusing on the code presented in the Module. A keen learner may have noticed that all of the code chunks use a similar style of formatting. Let's review one quickly:

`kali@kali:~$ ls -l chmodfix
-rwxr-xr-x 1 kali kali 64448 Jun  8 08:21 chmodfix`

    Listing 16 - A sample code listing.

The "kali@kali:~$" is what will appear on the screen for a user who is following along. Everything that appears in bold text (in this case, "ls -l chmodfix") is a command that we can type into the terminal. The text that follows is the output.

It's also important to understand where the focus is, which brings us to the skill, not the tool.

If you are already familiar with chmod, you may have noticed that we chose one of many different methods to use this tool. We chose, for example, not to explore how the permissions for our script (before we were able to execute) could have been represented with the numerical expression 644, which we could have fixed by running chmod 755.

Of course, it's almost impossible to remember every specific command and syntax, and piling on too much information increases cognitive load, making it more difficult to remember the material later. Even the most experienced security researchers find themselves looking things up now and then, and so we encourage learners to focus on why a command is being run versus what command is being run.

Sometimes when new ideas are introduced or when there is an opportunity to learn more outside the text, we might introduce a footnote. Getting used to "leaving" the immediate problem in order to go do a bit of research is also a critical skill. There have been a number of footnotes in this Module already, and they appear in numbered superscript in the text.

Interleaving is inevitable with this type of hands-on training. As a quick reminder, in the context of education, interleaving is mixing of multiple subjects. In this case, we reviewed the touch, cat, and ls commands, even though they weren't directly related to the things we were trying to study. They were, of course, related to our ability to modify chmod and our employee name script.

Another way of thinking about this is that the OffSec training materials are organized around concepts, not commands.

Finally, teaching learners how to expect the unexpected is not always easy to deliver. However, we often accomplish this by taking an indirect route to our goal with the intention of realistically highlighting issues you may experience in the field. Again, we hope to convey the logic behind our decisions instead of simply presenting commands and syntax.

In this example, we mentioned a potential pitfall with directory permissions (in a sidebar). We also knew that ./chmodfix +x /usr/bin/chmod wouldn't work, but we included it and ran it. We'll often walk through "unexpected" scenarios when we present new Modules and we'll include unexpected outcomes in many of our challenges.

As learners, it's imperative that we grow comfortable being in situations we don't fully understand and try things that might not work. The only way to really be prepared for the "unexpected" is to become comfortable in situations where we don't know exactly how things will pan out.

Not only this, but we cannot afford to avoid situations where we might feel stuck. In cyber security, it's extremely rare that the first approach we try works. In order to accurately represent this field, OffSec's approach is to teach the material in such a way that learners can become more resilient and agile, working through a particular problem until we are "unstuck".

There is often more than one way to accomplish any goal, and we encourage you to attempt other paths to reaching the goals we present. A curious learner might ask if, in the example presented, we could solve the issue by simply running sudo chmod +x /usr/bin/chmod. This is exactly the sort of thinking that we encourage, and why many of the challenges are presented in a virtual environment where learners can experiment and try things. Trying out an approach that doesn't work is also a valuable learning experience.

This experiment-and-experiment-again mindset is at the heart of what we believe it takes to be highly successful in this field, and at the risk of being redundant, the goal of our training is always to teach the methodology and the mindset.
1

(Samson, 2015), https://files.eric.ed.gov/fulltext/EJ1069715.pdf ↩︎

# Tactics and Common Methods

Next, we need to think about strategy and tactics. Consider the following quote from Sun Tzu:

Strategy without tactics is the slowest route to victory. Tactics without strategy is the noise before defeat. – Sun Tzu

In the most basic sense, we can think of strategy as being a long-term vision, while tactics are the short-term, immediate actions that we take. Strategy is the map, and tactics are the steps.

For learners in a formal school structure, the strategy and tactics of study are often built into the school structure itself. A learner's schedule and the Modules of study, and even how that learner will approach the learning material, are all dictated by the school district or the instructor.

In the absence of that rigid school structure, a common mistake of adult learners is to approach their studies casually, without thinking about either tactics or strategy. We might know, for example, that it's important to "take notes", but what exactly should we be writing down? And what should we do with those notes?

This Learning Unit will present a series of specific tactics for learners to choose from. The Learning Unit that follows will discuss a few strategies that we can use to approach our studies.

The tactics that follow are not intended as a complete or prescriptive list. What works for one learner may not work for others. learners should take ideas and determine for themselves what might work for them.

This Learning Unit covers the following Learning Objectives:

- Understand one potential note taking method called Cornell Notes
- Learn about Retrieval Practice
- Understand Spaced Practice
- Explore the SQ3R and PQ4R Method
- Examine the Feynman Technique
- Understand the Leitner System

Since this Learning Unit is intended as a reference list of tactics, we will not provide exercise questions at the end as we have with other Learning Units in this Module.

## Cornell Notes

There are many different note taking systems. Let's briefly examine one called Cornell Notes,1 which was developed by a Cornell University Professor named Walter Pauk in the 1950s. This method involves using a pen and paper, which helps with dual coding.

The first step is to divide the page into three areas. These are the cue (on the left hand side of the page), the notes (the large area on the right hand side of the page), and the summary (several lines of space at the bottom of the page).

Figure 3: An Illustration of Cornell Notes
Figure 3: An Illustration of Cornell Notes

The cue might be questions we have about the text or key words or phrases. To illustrate an example, let's discuss a Module like password hashing. This Module might have key terms to learn such as one-way encryption, salting, and cracking passwords. We might also have a question, for example, "Are some hashing methods better than others?"

The notes section for that page should be directly related to the items in the cue section. For example, near where we've written one-way encryption, we might write a long form definition of what is meant by this term.

Finally, we will complete the summary section as we review our notes. To continue the example, we might write "hashing a password = additional protection. Interested in more about cracking." The content here does not need to necessarily be directly related to the material

- this is an opportunity to reflect on our own interest, knowledge, and the study experience itself as well. Later in this Module, we will explore how self-reflection can be helpful.

1(Cornell University, 2022), https://lsc.cornell.edu/how-to-study/taking-notes/cornell-note-taking-system/ ↩︎

## Retrieval Practice 

Retrieval Practice is, as the name suggests, the practice of determining whether or not information can be recalled.1,2 We can think of this simply as quizzing yourself.

This practice can take many forms, including covering our notes and trying to recall what was written, or creating challenges or flashcards.

Let's discuss flashcards first. The Leitner System3 is named for German scientist Sebastian Leitner and involves making flashcards as a method to review and repeat learning. Both the act of creating and then practicing with flashcards can be incredibly useful. A flashcard is a small paper card that has a question or term on one side and then the answer or definition on the other side. Practice involves reading the question and guessing the answer.

There are a multitude of applications that can help create flashcards, but consider the benefits of taking small index cards and a pen or pencil and creating your own. The act of writing down the information and creating our own flashcards is dual coding at its best.

This method can be used in a number of different ways, but often takes full advantage of Spaced Practice as well as shuffling the cards and reviewing different cards on different days. The Leitner System is not incredibly useful for learning methodologies and problem-solving skills, but can be helpful when trying to memorize things, like a particular tool's syntax.

Creating actual challenges can be difficult. Learners have a few options here. The most obvious is to complete the included challenges for every Module. Whenever possible, these challenges do not simply repeat the information or the methods included in the Module, but ask the learner to go just one step further. Another option is to return to a completed hands-on exercise and repeat it. Finally, some courses include challenge labs, which are virtual machines that allow for a more hands-on retrieval practice or self-testing.

1(Pan for UCSD Psychology, 2022), https://psychology.ucsd.edu/undergraduate-program/undergraduate-resources/academic-writing-resources/effective-studying/retrieval-practice.html ↩︎
2(Smith and Weinstein, 2016), https://www.learningscientists.org/blog/2016/6/23-1 ↩︎
3(Gromada, 2021), https://www.mindedge.com/learning-science/the-leitner-system-how-does-it-work/ ↩︎

## Spaced Practice

Many learners have had the experience of "cramming," or staying up late to study and try to memorize a lot of information on the night before a big exam. Any learner who has tried this method can attest to how ineffective it can be, especially just a few days after the exam has concluded. Spaced practice1 is the opposite of this style of study.

Spaced practice has to do with the timing and duration of our study time. It is recommended to spread out the study time over days and weeks rather than do it all at once. Long, "cramming"-style study sessions actually take more time, often come at the expense of sleep, and (because they overwhelm our cognitive load) are significantly less effective.

The exact duration and space between study sessions will be different for each individual. Taking breaks and walking away from the computer screen for five or ten minutes can be very helpful. Take a nap or get some sleep. Do an activity that has nothing to do with your studies at all to space practice.

1(Smith and Weinstein, 2016), https://www.learningscientists.org/blog/2016/7/21-1 ↩︎

## The SQ3R Method

The SQ3R method1 has learners follow a pattern of study activities - survey, question, read, recite, review. We will detail the SQ3R method here, but it is notably very similar to the PQ4R method,2 which is useful for reading comprehension. learners who find the following tactic useful may want to check out the PQ4R method as well.

A learner begins by surveying the Module, or reviewing a high level outline, scanning through the material that might be covered during the study session. In particular, it would be important to review any highlighted text, diagrams, and headings.

Let's give an example. In the case of our current Module, a learner might encounter the various headings and subheadings: Learning Theory, Unique Challenges to Learning Technical Skills, Offsec Training Methodology, and so on. They might then review the subheadings.

Next, they will create, preferably in writing, a list of questions that they hope to have answered via the material. This may or may not reflect what the material will actually cover, but should be based largely on the survey. This is a very important step, as learners will return to the questions repeatedly.

Next, the learner reads the material one section at a time. If there are videos or other activities for this section, they can also complete those.

Next, the learner returns to their list of questions for that smaller section. They should try and recite the questions back from memory and determine if they're now able to answer them.

Finally, in the review, a learner returns to all of the smaller sections from a larger Module or chapter to check whether or not the questions have been answered and they can recall the answers.

For learners who have been taught that note taking is simply "writing down things that seem important", the SQ3R method represents an alternative that is much more effective.

1(Virginia Tech, 2022), https://ucc.vt.edu/academic_support/study_skills_information/sq3r_reading-study_system.html ↩︎
2(Logsdon, 2020), https://www.verywellfamily.com/strategy-improves-reading-comprehension-2162266 ↩︎

## The Feynman Technique

The Feynman Technique1 takes its name from Richard Feynman, a Nobel-prize winning physicist with a unique gift for explaining complex Modules in everyday terms. The technique that bears his name has four simple steps:

- Learn a Module
- Explain it to a beginner
- Identify gaps
- Return to study

What makes this method of study unique is Step 2. Many descriptions of this technique use the example of explaining the Module to a child who is unfamiliar with it. If we don't have access to a child (or a child who is willing to listen to an explanation about, for example, network scripting), this technique can still be useful.

In the act of explaining things to children, we change our language to make things more simple. For example, when discussing a Brute Force Attack2 with another professional, we might quickly devolve into a discussion on the massive computational power needed to crack a certain key. While explaining it to a child, we could simply say "it's a way to keep guessing lots and lots of passwords until, hopefully, one of them works."

The explanation itself isn't as important as the work the brain has to do to wrestle with the concepts and make them understandable outside of jargon. Similarly, when it's very difficult for us to break something down in this manner, that may be a sign that we don't understand it very well yet ourselves. All of this work helps us increase our own understanding.
1(Farnam Street, 2022), https://fs.blog/feynman-technique/ ↩︎
2(Wikipedia, 2022), https://en.wikipedia.org/wiki/Brute-force_attack ↩︎

# Advice and Suggestions on Exams

We want to take a few moments to discuss exams and assessments, since the experience and approach for exam taking is very different from the rest of the learning experience.

First, a word about the difference between the two. Some OffSec Learning Paths culminate in an optional assessment, which is generally a timed series of practical exercises. The learner has a great deal of freedom with scheduling and retaking the assessment, and can complete these exercises and submit the answers.

In other cases, OffSec courses culminate in a proctored exam, during which a learner has a set amount of time to complete a specific set of hands-on challenges. A successful exam results in an OffSec Certification.

The contents of this section are centered on exams specifically, since we know they are points of anxiety for some learners. However, many of the suggestions provided will also be helpful for individuals taking an assessment.

This Learning Unit covers the following Learning Objectives:

- Develop strategies for dealing with exam-related stress
- Recognize when you might be ready to take the exams
- Understand a practical approach to exams

This section is intended as a reference specifically for individuals who intend on taking an exam. Much of the material here will be useful for exams and assessments outside the context of OffSec training. No exercise questions are included at the end of it.

## Dealing with Stress

OffSec certifications are earned, not given. We use this language intentionally. Having a certification from OffSec is a significant accomplishment. You can't fake your way to the finish line or guess your way to a passing score.

For some individuals, this means that the exam and the weeks and months leading up to it can become a very stressful time. We want to take a few moments to try and address that experience now.

A great deal has been written on dealing with stress in general, but we'll focus in particular on high-stakes exam stress. There are some excellent resources surrounding the taking of the Bar Exam, a requirement in the United States for all lawyers. Each state has its own requirements, but the California bar exam, for example, has five hours dedicated to essay questions, a Performance Test that lasts an another hour and 30 minutes, and an additional portion of the exam that is typically around 200 multiple-choice questions. There are also additional certifications required just to qualify to take the exam.

Since this exam is extremely well known and notoriously stress-inducing, there are a number of excellent resources about how to manage the experience. Let's review a few of the common themes.1,2,3

- Take Care of Yourself
- Schedule and Plan Your Study
- Have a Growth Mindset

First and foremost, any learner can't be expected to perform as well if they are feeling too hungry, tired, or sick to keep pressing on. Managing stress can begin with simply being aware of what's happening with our physiological bodies. Lack of sleep and poor diet can put us at a disadvantage before we even start.

Positivity and optimism are also important factors. Making sure that we have things to look forward to - whether that is a study break or time with friends - can really help to fuel us when we're feeling discouraged with our studies. The reward can be as simple as a pleasant walk in nature or sitting down to watch a favorite TV show.

Second, creating a plan for ourselves is critical. We will describe this in more detail shortly.

Third, a growth mindset4 can be extremely powerful. Essentially, the growth mindset has to do with the belief in one's own potential. If a learner believes they have the potential to conquer a challenge, they will have a huge head start. Alternatively, if a learner assumes they will fail, it's not likely that they will accidentally succeed.

We previously mentioned the Try Harder mindset to describe resilience and persistence. The growth mindset might be better described as the "Not Yet Mindset." A learner who encounters some particularly difficult material in preparing for a tough, stressful exam is likely to feel as if they can't do the exercise or can't understand the concepts. If it ends there, the emotional impact of this sort of self-awareness can be devastating. Consider, on the other hand, that same learner with a Not Yet Mindset who thinks, for example, "I can't do the exercise yet", or "I can't understand the concepts yet."

The second learner in this example is still being honest about their understanding, but they are now opening the door to be successful in the future. This one small word can be incredibly powerful.

1(Kaplan, 2023), https://www.kaptest.com/study/bar/getting-mentally-prepared-for-the-bar/ ↩︎
2(Burgess, 2016), https://ms-jd.org/blog/article/dealing-with-bar-exam-stress-and-anxiety ↩︎
3(ABA Law learner Division, 2022), https://www.americanbar.org/groups/gpsolo/publications/gp_solo/2022/september-october/healthy-lifestyle-tips-lawyers-maintain-wellness-well-being/ ↩︎
4(Dweck, 2015), https://www.edweek.org/leadership/opinion-carol-dweck-revisits-the-growth-mindset/2015/09 ↩︎


## Knowing when you're ready

One of the most common questions that we receive regarding exams is, "How will I know when I'm ready?" Sometimes this question takes other forms, such as, "Do I need to do all of the exercises to prepare for the exam?" or "Can I prepare for the exam by completing a certain set or a certain number of machines on VulnHub?"

It's difficult to answer this question because each learner is different. One learner might have decades of professional experience and will only need a quick refresh of a Module or two in order to complete the exam. Another might be coming into the Module without much professional experience at all and will need to study a bit harder.

The quickest answer to this question then, is "it depends on the individual." Rather than leave it there, however, let's take a closer look at one specific piece of data that shows us a certain group of learners who have a clear advantage on the exam.

The following chart focuses on the OSCP certification. It shows a direct correlation between preparedness (working on more PEN-200 lab machines) and succeeding in the exam.

Figure 4: Lab Machine completeion contributing to success
Figure 4: Lab Machine completeion contributing to success

Perhaps not surprisingly, the more time spent preparing for the exam, the more likely a learner is to be successful. Unfortunately there is no shortcut here. As the saying goes, "preparation makes passing."


## Practical Advice for Exam takers

In general, we would advise two tactics for exam takers:

- Prepare for the exam
- Understand the exam

The first item, preparing for the exam, is tied to everything we've covered elsewhere in this Module. Each exam covers the content from the course, so it follows that reading the course materials, watching any videos, and doing exercises will all be incredibly helpful. Using effective learning strategies will also give learners an advantage.

Second, we recommend understanding the exam. The OffSec help site provides detailed descriptions of each exam, including what exam takers can expect and useful tips about how to approach enumeration tasks or submit proof that you were able to perform the required tasks. These exam descriptions are available alongside other course-specific help items.1

In addition to this particular resource, there are webinars,2 searchable blog posts, and YouTube videos of former learners reviewing their exam experiences. Heading into the exam with a clear understanding about what exactly it entails will not only reduce stress, but also improve performance.
1(OffSec, 2022), https://help.offsec.com/hc/en-us/categories/6965809783316-Course-Specific-Resources-for-Offsec-learners ↩︎
2(OffSec, 2022), https://www.youtube.com/watch?v=griDEeIcXQc ↩︎

# Practical Steps

We've covered a great deal in terms of abstract tactics and strategies. We're now ready to think practically and plan our approach to the coursework ahead.

This Learning Unit covers the following Learning Objectives:

  -  Create a long term strategy
  -  Understand how to use a time allotment strategy
  -  Learn how and when to narrow your focus
  -  Understand the importance of a group of co-learners and finding a community
  -  Explore how best to pay attention and capitalize on our own successful learning strategies

## Creating a Long Term Strategy 

Choosing a particular focus, Course, or Learning Path is a critical first step to creating a long term strategy. Having specific goals will help guide your decisions in terms of how much, when, and what Modules you choose to study.

It's entirely possible that a few weeks into this plan you will need to adjust it or change it, and that's fine. In fact, the best plans often need to be adjusted over time. The alternative - having no plan at all - would mean studying in an ad hoc manner, picking up (and putting down) materials whenever convenient.

Planning can also greatly reduce stress levels.1 In essence, planning helps us to create an idea of what will happen rather than allowing it to happen to us. This helps with feeling more in control of a situation and reduces anxiety.

Unfortunately, the saying, "failing to plan is planning to fail" is often true, and we can sometimes set ourselves up for a very emotionally taxing and stressful failure.

Let's spend a bit more time on what exactly that plan might look like.
1(Peláez, 2011): https://healthland.time.com/2011/05/31/study-25-of-happiness-depends-on-stress-management/ ↩︎


## Use Time Allotment Strategies 

Let's begin with when to study. As we've touched on a few times, one of the most impactful strategies is distributing study time over multiple sessions instead of cramming as much studying as possible into long sessions.

This strategy, called Spaced Practice,1 requires looking at a calendar, finding reasonable time slots, and sticking to a schedule. In addition to avoiding "marathon" sessions whenever possible, there are a few things to consider when choosing the best times to schedule studying.

Before exploring this more deeply, we need to acknowledge that many of our learners have jobs, families, and other events going on in their personal lives. When we suggest (as we will shortly) to study in the evenings, we don't want to assume that every learner can make this happen. It is merely something to take into consideration when planning.

Some research2 has suggested that before sleep might be a great time to study. The danger here is that it is quite easy to push back the bedtime to continue studying. Intuitively, we might think that we are being more productive by staying up later and studying more, but a lack of sleep3 can negatively impact our brain's ability to retain information. Planning study time also means planning an end to the studying.

If sleep is important for studying, a learner might correctly assume that exercise is as well.4 Intense physical activity increases blood to flow to the brain, and fires neurons in the hippocampus (the center for memory). In addition to generally improving brain health, exercising either before or after studying can be highly beneficial to improving memory and recall.5

1(Pan, 2022), https://psychology.ucsd.edu/undergraduate-program/undergraduate-resources/academic-writing-resources/effective-studying/spaced-practice.html ↩︎
2(Sandoiu, 2018), https://www.medicalnewstoday.com/articles/321161 ↩︎
3(Massachusetts Institute of Technology, 2019), https://www.sciencedaily.com/releases/2019/10/191001083956.htm ↩︎
4(Warner, 2006): https://www.webmd.com/diet/news/20061103/exercise-fights-fatigue-boosts-energy ↩︎
5(Rodriguez, 2015): https://www.scientificamerican.com/article/hit-the-gym-after-studying-to-boost-recall/ ↩︎


## Narrowing our Focus 

Now that we know to schedule study time on our calendar, let's consider how to organize our physical space. For quite some time, educational scientists have been trying to determine the ideal study space. One of the reasons there is no consensus is because the research1 seems to suggest that changing environments occasionally is good for us.

Maybe our study space is at the dining room table one week and a desk in a quiet corner of a library the next week. It's okay to move around a bit, but there are a few things we will need from this space, regardless of where it is and how often we return to it.

To that end, we need to address a significant problem: multitasking. Study after study has shown the negative impact that multitasking has on learning, job performance, and even brain health in general. Sometimes we feel like we can accomplish more by doing more things at once, but this simply isn't true.2,3,4,5

Creating a productive study space isn't just about only doing one thing at a time, but it's also about minimizing extra noise. Even though listening to music may not seem like much of a distraction at the time, processing this background noise still takes up a finite amount of mental space. Studies show that in general, listening to music - especially fast music with lyrics - while studying gets in the way of learning.6 However, there is some additional research that suggests certain types of music (slow, instrumental music, in particular), may be actually helpful to some.7

In cases where it is actually helpful, it's entirely possible that music is blocking out other, even more distracting sounds (a learner in a coffee shop may find it easier to focus with headphones that cancel out the surrounding conversations, for example). It's also reasonable to do what we can to make the study space one that we feel comfortable in and one that we enjoy spending time in.

More to the point, interruptions caused by phone alerts, text messages, emails, and individuals who might need our attention are another form of multitasking. Small habits, like putting your phone in airplane mode or choosing a relatively isolated place for study, can help sharpen focus.

1(Smith, Glenberg, and Bjork, 1978) https://link.springer.com/content/pdf/10.3758/BF03197465.pdf ↩︎
2(Junco and Cotten, 2012), https://www.sciencedirect.com/science/article/abs/pii/S036013151100340X ↩︎
3(Bradberry, 2014), https://www.forbes.com/sites/travisbradberry/2014/10/08/multitasking-damages-your-brain-and-career-new-studies-suggest/?sh=3cdbceba56ee ↩︎
4(Atchley, 2010), https://hbr.org/2010/12/you-cant-multi-task-so-stop-tr ↩︎
5(Hurt, 2021), https://www.discovermagazine.com/mind/why-multitasking-does-more-harm-than-good ↩︎
6(Busch, 2018), https://www.theguardian.com/teacher-network/2018/mar/14/sound-how-listening-music-hinders-learning-lessons-research ↩︎
7(Thompson, Schellenberg, Letnic, 2011), https://www.utm.utoronto.ca/~w3psygs/ThompsonEtAl2012.pdf ↩︎


## Pick a Strategy 

Let's refer back to the list of strategies presented in this Module, including the SQ3R method, The Feynman Technique, and Retrieval Practice.

As with choosing a time and a location, it's okay to change strategies mid-stream. It's also okay to come up with and iteratively improve on a pattern that works individually. In the case of OffSec materials, some learners may want to read first, then watch the videos, or vice versa. Some learners may want to preview the challenge exercises before reading the material. Others may want to follow along with the text on a local or virtual machine, moving one command at a time. The list of study methods included previously is not all-encompassing.

No matter which strategy we select, it's important to have a plan in place and actively think about it. It's very difficult to assess whether or not a strategy is successful without recognizing what that strategy actually is.

## Find a Community of Co-Learners 

Let's take a moment to talk about and acknowledge the positive power of community.

There are numerous benefits to studying as part of a community of learners,1 not least of which is the opportunity to develop an entirely new set of soft skills. Group work is often used by educators as a way to encourage learners to learn the social skills required in a collaborative environment. Even if one hopes to work as a sole-proprietor and not have any co-workers, the tools learned when working as part of a group can be immensely helpful to one's professional career.

In addition to social skills, there's a major benefit to being responsible for explaining ideas to co-learners who might be struggling. This is at the core of the Feynman Technique that we reviewed earlier.

Finally, there is something to be said for the camaraderie and the sheer enjoyment of being part of a group of co-learners, sharing the ups and downs of a course. A German proverb, "Geteiltes Leid ist halbes Leid", roughly translated means "A problem that is shared is half of a problem." In our case, sharing the struggle of a particular course, Module, Learning Unit, or even an exercise with another learner can help that struggle feel half as big as it was alone.

OffSec learners may want to reach out to local information security groups or coworkers to create their own study cohort. The OffSec Discord server also provides a way to collaborate and learn together with other learners across the globe.2 Discord participants also have access to course alumni, OffSec learner Mentors, and staff.

1(Washington University of St. Louis, 2020), https://ctl.wustl.edu/resources/benefits-of-group-work/ ↩︎
2(OffSec, 2022), https://offs.ec/discord ↩︎

## Study Your Own Studies 

Let's wrap up this Module by examining our responsibility not just for learning, but the assessment of that strategy. Since many of the details of how a "classroom" is constructed is up to you (the learner), you are also responsible for assessing and improving on that strategy.

While this might sound like a lot, let's review an easy and effective approach: at the end of a study session, take just 10 seconds to think about how well it went. It's a very small thing, but it can make a huge difference. To understand how, we'll look at the two most obvious and extreme outcomes of a study session.

If the study session was particularly difficult, this moment of self-reflection might lead you to think about some of the content that made it difficult. Generally speaking, we want to ask why it was difficult. The easy answer here might be "that SQL Injection is just tough!" but the difficulty of the material is at least somewhat out of our hands (though this might indicate a need to spend the next study session reviewing some more foundational materials).

We're specifically interested in the things that we, as learners, have some control over. Here is a list of potential questions to ask about the study session:

1. What time did I start the study session?
2. How long was the study session?
3. Did I get interrupted (if so, how did that happen)?
4. What did I do just before I started studying?
5. What did I eat or drink before I started studying?
6. What was my study location like? Was it quiet or busy?
7. What did I do during the study session specifically?

This is not a complete list of possible questions.

The answer to each of these things might lead us to locate a more specific point of frustration. For example, if we discover that a heavy meal immediately before a study session led to us feeling unproductive and sluggish, then we can adjust either when we study or how much we eat beforehand.

Let's consider the opposite scenario. Let's say that we finish a study session and we feel great about how it went. Again, it might be easy to say, "That went really well because I'm fascinated by SQL Injection," but we should think beyond the content itself.

In this case, the answers to these questions may reveal keys to future successful study sessions.

Let's say we studied for one hour in the morning after a light breakfast at the dining room table with a cup of coffee, using our own version of the Feynman Technique. If that led to a successful session, it's worth making a note of this and then planning the next study session to recreate as much of the scenario as possible.

Finally, as a closing note, we want to acknowledge that we can't possibly cover every effective strategy or give a full picture of all of the things involved in learning a new set of skills. We hope that the items presented in this Module are useful and helpful in some way.

If you are a learner just starting out with OffSec's training, we want to wish you the best of luck on your journey.


== END OF LINE == 