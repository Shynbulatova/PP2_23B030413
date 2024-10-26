package lab2.pr2;

public class Bishop extends Piece {
	public Bishop(){ 
	}
	
	public Bishop(String color ) { 
		super("Bishop", color); 
	}
	@Override 
	public boolean isLegalMove(Position a, Position b) { 
		int xDiff = Math.abs(a.getX() - b.getX());
        int yDiff = Math.abs(a.getY() - b.getY());
        return xDiff == yDiff;
	}
}
