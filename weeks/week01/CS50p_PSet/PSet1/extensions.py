# Question -------------------------------------------------------------------------------------------------------------

# Implement a program that prompts the user for the name of a file and then outputs that file’s media type 
# if the file’s name ends, case-insensitively, in any of these suffixes:
# .gif, .jpg, .jpeg, .png, .pdf, .txt, .zip
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, 
# which is a common default.


### Solution ###

# Prompts user for the name of a file
file_name = input('File name: ').lower().strip()

# Check file type
if '.gif' in file_name:
# Output file media type
    print('image/gif')

# Check file type
elif '.jpg' in file_name:
# Output file media type
    print('image/jpeg')

# Check file type
elif '.jpeg' in file_name:
# Output file media type
    print('image/jpeg')

# Check file type
elif '.png' in file_name:
# Output file media type
    print('image/png')

# Check file type
elif '.pdf' in file_name:
# Output file media type
    print('application/pdf')

# Check file type
elif '.txt' in file_name:
# Output file media type
    print('text/plain')

# Check file type
elif '.zip' in file_name:
# Output file media type
    print('application/zip')

else:
    print('application/octet-stream')
