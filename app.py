from RandomAccount import randomacc
from input import inputtogoogle

####input your acc you want info######
youraccusername = "simon"
yourpasswd      = "simon"
yourlastname    = "lee"
yourfristName   = "simon"
yourphonenum    = "123456789"
year            = ""
day             = ""
month           = ""
gender          = ""
yourdriver      = "C:\\Users\\simon\\Desktop\\app\\my_python_app\\GoogleAccountCreater\\geckodriver-v0.31.0-win64\\geckodriver.exe"
######################################


#rng acc
rngaccinfo = randomacc(youraccusername, yourpasswd)

username = rngaccinfo.randomusernamea()
passwd   = rngaccinfo.randompasswda()
print("username: " + username )
print("passwd: "   + passwd   )
#input
inputtogoogle.runweb(yourdriver, username, passwd, yourlastname, yourfristName, yourphonenum, year, day, month, gender)




