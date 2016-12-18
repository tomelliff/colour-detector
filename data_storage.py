class DataStorage(object):
    """
    Store RGB values against product code and retrieve product codes for
    given RGB values.
    """
    def _format_rgb_values(self, rgb_values):
        for rgb_value in rgb_values:
            return ''.join([self._zero_pad_number(v) for v in rgb_values])

    def _zero_pad_number(self, number, length=3):
        return str(number).zfill(length)

    def store_rgb_for_product(self, rgb, product_code):
        """
        Store the RGB values against the product code.
        For now this is just a flat CSV file.
        """

        rgb_values = self._format_rgb_values(rgb)
        with open('database.txt', 'a') as database:
            database.write('{},{}\n'.format(rgb_values, product_code))

    def get_product_for_rgb(self, rgb):
        """
        Get the product code for an inputted RGB tuple.
        For now this is just from a flat CSV file.
        """

        rgb_values = self._format_rgb_values(rgb)
        with open('database.txt', 'r') as database:
            lines = [line.rstrip('\n') for line in database.readlines()]
            for line in lines:
                if line.startswith(rgb_values):
                    return line.split(',')[1]
