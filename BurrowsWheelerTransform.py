class BurrowsWheelerTransform:
    """Transforming a string using Burrows-Wheeler Transform"""

    def __init__(self):    
        pass
    def bwt(self,f):
        """Applies Burrows-Wheeler transform to input string.
        Args:
            f (File): The file object where each line is a '0' or '1'.

        Returns:
            string: transformed string

        """
        s = ""
        for line in f:
            s+=line.strip()
        table = sorted(s[i:] + s[:i] for i in range(len(s))) 
        last_column = [row[-1:] for row in table] 
        return "".join(last_column)

    def invbwt(self,f):
        """Applies inverse Burrows-Wheeler transform.
        Args:
            r (File): The file object where each line is a '0' or '1'.

        Returns:
            string: transformed string

        """
        r = ""
        for line in f:
            r+=line.strip()
        table = [""] * len(r)  # Make empty table
        for i in range(len(r)):
            table = sorted(r[i] + table[i] for i in range(len(r)))  # Add a column of r
        s = [row for row in table if row.endswith("\0")][0]  # Find the correct row (ending in "\0")
        return s.rstrip("\0")  # Get rid of trailing null character