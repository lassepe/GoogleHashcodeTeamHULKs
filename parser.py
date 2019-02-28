from picture import Picture

class IO:
    """Handles file IO"""

    def __init__(self):
        """Constructor for io"""

    def _read_file_line_by_line(self, filepath):
        """
        Read file line by line
        :param filepath:
        :return: List of all lines
        """
        with open(filepath) as f:
            content = f.readlines()

        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]

        return content

    def load_data(self, filepath):
        """
        Loads data from file and return it in a structured manner
        :param filepath:
        :return:
        """
        raw = self._read_file_line_by_line(filepath)
        data = {}
        # read number of pictures
        data['N'] = int(raw[0])
        #del 1st row
        raw = raw[1:]
        pictures = []
        for i, picture in enumerate(raw[1:]):
            # for all following lines
            row = list(raw[i].split())
            isHorizontal = bool(row[0] == 'H')
            tag_list = []
            for tag in row[2:]:
                tag_list.append(tag)
            # create picture and append it
            pictures.append(Picture(i, isHorizontal, tag_list))


        data['pictures'] = pictures
        return pictures
        #return data