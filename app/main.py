from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serialize import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        match cmd:
            case "print":
                match method_type:
                    case "console":
                        ConsolePrint().print(book)
                    case "reverse":
                        ReversePrint().print(book)
            case "display":
                match method_type:
                    case "console":
                        ConsoleDisplay().display(book)
                    case "reverse":
                        ReverseDisplay().display(book)
            case "serialize":
                match method_type:
                    case "json":
                        return JSONSerializer().serialize(book)
                    case "xml":
                        return XMLSerializer().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
