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


