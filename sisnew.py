import requests
from lxml import html

req = requests.session()
def logindetails():
    #Taking Username and Splitting it
    username = input("Enter Your Username: ").upper()
    username = username.split("-")
    session = username[0]
    programme = username[1]
    rollno = username[2]
    password = input("Enter Your Password: ")
    loginrequest(session,programme,rollno,password) #CALLING FOR POST REQUEST

#=============================================================
def loginrequest(session,programme,rollno,password):
    url = "https://sis.cuonlineatd.edu.pk/login.aspx"
    print("\n|#| ==> SENDING LOGIN REQUEST TO CUONLINE FOR ABBOTTABAD")
    postlogin = "https://sis.cuonlineatd.edu.pk/DashBoard.aspx"

    #GETTING FORM READY, HIDDEN FIELDS ARE STATIC SO!
    payload = {"__EVENTTARGET=":"",
               "__EVENTARGUMENT":"",
               "__VIEWSTATE":"/wEPDwUILTI4Mzk1MDAPZBYCZg9kFggCAQ8PFgIeCEltYWdlVXJsBSAuLi9yZXNvdXJjZXMvaW1hZ2VzL2xvZ29BYmJ0LnBuZ2RkAgcPEA8WBh4NRGF0YVRleHRGaWVsZAUKU2hvcnRfTmFtZR4ORGF0YVZhbHVlRmllbGQFClNob3J0X05hbWUeC18hRGF0YUJvdW5kZxYCHghvbkNoYW5nZQUOdXBkYXRlRGV0YWlsKCkQFSIERkEwMQRGQTAyBEZBMDMERkEwNARGQTA1BEZBMDYERkEwNwRGQTA4BEZBMDkERkExMARGQTExBEZBMTIERkExMwRGQTE0BEZBMTUERkExNgRGQTE3BFNQMDIEU1AwMwRTUDA0BFNQMDUEU1AwNgRTUDA3BFNQMDgEU1AwOQRTUDEwBFNQMTEEU1AxMgRTUDEzBFNQMTQEU1AxNQRTUDE2BFNQMTcEU1AxOBUiBEZBMDEERkEwMgRGQTAzBEZBMDQERkEwNQRGQTA2BEZBMDcERkEwOARGQTA5BEZBMTAERkExMQRGQTEyBEZBMTMERkExNARGQTE1BEZBMTYERkExNwRTUDAyBFNQMDMEU1AwNARTUDA1BFNQMDYEU1AwNwRTUDA4BFNQMDkEU1AxMARTUDExBFNQMTIEU1AxMwRTUDE0BFNQMTUEU1AxNgRTUDE3BFNQMTgUKwMiZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAgkPEA8WBh8BBQROYW1lHwIFBE5hbWUfA2cWAh8EBQ51cGRhdGVEZXRhaWwoKRAVUANCQkEDQkJTA0JDRQNCQ1MDQkNWA0JEUwNCRUMDQkVFA0JFUwNCSVQHQlMgKENFKQdCUyAoQ0UpA0JTRQNCU1MDQlROA0JUWQNDVkUERUNFMQNFRUUDRVBFA0VSUwNIVU0DTUJBA01CTwNNQ1MDTURTA01FUwNNSVQGTVMoQ0UpA1BCVANQQ00DUENTA1BEUwNQRUUDUEVTA1BITQNQTVMDUFBZA1IwMANSMDEDUjAyA1IwMwNSMDQDUjA1A1IwNgNSMDcDUjA4A1IwOQNSMTADUjExA1IxMgNSMTMDUjE0A1IxNQNSMTYDUjE3A1I2MANSNjEDUjYyA1I2NANSNjUDUjY2A1I2NwNSNzADUkJGA1JCVANSQ0UDUkNNA1JDUANSQ1MDUkRTA1JFQwNSRUUDUkVOA1JFUwNSTVMDUk1UA1JQTQNSUFkDUlNXFVADQkJBA0JCUwNCQ0UDQkNTA0JDVgNCRFMDQkVDA0JFRQNCRVMDQklUB0JTIChDRSkHQlMgKENFKQNCU0UDQlNTA0JUTgNCVFkDQ1ZFBEVDRTEDRUVFA0VQRQNFUlMDSFVNA01CQQNNQk8DTUNTA01EUwNNRVMDTUlUBk1TKENFKQNQQlQDUENNA1BDUwNQRFMDUEVFA1BFUwNQSE0DUE1TA1BQWQNSMDADUjAxA1IwMgNSMDMDUjA0A1IwNQNSMDYDUjA3A1IwOANSMDkDUjEwA1IxMQNSMTIDUjEzA1IxNANSMTUDUjE2A1IxNwNSNjADUjYxA1I2MgNSNjQDUjY1A1I2NgNSNjcDUjcwA1JCRgNSQlQDUkNFA1JDTQNSQ1ADUkNTA1JEUwNSRUMDUkVFA1JFTgNSRVMDUk1TA1JNVANSUE0DUlBZA1JTVxQrA1BnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAgsPD2QWAh4Hb25LZXlVcAUOdXBkYXRlRGV0YWlsKClkZHQ3a83syJDjxRhdcQ8RpOZqxCyi",
               "__VIEWSTATEGENERATOR":"C2EE9ABB",
               "__EVENTVALIDATION":"/wEWdwLglunyAQKwrt/4BQKwrsuFDAKwrueuBwKwrpPLDwKwro+UBgKwrruxCQKwrtfdAQKwroO1BwKwrr/eDwLLmI3JCALLmLmSAwLLmNW+CgLLmMHbAgLLmP3kBQLLmOmBDALLmIWqBwLLmLH3DwLDr4+CDALDr7uvBwLDr9fLDwLDr8OUBgLDr/+xCQLDr+vaAQLDr8e1BwLDr/PeDwLmmMHJCALmmP2SAwLmmOm/CgLmmIXYAgLmmLHlBQLmmK2ODALmmNmqBwLmmPX3DwLmmKGvDQK6gNLdBQKwwaz3BwKW68f2DAKwwaj3BwLjhoa3BQKwwaT3BwLAvoKrAQKW67/xDAKwwaD3BwLd6PLpCQLlhJTgBwLlhJTgBwKW64f2DAKwwej0BwLLzKydBAKC7b7DCQKX6/v2DAKV6/OEAQKV67/xDAKV65P2DAK/wez0BwLYpY2oAgKxgNLdBQLr05b2CQK3waj3BwK3waT3BwK3waD3BwLQ6PLpCQLJxKnmAQLP6M7pCQLQpdWoAgKiwaj3BwKiwaT3BwK467/xDAKiwaD3BwLQpYGoAgKiwcD0BwK07c7ACQKRmM7IBgK6r+i9CAKntoqWAgLA3aWLBALt5Mf9CQKWiuHWAwKzkYPLBQLcuJ28DwKp0t3iBwLS+f/XCQKRmMrIBgK6r+S9CAKntoaWAgLA3aGLBALt5MP9CQKWit3WAwKzkf/LBQLcuJm8DwKRmLbLBgK6r9C9CAKntvKWAgLt5K/8CQKWisnWAwKzkevLBQLcuIW8DwKRmLLLBgKj8uXrBgLN6M7pCQKG68f2DALepdWoAgLxjdG0BgKgwaj3BwKgwaT3BwLwvoKrAQKG67/xDAL7zOidBAKgwaD3BwKgwcD0BwLN6OLpCQLepaGoAgKy7c7ACQK8rOCpDwLgg8X7CQLS9cL8AgLOlouGBgLrpvP/BrsAfEWjf8bVrrCCbA11ezQB4pae",
               "ddl_Session":session,
               "ddl_Program":programme,
               "txt_RollNo":rollno,
               "txt_Password":password,
               "btn_StudentSignIn":"Sign In"}

    result = req.post(url=url,data=payload)
    if (result.history == 302 or result.url == postlogin):
        print("\n|#| ==> LOGIN IS SUCCESSFUL")
        print("\n|#| ==> GETTING YOUR BASIC DETAILS")
        basicdetails(result)
    else:
        print("\n|#| ==> LOGIN IS NOT SUCCESSFUL")

