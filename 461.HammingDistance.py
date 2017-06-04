class Solution(object):
    def hammingDistance(self, x, y):
        """
            :type x: int
            :type y: int
            :rtype: int
            """
        x_bin = ""
        y_bin = ""
        while (1):
            if (x % 2 != 0):
                x_bin = "1" + x_bin
            else:
                x_bin = "0" + x_bin
            x = (int)(x / 2)
            if(x == 0):
                break;

        while (1):
            if (y % 2 != 0):
                y_bin = "1" + y_bin

            else:
                y_bin = "0" + y_bin
            y = (int) (y / 2)
            if (y == 0):
                break;

        x_bin_len = len(x_bin)
        y_bin_len = len(y_bin)

        new_len = 0
        if (x_bin_len < y_bin_len):
            while len(x_bin) % len(y_bin) != 0:
                x_bin = "0" + x_bin
            new_len = y_bin_len
        else:
            while len(y_bin) % len(x_bin) != 0:
                y_bin = "0" + y_bin
            new_len = x_bin_len

        count = 0
        number = 0
        while(number < new_len):
            #compare
            if (x_bin[number] != y_bin[number]):
                count += 1
            number = number + 1
        return count
