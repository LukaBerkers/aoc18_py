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

    counts = day_2.count_box_ids_containing_a_letter_two_and_three_times(box_ids)
    id_has_a_letter_two_times_count, id_has_a_letter_three_times_count = counts
    _logger.info(
        f'Number of IDs containing a letter twice: {id_has_a_letter_two_times_count}'
    )
    _logger.info(
        f'Number of IDs containing a letter three times: {id_has_a_letter_three_times_count}'
    )
    print(f'Checksum: {id_has_a_letter_two_times_count * id_has_a_letter_three_times_count}')


if __name__ == '__main__':
    main()
