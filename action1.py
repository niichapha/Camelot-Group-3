def check_for_success(command):

    # Keep getting responses until the success of fail the given command is received
    while True:

        # Get response from Camelot
        received = input()

        # Return True if success response, else false for fail response
        if received == 'succeeded ' + command:
            return True
        elif received.startswith('failed ' + command):
            return False
        elif received.startswith('error ' + command):
            return False

def action(command, wait=True):
    # Format command
    print('start ' + command)
    if wait==True:
        # Call function to check for its success
        return check_for_success(command)
    else:
        return True

