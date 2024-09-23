import logging

import day_1

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s')
logger = logging.getLogger(__name__)


def main():
    try:
        frequency_changes = day_1.read_frequency_changes()
    except OSError:
        logger.critical('Could not read the file of frequency changes.')
        return

    first_repeated_frequency = day_1.find_first_repeated_frequency(frequency_changes)
    print(first_repeated_frequency)


if __name__ == '__main__':
    main()
