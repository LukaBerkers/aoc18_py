import day_1


def main():
    frequency_changes = day_1.read_frequency_changes()
    final_frequency = day_1.apply_frequency_changes(frequency_changes)
    print(final_frequency)


if __name__ == '__main__':
    main()
