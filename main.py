from app.services.average_service import calculate_average
from app.utils.formatter import format_average


def main():
    values = [5, 4, 5, 3, 5]
    average = calculate_average(values)
    print(format_average(average))


if __name__ == "__main__":
    main()