#======================================================================
def basicdetails(result):
    summary_url = "https://sis.cuonlineatd.edu.pk/Summary.aspx"
    result = req.get(summary_url)

    tree = html.fromstring(result.text)
    name = tree.xpath('.//span[@id="ctl00_lbl_Name"]/text()')
    rollno = tree.xpath('.//span[@id="ctl00_lbl_RollNo"]/text()')
    advisor = tree.xpath('.//span[@id="ctl00_lblStuAdv"]/text()')
    section = tree.xpath('.//span[@id="ctl00_lbl_CurrentSection"]/text()')
    registeredcourses = tree.xpath('.//span[@id="ctl00_lbl_RegisteredCourses"]/text()')
#PRINTING STUDENTS DETAILS
    print(str(" +--------------------------+ " +
          "\n Student Name: " + name[0] +
          "\n Roll No: " + rollno[0] +
          "\n Section: " + section[0] +
          "\n Registered Courses: " + registeredcourses[0] +
          "\n Current Advisor: "+ advisor[0] +
          "\n +--------------------------+"))
    course_data(result,tree,registeredcourses)

def course_data(result, tree, registeredcourses):
#PRINTING COURSES DETAILS AND EXTRA
    print("|$| COURSES REGISTERED ARE: \n")
    course = []
    teacher = []
    classes = []
    for i in range(0,int(registeredcourses[0])):
        course += tree.xpath('.//a[@id="ctl00_DataContent_gvCourseSummary_ctl0%d_lbCourse"]/text()'%(i+2))
        teacher += tree.xpath('.//span[@id="ctl00_DataContent_gvCourseSummary_ctl0%d_lbFaculty"]/text()'%(i+2))
        classes += tree.xpath('.//span[@id="ctl00_DataContent_gvCourseSummary_ctl0%d_lbClass"]/text()'%(i+2))
        print(str((i+1)) + ") " + course[i] + "\n \t FACULTY: " + teacher[i]+ "\n \t CLASS: " + classes[i])
    print(" +--------------------------------------+")
    scholorships()

def scholorships():
    scholorship_url = "https://sis.cuonlineatd.edu.pk/scholarship/ViewScholarshipFormLinks.aspx"
    result = req.get(scholorship_url)
    tree = html.fromstring(result.text)
    i = True
    loop = 2
    scholorshipnew = []
    print("+=========================+\n |$| AVAILIBLE SCHOLORSHIPS: \n")
    while(i==True):
        scholorship = tree.xpath('.//a[@id="ctl00_DataContent_gvschlinks_ctl0%d_SchEntryFormLink"]/text()' %(loop))
        if(len(scholorship) == 0):
            i = False;
        else:
            scholorshipnew += scholorship[loop-2]
            loop = loop+1
            print(scholorship[0])


logindetails()

