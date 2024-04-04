# Name: Eva Deans

class ErrorDetection:

    def computeCheckSum(self, message, parity):
        '''
        Calculates and returns a new message with a specified parity.
        :param message: str: The input message to calculate the checksum.
        :param parity: int: The desired parity (0 or 1).
        :return: str: The new message with the calculated checksum.
        '''
        # turn the string of ASCII char (message) into int, create a list of the int
        int_lst = []

        for char in message:
            int_lst.append(ord(char))
        # for each int in list, count the number of 1's in binary
        for x in range(len(int_lst)):
            count = int.bit_count(int_lst[x])
            # if count % 2 != parity, set most significant bit to 1
            if count % 2 != parity:
                # set significant bit to 1
                mask = 1 << 7
                int_lst[x] |= mask

        # make new str
        new_str = "".join(chr(x) for x in int_lst)
        return new_str



    def verifyCheckSum(self, message, parity):
        '''
        Verifies the checksum in the given message and returns a tuple indicating
        the error status and the corrected message.
        :param message: str: The input message to verify the checksum.
        :param parity: int: The expected parity (0 or 1).
        :return: tuple[bool, str]: A tuple containing a boolean indicating the error status
        and the corrected message.
        '''
        # turn the string of ASCII char (message) into int, create a list of the int
        int_lst = []
        # error flag
        error = False
        for char in message:
            int_lst.append(ord(char))
        # for int in list
        for x in range(len(int_lst)):
            # count 1s
            count = int.bit_count(int_lst[x])
            # if count % 2 not equal to parity raise flag
            if count % 2 != parity:
                error = True
            # set sig bit to 0
            mask = 255 - (1 << 7)
            int_lst[x] &= mask

        new_str = "".join(chr(x) for x in int_lst)
        return error, new_str



