# Name: PUT YOUR NAME HERE


import math
import random
import copy

class ErrorCorrection:
    def __init__(self, m, r):
        '''
        This is the constructor
        :param m: int: Number of message bits
        :param r: int: Number of check bits
        '''

        self.__m = m
        self.__r = r
    def prepareMessage(self, message):
        asciiCode = ord(message)
        codeword = []

        # Convert the Ascii code of the message to a list of zeros and ones.

        # This will only work if we have atmost 7 significant bits (i.e. the
        # message is in the ASCII table and least than 128).
        for bitNum in range(7):
            # Because we are inserting, we will have the most significant bit be in
            # position 0, but that's ok as long as we convert it back to ascii in
            # the same order.
            codeword.insert(0, asciiCode % 2) # Insert the least significant bit.
            asciiCode = asciiCode >> 1         # Shift the bits
            bitNum += 1

        # Put a None in position zero so that the bits start numbering at 1 instead of 0.
        codeword.insert(0, None)

        # Add the checkbits at the positions of powers of two.
        checkBitNum = 1
        for i in range(self.__r):
            codeword.insert(checkBitNum, 0)
            checkBitNum = checkBitNum << 1
        return codeword
    def extractMessage(self, codeword):
        asciiCode = 0

        # Remove the checkbits at the positions of powers of two.
        # We need to go backwards so that the indexes don't get off.
        # If we delete index 1, then index 2 will become the new 1.
        # But if we go backward, e.g. delete index 8, then index 2
        # is still the same one.
        checkBitNum = 1 << (self.__r - 1)
        while checkBitNum > 0:
            del codeword[checkBitNum]
            checkBitNum = checkBitNum >> 1

        # delete the None that was put into position 0.
        del codeword[checkBitNum]

        # Convert the list back to an integer
        for i in range(len(codeword)):
            asciiCode = asciiCode * 2 + codeword[i]

        # Finally, return the character
        return chr(asciiCode)

    def encodeMessage(self, message, parity):
        """
        Encode the message using Hamming code.

        :param message: str: The ASCII character to be encoded
        :param parity: int: Parity (0 for even, 1 for odd)
        :return: list: The encoded message with check bits
        """

        def flip(num):
            """
            Flips a 1 to 0, or vice versa.
            :param num: int: A 1 or 0
            :return: int: A 1 or 0
            """
            if num == 0:
                num = 1
            else:
                num = 0
            return num

        # use prepareMessage to turn message into list
        full = self.prepareMessage(message)

        # compute checkbits
        bitOne = (full[3] + full[5] + full[7] + full[9] + full[11]) % 2
        bitTwo = (full[3] + full[6] + full[7] + full[10] + full[11]) % 2
        bitFour = (full[5] + full[6] + full[7]) % 2
        bitEight = (full[9] + full[10] + full[11]) % 2

        # check parity and assign the bits
        if parity == 0:
            full[1] = bitOne
            full[2] = bitTwo
            full[4] = bitFour
            full[8] = bitEight
        elif parity == 1:
            full[1] = flip(bitOne)
            full[2] = flip(bitTwo)
            full[4] = flip(bitFour)
            full[8] = flip(bitEight)

        # return list
        return full


    def correctMessage(self, codeword, parity):
        """
        Correct 1-bit errors using Hamming code.

        :param message: list: A list of 1's and 0's
        :param parity: int: Parity (0 for even, 1 for odd)
        :return: str: The corrected message
        """

        wrong = []

        # compute proper checkbits
        bitOne = (codeword[1] + codeword[3] + codeword[5] + codeword[7] + codeword[9] + codeword[11]) % 2
        bitTwo = (codeword[2] + codeword[3] + codeword[6] + codeword[7] + codeword[10] + codeword[11]) % 2
        bitFour = (codeword[4] + codeword[5] + codeword[6] + codeword[7]) % 2
        bitEight = (codeword[8] + codeword[9] + codeword[10] + codeword[11]) % 2

        # check parity and find incorrect bit
        if bitOne != parity:
            wrong.append(1)
        if bitTwo != parity:
            wrong.append(2)
        if bitFour != parity:
            wrong.append(4)
        if bitEight != parity:
            wrong.append(8)
        wrongBit = sum(wrong)

        # fix wrong bit
        if wrongBit > 0:
            codeword[wrongBit] = 1 - codeword[wrongBit]

        # return fixed message
        fixedMessage = self.extractMessage(codeword)
        return fixedMessage
