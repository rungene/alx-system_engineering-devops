# 0x04. Loops, conditions and parsing

<span style="color: red"> DevOps Shell Bash Scripting  </span>

# About Bash projects 

Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.

## Background Context


## Resources

**Read or watch:**

	- [Loops sample](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html)
	- [Variable assignment and arithmetic](https://tldp.org/LDP/abs/html/ops.html)
	- [Comparison operators](https://tldp.org/LDP/abs/html/comparison-ops.html)
	- [File test operators](https://tldp.org/LDP/abs/html/fto.html)
	- [Make your scripts portable](https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html)


**man or help:**

	- env
	- cut
	- for
	- while
	- until
	- if

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google:

### General

	- How to create SSH keys
	- What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
	- How to use while, until and for loops
	- How to use if, else, elif and case condition statements
	- How to use the cut command
	- What are files and other comparison operators, and how to use them

## Requirements

	- Allowed editors: vi, vim, emacs
	- All your files will be interpreted on Ubuntu 20.04 LTS
	- All your files should end with a new line
	- A README.md file, at the root of the folder of the project, is mandatory
	- All your Bash script files must be executable
	- You are not allowed to use awk
	- Your Bash script must pass Shellcheck (version 0.7.0) without any error
	- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
	- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Copyright - Plagiarism

	- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
	- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. 
	- You are not allowed to publish any content of this project.
	- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## More Info

## Shellcheck

[Shellcheck](https://github.com/koalaman/shellcheck) is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. Shellcheck is your friend! All your Bash scripts must pass Shellcheck without any error or you will not get any points on the task.

Shellcheck is available on the school’s computers. If you want to use it on your own computer, here is how to [install it](https://github.com/koalaman/shellcheck#installing).

Examples:

Not passing Shellcheck:

![Not passing Shellcheck](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/Vxotqyj.png)


Passing Shellcheck:

![Passing Shellcheck:](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/ubHWxDU.png)

For every feedback, Shellcheck will provide a code that you can use to get more information about the issue, for example for code SC2034, you can browse https://github.com/koalaman/shellcheck/wiki/SC2034.

## Tasks

**0. Create a SSH RSA key pair**

Read for this task:
	
	- [Linux and Mac OS users](https://askubuntu.com/questions/61557/how-do-i-set-up-ssh-authentication-keys)
	- [Windows users](https://docs.rackspace.com/support/how-to/generating-rsa-keys-with-ssh-puttygen/)

man: ssh-keygen

You will soon have to manage your own servers concept page hosted on remote [data centers](https://www.youtube.com/watch?v=iuqXFC_qIvA&t=46s). We need to set them up with your RSA public key so that you can access them via SSH.

Create a RSA key pair.

Requirements:

	- Share your public key in your answer file 0-RSA_public_key.pub
	- Fill the SSH public key field of your [intranet profile](https://intranet.alxswe.com/users/my_profile) with the public key you just generated
	- **Keep the private key to yourself in a secure location**, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
	- If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase

SSH and RSA keys will be covered in depth in a later project.

**1. For Best School loop**

Write a Bash script that displays Best School 10 times.

Requirement:

	- You must use the for loop (while and until are forbidden)

Note that: 

	- The first line of my Bash script starts with #!/usr/bin/env bash
	- The second line of my Bash scripts is a comment explaining what it is doing

**2. While Best School loop**

Write a Bash script that displays Best School 10 times.

Requirements:

	- You must use the while loop (for and until are forbidden)

**3. Until Best School loop**

Write a Bash script that displays Best School 10 times.

Requirements:

	- You must use the until loop (for and while are forbidden)

**4. If 9, say Hi!**

Write a Bash script that displays Best School 10 times, but for the 9th iteration, displays Best School and then Hi on a new line.

Requirements:

	- You must use the while loop (for and until are forbidden)
	- You must use the if statement

**5. 4 bad luck, 8 is your chance**

Write a Bash script that loops from 1 to 10 and:

	- displays bad luck for the 4th loop iteration
	- displays good luck for the 8th loop iteration
	- displays Best School for the other iterations

Requirements:

	- You must use the while loop (for and until are forbidden)
	- You must use the if, elif and else statements

**6. Superstitious numbers**

Write a Bash script that displays numbers from 1 to 20 and:

	- displays 4 and then bad luck from China for the 4th loop iteration
	- displays 9 and then bad luck from Japan for the 9th loop iteration
	- displays 17 and then bad luck from Italy for the 17th loop iteration

Requirements:

	- You must use the while loop (for and until are forbidden)
	- You must use the case statement

**7. Clock**

Write a Bash script that displays the time for 12 hours and 59 minutes:

	- display hours from 0 to 12
	- display minutes from 1 to 59

Requirements:

	- You must use the while loop (for and until are forbidden)

Note that in this example, we only display the first 70 lines using the head command.