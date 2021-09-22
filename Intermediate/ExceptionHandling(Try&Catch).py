import sys

def assertion_Error():
    assert ('linux' in sys.platform), "This code run only on linux operating system"


# try:
#     assertion_Error()
# except:
#     print("your are on an windows platform")
#
# try:
#     assertion_Error()
# except AssertionError as error:
#     print(error)
#     print("The linux function is  not executable on windows system")

# try:
#     with open ('file.log') as file:
#         read_data = file.read()
# except:
#     print('could not open file.log')


try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)

finally:
    print('Cleaning up, irrespective of any exceptions.')