class TextReader:
    INSTANCE = None

    def __new__(cls, val):
        if TextReader.__instance is None:
            TextReader.__instance = object.__new__(cls)
        TextReader.__instance.val = val
        return TextReader.INSTANCE

    def get_commands_from_file(self, file_name):
        commands = []
        file = open(file_name, 'r')
        for line in file:
            commands.append(line)
        file.close()
        return commands
