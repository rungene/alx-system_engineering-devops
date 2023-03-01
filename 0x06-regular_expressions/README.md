# 0x06. Regular expression

<span style="color: red"> Regex DevOps </span>

```
Concepts
```
For this project, we expect you to look at this concept:

	- [Regular Expression](https://intranet.alxswe.com/concepts/29)

## Background Context

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```
## Resources

**Read or watch:**

	- [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
	- [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
	- [Rubular is your best friend](https://rubular.com/)
	- [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
	- [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)


## Requirements

### General

	- Allowed editors: vi, vim, emacs
	- All your files will be interpreted on Ubuntu 20.04 LTS
	- All your files should end with a new line
	- A README.md file, at the root of the folder of the project, is mandatory
	- All your Bash script files must be executable
	- The first line of all your Bash scripts should be exactly #!/usr/bin/env ruby
	- All your regex must be built for the Oniguruma library

## Tasks

```
0. Simply matching School 
```

![The regular expression must match Schoo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/ec65557f0da1fbfbff6659413885e4d4822f5b1d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230228%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230228T180029Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a90cffa5818324128bd893fa90e590803f61443fcbb8e9a91977107dce4bd905)

Requirements:

	- The regular expression must match School
	- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:

```
sylvain@ubuntu$ ./0-simply_match_school.rb School | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "Best School" | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$
sylvain@ubuntu$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
$
```

Repo:

	- GitHub repository: alx-system_engineering-devops
	- Directory: 0x06-regular_expressions
	- File: 0-simply_match_school.rb

```
1. Repetition Token #0 
```

![regular expression](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230228%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230228T180029Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=934f556958b77060c4b5f75cbc2bc50e2463104a785b1901dc61910e686fc495)

Requirements:

	- Find the regular expression that will match the above cases
	- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method


Repo:
	
	- GitHub repository: alx-system_engineering-devops
	- Directory: 0x06-regular_expressions
	- File: 1-repetition_token_0.rb
