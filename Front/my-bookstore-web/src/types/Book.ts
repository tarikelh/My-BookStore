import { Author } from "./Author";
import { BookType } from "./BookType";
import { Editor } from "./Editor";
import { Product } from "./Product";

export interface Book extends Product{
    isbn: string;
    editor: Editor;
    author: Author;
    type: BookType;
}