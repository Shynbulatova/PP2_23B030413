package lab2.pr2;

public class Knight extends Piece{
	public Knight() { 
		
	}
	
	public Knight(String color) { 
		super("Knight", color); 
	}
	
	public boolean isLegalMove(Position a, Position b){ 
		int xDiff = Math.abs(a.getX() - b.getX());
        int yDiff = Math.abs(a.getY() - b.getY());
        return (xDiff == 2 && yDiff == 1) || (xDiff == 1 && yDiff == 2);
	}
}
