package lab2.pr2;

public class Main {
	 public static void main(String[] args) {
	        Piece rook = new Rook("Black");
	        Position from = new Position(1, 1);
	        Position to = new Position(1, 5);
	        boolean isLegalMove = rook.isLegalMove(from, to);
	        System.out.println("Is the move legal? " + isLegalMove);

	        Piece king = new King("White");
	        from = new Position(4, 4);
	        to = new Position(5, 5);
	        isLegalMove = king.isLegalMove(from, to);
	        System.out.println("Is the move legal? " + isLegalMove);

	        Piece bishop = new Bishop("White");
	        from = new Position(3, 3);
	        to = new Position(6, 6);
	        isLegalMove = bishop.isLegalMove(from, to);
	        System.out.println("Is the move legal? " + isLegalMove);

	        Piece knight = new Knight("Black");
	        from = new Position(2, 1);
	        to = new Position(4, 2);
	        isLegalMove = knight.isLegalMove(from, to);
	        System.out.println("Is the move legal? " + isLegalMove);

	        Piece queen = new Queen("White");
	        from = new Position(4, 4);
	        to = new Position(7, 7);
	        isLegalMove = queen.isLegalMove(from, to);
	        System.out.println("Is the move legal? " + isLegalMove);

	        Piece pawn = new Pawn("Black");
	        from = new Position(2, 2);
	        to = new Position(2, 3);
	        isLegalMove = pawn.isLegalMove(from, to);
	        System.out.println("Is the move legal? " + isLegalMove);
	    }
}
