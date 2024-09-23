import logging

import day_2

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s'
)
_logger = logging.getLogger(__name__)


def main():
    try:
        box_ids = day_2.read_box_ids()
    except OSError:
        _logger.critical('Could not open or read the file containing the box IDs.')
        return

    equal_letters = day_2.find_box_ids_that_differ_by_one_letter(box_ids)
    if equal_letters:
        print(f'The common letters are: {equal_letters}.')
    else:
        print('No box ids found that only differ by one letter.')


if __name__ == '__main__':
    main()
