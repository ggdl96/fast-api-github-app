from core.constants.base_config import settings


def read_private_key():
    # Open the file and read its content.
    with open(settings.GITHUB_PRIVATE_KEY) as private_file:
        content = private_file.readlines()

        # Display the file's content line by line.
        for line in content:
            print(line, end="")
        
        private_file.close()
