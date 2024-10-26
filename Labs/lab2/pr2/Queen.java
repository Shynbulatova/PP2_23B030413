package lab2.pr2;

public class Queen extends Piece{
	public Queen() { 
		
	}
	
	public Queen(String color) { 
		super("Queen", color); 
	}
	@Override
	public boolean isLegalMove(Position a, Position b) {
        // Queen can move horizontally, vertically, or diagonally any number of squares
        int xDiff = Math.abs(a.getX() - b.getX());
        int yDiff = Math.abs(a.getY() - b.getY());
        return a.getX() == b.getX() || a.getY() == b.getY() || xDiff == yDiff;
    }
}