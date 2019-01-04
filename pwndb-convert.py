import sys

with open(sys.argv[1]) as fp:
 line = fp.readline().strip()
 start = 0
 user = ""
 domain = ""
 password = ""
 while line:

  if "[luser]" in line:
	start = 1
  	user = line.split("=> ")[1]

  if "[domain]" in line:
  	if start == 1:
  		domain = line.split("=> ")[1]
  		start = 2

  if "[password]" in line:
   if start == 2:
   	password = line.split("=> ")[1]
	print user.strip() + "@" + domain.strip() + ":" + password.strip()
	start = 0
	user = ""

#  print line
  line = fp.readline()
