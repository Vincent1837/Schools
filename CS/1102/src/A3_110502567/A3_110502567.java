/**
 * Assignment 3
 * Student Number: 110502567
 * Course: CE_1002
 */
package A3_110502567;

import java.util.Vector;

public class A3_110502567 {
    //Book1 information
    static private String N1="book1";
    static private String iSBN1="978-3-14-131238-2";
    static Vector<String> CONTENT1= new Vector<>();

    //Book2 information
    static private String N2="book2";
    static private String iSBN2="278-33-4-133238-0";
    static Vector<String> CONTENT2= new Vector<>();

    public static void main (String[] args) {
        CONTENT1.add("book1p1");
        CONTENT1.add("book1p2");
        CONTENT1.add("book1p3");

        CONTENT2.add("book2p1");
        CONTENT2.add("book2p2");

        Book myBook1 = new Book(N1, iSBN1, CONTENT1);
        Book myBook2 = new Book(N2, iSBN2, CONTENT2);

        //Testing
        System.out.println(myBook1.getName() + " " + myBook1.getISBN());
        System.out.println(myBook2.getName() + " " + myBook2.getISBN());
        System.out.println(myBook1.getContent(0) + " " + myBook1.getContent(3));
        myBook1.addPage("book1p4");
        System.out.println(myBook1.getContent(0) + " " + myBook1.getContent(3));

        BookShelf myBookShelf = new BookShelf();
        myBookShelf.addBook(myBook1);
        myBookShelf.addBook(myBook1);
        myBookShelf.addBook(myBook2);
        myBookShelf.showBookShelf();
    }
}
class Book {
    private String NAME, iSBN;
    private Vector<String> CONTENT = new Vector<>();

    Book(String NAME, String iSBN, Vector<String> CONTENT) {
        this.NAME = NAME;
        this.iSBN = iSBN;
        this.CONTENT = CONTENT;
    }

    public String getName(){
        return this.NAME;
    }
    public String getISBN(){
        return this.iSBN;
    }
    public String getContent(int PAGE){
        if (PAGE >= CONTENT.size()){
            return "Error";
        }
        return CONTENT.get(PAGE);
    }
    public void addPage(String SENTENCE){
        CONTENT.add(SENTENCE);
    }
}
class BookShelf {
    private Vector<Book> Shelf = new Vector<>();

    BookShelf(){}

    public void addBook(Book MYBook){
        Shelf.add(MYBook);
    }
    public void showBookShelf(){
        for(int i = 0; i < Shelf.size(); ++i) {
            System.out.println(Integer.toString(i) + ' ' + Shelf.get(i).getName() + ' ' + Shelf.get(i).getISBN());
        }
    }
}
