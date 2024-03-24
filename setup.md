---
title: Setup
questions:
- "What accounts do I need to perform my work on CMS?"
- "How do I obtain and install a grid certificate?"
- "Who can I contact if I need help with the pre-exercises?"
---

# Getting Help

## Mattermost (chat)

There is a dedicated Mattermost team, called [CMSDAS@CERN2024](https://mattermost.web.cern.ch/signup_user_complete/?id=yxyqcyputby3ig9rzxsqyjoi1e&md=link&sbr=su), setup to facilitate communication and discussions via live chat (which is also archived). The channel is hosted by the [CERN Mattermost instance](https://mattermost.web.cern.ch).

If you have never used Mattermost at CERN, please know that you will need your CERN login credentials (SSO) and you will need to join the private CMSDAS@CERN 2024 team in order to be able to see (or find using the search channels functionality) the channels setup for communications related to the school.

If you already have used Mattermost at CERN, please know that when you click direct links to channels (as you will find below) that are within the CMSDAS@CERN 2024 team, you **may** be redirected to the last Mattermost team you used. If this happens, remember to click the [signup link to join the CMSDAS@CERN 2024 team](https://mattermost.web.cern.ch/signup_user_complete/?id=yxyqcyputby3ig9rzxsqyjoi1e&md=link&sbr=su) to switch to the correct team from which you should be able to see the individual channels. If that still doesn't work, remove all cookies associated with cern.ch and restart your browser.

The [Pre-exercises channel](https://mattermost.web.cern.ch/cmsdascern2024/channels/pre-exercises) will be available once you join or switch to the CMSDAS@DAS 2024 team!
You can find it by clicking the plus symbol next to the team name, choosing "Browse Channels", and selecting "Pre-exercises". 

Note that you can access Mattermost via browser or you can download the corresponding application running standalone on your laptop or smartphone. You can find the installation instructions [here](https://docs.mattermost.com/install/desktop-app-install.html). The laptop application does not work with CERN certificate login. 

As you proceed with the pre-exercises, please don't hesitate to use this channel to have any questions or clarifications, or share useful tips with other participants!

## Support Email

For CMSDAS@CERN 2024, you may e-mail [cmsdas-cern-organizers@cern.ch](mailto:cmsdas-cern-organizers@cern.ch) with a detailed description of your problem. The instructors will be happy to help you.

# Setting Up Tools

If you have not used the Linux command line before, you may learn more at [WorkBookBasicLinux](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookBasicLinux).

## Obtain a Computer Account

To get a CERN account, please have a look at [Get Account at CERN](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookGetAccount). Obtaining a CERN account can be time-consuming and requires response from people at CERN during CERN business hours. CERN account application starts with the institutional team leader filling out a pre-registration form, so your institutional team leader also needs to be available for this task.

## Obtain a Grid Certificate and CMS VO Registration

A Grid Certificate and CMS Virtual Organization (VO) registration will be needed for the following sets of exercises. The registration process can be time-consuming (actions by several people are required), so it is important to start it as soon as possible. There are two main requirements which can be simply summarized: A certificate ensures that you are who you claim to be. A registration in the VO recognizes you (identified by your certificate) as a member of CMS. Both are needed to submit jobs to the grid and access files remotely using XRootD.

If you do not have a grid certificate or VO membership yet, please follow the instructions here: [Get Your Grid Certificate and CMSVO](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideLcgAccess#Getting_a_personal_certificate).

## Obtain a GitHub Account

Since 2013, most of the CMS software are hosted on [GitHub].  In short, Git is a distributed revision control system, and Github is a web-based Git repository hosting service. In your future analysis work, version control of your analysis code will become an important task and git will be a very useful tool. A small git tutorial is waiting for you in the [fifth exercise set]({{ page.root }}{% link _episodes/05-CMSDataAnalysisSchoolPreExerciseFifthSet.md %}).

In order to checkout and develop CMS software, you will need a github account, which is free.
  * In case you don’t have one already, simply go to [https://github.com/join](https://github.com/join) and follow the instructions to create a new account. Make sure you use a username people can recognize easily or to specify your real name.
  * In case you already have an account you can simply use the "[Sign in](https://github.com/login)" dialog and put your username and password.
  * Make sure you register your ssh key in [GitHub]. You can register more than one ssh key and it's usually a good idea to do so for every computer/cluster on which you regularly work (i.e. you laptop, CERN lxplus machines, your university cluster, etc.). You don't need to use an ssh-agent, but you can try if you want to. For more about ssh-agents, see [CMSGitTutorial#SSH_agent_in_logon_file](https://twiki.cern.ch/twiki/bin/view/CMSPublic/CMSGitTutorialPublic#SSH_agent_in_logon_file).
  * You will learn more about [GitHub] in the [fifth set of exercises]({{ page.root }}{% link _episodes/05-CMSDataAnalysisSchoolPreExerciseFifthSet.md %}).

## Install Docker

To install Docker Community Edition on your Linux, Mac, or Windows 10 (Pro, Enterprise, and Education) machine follow the [instructions in the Docker docs](https://docs.docker.com/get-docker/). If you are using Windows 10 Home you will need to follow [this Docker doc](https://docs.docker.com/docker-for-windows/install-windows-home/). Fair warning, the Windows 10 Home installation is more involved and requires Windows Subsystem for Linux 2 (WSL2), among other intricacies.

## Docker Hub

To sign up for Docker Hub, follow the instructions [here](https://hub.docker.com/signup).

## Some Windows Specific Tools

If you are using Microsoft Windows on your computer, consider installing [Cygwin](https://www.cygwin.com/) that provides Unix-like environment and command line interface.
More installation instructions e.g. [here](http://uscms.org/uscms_at_work/physics/computing/getstarted/uaf.shtml#windowsXServers).

If you would like to use Dockwe with cygwin, you will need to install [winpty](https://github.com/rprichard/winpty) and prefix your docker command like `winpty docker`.

You may also benefit from installing an SSH client, such as [PuTTY](https://www.putty.org/). More instructions to install and configure it  [here](http://uscms.org/uscms_at_work/physics/computing/getstarted/uaf.shtml#windowsKerberosPuTTY).

{% include links.md %}
