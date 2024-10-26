package lab2.pr2;

class Rook extends Piece {
	public Rook(String color) { 
		super("Rook", color); 
	}
	
	@Override
    public boolean isLegalMove(Position a, Position b) {
        // Rook can move horizontally or vertically any number of squares
        return a.getX() == b.getX() || a.getY() == b.getY();
    }
}
