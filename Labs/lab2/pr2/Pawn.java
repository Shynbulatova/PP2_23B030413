package lab2.pr2;

public class Pawn extends Piece {
	public Pawn() { 
		
	}
	
	public Pawn(String color) { 
		super("Pawn", color); 
	}
	
	@Override
	public boolean isLegalMove(Position a, Position b) { 
		int xDiff= Math.abs(a.getX()-b.getX()); 
		int yDiff = Math.abs((a.getY()- b.getY())); 
		if(getColor().equalsIgnoreCase("White")) { 
			return xDiff==0 && (yDiff ==1 || (yDiff==2 && a.getY()==2)); 
		}
		else { 
			return xDiff == 0 && (yDiff == 1 || (yDiff == 2 && a.getY() == 7));
		}
	}
}
