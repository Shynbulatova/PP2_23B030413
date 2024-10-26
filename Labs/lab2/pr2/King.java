package lab2.pr2;

class King extends Piece{
	public King() { 
		
	}
	
	public King(String color) { 
		super("King", color);
	}
	@Override 
	public boolean isLegalMove(Position a , Position b) { 
		int xDiff = Math.abs(a.getX() - b.getX()); 
		int yDiff= Math.abs(a.getY()- b.getY()); 
		return xDiff <=1 && yDiff <=1; 
	}
	
}
