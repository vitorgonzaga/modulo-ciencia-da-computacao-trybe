import csv
import json


def retrieve_books(file):
    # return [json.loads(line) for line in file] # this line doesn't work
    return json.load(file)


def count_books_by_categories(books):
    categories = {}
    for book in books:
        for category in book["categories"]:
            if not categories.get(category):  # feed a dict with unique values
                categories[
                    category
                ] = 0  # if category not exists in dict the value starts with 0
            categories[
                category
            ] += 1  # if category already exists in dict plus 1
    return categories  # dict with only unique values


def calculate_porcentage_by_category(book_count_by_category, total_books):
    return [
        [category, num_books / total_books]
        for category, num_books in book_count_by_category.items()  # returns a dict_items object -> list with tuples (category, num_books)
    ]


def write_csv_report(file, header, rows):
    writer = csv.writer(file)  # create the file
    writer.writerow(header)  # add the header (expect receive a list)
    writer.writerows(rows)  # add rows (expect receive a list)


if __name__ == "__main__":
    # retrieve books
    with open("books.json") as file:
        books = retrieve_books(file)

    # count by category
    book_count_by_category = count_books_by_categories(books)

    # calculate porcentage
    number_of_books = len(books)
    books_percentage_rows = calculate_porcentage_by_category(
        book_count_by_category, number_of_books
    )

    # write csv
    header = ["categoria", "porcentagem"]
    with open(
        "report.csv", "w"
    ) as file:  # informando um nome que não existe ele cria o arquivo
        write_csv_report(file, header, books_percentage_rows)
